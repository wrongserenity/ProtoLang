import sys
from antlr4 import *
from dist.protoLexer import protoLexer
from dist.protoParser import protoParser
from dist.protoVisitor import protoVisitor


class MyVisitor(protoVisitor):
    def __init__(self, memory):
        super().__init__()
        self.memory = {} if not memory else memory

    def visitPrintstmt(self, ctx: protoParser.PrintstmtContext):
        return self.visit(ctx.expression())

    def visitInteger(self, ctx: protoParser.IntegerContext):
        return int(ctx.getText())

    def visitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        name = ctx.NAME().getText()
        value = self.visit(ctx.expression())
        self.memory[name] = value

    def visitIdentifier(self, ctx: protoParser.IdentifierContext):
        return self.memory[ctx.NAME().getText()] if ctx.NAME().getText() in self.memory else 0

    def getMemory(self):
        return self.memory

    def visitExpression(self, ctx:protoParser.ExpressionContext):
        left = self.visit(ctx.term(0))
        right = ctx.term(1)
        if right:
            return left + self.visit(right)
        else:
            return left


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
