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


    # Visit a parse tree produced by protoParser#intDecl.
    def visitIntDecl(self, ctx:protoParser.IntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#fltDecl.
    def visitFltDecl(self, ctx:protoParser.FltDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#statement.
    def visitStatement(self, ctx:protoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#ifstmt.
    def visitIfstmt(self, ctx:protoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#whilestmt.
    def visitWhilestmt(self, ctx:protoParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#printstmt.
    def visitPrintstmt(self, ctx:protoParser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#assignstmt.
    def visitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#condblock.
    def visitCondblock(self, ctx:protoParser.CondblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#notExpr.
    def visitNotExpr(self, ctx:protoParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:protoParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#termExpr.
    def visitTermExpr(self, ctx:protoParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:protoParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#orExpr.
    def visitOrExpr(self, ctx:protoParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:protoParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#relationalExpr.
    def visitRelationalExpr(self, ctx:protoParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#equalityExpr.
    def visitEqualityExpr(self, ctx:protoParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#andExpr.
    def visitAndExpr(self, ctx:protoParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#parenAtom.
    def visitParenAtom(self, ctx:protoParser.ParenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#integerAtom.
    def visitIntegerAtom(self, ctx:protoParser.IntegerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#floatAtom.
    def visitFloatAtom(self, ctx:protoParser.FloatAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#booleanAtom.
    def visitBooleanAtom(self, ctx:protoParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#idAtom.
    def visitIdAtom(self, ctx:protoParser.IdAtomContext):
        return self.visitChildren(ctx)



del protoParser