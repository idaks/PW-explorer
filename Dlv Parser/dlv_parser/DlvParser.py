# Generated from Dlv.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\t*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write(u"\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\3\3\3\3")
        buf.write(u"\3\3\4\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\4\3\4")
        buf.write(u"\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2&\2\f\3\2\2")
        buf.write(u"\2\4\27\3\2\2\2\6\32\3\2\2\2\b%\3\2\2\2\n\'\3\2\2\2\f")
        buf.write(u"\r\7\3\2\2\r\22\5\4\3\2\16\17\7\4\2\2\17\21\5\4\3\2\20")
        buf.write(u"\16\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2")
        buf.write(u"\23\25\3\2\2\2\24\22\3\2\2\2\25\26\7\5\2\2\26\3\3\2\2")
        buf.write(u"\2\27\30\5\n\6\2\30\31\5\6\4\2\31\5\3\2\2\2\32\33\7\6")
        buf.write(u"\2\2\33 \5\b\5\2\34\35\7\4\2\2\35\37\5\b\5\2\36\34\3")
        buf.write(u"\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\"")
        buf.write(u" \3\2\2\2#$\7\7\2\2$\7\3\2\2\2%&\7\b\2\2&\t\3\2\2\2\'")
        buf.write(u"(\7\b\2\2(\13\3\2\2\2\4\22 ")
        return buf.getvalue()


class DlvParser ( Parser ):

    grammarFileName = "Dlv.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"','", u"'}'", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"TEXT", u"WS" ]

    RULE_solution = 0
    RULE_atoms = 1
    RULE_atom_vals = 2
    RULE_val = 3
    RULE_atom = 4

    ruleNames =  [ u"solution", u"atoms", u"atom_vals", u"val", u"atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    TEXT=6
    WS=7

    def __init__(self, input, output=sys.stdout):
        super(DlvParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SolutionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.SolutionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atoms(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DlvParser.AtomsContext)
            else:
                return self.getTypedRuleContext(DlvParser.AtomsContext,i)


        def getRuleIndex(self):
            return DlvParser.RULE_solution

        def enterRule(self, listener):
            if hasattr(listener, "enterSolution"):
                listener.enterSolution(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSolution"):
                listener.exitSolution(self)




    def solution(self):

        localctx = DlvParser.SolutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_solution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(DlvParser.T__0)
            self.state = 11
            self.atoms()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DlvParser.T__1:
                self.state = 12
                self.match(DlvParser.T__1)
                self.state = 13
                self.atoms()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(DlvParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.AtomsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(DlvParser.AtomContext,0)


        def atom_vals(self):
            return self.getTypedRuleContext(DlvParser.Atom_valsContext,0)


        def getRuleIndex(self):
            return DlvParser.RULE_atoms

        def enterRule(self, listener):
            if hasattr(listener, "enterAtoms"):
                listener.enterAtoms(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtoms"):
                listener.exitAtoms(self)




    def atoms(self):

        localctx = DlvParser.AtomsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_atoms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.atom()
            self.state = 22
            self.atom_vals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_valsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.Atom_valsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def val(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DlvParser.ValContext)
            else:
                return self.getTypedRuleContext(DlvParser.ValContext,i)


        def getRuleIndex(self):
            return DlvParser.RULE_atom_vals

        def enterRule(self, listener):
            if hasattr(listener, "enterAtom_vals"):
                listener.enterAtom_vals(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtom_vals"):
                listener.exitAtom_vals(self)




    def atom_vals(self):

        localctx = DlvParser.Atom_valsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom_vals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(DlvParser.T__3)
            self.state = 25
            self.val()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DlvParser.T__1:
                self.state = 26
                self.match(DlvParser.T__1)
                self.state = 27
                self.val()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(DlvParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.ValContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(DlvParser.TEXT, 0)

        def getRuleIndex(self):
            return DlvParser.RULE_val

        def enterRule(self, listener):
            if hasattr(listener, "enterVal"):
                listener.enterVal(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVal"):
                listener.exitVal(self)




    def val(self):

        localctx = DlvParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(DlvParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.AtomContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(DlvParser.TEXT, 0)

        def getRuleIndex(self):
            return DlvParser.RULE_atom

        def enterRule(self, listener):
            if hasattr(listener, "enterAtom"):
                listener.enterAtom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAtom"):
                listener.exitAtom(self)




    def atom(self):

        localctx = DlvParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(DlvParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





