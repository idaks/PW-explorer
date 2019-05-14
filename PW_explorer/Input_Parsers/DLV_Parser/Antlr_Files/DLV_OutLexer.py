# Generated from PW_explorer/Input_Parsers/DLV_Parser/Antlr_Files/DLV_Out.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("m\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\6\rc\n\r\r\r\16\rd\3\16\6\16h\n\16\r\16")
        buf.write("\16\16i\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\t\2#$/<>@C\\^")
        buf.write("^aac|\5\2\13\f\16\17\"\"\2n\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5)\3\2\2\2")
        buf.write("\7@\3\2\2\2\tC\3\2\2\2\13F\3\2\2\2\rL\3\2\2\2\17W\3\2")
        buf.write("\2\2\21Y\3\2\2\2\23[\3\2\2\2\25]\3\2\2\2\27_\3\2\2\2\31")
        buf.write("b\3\2\2\2\33g\3\2\2\2\35\36\7D\2\2\36\37\7g\2\2\37 \7")
        buf.write("u\2\2 !\7v\2\2!\"\7\"\2\2\"#\7o\2\2#$\7q\2\2$%\7f\2\2")
        buf.write("%&\7g\2\2&\'\7n\2\2\'(\7<\2\2(\4\3\2\2\2)*\7E\2\2*+\7")
        buf.write("q\2\2+,\7u\2\2,-\7v\2\2-.\7\"\2\2./\7*\2\2/\60\7]\2\2")
        buf.write("\60\61\7Y\2\2\61\62\7g\2\2\62\63\7k\2\2\63\64\7i\2\2\64")
        buf.write("\65\7j\2\2\65\66\7v\2\2\66\67\7<\2\2\678\7N\2\289\7g\2")
        buf.write("\29:\7x\2\2:;\7g\2\2;<\7n\2\2<=\7_\2\2=>\7+\2\2>?\7<\2")
        buf.write("\2?\6\3\2\2\2@A\7>\2\2AB\7]\2\2B\b\3\2\2\2CD\7_\2\2DE")
        buf.write("\7@\2\2E\n\3\2\2\2FG\7V\2\2GH\7t\2\2HI\7w\2\2IJ\7g\2\2")
        buf.write("JK\7<\2\2K\f\3\2\2\2LM\7W\2\2MN\7p\2\2NO\7f\2\2OP\7g\2")
        buf.write("\2PQ\7h\2\2QR\7k\2\2RS\7p\2\2ST\7g\2\2TU\7f\2\2UV\7<\2")
        buf.write("\2V\16\3\2\2\2WX\7}\2\2X\20\3\2\2\2YZ\7.\2\2Z\22\3\2\2")
        buf.write("\2[\\\7\177\2\2\\\24\3\2\2\2]^\7*\2\2^\26\3\2\2\2_`\7")
        buf.write("+\2\2`\30\3\2\2\2ac\t\2\2\2ba\3\2\2\2cd\3\2\2\2db\3\2")
        buf.write("\2\2de\3\2\2\2e\32\3\2\2\2fh\t\3\2\2gf\3\2\2\2hi\3\2\2")
        buf.write("\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\b\16\2\2l\34\3\2\2")
        buf.write("\2\5\2di\3\b\2\2")
        return buf.getvalue()


class DLV_OutLexer(Lexer):

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
            "'Best model:'", "'Cost ([Weight:Level]):'", "'<['", "']>'", 
            "'True:'", "'Undefined:'", "'{'", "','", "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "TEXT", "WHITESPACE" ]

    grammarFileName = "DLV_Out.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


