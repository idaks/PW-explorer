# Generated from PW-explorer/Clingo Parser/Clingo.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\20\u0080\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\fe\n\f")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\3\16\6\16v\n\16\r\16\16\16w\3\17\6\17{\n\17\r\17")
        buf.write(u"\16\17|\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write(u"\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\4\t\2.")
        buf.write(u".\60\60\62<C\\^^aac|\5\2\13\f\16\17\"\"\2\u0082\2\3\3")
        buf.write(u"\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write(u"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write(u"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write(u"\2\35\3\2\2\2\3\37\3\2\2\2\5&\3\2\2\2\7(\3\2\2\2\t\60")
        buf.write(u"\3\2\2\2\13=\3\2\2\2\rC\3\2\2\2\17E\3\2\2\2\21G\3\2\2")
        buf.write(u"\2\23O\3\2\2\2\25]\3\2\2\2\27d\3\2\2\2\31f\3\2\2\2\33")
        buf.write(u"u\3\2\2\2\35z\3\2\2\2\37 \7O\2\2 !\7q\2\2!\"\7f\2\2\"")
        buf.write(u"#\7g\2\2#$\7n\2\2$%\7u\2\2%\4\3\2\2\2&\'\7<\2\2\'\6\3")
        buf.write(u"\2\2\2()\7Q\2\2)*\7r\2\2*+\7v\2\2+,\7k\2\2,-\7o\2\2-")
        buf.write(u".\7w\2\2./\7o\2\2/\b\3\2\2\2\60\61\7Q\2\2\61\62\7r\2")
        buf.write(u"\2\62\63\7v\2\2\63\64\7k\2\2\64\65\7o\2\2\65\66\7k\2")
        buf.write(u"\2\66\67\7|\2\2\678\7c\2\289\7v\2\29:\7k\2\2:;\7q\2\2")
        buf.write(u";<\7p\2\2<\n\3\2\2\2=>\7E\2\2>?\7c\2\2?@\7n\2\2@A\7n")
        buf.write(u"\2\2AB\7u\2\2B\f\3\2\2\2CD\7*\2\2D\16\3\2\2\2EF\7+\2")
        buf.write(u"\2F\20\3\2\2\2GH\7C\2\2HI\7p\2\2IJ\7u\2\2JK\7y\2\2KL")
        buf.write(u"\7g\2\2LM\7t\2\2MN\7<\2\2N\22\3\2\2\2OP\7Q\2\2PQ\7r\2")
        buf.write(u"\2QR\7v\2\2RS\7k\2\2ST\7o\2\2TU\7k\2\2UV\7|\2\2VW\7c")
        buf.write(u"\2\2WX\7v\2\2XY\7k\2\2YZ\7q\2\2Z[\7p\2\2[\\\7<\2\2\\")
        buf.write(u"\24\3\2\2\2]^\7.\2\2^\26\3\2\2\2_`\7{\2\2`a\7g\2\2ae")
        buf.write(u"\7u\2\2bc\7p\2\2ce\7q\2\2d_\3\2\2\2db\3\2\2\2e\30\3\2")
        buf.write(u"\2\2fg\7Q\2\2gh\7R\2\2hi\7V\2\2ij\7K\2\2jk\7O\2\2kl\7")
        buf.write(u"W\2\2lm\7O\2\2mn\7\"\2\2no\7H\2\2op\7Q\2\2pq\7W\2\2q")
        buf.write(u"r\7P\2\2rs\7F\2\2s\32\3\2\2\2tv\t\2\2\2ut\3\2\2\2vw\3")
        buf.write(u"\2\2\2wu\3\2\2\2wx\3\2\2\2x\34\3\2\2\2y{\t\3\2\2zy\3")
        buf.write(u"\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b")
        buf.write(u"\17\2\2\177\36\3\2\2\2\6\2dw|\3\b\2\2")
        return buf.getvalue()


class ClingoLexer(Lexer):

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
    OPTIMUM_FOUND_OR_NOT = 11
    OPTIMUM_FOUND = 12
    TEXT = 13
    WHITESPACE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'Models'", u"':'", u"'Optimum'", u"'Optimization'", u"'Calls'", 
            u"'('", u"')'", u"'Answer:'", u"'Optimization:'", u"','", u"'OPTIMUM FOUND'" ]

    symbolicNames = [ u"<INVALID>",
            u"OPTIMUM_FOUND_OR_NOT", u"OPTIMUM_FOUND", u"TEXT", u"WHITESPACE" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"T__8", u"T__9", u"OPTIMUM_FOUND_OR_NOT", 
                  u"OPTIMUM_FOUND", u"TEXT", u"WHITESPACE" ]

    grammarFileName = u"Clingo.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(ClingoLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


