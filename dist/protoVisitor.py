# Generated from proto.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .protoParser import protoParser
else:
    from protoParser import protoParser

# This class defines a complete generic visitor for a parse tree produced by protoParser.

class protoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by protoParser#program.
    def visitProgram(self, ctx:protoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#declaration.
    def visitDeclaration(self, ctx:protoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#statement.
    def visitStatement(self, ctx:protoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#ifstmt.
    def visitIfstmt(self, ctx:protoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#printstmt.
    def visitPrintstmt(self, ctx:protoParser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#assignstmt.
    def visitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#expression.
    def visitExpression(self, ctx:protoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#term.
    def visitTerm(self, ctx:protoParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#identifier.
    def visitIdentifier(self, ctx:protoParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#integer.
    def visitInteger(self, ctx:protoParser.IntegerContext):
        return self.visitChildren(ctx)



del protoParser