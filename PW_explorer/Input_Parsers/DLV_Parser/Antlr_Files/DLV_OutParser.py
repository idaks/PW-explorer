# Generated from DLV_Out.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\5\2\32\n\2")
        buf.write("\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\5\5\5%\n\5\3")
        buf.write("\5\5\5(\n\5\3\6\6\6+\n\6\r\6\16\6,\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n@")
        buf.write("\n\n\f\n\16\nC\13\n\3\n\5\nF\n\n\3\n\3\n\3\13\6\13K\n")
        buf.write("\13\r\13\16\13L\3\13\3\13\3\13\5\13R\n\13\3\13\2\2\f\2")
        buf.write("\4\6\b\n\f\16\20\22\24\2\2\2T\2\31\3\2\2\2\4\36\3\2\2")
        buf.write("\2\6!\3\2\2\2\b$\3\2\2\2\n*\3\2\2\2\f.\3\2\2\2\16\65\3")
        buf.write("\2\2\2\208\3\2\2\2\22;\3\2\2\2\24J\3\2\2\2\26\32\5\4\3")
        buf.write("\2\27\32\5\b\5\2\30\32\5\n\6\2\31\26\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\35\5")
        buf.write("\6\4\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3")
        buf.write("\2\2\2\37\5\3\2\2\2 \36\3\2\2\2!\"\5\22\n\2\"\7\3\2\2")
        buf.write("\2#%\5\16\b\2$#\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&(\5\20\t")
        buf.write("\2\'&\3\2\2\2\'(\3\2\2\2(\t\3\2\2\2)+\5\f\7\2*)\3\2\2")
        buf.write("\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\13\3\2\2\2./\7\3\2\2")
        buf.write("/\60\5\22\n\2\60\61\7\4\2\2\61\62\7\5\2\2\62\63\7\16\2")
        buf.write("\2\63\64\7\6\2\2\64\r\3\2\2\2\65\66\7\7\2\2\66\67\5\22")
        buf.write("\n\2\67\17\3\2\2\289\7\b\2\29:\5\22\n\2:\21\3\2\2\2;E")
        buf.write("\7\t\2\2<=\5\24\13\2=>\7\n\2\2>@\3\2\2\2?<\3\2\2\2@C\3")
        buf.write("\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DF\5\24")
        buf.write("\13\2EA\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\7\13\2\2H\23\3\2")
        buf.write("\2\2IK\7\16\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2")
        buf.write("\2MQ\3\2\2\2NO\7\f\2\2OP\7\16\2\2PR\7\r\2\2QN\3\2\2\2")
        buf.write("QR\3\2\2\2R\25\3\2\2\2\13\31\36$\',AELQ")
        return buf.getvalue()


class DLV_OutParser ( Parser ):

    grammarFileName = "DLV_Out.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Best model:'", "'Cost ([Weight:Level]):'", 
                     "'<['", "']>'", "'True:'", "'Undefined:'", "'{'", "','", 
                     "'}'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "WHITESPACE" ]

    RULE_dlvOutput = 0
    RULE_pws_out = 1
    RULE_pw = 2
    RULE_wf_mode_out = 3
    RULE_optimization_out = 4
    RULE_opt_model = 5
    RULE_true_part = 6
    RULE_undefined_part = 7
    RULE_atom_set = 8
    RULE_atom = 9

    ruleNames =  [ "dlvOutput", "pws_out", "pw", "wf_mode_out", "optimization_out", 
                   "opt_model", "true_part", "undefined_part", "atom_set", 
                   "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    TEXT=12
    WHITESPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DlvOutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pws_out(self):
            return self.getTypedRuleContext(DLV_OutParser.Pws_outContext,0)


        def wf_mode_out(self):
            return self.getTypedRuleContext(DLV_OutParser.Wf_mode_outContext,0)


        def optimization_out(self):
            return self.getTypedRuleContext(DLV_OutParser.Optimization_outContext,0)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_dlvOutput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDlvOutput" ):
                listener.enterDlvOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDlvOutput" ):
                listener.exitDlvOutput(self)




    def dlvOutput(self):

        localctx = DLV_OutParser.DlvOutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dlvOutput)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 20
                self.pws_out()

            elif la_ == 2:
                self.state = 21
                self.wf_mode_out()

            elif la_ == 3:
                self.state = 22
                self.optimization_out()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pws_outContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_OutParser.PwContext)
            else:
                return self.getTypedRuleContext(DLV_OutParser.PwContext,i)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_pws_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPws_out" ):
                listener.enterPws_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPws_out" ):
                listener.exitPws_out(self)




    def pws_out(self):

        localctx = DLV_OutParser.Pws_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pws_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLV_OutParser.T__6:
                self.state = 25
                self.pw()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PwContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_set(self):
            return self.getTypedRuleContext(DLV_OutParser.Atom_setContext,0)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_pw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPw" ):
                listener.enterPw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPw" ):
                listener.exitPw(self)




    def pw(self):

        localctx = DLV_OutParser.PwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.atom_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Wf_mode_outContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def true_part(self):
            return self.getTypedRuleContext(DLV_OutParser.True_partContext,0)


        def undefined_part(self):
            return self.getTypedRuleContext(DLV_OutParser.Undefined_partContext,0)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_wf_mode_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWf_mode_out" ):
                listener.enterWf_mode_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWf_mode_out" ):
                listener.exitWf_mode_out(self)




    def wf_mode_out(self):

        localctx = DLV_OutParser.Wf_mode_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_wf_mode_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLV_OutParser.T__4:
                self.state = 33
                self.true_part()


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLV_OutParser.T__5:
                self.state = 36
                self.undefined_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Optimization_outContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opt_model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_OutParser.Opt_modelContext)
            else:
                return self.getTypedRuleContext(DLV_OutParser.Opt_modelContext,i)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_optimization_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimization_out" ):
                listener.enterOptimization_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimization_out" ):
                listener.exitOptimization_out(self)




    def optimization_out(self):

        localctx = DLV_OutParser.Optimization_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optimization_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.opt_model()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DLV_OutParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Opt_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_set(self):
            return self.getTypedRuleContext(DLV_OutParser.Atom_setContext,0)


        def TEXT(self):
            return self.getToken(DLV_OutParser.TEXT, 0)

        def getRuleIndex(self):
            return DLV_OutParser.RULE_opt_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_model" ):
                listener.enterOpt_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_model" ):
                listener.exitOpt_model(self)




    def opt_model(self):

        localctx = DLV_OutParser.Opt_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opt_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(DLV_OutParser.T__0)
            self.state = 45
            self.atom_set()
            self.state = 46
            self.match(DLV_OutParser.T__1)
            self.state = 47
            self.match(DLV_OutParser.T__2)
            self.state = 48
            self.match(DLV_OutParser.TEXT)
            self.state = 49
            self.match(DLV_OutParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class True_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_set(self):
            return self.getTypedRuleContext(DLV_OutParser.Atom_setContext,0)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_true_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue_part" ):
                listener.enterTrue_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue_part" ):
                listener.exitTrue_part(self)




    def true_part(self):

        localctx = DLV_OutParser.True_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_true_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(DLV_OutParser.T__4)
            self.state = 52
            self.atom_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Undefined_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_set(self):
            return self.getTypedRuleContext(DLV_OutParser.Atom_setContext,0)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_undefined_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUndefined_part" ):
                listener.enterUndefined_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUndefined_part" ):
                listener.exitUndefined_part(self)




    def undefined_part(self):

        localctx = DLV_OutParser.Undefined_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_undefined_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(DLV_OutParser.T__5)
            self.state = 55
            self.atom_set()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_setContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_OutParser.AtomContext)
            else:
                return self.getTypedRuleContext(DLV_OutParser.AtomContext,i)


        def getRuleIndex(self):
            return DLV_OutParser.RULE_atom_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_set" ):
                listener.enterAtom_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_set" ):
                listener.exitAtom_set(self)




    def atom_set(self):

        localctx = DLV_OutParser.Atom_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_atom_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(DLV_OutParser.T__6)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLV_OutParser.TEXT:
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 58
                        self.atom()
                        self.state = 59
                        self.match(DLV_OutParser.T__7) 
                    self.state = 65
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 66
                self.atom()


            self.state = 69
            self.match(DLV_OutParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(DLV_OutParser.TEXT)
            else:
                return self.getToken(DLV_OutParser.TEXT, i)

        def getRuleIndex(self):
            return DLV_OutParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = DLV_OutParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.match(DLV_OutParser.TEXT)
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DLV_OutParser.TEXT):
                    break

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLV_OutParser.T__9:
                self.state = 76
                self.match(DLV_OutParser.T__9)
                self.state = 77
                self.match(DLV_OutParser.TEXT)
                self.state = 78
                self.match(DLV_OutParser.T__10)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





