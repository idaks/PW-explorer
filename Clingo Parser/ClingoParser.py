# Generated from PW-explorer/Clingo Parser/Clingo.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u0084\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write("\n\2\f\2\16\2\35\13\2\3\2\5\2 \n\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\6\4-\n\4\r\4\16\4.\3\4\3\4\7")
        buf.write("\4\63\n\4\f\4\16\4\66\13\4\3\4\3\4\3\5\6\5;\n\5\r\5\16")
        buf.write("\5<\3\5\3\5\6\5A\n\5\r\5\16\5B\3\5\3\5\3\6\3\6\6\6I\n")
        buf.write("\6\r\6\16\6J\3\6\3\6\7\6O\n\6\f\6\16\6R\13\6\3\6\3\6\3")
        buf.write("\7\3\7\6\7X\n\7\r\7\16\7Y\3\7\3\7\7\7^\n\7\f\7\16\7a\13")
        buf.write("\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\7\13v\n\13\f\13\16\13y\13")
        buf.write("\13\3\f\3\f\7\f}\n\f\f\f\16\f\u0080\13\f\3\f\3\f\3\f\2")
        buf.write("\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2\u0084\2\33\3\2\2")
        buf.write("\2\4#\3\2\2\2\6*\3\2\2\2\b:\3\2\2\2\nF\3\2\2\2\fU\3\2")
        buf.write("\2\2\16d\3\2\2\2\20f\3\2\2\2\22h\3\2\2\2\24w\3\2\2\2\26")
        buf.write("~\3\2\2\2\30\32\5\22\n\2\31\30\3\2\2\2\32\35\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2")
        buf.write("\36 \7\r\2\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\5")
        buf.write("\4\3\2\"\3\3\2\2\2#$\5\6\4\2$%\5\b\5\2%&\5\n\6\2&\'\5")
        buf.write("\f\7\2\'(\5\16\b\2()\5\20\t\2)\5\3\2\2\2*,\7\3\2\2+-\7")
        buf.write("\23\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\60\3")
        buf.write("\2\2\2\60\64\7\4\2\2\61\63\7\23\2\2\62\61\3\2\2\2\63\66")
        buf.write("\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66")
        buf.write("\64\3\2\2\2\678\7\16\2\28\7\3\2\2\29;\7\23\2\2:9\3\2\2")
        buf.write("\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>@\7\5\2\2?")
        buf.write("A\7\23\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3")
        buf.write("\2\2\2DE\7\17\2\2E\t\3\2\2\2FH\7\6\2\2GI\7\23\2\2HG\3")
        buf.write("\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LP\7\4\2")
        buf.write("\2MO\7\23\2\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2")
        buf.write("QS\3\2\2\2RP\3\2\2\2ST\7\20\2\2T\13\3\2\2\2UW\7\7\2\2")
        buf.write("VX\7\23\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[")
        buf.write("\3\2\2\2[_\7\4\2\2\\^\7\23\2\2]\\\3\2\2\2^a\3\2\2\2_]")
        buf.write("\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3\2\2\2bc\7\21\2\2c\r\3")
        buf.write("\2\2\2de\7\22\2\2e\17\3\2\2\2fg\7\22\2\2g\21\3\2\2\2h")
        buf.write("i\7\b\2\2ij\7\27\2\2jk\7\24\2\2kl\5\24\13\2lm\7\24\2\2")
        buf.write("mn\7\t\2\2no\7\30\2\2o\23\3\2\2\2pq\7\31\2\2qr\7\n\2\2")
        buf.write("rs\5\26\f\2st\7\13\2\2tv\3\2\2\2up\3\2\2\2vy\3\2\2\2w")
        buf.write("u\3\2\2\2wx\3\2\2\2x\25\3\2\2\2yw\3\2\2\2z{\7\25\2\2{")
        buf.write("}\7\f\2\2|z\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2")
        buf.write("\2\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7\25")
        buf.write("\2\2\u0082\27\3\2\2\2\16\33\37.\64<BJPY_w~")
        return buf.getvalue()


class ClingoParser ( Parser ):

    grammarFileName = "Clingo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Models'", "':'", "'Optium'", "'Optimization'", 
                     "'Calls'", "'Answer:'", "'Optimization:'", "'('", "')'", 
                     "','", "'OPTIUM FOUND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OPTIUM_FOUND", 
                      "NUM_MODELS", "OPTIUM_FOUND_OR_NOT", "OPTIMAL_SOLN", 
                      "NUM_CALLS", "TEXT", "SPACE", "NEWLINE", "Word", "WHITESPACE", 
                      "ANS_NUM", "CURR_SOLN", "KEYWORD" ]

    RULE_clingoOutput = 0
    RULE_summary = 1
    RULE_models = 2
    RULE_optium = 3
    RULE_optimization = 4
    RULE_calls = 5
    RULE_time = 6
    RULE_cpuTime = 7
    RULE_solution = 8
    RULE_actual_soln = 9
    RULE_custom_representation_soln = 10

    ruleNames =  [ "clingoOutput", "summary", "models", "optium", "optimization", 
                   "calls", "time", "cpuTime", "solution", "actual_soln", 
                   "custom_representation_soln" ]

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
    OPTIUM_FOUND=11
    NUM_MODELS=12
    OPTIUM_FOUND_OR_NOT=13
    OPTIMAL_SOLN=14
    NUM_CALLS=15
    TEXT=16
    SPACE=17
    NEWLINE=18
    Word=19
    WHITESPACE=20
    ANS_NUM=21
    CURR_SOLN=22
    KEYWORD=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ClingoOutputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def summary(self):
            return self.getTypedRuleContext(ClingoParser.SummaryContext,0)


        def solution(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.SolutionContext)
            else:
                return self.getTypedRuleContext(ClingoParser.SolutionContext,i)


        def OPTIUM_FOUND(self):
            return self.getToken(ClingoParser.OPTIUM_FOUND, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_clingoOutput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClingoOutput" ):
                listener.enterClingoOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClingoOutput" ):
                listener.exitClingoOutput(self)




    def clingoOutput(self):

        localctx = ClingoParser.ClingoOutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_clingoOutput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.T__5:
                self.state = 22
                self.solution()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.OPTIUM_FOUND:
                self.state = 28
                self.match(ClingoParser.OPTIUM_FOUND)


            self.state = 31
            self.summary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SummaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def models(self):
            return self.getTypedRuleContext(ClingoParser.ModelsContext,0)


        def optium(self):
            return self.getTypedRuleContext(ClingoParser.OptiumContext,0)


        def optimization(self):
            return self.getTypedRuleContext(ClingoParser.OptimizationContext,0)


        def calls(self):
            return self.getTypedRuleContext(ClingoParser.CallsContext,0)


        def time(self):
            return self.getTypedRuleContext(ClingoParser.TimeContext,0)


        def cpuTime(self):
            return self.getTypedRuleContext(ClingoParser.CpuTimeContext,0)


        def getRuleIndex(self):
            return ClingoParser.RULE_summary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummary" ):
                listener.enterSummary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummary" ):
                listener.exitSummary(self)




    def summary(self):

        localctx = ClingoParser.SummaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.models()
            self.state = 34
            self.optium()
            self.state = 35
            self.optimization()
            self.state = 36
            self.calls()
            self.state = 37
            self.time()
            self.state = 38
            self.cpuTime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_MODELS(self):
            return self.getToken(ClingoParser.NUM_MODELS, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.SPACE)
            else:
                return self.getToken(ClingoParser.SPACE, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_models

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModels" ):
                listener.enterModels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModels" ):
                listener.exitModels(self)




    def models(self):

        localctx = ClingoParser.ModelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_models)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ClingoParser.T__0)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.match(ClingoParser.SPACE)
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 46
            self.match(ClingoParser.T__1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 47
                self.match(ClingoParser.SPACE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(ClingoParser.NUM_MODELS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptiumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIUM_FOUND_OR_NOT(self):
            return self.getToken(ClingoParser.OPTIUM_FOUND_OR_NOT, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.SPACE)
            else:
                return self.getToken(ClingoParser.SPACE, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_optium

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptium" ):
                listener.enterOptium(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptium" ):
                listener.exitOptium(self)




    def optium(self):

        localctx = ClingoParser.OptiumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optium)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.match(ClingoParser.SPACE)
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 60
            self.match(ClingoParser.T__2)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.match(ClingoParser.SPACE)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 66
            self.match(ClingoParser.OPTIUM_FOUND_OR_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimizationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIMAL_SOLN(self):
            return self.getToken(ClingoParser.OPTIMAL_SOLN, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.SPACE)
            else:
                return self.getToken(ClingoParser.SPACE, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_optimization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimization" ):
                listener.enterOptimization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimization" ):
                listener.exitOptimization(self)




    def optimization(self):

        localctx = ClingoParser.OptimizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optimization)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ClingoParser.T__3)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.match(ClingoParser.SPACE)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 74
            self.match(ClingoParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 75
                self.match(ClingoParser.SPACE)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(ClingoParser.OPTIMAL_SOLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_CALLS(self):
            return self.getToken(ClingoParser.NUM_CALLS, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.SPACE)
            else:
                return self.getToken(ClingoParser.SPACE, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_calls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalls" ):
                listener.enterCalls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalls" ):
                listener.exitCalls(self)




    def calls(self):

        localctx = ClingoParser.CallsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_calls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ClingoParser.T__4)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.match(ClingoParser.SPACE)
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 89
            self.match(ClingoParser.T__1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 90
                self.match(ClingoParser.SPACE)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(ClingoParser.NUM_CALLS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = ClingoParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CpuTimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_cpuTime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCpuTime" ):
                listener.enterCpuTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCpuTime" ):
                listener.exitCpuTime(self)




    def cpuTime(self):

        localctx = ClingoParser.CpuTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cpuTime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SolutionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANS_NUM(self):
            return self.getToken(ClingoParser.ANS_NUM, 0)

        def actual_soln(self):
            return self.getTypedRuleContext(ClingoParser.Actual_solnContext,0)


        def CURR_SOLN(self):
            return self.getToken(ClingoParser.CURR_SOLN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.NEWLINE)
            else:
                return self.getToken(ClingoParser.NEWLINE, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_solution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSolution" ):
                listener.enterSolution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSolution" ):
                listener.exitSolution(self)




    def solution(self):

        localctx = ClingoParser.SolutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_solution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ClingoParser.T__5)
            self.state = 103
            self.match(ClingoParser.ANS_NUM)

            self.state = 104
            self.match(ClingoParser.NEWLINE)
            self.state = 105
            self.actual_soln()

            self.state = 106
            self.match(ClingoParser.NEWLINE)
            self.state = 107
            self.match(ClingoParser.T__6)
            self.state = 108
            self.match(ClingoParser.CURR_SOLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Actual_solnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.KEYWORD)
            else:
                return self.getToken(ClingoParser.KEYWORD, i)

        def custom_representation_soln(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.Custom_representation_solnContext)
            else:
                return self.getTypedRuleContext(ClingoParser.Custom_representation_solnContext,i)


        def getRuleIndex(self):
            return ClingoParser.RULE_actual_soln

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_soln" ):
                listener.enterActual_soln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_soln" ):
                listener.exitActual_soln(self)




    def actual_soln(self):

        localctx = ClingoParser.Actual_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_actual_soln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.KEYWORD:
                self.state = 110
                self.match(ClingoParser.KEYWORD)
                self.state = 111
                self.match(ClingoParser.T__7)
                self.state = 112
                self.custom_representation_soln()
                self.state = 113
                self.match(ClingoParser.T__8)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Custom_representation_solnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Word(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.Word)
            else:
                return self.getToken(ClingoParser.Word, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_custom_representation_soln

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCustom_representation_soln" ):
                listener.enterCustom_representation_soln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCustom_representation_soln" ):
                listener.exitCustom_representation_soln(self)




    def custom_representation_soln(self):

        localctx = ClingoParser.Custom_representation_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_custom_representation_soln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.match(ClingoParser.Word)
                    self.state = 121
                    self.match(ClingoParser.T__9) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 127
            self.match(ClingoParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





