import sys
from antlr4 import *
from dist.protoLexer import protoLexer
from dist.protoParser import protoParser
from dist.protoVisitor import protoVisitor


def logError(msg):
    if not isinstance(msg, str):
        logError("Can not log error: message is not string")

    print(msg)

class Value:
    def __init__(self, value):
        self.value = value

    def bool(self):
        return bool(self.value)

    def float(self):
        return float(self.value)

    def int(self):
        return int(self.value)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if other is None or not isinstance(other, Value):
            return False

        return Value(self.value == other.value)

    def __ne__(self, other):
        return Value(not self.__eq__(other))

    def __gt__(self, other):
        return Value(self.value > other.value)

    def __lt__(self, other):
        return Value(self.value < other.value)

    def __ge__(self, other):
        return Value(self.__gt__(other) or self.__eq__(other))

    def __le__(self, other):
        return Value(self.__lt__(other) or self.__eq__(other))

    def __neg__(self):
        if isinstance(self.value, int) or isinstance(self.value, float):
            return Value(-self.value)
        elif isinstance(self.value, bool):
            logError("Not recomended using 'minus' with bool, use 'not'")
            return Value(not self.value)

    def __bool__(self):
        return self.bool()

    def __and__(self, other):
        return Value(bool(self.value and other.value))

    def __or__(self, other):
        return Value(bool(self.value or other.value))

    def __mul__(self, other):
        return Value(self.value * other.value)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if other.value == 0:
            logError("Zero division")
            return Value(0)
        return Value(self.value / other.value)

    def __mod__(self, other):
        if other.value == 0:
            logError("Zero division")
            return Value(0)
        return Value(self.value % other.value)

    def __add__(self, other):
        return Value(self.value + other.value)

    def __sub__(self, other):
        return Value(self.value - other.value)

class Function:
    def __init__(self, param_names, ctxBody:protoParser.FuncbodyContext, ctxRet:protoParser.FuncreturnContext):
        self.param_names = param_names
        self.context_body = ctxBody
        self.context_return = ctxRet
        self.func_mem = {}

    def getAllMem(self, params, visitor_mem):
        if len(params) != len(self.param_names):
            logError("Func: expected " + str(len(self.param_names)) +
                     " values, but received" + str(len(params)))
            return Value(0)

        for i in range(len(self.param_names)):
            self.func_mem[self.param_names[i]] = params[i]

        intersect = self.func_mem.keys() & visitor_mem.keys()
        if len(intersect) > 0:
            logError("Func: var name collision: " + str(intersect))
            return Value(0)

        all_mem = {**self.func_mem, **visitor_mem}
        return all_mem

    def getCtxBody(self):
        return self.context_body

    def getCtxRet(self):
        return self.context_return


class MyVisitor(protoVisitor):
    def __init__(self, memory, all_lines=None):
        super().__init__()
        self.memory = {} if not memory else memory
        self.all_lines = [] if not all_lines else all_lines

    def visitValDecl(self, ctx:protoParser.ValDeclContext):
        id_name = ctx.ID().getText()
        if id_name in self.memory:
            logError("id '" + id_name + "' already in memory")
        self.memory[id_name] = Value(0)

    def visitFuncDecl(self, ctx:protoParser.FuncDeclContext):
        id_name = ctx.ID().getText()
        if id_name in self.memory:
            logError("id '" + id_name + "' already in memory")
        param_names = self.visit(ctx.paramdecl())
        self.memory[id_name] = Function(param_names, ctx.funcbody(), ctx.funcreturn())

    def visitParamdecl(self, ctx:protoParser.ParamdeclContext):
        result = []
        for id_val in ctx.ID():
            result.append(id_val.getText())
        return result

    def visitFuncreturn(self, ctx:protoParser.FuncreturnContext):
        return self.visit(ctx.expr())

    def visitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value

    def visitIdAtom(self, ctx:protoParser.IdAtomContext):
        id_name = ctx.ID().getText()
        if not id_name in self.memory:
            logError("Has no '" + id_name + "' in memory")
            return Value(0)
        return self.memory[id_name]

    def visitFuncAtom(self, ctx:protoParser.FuncAtomContext):
        return self.visit(ctx.funccall())

    def visitFunccall(self, ctx:protoParser.FunccallContext):
        func_id = ctx.ID().getText()
        if not func_id in self.memory:
            logError("Has no function '" + func_id + "' in memory")
            return Value(0)

        func = self.memory[func_id]
        param_pass = self.visit(ctx.parampass())

        init_mem = self.memory.copy()
        self.memory = func.getAllMem(param_pass, self.memory.copy())

        self.visit(func.getCtxBody())

        result = None
        if not func.getCtxRet() is None:
            result = self.visit(func.getCtxRet())

        self.memory = init_mem
        if not result is None:
            return result

    def visitParampass(self, ctx:protoParser.ParampassContext):
        results = []
        for expr in ctx.expr():
            results.append(self.visit(expr))
        return results


    def visitFuncbody(self, ctx:protoParser.FuncbodyContext):
        stats = ctx.statement()
        for stat in stats:
            self.visit(stat)

    def visitIntegerAtom(self, ctx:protoParser.IntegerAtomContext):
        return Value(int(ctx.getText()))

    def visitFloatAtom(self, ctx:protoParser.FloatAtomContext):
        return Value(float(ctx.getText()))

    def visitParenAtom(self, ctx:protoParser.ParenAtomContext):
        return self.visit(ctx.expr())

    def visitStringAtom(self, ctx:protoParser.StringAtomContext):
        return Value(str(ctx.getText()[1:-1]))

    # expr

    def visitUnaryMinusExpr(self, ctx:protoParser.UnaryMinusExprContext):
        return -self.visit(ctx.expr())

    def visitNotExpr(self, ctx:protoParser.NotExprContext):
        return not self.visit(ctx.expr())

    def visitMultiplicationExpr(self, ctx:protoParser.MultiplicationExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        type_val = ctx.op.type
        if type_val == protoParser.MULT:
            return left * right
        elif type_val == protoParser.DIV:
            return left / right
        elif type_val == protoParser.MOD:
            return left % right
        else:
            logError("Unknown operator in multiplication")

    def visitAdditiveExpr(self, ctx:protoParser.AdditiveExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        type_val = ctx.op.type
        if type_val == protoParser.PLUS:
            return left + right
        elif type_val == protoParser.MINUS:
            return left - right
        else:
            logError("Unknown operator in additive")

    def visitRelationalExpr(self, ctx:protoParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        type_val = ctx.op.type
        if type_val == protoParser.LT:
            return left < right
        elif type_val == protoParser.LTEQ:
            return left <= right
        elif type_val == protoParser.GT:
            return left > right
        elif type_val == protoParser.GTEQ:
            return left >= right
        else:
            logError("Unknown operator in relational")

    def visitEqualityExpr(self, ctx:protoParser.EqualityExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        type_val = ctx.op.getType()
        if type_val == protoParser.EQ:
            return left == right
        elif type_val == protoParser.NEQ:
            return left != right
        else:
            logError("Unknown operator in equality")

    def visitAndExpr(self, ctx:protoParser.AndExprContext):
        return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

    def visitOrExpr(self, ctx:protoParser.OrExprContext):
        return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))

    # statements

    def visitPrintstmt(self, ctx: protoParser.PrintstmtContext):
        print(self.visit(ctx.expr()))

    def visitIfstmt(self, ctx:protoParser.IfstmtContext):
        cond_blocks = ctx.condblock()
        evaluated_block = False
        for block in cond_blocks:
            evaluated = self.visit(block.expr())
            if evaluated.bool():
                evaluated_block = True
                for st in block.statement():
                    self.visit(st)
                break;

        if not evaluated_block and not ctx.statement() is None:
            for st in ctx.statement():
                self.visit(st)

    def visitWhilestmt(self, ctx:protoParser.WhilestmtContext):
        val = self.visit(ctx.expr())
        while val.bool():
            for st in ctx.statement():
                self.visit(st)
            val = self.visit(ctx.expr())

    def visitSavelinesstmt(self, ctx:protoParser.SavelinesstmtContext):
        result_str = self.filterSavelines()


        with open(str(self.visit(ctx.term())) + '.proto', 'w') as file:
            file.write(result_str)

    def filterSavelines(self):
        lines_temp = self.all_lines.copy()
        for i in range(len(lines_temp)):
            if "func" in lines_temp[i]:
                lines_temp[i] = lines_temp[i].replace(")", ")\n   ")
                lines_temp[i] = lines_temp[i].replace("endfunc", "endfunc\n")
                lines_temp[i] = lines_temp[i].replace(";", ";\n   ")
        return '\n'.join(lines_temp)




    def getMemory(self):
        return self.memory


def getVisitorResultAndMem(data_, oldmem, lines):
    # lexer
    lexer_ = protoLexer(data_)
    stream_ = CommonTokenStream(lexer_)
    # parser
    parser_ = protoParser(stream_)
    tree_ = parser_.program()
    # evaluator
    visitor_ = MyVisitor(oldmem, lines)
    output_ = visitor_.visit(tree_)
    mem_ = visitor_.getMemory()
    return output_, mem_


if __name__ == "__main__":
    mem = {}
    lines = []
    while 1:
        input_str = input(">>> ")
        data = InputStream(input_str)
        lines.append(input_str)
        output, mem = getVisitorResultAndMem(data, mem, lines)
        if output:
            print(output)
