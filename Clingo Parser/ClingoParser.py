# Generated from PW-explorer/Clingo Parser/Clingo.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\27W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write(u"\n\2\f\2\16\2\35\13\2\3\2\5\2 \n\2\3\2\3\2\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13I\n\13\f")
        buf.write(u"\13\16\13L\13\13\3\f\3\f\7\fP\n\f\f\f\16\fS\13\f\3\f")
        buf.write(u"\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2O\2\33")
        buf.write(u"\3\2\2\2\4#\3\2\2\2\6*\3\2\2\2\b.\3\2\2\2\n\61\3\2\2")
        buf.write(u"\2\f\65\3\2\2\2\169\3\2\2\2\20;\3\2\2\2\22=\3\2\2\2\24")
        buf.write(u"J\3\2\2\2\26Q\3\2\2\2\30\32\5\22\n\2\31\30\3\2\2\2\32")
        buf.write(u"\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\37\3\2\2\2")
        buf.write(u"\35\33\3\2\2\2\36 \7\27\2\2\37\36\3\2\2\2\37 \3\2\2\2")
        buf.write(u" !\3\2\2\2!\"\5\4\3\2\"\3\3\2\2\2#$\5\6\4\2$%\5\b\5\2")
        buf.write(u"%&\5\n\6\2&\'\5\f\7\2\'(\5\16\b\2()\5\20\t\2)\5\3\2\2")
        buf.write(u"\2*+\7\3\2\2+,\7\4\2\2,-\7\r\2\2-\7\3\2\2\2./\7\5\2\2")
        buf.write(u"/\60\7\16\2\2\60\t\3\2\2\2\61\62\7\6\2\2\62\63\7\4\2")
        buf.write(u"\2\63\64\7\17\2\2\64\13\3\2\2\2\65\66\7\7\2\2\66\67\7")
        buf.write(u"\4\2\2\678\7\20\2\28\r\3\2\2\29:\7\21\2\2:\17\3\2\2\2")
        buf.write(u";<\7\21\2\2<\21\3\2\2\2=>\7\b\2\2>?\7\24\2\2?@\5\24\13")
        buf.write(u"\2@A\7\t\2\2AB\7\25\2\2B\23\3\2\2\2CD\7\26\2\2DE\7\n")
        buf.write(u"\2\2EF\5\26\f\2FG\7\13\2\2GI\3\2\2\2HC\3\2\2\2IL\3\2")
        buf.write(u"\2\2JH\3\2\2\2JK\3\2\2\2K\25\3\2\2\2LJ\3\2\2\2MN\7\22")
        buf.write(u"\2\2NP\7\f\2\2OM\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2")
        buf.write(u"\2RT\3\2\2\2SQ\3\2\2\2TU\7\22\2\2U\27\3\2\2\2\6\33\37")
        buf.write(u"JQ")
        return buf.getvalue()


class ClingoParser ( Parser ):

    grammarFileName = "Clingo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'Models'", u"':'", u"'Optium'", u"'Optimization'", 
                     u"'Calls'", u"'Answer:'", u"'Optimization:'", u"'('", 
                     u"')'", u"','", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'OPTIUM FOUND'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"NUM_MODELS", 
                      u"OPTIUM_FOUND_OR_NOT", u"OPTIMAL_SOLN", u"NUM_CALLS", 
                      u"TEXT", u"Word", u"WHITESPACE", u"ANS_NUM", u"CURR_SOLN", 
                      u"RELATION_NAME", u"OPTIUM_FOUND" ]

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

    ruleNames =  [ u"clingoOutput", u"summary", u"models", u"optium", u"optimization", 
                   u"calls", u"time", u"cpuTime", u"solution", u"actual_soln", 
                   u"custom_representation_soln" ]

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
    NUM_MODELS=11
    OPTIUM_FOUND_OR_NOT=12
    OPTIMAL_SOLN=13
    NUM_CALLS=14
    TEXT=15
    Word=16
    WHITESPACE=17
    ANS_NUM=18
    CURR_SOLN=19
    RELATION_NAME=20
    OPTIUM_FOUND=21

    def __init__(self, input, output=sys.stdout):
        super(ClingoParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ClingoOutputContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.ClingoOutputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def summary(self):
            return self.getTypedRuleContext(ClingoParser.SummaryContext,0)


        def solution(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.SolutionContext)
            else:
                return self.getTypedRuleContext(ClingoParser.SolutionContext,i)


        def OPTIUM_FOUND(self):
            return self.getToken(ClingoParser.OPTIUM_FOUND, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_clingoOutput

        def enterRule(self, listener):
            if hasattr(listener, "enterClingoOutput"):
                listener.enterClingoOutput(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClingoOutput"):
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.SummaryContext, self).__init__(parent, invokingState)
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

        def enterRule(self, listener):
            if hasattr(listener, "enterSummary"):
                listener.enterSummary(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSummary"):
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.ModelsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUM_MODELS(self):
            return self.getToken(ClingoParser.NUM_MODELS, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_models

        def enterRule(self, listener):
            if hasattr(listener, "enterModels"):
                listener.enterModels(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModels"):
                listener.exitModels(self)




    def models(self):

        localctx = ClingoParser.ModelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_models)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ClingoParser.T__0)
            self.state = 41
            self.match(ClingoParser.T__1)
            self.state = 42
            self.match(ClingoParser.NUM_MODELS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptiumContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.OptiumContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OPTIUM_FOUND_OR_NOT(self):
            return self.getToken(ClingoParser.OPTIUM_FOUND_OR_NOT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_optium

        def enterRule(self, listener):
            if hasattr(listener, "enterOptium"):
                listener.enterOptium(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOptium"):
                listener.exitOptium(self)




    def optium(self):

        localctx = ClingoParser.OptiumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optium)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ClingoParser.T__2)
            self.state = 45
            self.match(ClingoParser.OPTIUM_FOUND_OR_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimizationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.OptimizationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OPTIMAL_SOLN(self):
            return self.getToken(ClingoParser.OPTIMAL_SOLN, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_optimization

        def enterRule(self, listener):
            if hasattr(listener, "enterOptimization"):
                listener.enterOptimization(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOptimization"):
                listener.exitOptimization(self)




    def optimization(self):

        localctx = ClingoParser.OptimizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optimization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ClingoParser.T__3)
            self.state = 48
            self.match(ClingoParser.T__1)
            self.state = 49
            self.match(ClingoParser.OPTIMAL_SOLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.CallsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUM_CALLS(self):
            return self.getToken(ClingoParser.NUM_CALLS, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_calls

        def enterRule(self, listener):
            if hasattr(listener, "enterCalls"):
                listener.enterCalls(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCalls"):
                listener.exitCalls(self)




    def calls(self):

        localctx = ClingoParser.CallsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_calls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ClingoParser.T__4)
            self.state = 52
            self.match(ClingoParser.T__1)
            self.state = 53
            self.match(ClingoParser.NUM_CALLS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.TimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_time

        def enterRule(self, listener):
            if hasattr(listener, "enterTime"):
                listener.enterTime(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime"):
                listener.exitTime(self)




    def time(self):

        localctx = ClingoParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CpuTimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.CpuTimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_cpuTime

        def enterRule(self, listener):
            if hasattr(listener, "enterCpuTime"):
                listener.enterCpuTime(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCpuTime"):
                listener.exitCpuTime(self)




    def cpuTime(self):

        localctx = ClingoParser.CpuTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cpuTime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SolutionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.SolutionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ANS_NUM(self):
            return self.getToken(ClingoParser.ANS_NUM, 0)

        def actual_soln(self):
            return self.getTypedRuleContext(ClingoParser.Actual_solnContext,0)


        def CURR_SOLN(self):
            return self.getToken(ClingoParser.CURR_SOLN, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_solution

        def enterRule(self, listener):
            if hasattr(listener, "enterSolution"):
                listener.enterSolution(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSolution"):
                listener.exitSolution(self)




    def solution(self):

        localctx = ClingoParser.SolutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_solution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ClingoParser.T__5)
            self.state = 60
            self.match(ClingoParser.ANS_NUM)
            self.state = 61
            self.actual_soln()
            self.state = 62
            self.match(ClingoParser.T__6)
            self.state = 63
            self.match(ClingoParser.CURR_SOLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Actual_solnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.Actual_solnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RELATION_NAME(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.RELATION_NAME)
            else:
                return self.getToken(ClingoParser.RELATION_NAME, i)

        def custom_representation_soln(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.Custom_representation_solnContext)
            else:
                return self.getTypedRuleContext(ClingoParser.Custom_representation_solnContext,i)


        def getRuleIndex(self):
            return ClingoParser.RULE_actual_soln

        def enterRule(self, listener):
            if hasattr(listener, "enterActual_soln"):
                listener.enterActual_soln(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitActual_soln"):
                listener.exitActual_soln(self)




    def actual_soln(self):

        localctx = ClingoParser.Actual_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_actual_soln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.RELATION_NAME:
                self.state = 65
                self.match(ClingoParser.RELATION_NAME)
                self.state = 66
                self.match(ClingoParser.T__7)
                self.state = 67
                self.custom_representation_soln()
                self.state = 68
                self.match(ClingoParser.T__8)
                self.state = 74
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.Custom_representation_solnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Word(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.Word)
            else:
                return self.getToken(ClingoParser.Word, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_custom_representation_soln

        def enterRule(self, listener):
            if hasattr(listener, "enterCustom_representation_soln"):
                listener.enterCustom_representation_soln(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCustom_representation_soln"):
                listener.exitCustom_representation_soln(self)




    def custom_representation_soln(self):

        localctx = ClingoParser.Custom_representation_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_custom_representation_soln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.match(ClingoParser.Word)
                    self.state = 76
                    self.match(ClingoParser.T__9) 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 82
            self.match(ClingoParser.Word)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





