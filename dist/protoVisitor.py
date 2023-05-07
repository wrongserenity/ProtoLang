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


    # Visit a parse tree produced by protoParser#command.
    def visitCommand(self, ctx:protoParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#valDecl.
    def visitValDecl(self, ctx:protoParser.ValDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#funcDecl.
    def visitFuncDecl(self, ctx:protoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#paramdecl.
    def visitParamdecl(self, ctx:protoParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#funcbody.
    def visitFuncbody(self, ctx:protoParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#funcreturn.
    def visitFuncreturn(self, ctx:protoParser.FuncreturnContext):
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


    # Visit a parse tree produced by protoParser#savelinesstmt.
    def visitSavelinesstmt(self, ctx:protoParser.SavelinesstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#readfilestmt.
    def visitReadfilestmt(self, ctx:protoParser.ReadfilestmtContext):
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


    # Visit a parse tree produced by protoParser#funcAtom.
    def visitFuncAtom(self, ctx:protoParser.FuncAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#stringAtom.
    def visitStringAtom(self, ctx:protoParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#funccall.
    def visitFunccall(self, ctx:protoParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by protoParser#parampass.
    def visitParampass(self, ctx:protoParser.ParampassContext):
        return self.visitChildren(ctx)



del protoParser