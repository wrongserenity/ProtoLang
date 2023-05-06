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


    # Enter a parse tree produced by protoParser#declaration.
    def enterDeclaration(self, ctx:protoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by protoParser#declaration.
    def exitDeclaration(self, ctx:protoParser.DeclarationContext):
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


    # Enter a parse tree produced by protoParser#expression.
    def enterExpression(self, ctx:protoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by protoParser#expression.
    def exitExpression(self, ctx:protoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by protoParser#term.
    def enterTerm(self, ctx:protoParser.TermContext):
        pass

    # Exit a parse tree produced by protoParser#term.
    def exitTerm(self, ctx:protoParser.TermContext):
        pass


    # Enter a parse tree produced by protoParser#identifier.
    def enterIdentifier(self, ctx:protoParser.IdentifierContext):
        pass

    # Exit a parse tree produced by protoParser#identifier.
    def exitIdentifier(self, ctx:protoParser.IdentifierContext):
        pass


    # Enter a parse tree produced by protoParser#integer.
    def enterInteger(self, ctx:protoParser.IntegerContext):
        pass

    # Exit a parse tree produced by protoParser#integer.
    def exitInteger(self, ctx:protoParser.IntegerContext):
        pass



del protoParser