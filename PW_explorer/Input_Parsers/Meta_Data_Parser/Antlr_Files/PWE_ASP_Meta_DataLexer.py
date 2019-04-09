# Generated from PW_explorer/Input_Parsers/Meta_Data_Parser/Antlr_Files/PWE_ASP_Meta_Data.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\6\rR\n\r\r\r\16\rS\3\16\6\16W\n\16\r\16\16\16X\3")
        buf.write("\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\4\n\2#&))->@AC\\^^aac|\5")
        buf.write("\2\13\f\16\17\"\"\2]\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7&\3\2")
        buf.write("\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17\65\3\2\2\2\21")
        buf.write(">\3\2\2\2\23D\3\2\2\2\25I\3\2\2\2\27N\3\2\2\2\31Q\3\2")
        buf.write("\2\2\33V\3\2\2\2\35\36\7\'\2\2\36\4\3\2\2\2\37 \7u\2\2")
        buf.write(" !\7e\2\2!\"\7j\2\2\"#\7g\2\2#$\7o\2\2$%\7c\2\2%\6\3\2")
        buf.write("\2\2&\'\7*\2\2\'\b\3\2\2\2()\7+\2\2)\n\3\2\2\2*+\7\60")
        buf.write("\2\2+\f\3\2\2\2,-\7v\2\2-.\7g\2\2./\7o\2\2/\60\7r\2\2")
        buf.write("\60\61\7q\2\2\61\62\7t\2\2\62\63\7c\2\2\63\64\7n\2\2\64")
        buf.write("\16\3\2\2\2\65\66\7i\2\2\66\67\7t\2\2\678\7c\2\289\7r")
        buf.write("\2\29:\7j\2\2:;\7x\2\2;<\7k\2\2<=\7|\2\2=\20\3\2\2\2>")
        buf.write("?\7i\2\2?@\7t\2\2@A\7c\2\2AB\7r\2\2BC\7j\2\2C\22\3\2\2")
        buf.write("\2DE\7p\2\2EF\7q\2\2FG\7f\2\2GH\7g\2\2H\24\3\2\2\2IJ\7")
        buf.write("g\2\2JK\7f\2\2KL\7i\2\2LM\7g\2\2M\26\3\2\2\2NO\7?\2\2")
        buf.write("O\30\3\2\2\2PR\t\2\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2S")
        buf.write("T\3\2\2\2T\32\3\2\2\2UW\t\3\2\2VU\3\2\2\2WX\3\2\2\2XV")
        buf.write("\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\b\16\2\2[\34\3\2\2\2\5")
        buf.write("\2SX\3\b\2\2")
        return buf.getvalue()


class PWE_ASP_Meta_DataLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    TEXT = 12
    WHITESPACE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'%'", "'schema'", "'('", "')'", "'.'", "'temporal'", "'graphviz'", 
            "'graph'", "'node'", "'edge'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "TEXT", "WHITESPACE" ]

    grammarFileName = "PWE_ASP_Meta_Data.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


