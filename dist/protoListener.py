# Generated from proto.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .protoParser import protoParser
else:
    from protoParser import protoParser

# This class defines a complete listener for a parse tree produced by protoParser.
class protoListener(ParseTreeListener):

    # Enter a parse tree produced by protoParser#program.
    def enterProgram(self, ctx:protoParser.ProgramContext):
        pass

    # Exit a parse tree produced by protoParser#program.
    def exitProgram(self, ctx:protoParser.ProgramContext):
        pass


    # Enter a parse tree produced by protoParser#valDecl.
    def enterValDecl(self, ctx:protoParser.ValDeclContext):
        pass

    # Exit a parse tree produced by protoParser#valDecl.
    def exitValDecl(self, ctx:protoParser.ValDeclContext):
        pass


    # Enter a parse tree produced by protoParser#funcDecl.
    def enterFuncDecl(self, ctx:protoParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by protoParser#funcDecl.
    def exitFuncDecl(self, ctx:protoParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by protoParser#paramdecl.
    def enterParamdecl(self, ctx:protoParser.ParamdeclContext):
        pass

    # Exit a parse tree produced by protoParser#paramdecl.
    def exitParamdecl(self, ctx:protoParser.ParamdeclContext):
        pass


    # Enter a parse tree produced by protoParser#funcbody.
    def enterFuncbody(self, ctx:protoParser.FuncbodyContext):
        pass

    # Exit a parse tree produced by protoParser#funcbody.
    def exitFuncbody(self, ctx:protoParser.FuncbodyContext):
        pass


    # Enter a parse tree produced by protoParser#funcreturn.
    def enterFuncreturn(self, ctx:protoParser.FuncreturnContext):
        pass

    # Exit a parse tree produced by protoParser#funcreturn.
    def exitFuncreturn(self, ctx:protoParser.FuncreturnContext):
        pass


    # Enter a parse tree produced by protoParser#statement.
    def enterStatement(self, ctx:protoParser.StatementContext):
        pass

    # Exit a parse tree produced by protoParser#statement.
    def exitStatement(self, ctx:protoParser.StatementContext):
        pass


    # Enter a parse tree produced by protoParser#ifstmt.
    def enterIfstmt(self, ctx:protoParser.IfstmtContext):
        pass

    # Exit a parse tree produced by protoParser#ifstmt.
    def exitIfstmt(self, ctx:protoParser.IfstmtContext):
        pass


    # Enter a parse tree produced by protoParser#whilestmt.
    def enterWhilestmt(self, ctx:protoParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by protoParser#whilestmt.
    def exitWhilestmt(self, ctx:protoParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by protoParser#printstmt.
    def enterPrintstmt(self, ctx:protoParser.PrintstmtContext):
        pass

    # Exit a parse tree produced by protoParser#printstmt.
    def exitPrintstmt(self, ctx:protoParser.PrintstmtContext):
        pass


    # Enter a parse tree produced by protoParser#assignstmt.
    def enterAssignstmt(self, ctx:protoParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by protoParser#assignstmt.
    def exitAssignstmt(self, ctx:protoParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by protoParser#savelinesstmt.
    def enterSavelinesstmt(self, ctx:protoParser.SavelinesstmtContext):
        pass

    # Exit a parse tree produced by protoParser#savelinesstmt.
    def exitSavelinesstmt(self, ctx:protoParser.SavelinesstmtContext):
        pass


    # Enter a parse tree produced by protoParser#readfilestmt.
    def enterReadfilestmt(self, ctx:protoParser.ReadfilestmtContext):
        pass

    # Exit a parse tree produced by protoParser#readfilestmt.
    def exitReadfilestmt(self, ctx:protoParser.ReadfilestmtContext):
        pass


    # Enter a parse tree produced by protoParser#condblock.
    def enterCondblock(self, ctx:protoParser.CondblockContext):
        pass

    # Exit a parse tree produced by protoParser#condblock.
    def exitCondblock(self, ctx:protoParser.CondblockContext):
        pass


    # Enter a parse tree produced by protoParser#notExpr.
    def enterNotExpr(self, ctx:protoParser.NotExprContext):
        pass

    # Exit a parse tree produced by protoParser#notExpr.
    def exitNotExpr(self, ctx:protoParser.NotExprContext):
        pass


    # Enter a parse tree produced by protoParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:protoParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by protoParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:protoParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by protoParser#termExpr.
    def enterTermExpr(self, ctx:protoParser.TermExprContext):
        pass

    # Exit a parse tree produced by protoParser#termExpr.
    def exitTermExpr(self, ctx:protoParser.TermExprContext):
        pass


    # Enter a parse tree produced by protoParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:protoParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by protoParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:protoParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by protoParser#orExpr.
    def enterOrExpr(self, ctx:protoParser.OrExprContext):
        pass

    # Exit a parse tree produced by protoParser#orExpr.
    def exitOrExpr(self, ctx:protoParser.OrExprContext):
        pass


    # Enter a parse tree produced by protoParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:protoParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by protoParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:protoParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by protoParser#relationalExpr.
    def enterRelationalExpr(self, ctx:protoParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by protoParser#relationalExpr.
    def exitRelationalExpr(self, ctx:protoParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by protoParser#equalityExpr.
    def enterEqualityExpr(self, ctx:protoParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by protoParser#equalityExpr.
    def exitEqualityExpr(self, ctx:protoParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by protoParser#andExpr.
    def enterAndExpr(self, ctx:protoParser.AndExprContext):
        pass

    # Exit a parse tree produced by protoParser#andExpr.
    def exitAndExpr(self, ctx:protoParser.AndExprContext):
        pass


    # Enter a parse tree produced by protoParser#parenAtom.
    def enterParenAtom(self, ctx:protoParser.ParenAtomContext):
        pass

    # Exit a parse tree produced by protoParser#parenAtom.
    def exitParenAtom(self, ctx:protoParser.ParenAtomContext):
        pass


    # Enter a parse tree produced by protoParser#integerAtom.
    def enterIntegerAtom(self, ctx:protoParser.IntegerAtomContext):
        pass

    # Exit a parse tree produced by protoParser#integerAtom.
    def exitIntegerAtom(self, ctx:protoParser.IntegerAtomContext):
        pass


    # Enter a parse tree produced by protoParser#floatAtom.
    def enterFloatAtom(self, ctx:protoParser.FloatAtomContext):
        pass

    # Exit a parse tree produced by protoParser#floatAtom.
    def exitFloatAtom(self, ctx:protoParser.FloatAtomContext):
        pass


    # Enter a parse tree produced by protoParser#booleanAtom.
    def enterBooleanAtom(self, ctx:protoParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by protoParser#booleanAtom.
    def exitBooleanAtom(self, ctx:protoParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by protoParser#idAtom.
    def enterIdAtom(self, ctx:protoParser.IdAtomContext):
        pass

    # Exit a parse tree produced by protoParser#idAtom.
    def exitIdAtom(self, ctx:protoParser.IdAtomContext):
        pass


    # Enter a parse tree produced by protoParser#funcAtom.
    def enterFuncAtom(self, ctx:protoParser.FuncAtomContext):
        pass

    # Exit a parse tree produced by protoParser#funcAtom.
    def exitFuncAtom(self, ctx:protoParser.FuncAtomContext):
        pass


    # Enter a parse tree produced by protoParser#stringAtom.
    def enterStringAtom(self, ctx:protoParser.StringAtomContext):
        pass

    # Exit a parse tree produced by protoParser#stringAtom.
    def exitStringAtom(self, ctx:protoParser.StringAtomContext):
        pass


    # Enter a parse tree produced by protoParser#funccall.
    def enterFunccall(self, ctx:protoParser.FunccallContext):
        pass

    # Exit a parse tree produced by protoParser#funccall.
    def exitFunccall(self, ctx:protoParser.FunccallContext):
        pass


    # Enter a parse tree produced by protoParser#parampass.
    def enterParampass(self, ctx:protoParser.ParampassContext):
        pass

    # Exit a parse tree produced by protoParser#parampass.
    def exitParampass(self, ctx:protoParser.ParampassContext):
        pass



del protoParser