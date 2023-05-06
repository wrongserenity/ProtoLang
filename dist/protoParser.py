# Generated from proto.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,5,
        0,28,8,0,10,0,12,0,31,9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,40,8,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,70,8,
        6,1,7,1,7,3,7,74,8,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,
        14,16,18,0,0,76,0,23,1,0,0,0,2,32,1,0,0,0,4,39,1,0,0,0,6,41,1,0,
        0,0,8,55,1,0,0,0,10,59,1,0,0,0,12,69,1,0,0,0,14,73,1,0,0,0,16,75,
        1,0,0,0,18,77,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,
        23,21,1,0,0,0,23,24,1,0,0,0,24,29,1,0,0,0,25,23,1,0,0,0,26,28,3,
        4,2,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,
        1,1,0,0,0,31,29,1,0,0,0,32,33,5,4,0,0,33,34,5,13,0,0,34,35,5,9,0,
        0,35,3,1,0,0,0,36,40,3,6,3,0,37,40,3,8,4,0,38,40,3,10,5,0,39,36,
        1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,0,40,5,1,0,0,0,41,42,5,1,0,0,42,
        43,5,10,0,0,43,44,3,16,8,0,44,45,5,6,0,0,45,46,3,18,9,0,46,50,5,
        11,0,0,47,49,3,4,2,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,
        51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,2,0,0,54,7,1,0,0,
        0,55,56,5,3,0,0,56,57,3,12,6,0,57,58,5,9,0,0,58,9,1,0,0,0,59,60,
        5,13,0,0,60,61,5,7,0,0,61,62,3,12,6,0,62,63,5,9,0,0,63,11,1,0,0,
        0,64,70,3,14,7,0,65,66,3,14,7,0,66,67,5,5,0,0,67,68,3,14,7,0,68,
        70,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,70,13,1,0,0,0,71,74,3,16,
        8,0,72,74,3,18,9,0,73,71,1,0,0,0,73,72,1,0,0,0,74,15,1,0,0,0,75,
        76,5,13,0,0,76,17,1,0,0,0,77,78,5,12,0,0,78,19,1,0,0,0,6,23,29,39,
        50,69,73
    ]

class protoParser ( Parser ):

    grammarFileName = "proto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'endif'", "'print'", "'int'", 
                     "'+'", "'=='", "'='", "'!='", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "ENDIF", "PRINT", "INT", "PLUS", 
                      "EQUAL", "ASSIGN", "NOTEQUAL", "SEMICOLON", "LPAREN", 
                      "RPAREN", "INTEGER", "NAME", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_statement = 2
    RULE_ifstmt = 3
    RULE_printstmt = 4
    RULE_assignstmt = 5
    RULE_expression = 6
    RULE_term = 7
    RULE_identifier = 8
    RULE_integer = 9

    ruleNames =  [ "program", "declaration", "statement", "ifstmt", "printstmt", 
                   "assignstmt", "expression", "term", "identifier", "integer" ]

    EOF = Token.EOF
    IF=1
    ENDIF=2
    PRINT=3
    INT=4
    PLUS=5
    EQUAL=6
    ASSIGN=7
    NOTEQUAL=8
    SEMICOLON=9
    LPAREN=10
    RPAREN=11
    INTEGER=12
    NAME=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(protoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(protoParser.DeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(protoParser.StatementContext)
            else:
                return self.getTypedRuleContext(protoParser.StatementContext,i)


        def getRuleIndex(self):
            return protoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = protoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 20
                self.declaration()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8202) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(protoParser.INT, 0)

        def NAME(self):
            return self.getToken(protoParser.NAME, 0)

        def SEMICOLON(self):
            return self.getToken(protoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return protoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = protoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(protoParser.INT)
            self.state = 33
            self.match(protoParser.NAME)
            self.state = 34
            self.match(protoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(protoParser.IfstmtContext,0)


        def printstmt(self):
            return self.getTypedRuleContext(protoParser.PrintstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(protoParser.AssignstmtContext,0)


        def getRuleIndex(self):
            return protoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = protoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.ifstmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.printstmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.assignstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(protoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(protoParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(protoParser.IdentifierContext,0)


        def EQUAL(self):
            return self.getToken(protoParser.EQUAL, 0)

        def integer(self):
            return self.getTypedRuleContext(protoParser.IntegerContext,0)


        def RPAREN(self):
            return self.getToken(protoParser.RPAREN, 0)

        def ENDIF(self):
            return self.getToken(protoParser.ENDIF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(protoParser.StatementContext)
            else:
                return self.getTypedRuleContext(protoParser.StatementContext,i)


        def getRuleIndex(self):
            return protoParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = protoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(protoParser.IF)
            self.state = 42
            self.match(protoParser.LPAREN)
            self.state = 43
            self.identifier()
            self.state = 44
            self.match(protoParser.EQUAL)
            self.state = 45
            self.integer()
            self.state = 46
            self.match(protoParser.RPAREN)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8202) != 0):
                self.state = 47
                self.statement()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(protoParser.ENDIF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(protoParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(protoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(protoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return protoParser.RULE_printstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintstmt" ):
                listener.enterPrintstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintstmt" ):
                listener.exitPrintstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintstmt" ):
                return visitor.visitPrintstmt(self)
            else:
                return visitor.visitChildren(self)




    def printstmt(self):

        localctx = protoParser.PrintstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(protoParser.PRINT)
            self.state = 56
            self.expression()
            self.state = 57
            self.match(protoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(protoParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(protoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(protoParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(protoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return protoParser.RULE_assignstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignstmt" ):
                listener.enterAssignstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignstmt" ):
                listener.exitAssignstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = protoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(protoParser.NAME)
            self.state = 60
            self.match(protoParser.ASSIGN)
            self.state = 61
            self.expression()
            self.state = 62
            self.match(protoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(protoParser.TermContext)
            else:
                return self.getTypedRuleContext(protoParser.TermContext,i)


        def PLUS(self):
            return self.getToken(protoParser.PLUS, 0)

        def getRuleIndex(self):
            return protoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = protoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.term()
                self.state = 66
                self.match(protoParser.PLUS)
                self.state = 67
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(protoParser.IdentifierContext,0)


        def integer(self):
            return self.getTypedRuleContext(protoParser.IntegerContext,0)


        def getRuleIndex(self):
            return protoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = protoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.identifier()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.integer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(protoParser.NAME, 0)

        def getRuleIndex(self):
            return protoParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = protoParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(protoParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(protoParser.INTEGER, 0)

        def getRuleIndex(self):
            return protoParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = protoParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(protoParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





