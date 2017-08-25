# Generated from Dlv.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\t\'\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write(u"\3\7\6\7\35\n\7\r\7\16\7\36\3\b\6\b\"\n\b\r\b\16\b#\3")
        buf.write(u"\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\4\b\2")
        buf.write(u"#),-/\\`|~~\u0080\u0080\5\2\13\f\17\17\"\"\2(\2\3\3\2")
        buf.write(u"\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write(u"\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7")
        buf.write(u"\25\3\2\2\2\t\27\3\2\2\2\13\31\3\2\2\2\r\34\3\2\2\2\17")
        buf.write(u"!\3\2\2\2\21\22\7}\2\2\22\4\3\2\2\2\23\24\7\177\2\2\24")
        buf.write(u"\6\3\2\2\2\25\26\7.\2\2\26\b\3\2\2\2\27\30\7*\2\2\30")
        buf.write(u"\n\3\2\2\2\31\32\7+\2\2\32\f\3\2\2\2\33\35\t\2\2\2\34")
        buf.write(u"\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2")
        buf.write(u"\37\16\3\2\2\2 \"\t\3\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2")
        buf.write(u"\2\2#$\3\2\2\2$%\3\2\2\2%&\b\b\2\2&\20\3\2\2\2\5\2\36")
        buf.write(u"#\3\b\2\2")
        return buf.getvalue()


class DlvLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    TEXT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'{'", u"'}'", u"','", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"TEXT", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"TEXT", 
                  u"WS" ]

    grammarFileName = u"Dlv.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(DlvLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


