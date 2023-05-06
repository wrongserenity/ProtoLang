# Generated from proto.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .protoParser import protoParser
else:
    from protoParser import protoParser

# This class defines a complete listener for a parse tree produced by protoParser.
class protoListener(ParseTreeListener):

    # Enter a parse tree produced by protoParser#NumberExpr.
    def enterNumberExpr(self, ctx:protoParser.NumberExprContext):
        pass

    # Exit a parse tree produced by protoParser#NumberExpr.
    def exitNumberExpr(self, ctx:protoParser.NumberExprContext):
        pass


    # Enter a parse tree produced by protoParser#ByeExpr.
    def enterByeExpr(self, ctx:protoParser.ByeExprContext):
        pass

    # Exit a parse tree produced by protoParser#ByeExpr.
    def exitByeExpr(self, ctx:protoParser.ByeExprContext):
        pass


    # Enter a parse tree produced by protoParser#HelloExpr.
    def enterHelloExpr(self, ctx:protoParser.HelloExprContext):
        pass

    # Exit a parse tree produced by protoParser#HelloExpr.
    def exitHelloExpr(self, ctx:protoParser.HelloExprContext):
        pass


    # Enter a parse tree produced by protoParser#ParenExpr.
    def enterParenExpr(self, ctx:protoParser.ParenExprContext):
        pass

    # Exit a parse tree produced by protoParser#ParenExpr.
    def exitParenExpr(self, ctx:protoParser.ParenExprContext):
        pass


    # Enter a parse tree produced by protoParser#InfixExpr.
    def enterInfixExpr(self, ctx:protoParser.InfixExprContext):
        pass

    # Exit a parse tree produced by protoParser#InfixExpr.
    def exitInfixExpr(self, ctx:protoParser.InfixExprContext):
        pass



del protoParser