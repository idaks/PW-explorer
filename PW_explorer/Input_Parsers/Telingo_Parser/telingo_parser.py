from antlr4 import *
from .Antlr_Files.Telingo_OutputLexer import Telingo_OutputLexer
from .Antlr_Files.Telingo_OutputParser import Telingo_OutputParser
from .Antlr_Files.Telingo_OutputListener import Telingo_OutputListener
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
        cls = ['pw', 'state']
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

class AntlrTelingoListener(Telingo_OutputListener):

    def __init__(self):
        self.pws = []
        self.relations = []
        self.expected_pws = 0
        self.curr_pw = None
        self.curr_pw_id = 1
        self.curr_state = -1
        self.curr_fact = None
        self.curr_fact_data = None
        self.curr_fact_depth = 0
        self.n_facts = 0
        self.dfs = {}
        self.silent = False

    def enterTelingoOutput(self, ctx):
        if ctx.OPTIMUM_FOUND() is not None:
            if ctx.OPTIMUM_FOUND().getText() == 'UNSATISFIABLE':
                if not self.silent:
                    print("The problem is unsatisfiable")
        # print("enterTelingoOutput")

    def enterPw(self, ctx):
        self.curr_pw = PossibleWorld(self.curr_pw_id)
        # assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
        if ctx.TEXT(1) is not None:
            self.curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()

        self.curr_state = -1  # Reset State ID

    def enterState_desc(self, ctx:Telingo_OutputParser.State_descContext):
        self.curr_state += 1

    def enterFact(self, ctx):
        self.curr_fact_depth += 1
        rel_name = ctx.TEXT().getText()
        if self.curr_fact_depth == 1:
            self.curr_fact = Relation(rel_name)
            # Set defaults in case this is a 0-arity relation
            self.curr_fact_data = [self.curr_state]
        else:
            tmp_ptr = self.curr_fact_data
            for _ in range(self.curr_fact_depth-2):
                tmp_ptr = tmp_ptr[-1]
            tmp_ptr.append([rel_name])

    def enterFact_text(self, ctx:Telingo_OutputParser.Fact_textContext):

        tmp_ptr = self.curr_fact_data
        for _ in range(self.curr_fact_depth - 1):
            tmp_ptr = tmp_ptr[-1]
        tmp_ptr.append(ctx.TEXT().getText())

    def exitFact(self, ctx):

        if self.curr_fact_depth == 1:
            self.curr_fact.arity = len(self.curr_fact_data) - 1  # -1 to a/c for the state field at the front
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

    def exitTelingoOutput(self, ctx):

        # loading into pandas DF
        rearrangePWSandRLS(self.relations, self.pws)
        loadIntoPandas(self.relations, self.pws, self.dfs)


######################################################################################

def __parse_telingo_output__(input_stream, silent=False, print_parse_tree=False):

    lexer = Telingo_OutputLexer(input_stream)

    # use this line to take input from the cmd line
    # lexer = ClingoLexer(StdinStream())

    ct_stream = CommonTokenStream(lexer)
    parser = Telingo_OutputParser(ct_stream)
    tree = parser.telingoOutput()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    pw_analyzer = AntlrTelingoListener()
    pw_analyzer.silent = silent
    walker = ParseTreeWalker()
    walker.walk(pw_analyzer, tree)

    return pw_analyzer.dfs, pw_analyzer.relations, pw_analyzer.pws


def parse_telingo_output_from_file(fname, silent=False, print_parse_tree=False):

    input_stream = FileStream(fname)
    return __parse_telingo_output__(input_stream, silent, print_parse_tree)


def parse_telingo_output_from_string(telingo_output_string, silent=False, print_parse_tree=False):

    input_stream = InputStream(telingo_output_string)
    return __parse_telingo_output__(input_stream, silent, print_parse_tree)

