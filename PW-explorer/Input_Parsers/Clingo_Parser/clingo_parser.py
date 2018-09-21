from antlr4 import *
from .Antlr_Files.ClingoLexer import ClingoLexer
from .Antlr_Files.ClingoParser import ClingoParser
from .Antlr_Files.ClingoListener import ClingoListener
from .pwe_helper import isfloat, PossibleWorld, Relation
import pandas as pd
import numpy as np
from antlr4.tree.Trees import Trees


def rearrangePWSandRLS(relations, pws):
    """
    Sort the possible worlds and relations by their ids
    :return: None
    """
    relations.sort(key=lambda x: x.r_id)
    pws.sort(key=lambda x: x.pw_id)


def loadIntoPandas(relations, pws, dfs):
    """
    Populate the Pandas DF, one for each relation
    :return: None
    """
    # print lineno()
    for n, rl in enumerate(relations):
        cls = ['pw']
        cls.extend([str('x' + str(i)) for i in range(1, rl.arity + 1)])

        rws = []  # could convert into numpy if sure it's all float/int
        for m, pw in enumerate(pws):
            # print rl.r_id
            if rl.r_id < len(pw.rls):
                rl_data_pw = pw.rls[rl.r_id]
                for i in range(len(rl_data_pw)):
                    rl_data_pw[i].insert(0, pw.pw_id)
                rws.extend(rl_data_pw)

        df = pd.DataFrame(rws, columns=cls)
        dfs.append(df)


######################################################################################

######################################################################################

class AntlrClingoListener(ClingoListener):

    def __init__(self):
        self.pws = []
        self.relations = []
        self.expected_pws = 0
        self.curr_pw = None
        self.curr_pw_id = 1
        self.curr_rl = None
        self.curr_rl_data = None
        self.n_rls = 0
        self.dfs = []
        self.out_file = None

    def enterClingoOutput(self, ctx):
        if ctx.OPTIMUM_FOUND() is not None:
            if ctx.OPTIMUM_FOUND().getText() == 'UNSATISFIABLE':
                print("The problem is unsatisfiable")

    def enterSolution(self, ctx):
        self.curr_pw = PossibleWorld(self.n_rls, self.curr_pw_id)
        # assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
        if ctx.TEXT(1) is not None:
            self.curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()

    def enterActual_soln(self, ctx):
        i = 0
        while ctx.TEXT(i) is not None:
            i += 1
        self.curr_rl = Relation(ctx.TEXT(i - 1).getText())

    def enterCustom_representation_soln(self, ctx):

        sol = ctx.TEXT().getText();
        self.curr_rl_data = sol.split(',')
        self.curr_rl.arity = len(self.curr_rl_data)
        rl_name_mod = str(self.curr_rl.relation_name + '_' + str(self.curr_rl.arity))
        self.curr_rl.relation_name = rl_name_mod

    def exitCustom_representation_soln(self, ctx):

        foundMatch = False
        for rl in self.relations:
            if self.curr_rl.relation_name == rl.relation_name and self.curr_rl.arity == rl.arity:
                self.curr_rl.r_id = rl.r_id
                # print rl.r_id, lineno() ##for debugging purposes
                foundMatch = True
                break

        if not foundMatch:
            newRl = Relation(self.curr_rl.relation_name)
            newRl.arity = self.curr_rl.arity
            newRl.r_id = self.n_rls
            # print n_rls, lineno()
            self.n_rls += 1
            self.relations.append(newRl)
            self.curr_rl.r_id = newRl.r_id

        self.curr_pw.add_relation(self.curr_rl.r_id, self.curr_rl_data)
        self.curr_rl = None  # could introduce bugs if passed by pointer in the upper statement, so be careful, use copy() if needed
        self.curr_rl_data = None

    def exitActual_soln(self, ctx):
        # print lineno()
        self.curr_rl = None
        self.curr_rl_data = None

    def exitSolution(self, ctx):
        # print lineno()
        self.pws.append(self.curr_pw)  # again be wary, else use .copy()
        self.curr_pw = None
        self.curr_pw_id += 1

    def enterOptimum(self, ctx):

        # print lineno()
        optimum_found = ctx.TEXT().getText()
        if optimum_found == 'yes':
            print('Optimum Solution was found')
        elif optimum_found == 'no':
            print('Optimum Solution was not found')
        else:
            print('Unexpected Output:', optimum_found)

    def enterOptimization(self, ctx):
        # print lineno()
        opt_soln = ctx.TEXT().getText()
        print('Optimized Solution is', opt_soln)

    def enterModels(self, ctx):

        # print lineno()
        num_models = ctx.TEXT().getText()
        num_models = int(num_models)
        print("Number of Models:", num_models)
        self.expected_pws = num_models

    def exitClingoOutput(self, ctx):

        # loading into pandas DF
        rearrangePWSandRLS(self.relations, self.pws)
        loadIntoPandas(self.relations, self.pws, self.dfs)


######################################################################################

def parse_clingo_output(fname):

    input_ = FileStream(fname)
    lexer = ClingoLexer(input_)

    # use this line to take input from the cmd line
    # lexer = ClingoLexer(StdinStream())

    stream = CommonTokenStream(lexer)
    parser = ClingoParser(stream)
    tree = parser.clingoOutput()
    # Use (uncomment) the line below to see the parse tree of the given input
    # print Trees.toStringTree(tree, None, parser)
    pw_analyzer = AntlrClingoListener()
    walker = ParseTreeWalker()
    walker.walk(pw_analyzer, tree)

    return pw_analyzer.dfs, pw_analyzer.relations, pw_analyzer.pws