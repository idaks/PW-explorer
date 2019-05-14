from antlr4 import *
from .Antlr_Files.ClingoLexer import ClingoLexer
from .Antlr_Files.ClingoParser import ClingoParser
from .Antlr_Files.ClingoListener import ClingoListener
from ...helper import isfloat, PossibleWorld, Relation
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
    for n, rl in enumerate(relations):
        cls = ['pw']
        cls.extend([str('x' + str(i)) for i in range(1, rl.arity + 1)])

        rws = []  # could convert into numpy if sure it's all float/int
        for m, pw in enumerate(pws):
            if rl.relation_name in pw.rls:
                rl_data_pw = []
                for rl_data in pw.rls[rl.relation_name]:
                    rl_data_pw.append(rl_data.copy())
                    rl_data_pw[-1].insert(0, pw.pw_id)
                rws.extend(rl_data_pw)

        df = pd.DataFrame(rws, columns=cls)
        dfs[rl.relation_name] = df


######################################################################################

######################################################################################

class AntlrClingoListener(ClingoListener):

    def __init__(self):
        self.pws = []
        self.relations = []
        self.expected_pws = 0
        self.curr_pw = None
        self.curr_pw_id = 1
        self.curr_fact = None
        self.curr_fact_data = None
        self.curr_fact_depth = 0
        self.n_facts = 0
        self.dfs = {}
        self.silent = False

    def enterClingoOutput(self, ctx):
        if ctx.OPTIMUM_FOUND() is not None:
            if ctx.OPTIMUM_FOUND().getText() == 'UNSATISFIABLE':
                if not self.silent:
                    print("The problem is unsatisfiable")
        # print("enterClingoOutput")

    def enterPw(self, ctx):
        self.curr_pw = PossibleWorld(self.curr_pw_id)
        # assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
        if ctx.TEXT(1) is not None:
            self.curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()

    def enterFact(self, ctx):
        self.curr_fact_depth += 1
        rel_name = ctx.TEXT().getText()
        if self.curr_fact_depth == 1:
            self.curr_fact = Relation(rel_name)
            # Set defaults in case this is a 0-arity relation
            self.curr_fact_data = []
        else:
            tmp_ptr = self.curr_fact_data
            for _ in range(self.curr_fact_depth-2):
                tmp_ptr = tmp_ptr[-1]
            tmp_ptr.append([rel_name])

    def enterFact_text(self, ctx:ClingoParser.Fact_textContext):

        tmp_ptr = self.curr_fact_data
        for _ in range(self.curr_fact_depth - 1):
            tmp_ptr = tmp_ptr[-1]
        tmp_ptr.append(ctx.TEXT().getText())

    def exitFact(self, ctx):

        if self.curr_fact_depth == 1:
            self.curr_fact.arity = len(self.curr_fact_data)
            rl_name_mod = str(self.curr_fact.relation_name + '_' + str(self.curr_fact.arity))
            self.curr_fact.relation_name = rl_name_mod

            foundMatch = False
            for rl in self.relations:
                if self.curr_fact.relation_name == rl.relation_name and self.curr_fact.arity == rl.arity:
                    self.curr_fact.r_id = rl.r_id
                    foundMatch = True
                    break

            if not foundMatch:
                newRl = Relation(self.curr_fact.relation_name)
                newRl.arity = self.curr_fact.arity
                newRl.r_id = self.n_facts
                self.n_facts += 1
                self.relations.append(newRl)
                self.curr_fact.r_id = newRl.r_id

            self.curr_pw.add_relation(self.curr_fact.relation_name, self.curr_fact_data)
            self.curr_fact = None  # could introduce bugs if passed by pointer in the upper statement, so be careful, use copy() if needed
            self.curr_fact_data = None

        self.curr_fact_depth -= 1


    def exitPw(self, ctx):
        self.pws.append(self.curr_pw)  # again be wary, else use .copy()
        self.curr_pw = None
        self.curr_pw_id += 1

    def enterOptimum(self, ctx):

        optimum_found = ctx.TEXT().getText()
        if optimum_found == 'yes':
            if not self.silent:
                print('Optimum Solution was found')
        elif optimum_found == 'no':
            if not self.silent:
                print('Optimum Solution was not found')
        else:
            if not self.silent:
                print('Unexpected Output:', optimum_found)

    def enterOptimization(self, ctx):
        opt_soln = ctx.TEXT().getText()
        if not self.silent:
            print('Optimized Solution is', opt_soln)

    def enterModels(self, ctx):

        num_models = ctx.TEXT().getText()
        num_models = int(num_models)
        if not self.silent:
            print("Number of Models:", num_models)
        self.expected_pws = num_models

    def exitClingoOutput(self, ctx):

        # loading into pandas DF
        rearrangePWSandRLS(self.relations, self.pws)
        loadIntoPandas(self.relations, self.pws, self.dfs)


######################################################################################

def __parse_clingo_output__(input_stream, silent=False, print_parse_tree=False):

    lexer = ClingoLexer(input_stream)

    # use this line to take input from the cmd line
    # lexer = ClingoLexer(StdinStream())

    ct_stream = CommonTokenStream(lexer)
    parser = ClingoParser(ct_stream)
    tree = parser.clingoOutput()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    pw_analyzer = AntlrClingoListener()
    pw_analyzer.silent = silent
    walker = ParseTreeWalker()
    walker.walk(pw_analyzer, tree)

    return pw_analyzer.dfs, pw_analyzer.relations, pw_analyzer.pws


def parse_clingo_output_from_file(fname, silent=False, print_parse_tree=False):

    input_stream = FileStream(fname)
    return __parse_clingo_output__(input_stream, silent, print_parse_tree)


def parse_clingo_output_from_string(clingo_output_string, silent=False, print_parse_tree=False):

    input_stream = InputStream(clingo_output_string)
    return __parse_clingo_output__(input_stream, silent, print_parse_tree)

