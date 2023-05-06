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


class MyVisitor(protoVisitor):
    def __init__(self, memory):
        super().__init__()
        self.memory = {} if not memory else memory

    def visitIntDecl(self, ctx:protoParser.IntDeclContext):
        id_name = ctx.ID().getText()
        if id_name in self.memory:
            logError("id '" + id_name + "' already in memory")
        self.memory[id_name] = 0

    def visitFltDecl(self, ctx:protoParser.FltDeclContext):
        id_name = ctx.ID().getText()
        if id_name in self.memory:
            logError("id '" + id_name + "' already in memory")
        self.memory[id_name] = .0

    def visitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value

    def visitIdAtom(self, ctx:protoParser.IdAtomContext):
        id_name = ctx.ID().getText()
        if not id_name in self.memory:
            logError("Has no '" + id_name + "' in memory")
            return False
        return self.memory[id_name]

    def visitIntegerAtom(self, ctx:protoParser.IntegerAtomContext):
        return Value(int(ctx.getText()))

    def visitFloatAtom(self, ctx:protoParser.FloatAtomContext):
        return Value(float(ctx.getText()))

    def visitParenAtom(self, ctx:protoParser.ParenAtomContext):
        return self.visit(ctx.expr())

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

    def getMemory(self):
        return self.memory


if __name__ == "__main__":
    mem = {}
    while 1:
        data = InputStream(input(">>> "))
        # lexer
        lexer = protoLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = protoParser(stream)
        tree = parser.program()
        # evaluator
        visitor = MyVisitor(mem)
        output = visitor.visit(tree)
        mem = visitor.getMemory()
        if output:
            print(output)
