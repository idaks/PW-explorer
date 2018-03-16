from antlr4 import *
from .Antlr_Files.ClingoLexer import ClingoLexer
from .Antlr_Files.ClingoParser import ClingoParser
from .Antlr_Files.ClingoListener import ClingoListener
from ...helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation
import pandas as pd
import numpy as np
from antlr4.tree.Trees import Trees

# global variables to use throughout the parsing process and further

pws = []
relations = []
expected_pws = 0
curr_pw = None
curr_rl = None
curr_rl_data = None
n_rls = 0
dfs = []
out_file = None

# global pws
# global relations 
# global expected_pws 
# global curr_pw
# global curr_rl 
# global curr_rl_data 
# global n_rls
# global dfs


def rearrangePWSandRLS():
    """
    Sort the possible worlds and relations by their ids
    :return: None
    """
    global pws
    global relations
    global expected_pws
    global curr_pw
    global curr_rl
    global curr_rl_data
    global n_rls
    global dfs
    global out_file
    # sort PWs and Rls by their ids
    relations.sort(key=lambda x: x.r_id)
    pws.sort(key=lambda x: x.pw_id)


def loadIntoPandas():
    """
    Populate the Pandas DF, one for each relation
    :return: None
    """
    global pws
    global relations
    global expected_pws
    global curr_pw
    global curr_rl
    global curr_rl_data
    global n_rls
    global dfs
    global out_file

    # print lineno()
    for n, rl in enumerate(relations):
        cls = ['pw']
        cls.extend([str('x' + str(i)) for i in range(1, rl.arrity + 1)])

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

    def enterClingoOutput(self, ctx):
        if ctx.OPTIMUM_FOUND() is not None:
            if ctx.OPTIMUM_FOUND().getText() == 'UNSATISFIABLE':
                print("The problem is unsatisfiable")

    def enterSolution(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        curr_pw = PossibleWorld(n_rls)
        # assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
        if ctx.TEXT(1) is not None:
            curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()

    def enterActual_soln(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        i = 0
        while ctx.TEXT(i) is not None:
            i += 1
        curr_rl = Relation(ctx.TEXT(i - 1).getText())

    def enterCustom_representation_soln(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        sol = ctx.TEXT().getText();
        curr_rl_data = sol.split(',')
        curr_rl.arrity = len(curr_rl_data)
        rl_name_mod = str(curr_rl.relation_name + '_' + str(curr_rl.arrity))
        curr_rl.relation_name = rl_name_mod

    def exitCustom_representation_soln(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        foundMatch = False
        for rl in relations:
            if curr_rl.relation_name == rl.relation_name and curr_rl.arrity == rl.arrity:
                curr_rl.r_id = rl.r_id
                # print rl.r_id, lineno() ##for debugging purposes
                foundMatch = True
                break

        if not foundMatch:
            newRl = Relation(curr_rl.relation_name)
            newRl.arity = curr_rl.arrity
            newRl.r_id = n_rls
            # print n_rls, lineno()
            n_rls += 1
            relations.append(newRl)
            curr_rl.r_id = newRl.r_id

        curr_pw.add_relation(curr_rl.r_id, curr_rl_data)
        curr_rl = None  # could introduce bugs if passed by pointer in the upper statement, so be careful, use copy() if needed
        curr_rl_data = None

    def exitActual_soln(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # print lineno()
        curr_rl = None
        curr_rl_data = None

    def exitSolution(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # print lineno()
        pws.append(curr_pw)  # again be wary, else use .copy()
        curr_pw = None

    def enterOptimum(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # print lineno()
        optimum_found = ctx.TEXT().getText()
        if optimum_found == 'yes':
            print('Optimum Solution was found')
        elif optimum_found == 'no':
            print('Optimum Solution was not found')
        else:
            print('Unexpected Output:', optimum_found)

    def enterOptimization(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # print lineno()
        opt_soln = ctx.TEXT().getText()
        print('Optimized Solution is', opt_soln)

    def enterModels(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # print lineno()
        num_models = ctx.TEXT().getText()
        num_models = int(num_models)
        print("Number of Models:", num_models)
        expected_pws = num_models

    def exitClingoOutput(self, ctx):

        global pws
        global relations
        global expected_pws
        global curr_pw
        global curr_rl
        global curr_rl_data
        global n_rls
        global dfs
        global out_file

        # loading into pandas DF
        rearrangePWSandRLS()
        loadIntoPandas()


######################################################################################

def parse_clingo_output(fname):

    global pws
    global relations
    global expected_pws
    global curr_pw
    global curr_rl
    global curr_rl_data
    global n_rls
    global dfs
    global out_file

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

    return dfs, relations, pws
