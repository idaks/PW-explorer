# Generated from Dlv.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\t\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\5\3")
        buf.write(u"\5\3\5\3\5\7\5(\n\5\f\5\16\5+\13\5\3\5\3\5\3\6\3\6\3")
        buf.write(u"\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2/\2\21\3\2\2\2\4\24")
        buf.write(u"\3\2\2\2\6\30\3\2\2\2\b#\3\2\2\2\n.\3\2\2\2\f\60\3\2")
        buf.write(u"\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17")
        buf.write(u"\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\24")
        buf.write(u"\25\7\3\2\2\25\26\5\6\4\2\26\27\7\4\2\2\27\5\3\2\2\2")
        buf.write(u"\30\31\5\f\7\2\31 \5\b\5\2\32\33\7\5\2\2\33\34\5\f\7")
        buf.write(u"\2\34\35\5\b\5\2\35\37\3\2\2\2\36\32\3\2\2\2\37\"\3\2")
        buf.write(u"\2\2 \36\3\2\2\2 !\3\2\2\2!\7\3\2\2\2\" \3\2\2\2#$\7")
        buf.write(u"\6\2\2$)\5\n\6\2%&\7\5\2\2&(\5\n\6\2\'%\3\2\2\2(+\3\2")
        buf.write(u"\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2\2,-\7\7\2")
        buf.write(u"\2-\t\3\2\2\2./\7\b\2\2/\13\3\2\2\2\60\61\7\b\2\2\61")
        buf.write(u"\r\3\2\2\2\5\21 )")
        return buf.getvalue()


class DlvParser ( Parser ):

    grammarFileName = "Dlv.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"','", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"TEXT", u"WS" ]

    RULE_dlvOutput = 0
    RULE_solution = 1
    RULE_atoms = 2
    RULE_atom_vals = 3
    RULE_val = 4
    RULE_atom = 5

    ruleNames =  [ u"dlvOutput", u"solution", u"atoms", u"atom_vals", u"val", 
                   u"atom" ]

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



    class DlvOutputContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.DlvOutputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def solution(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DlvParser.SolutionContext)
            else:
                return self.getTypedRuleContext(DlvParser.SolutionContext,i)


        def getRuleIndex(self):
            return DlvParser.RULE_dlvOutput

        def enterRule(self, listener):
            if hasattr(listener, "enterDlvOutput"):
                listener.enterDlvOutput(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDlvOutput"):
                listener.exitDlvOutput(self)




    def dlvOutput(self):

        localctx = DlvParser.DlvOutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dlvOutput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DlvParser.T__0:
                self.state = 12
                self.solution()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SolutionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DlvParser.SolutionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atoms(self):
            return self.getTypedRuleContext(DlvParser.AtomsContext,0)


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
        self.enterRule(localctx, 2, self.RULE_solution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(DlvParser.T__0)
            self.state = 19
            self.atoms()
            self.state = 20
            self.match(DlvParser.T__1)
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

        def atom(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DlvParser.AtomContext)
            else:
                return self.getTypedRuleContext(DlvParser.AtomContext,i)


        def atom_vals(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DlvParser.Atom_valsContext)
            else:
                return self.getTypedRuleContext(DlvParser.Atom_valsContext,i)


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
        self.enterRule(localctx, 4, self.RULE_atoms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.atom()
            self.state = 23
            self.atom_vals()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DlvParser.T__2:
                self.state = 24
                self.match(DlvParser.T__2)
                self.state = 25
                self.atom()
                self.state = 26
                self.atom_vals()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_atom_vals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(DlvParser.T__3)
            self.state = 34
            self.val()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DlvParser.T__2:
                self.state = 35
                self.match(DlvParser.T__2)
                self.state = 36
                self.val()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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
        self.enterRule(localctx, 8, self.RULE_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
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
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(DlvParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





