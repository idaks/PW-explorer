# Generated from PW_explorer/Input_Parsers/Clingo_Parser/Antlr_Files/Clingo.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\2\5\2 \n\2\3\2\3\2\3\3\3\3\3\3\7\3")
        buf.write("\'\n\3\f\3\16\3*\13\3\3\3\5\3-\n\3\3\3\5\3\60\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\67\n\4\3\5\3\5\3\6\3\6\5\6=\n\6\3")
        buf.write("\6\5\6@\n\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7J\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6")
        buf.write("\13Y\n\13\r\13\16\13Z\3\f\6\f^\n\f\r\f\16\f_\3\f\2\2\r")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\2\3\5\2\5\6\b\b\16\16\2a\2")
        buf.write("\33\3\2\2\2\4#\3\2\2\2\6\61\3\2\2\2\b8\3\2\2\2\n:\3\2")
        buf.write("\2\2\fE\3\2\2\2\16K\3\2\2\2\20O\3\2\2\2\22S\3\2\2\2\24")
        buf.write("X\3\2\2\2\26]\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\35")
        buf.write("\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\37\3\2\2\2\35")
        buf.write("\33\3\2\2\2\36 \7\r\2\2\37\36\3\2\2\2\37 \3\2\2\2 !\3")
        buf.write("\2\2\2!\"\5\n\6\2\"\3\3\2\2\2#$\7\3\2\2$(\7\16\2\2%\'")
        buf.write("\5\6\4\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2),\3")
        buf.write("\2\2\2*(\3\2\2\2+-\7\4\2\2,+\3\2\2\2,-\3\2\2\2-/\3\2\2")
        buf.write("\2.\60\7\16\2\2/.\3\2\2\2/\60\3\2\2\2\60\5\3\2\2\2\61")
        buf.write("\66\7\16\2\2\62\63\7\5\2\2\63\64\5\b\5\2\64\65\7\6\2\2")
        buf.write("\65\67\3\2\2\2\66\62\3\2\2\2\66\67\3\2\2\2\67\7\3\2\2")
        buf.write("\289\7\16\2\29\t\3\2\2\2:<\5\f\7\2;=\5\16\b\2<;\3\2\2")
        buf.write("\2<=\3\2\2\2=?\3\2\2\2>@\5\20\t\2?>\3\2\2\2?@\3\2\2\2")
        buf.write("@A\3\2\2\2AB\5\22\n\2BC\5\24\13\2CD\5\26\f\2D\13\3\2\2")
        buf.write("\2EF\7\7\2\2FG\7\b\2\2GI\7\16\2\2HJ\7\t\2\2IH\3\2\2\2")
        buf.write("IJ\3\2\2\2J\r\3\2\2\2KL\7\n\2\2LM\7\b\2\2MN\7\16\2\2N")
        buf.write("\17\3\2\2\2OP\7\13\2\2PQ\7\b\2\2QR\7\16\2\2R\21\3\2\2")
        buf.write("\2ST\7\f\2\2TU\7\b\2\2UV\7\16\2\2V\23\3\2\2\2WY\t\2\2")
        buf.write("\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\25\3\2\2\2")
        buf.write("\\^\t\2\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`")
        buf.write("\27\3\2\2\2\r\33\37(,/\66<?IZ_")
        return buf.getvalue()


class ClingoParser ( Parser ):

    grammarFileName = "Clingo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Answer:'", "'Optimization:'", "'('", 
                     "')'", "'Models'", "':'", "'+'", "'Optimum'", "'Optimization'", 
                     "'Calls'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OPTIMUM_FOUND", 
                      "TEXT", "WHITESPACE" ]

    RULE_clingoOutput = 0
    RULE_solution = 1
    RULE_actual_soln = 2
    RULE_custom_representation_soln = 3
    RULE_summary = 4
    RULE_models = 5
    RULE_optimum = 6
    RULE_optimization = 7
    RULE_calls = 8
    RULE_time = 9
    RULE_cpuTime = 10

    ruleNames =  [ "clingoOutput", "solution", "actual_soln", "custom_representation_soln", 
                   "summary", "models", "optimum", "optimization", "calls", 
                   "time", "cpuTime" ]

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
    OPTIMUM_FOUND=11
    TEXT=12
    WHITESPACE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
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


        def OPTIMUM_FOUND(self):
            return self.getToken(ClingoParser.OPTIMUM_FOUND, 0)

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
            while _la==ClingoParser.T__0:
                self.state = 22
                self.solution()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.OPTIMUM_FOUND:
                self.state = 28
                self.match(ClingoParser.OPTIMUM_FOUND)


            self.state = 31
            self.summary()
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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def actual_soln(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.Actual_solnContext)
            else:
                return self.getTypedRuleContext(ClingoParser.Actual_solnContext,i)


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
        self.enterRule(localctx, 2, self.RULE_solution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ClingoParser.T__0)
            self.state = 34
            self.match(ClingoParser.TEXT)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 35
                    self.actual_soln() 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.T__1:
                self.state = 41
                self.match(ClingoParser.T__1)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.TEXT:
                self.state = 44
                self.match(ClingoParser.TEXT)


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

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def custom_representation_soln(self):
            return self.getTypedRuleContext(ClingoParser.Custom_representation_solnContext,0)


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
        self.enterRule(localctx, 4, self.RULE_actual_soln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ClingoParser.TEXT)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.T__2:
                self.state = 48
                self.match(ClingoParser.T__2)
                self.state = 49
                self.custom_representation_soln()
                self.state = 50
                self.match(ClingoParser.T__3)


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

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

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
        self.enterRule(localctx, 6, self.RULE_custom_representation_soln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ClingoParser.TEXT)
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


        def calls(self):
            return self.getTypedRuleContext(ClingoParser.CallsContext,0)


        def time(self):
            return self.getTypedRuleContext(ClingoParser.TimeContext,0)


        def cpuTime(self):
            return self.getTypedRuleContext(ClingoParser.CpuTimeContext,0)


        def optimum(self):
            return self.getTypedRuleContext(ClingoParser.OptimumContext,0)


        def optimization(self):
            return self.getTypedRuleContext(ClingoParser.OptimizationContext,0)


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
        self.enterRule(localctx, 8, self.RULE_summary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.models()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.T__7:
                self.state = 57
                self.optimum()


            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.T__8:
                self.state = 60
                self.optimization()


            self.state = 63
            self.calls()
            self.state = 64
            self.time()
            self.state = 65
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

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

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
        self.enterRule(localctx, 10, self.RULE_models)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ClingoParser.T__4)
            self.state = 68
            self.match(ClingoParser.T__5)
            self.state = 69
            self.match(ClingoParser.TEXT)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.T__6:
                self.state = 70
                self.match(ClingoParser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_optimum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptimum" ):
                listener.enterOptimum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptimum" ):
                listener.exitOptimum(self)




    def optimum(self):

        localctx = ClingoParser.OptimumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_optimum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ClingoParser.T__7)
            self.state = 74
            self.match(ClingoParser.T__5)
            self.state = 75
            self.match(ClingoParser.TEXT)
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

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

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
        self.enterRule(localctx, 14, self.RULE_optimization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ClingoParser.T__8)
            self.state = 78
            self.match(ClingoParser.T__5)
            self.state = 79
            self.match(ClingoParser.TEXT)
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

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

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
        self.enterRule(localctx, 16, self.RULE_calls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ClingoParser.T__9)
            self.state = 82
            self.match(ClingoParser.T__5)
            self.state = 83
            self.match(ClingoParser.TEXT)
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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

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
        self.enterRule(localctx, 18, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 85
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__2) | (1 << ClingoParser.T__3) | (1 << ClingoParser.T__5) | (1 << ClingoParser.TEXT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

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
        self.enterRule(localctx, 20, self.RULE_cpuTime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__2) | (1 << ClingoParser.T__3) | (1 << ClingoParser.T__5) | (1 << ClingoParser.TEXT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__2) | (1 << ClingoParser.T__3) | (1 << ClingoParser.T__5) | (1 << ClingoParser.TEXT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





