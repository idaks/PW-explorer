# Generated from Desktop/SPIN/ANTLR/Clingo.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\5\2\36\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\6\4+\n\4\r\4\16\4,\3\4\3\4\7\4\61\n\4\f")
        buf.write("\4\16\4\64\13\4\3\4\3\4\3\5\6\59\n\5\r\5\16\5:\3\5\3\5")
        buf.write("\6\5?\n\5\r\5\16\5@\3\5\3\5\3\6\3\6\6\6G\n\6\r\6\16\6")
        buf.write("H\3\6\3\6\7\6M\n\6\f\6\16\6P\13\6\3\6\3\6\3\7\3\7\6\7")
        buf.write("V\n\7\r\7\16\7W\3\7\3\7\7\7\\\n\7\f\7\16\7_\13\7\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2p\2\31\3")
        buf.write("\2\2\2\4!\3\2\2\2\6(\3\2\2\2\b8\3\2\2\2\nD\3\2\2\2\fS")
        buf.write("\3\2\2\2\16b\3\2\2\2\20d\3\2\2\2\22f\3\2\2\2\24n\3\2\2")
        buf.write("\2\26\30\5\22\n\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3")
        buf.write("\2\2\2\31\32\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\34\36")
        buf.write("\7\n\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37")
        buf.write(" \5\4\3\2 \3\3\2\2\2!\"\5\6\4\2\"#\5\b\5\2#$\5\n\6\2$")
        buf.write("%\5\f\7\2%&\5\16\b\2&\'\5\20\t\2\'\5\3\2\2\2(*\7\3\2\2")
        buf.write(")+\7\17\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.")
        buf.write("\3\2\2\2.\62\7\4\2\2/\61\7\17\2\2\60/\3\2\2\2\61\64\3")
        buf.write("\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62")
        buf.write("\3\2\2\2\65\66\7\26\2\2\66\7\3\2\2\2\679\7\17\2\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<>\7\5")
        buf.write("\2\2=?\7\17\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2")
        buf.write("\2AB\3\2\2\2BC\7\13\2\2C\t\3\2\2\2DF\7\6\2\2EG\7\17\2")
        buf.write("\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2J")
        buf.write("N\7\4\2\2KM\7\17\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3")
        buf.write("\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\7\f\2\2R\13\3\2\2\2SU\7\7")
        buf.write("\2\2TV\7\17\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2")
        buf.write("\2XY\3\2\2\2Y]\7\4\2\2Z\\\7\17\2\2[Z\3\2\2\2\\_\3\2\2")
        buf.write("\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7\r\2\2a")
        buf.write("\r\3\2\2\2bc\7\16\2\2c\17\3\2\2\2de\7\16\2\2e\21\3\2\2")
        buf.write("\2fg\7\b\2\2gh\7\23\2\2hi\7\20\2\2ij\5\24\13\2jk\7\20")
        buf.write("\2\2kl\7\t\2\2lm\7\24\2\2m\23\3\2\2\2no\7\25\2\2o\25\3")
        buf.write("\2\2\2\f\31\35,\62:@HNW]")
        return buf.getvalue()


class ClingoParser ( Parser ):

    grammarFileName = "Clingo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Models'", "':'", "'Optium'", "'Optimization'", 
                     "'Calls'", "'Answer:'", "'Optimization:'", "'OPTIUM FOUND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "OPTIUM_FOUND", "OPTIUM_FOUND_OR_NOT", "OPTIMAL_SOLN", 
                      "NUM_CALLS", "TEXT", "SPACE", "NEWLINE", "Word", "WHITESPACE", 
                      "ANS_NUM", "CURR_SOLN", "STUFF", "NUM_MODELS" ]

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

    ruleNames =  [ "clingoOutput", "summary", "models", "optium", "optimization", 
                   "calls", "time", "cpuTime", "solution", "actual_soln" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    OPTIUM_FOUND=8
    OPTIUM_FOUND_OR_NOT=9
    OPTIMAL_SOLN=10
    NUM_CALLS=11
    TEXT=12
    SPACE=13
    NEWLINE=14
    Word=15
    WHITESPACE=16
    ANS_NUM=17
    CURR_SOLN=18
    STUFF=19
    NUM_MODELS=20

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.T__5:
                self.state = 20
                self.solution()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.OPTIUM_FOUND:
                self.state = 26
                self.match(ClingoParser.OPTIUM_FOUND)


            self.state = 29
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
            self.state = 31
            self.models()
            self.state = 32
            self.optium()
            self.state = 33
            self.optimization()
            self.state = 34
            self.calls()
            self.state = 35
            self.time()
            self.state = 36
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
            self.state = 38
            self.match(ClingoParser.T__0)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.match(ClingoParser.SPACE)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 44
            self.match(ClingoParser.T__1)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 45
                self.match(ClingoParser.SPACE)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.match(ClingoParser.SPACE)
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 58
            self.match(ClingoParser.T__2)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(ClingoParser.SPACE)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 64
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
            self.state = 66
            self.match(ClingoParser.T__3)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.match(ClingoParser.SPACE)
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 72
            self.match(ClingoParser.T__1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 73
                self.match(ClingoParser.SPACE)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
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
            self.state = 81
            self.match(ClingoParser.T__4)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.match(ClingoParser.SPACE)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClingoParser.SPACE):
                    break

            self.state = 87
            self.match(ClingoParser.T__1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.SPACE:
                self.state = 88
                self.match(ClingoParser.SPACE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
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
            self.state = 96
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
            self.state = 98
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
            self.state = 100
            self.match(ClingoParser.T__5)
            self.state = 101
            self.match(ClingoParser.ANS_NUM)

            self.state = 102
            self.match(ClingoParser.NEWLINE)
            self.state = 103
            self.actual_soln()

            self.state = 104
            self.match(ClingoParser.NEWLINE)
            self.state = 105
            self.match(ClingoParser.T__6)
            self.state = 106
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

        def STUFF(self):
            return self.getToken(ClingoParser.STUFF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ClingoParser.STUFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





