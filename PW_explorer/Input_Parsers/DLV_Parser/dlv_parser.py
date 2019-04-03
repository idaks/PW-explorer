from antlr4 import *
from .Antlr_Files.DLV_OutLexer import DLV_OutLexer
from .Antlr_Files.DLV_OutParser import DLV_OutParser
from .Antlr_Files.DLV_OutListener import DLV_OutListener
from ...helper import isfloat, PossibleWorld, Relation
import pandas as pd
import numpy as np
from antlr4.tree.Trees import Trees


class AntlrDLVListener(DLV_OutListener):

    ASP_SOLN = 'asp_soln'
    WFS_SOLN = 'wfs_soln'
    OPT_SOLN = 'opt_soln'

    WFS_TRUE_CATEGORY = 'true'
    WFS_UNDEFINED_CATEGORY = 'undefined'

    def __init__(self):

        self.silent = False

        self.pws = []
        self.relations = []
        self.dfs = {}

        self.curr_atom_set = {}

        self.soln_type = None

        # PWS_OUT or OPT MODE
        self.curr_pw: PossibleWorld = None
        self.curr_pw_id: int = 1

        # WFS MODE
        self.true_set = {}
        self.undefined_set = {}
        self.curr_category = None

    def enterDlvOutput(self, ctx):
        pass

    def enterPws_out(self, ctx:DLV_OutParser.Pws_outContext):
        self.soln_type = AntlrDLVListener.ASP_SOLN

    def enterOptimization_out(self, ctx:DLV_OutParser.Optimization_outContext):
        self.soln_type = AntlrDLVListener.OPT_SOLN

    def enterWf_mode_out(self, ctx:DLV_OutParser.Wf_mode_outContext):
        self.soln_type = AntlrDLVListener.WFS_SOLN

    def enterPw(self, ctx:DLV_OutParser.PwContext):
        self.curr_pw = PossibleWorld(self.curr_pw_id)

    def enterOpt_model(self, ctx:DLV_OutParser.Opt_modelContext):
        self.curr_pw = PossibleWorld(self.curr_pw_id)
        [weight, level] = ctx.TEXT().getText().split(':')
        self.curr_pw.pw_soln = float(weight)

    def enterTrue_part(self, ctx:DLV_OutParser.True_partContext):
        self.curr_category = AntlrDLVListener.WFS_TRUE_CATEGORY

    def enterUndefined_part(self, ctx:DLV_OutParser.Undefined_partContext):
        self.curr_category = AntlrDLVListener.WFS_UNDEFINED_CATEGORY

    def enterAtom_set(self, ctx:DLV_OutParser.Atom_setContext):
        self.curr_atom_set = {}

    def enterAtom(self, ctx:DLV_OutParser.AtomContext):
        atom_name = ctx.TEXT(0).getText()
        attrs = []
        if ctx.TEXT(1) is not None:
            attrs = ctx.TEXT(1).getText().split(',')
        arity = len(attrs)
        rl_name = "{}_{}".format(atom_name, arity)
        if rl_name not in self.curr_atom_set:
            self.curr_atom_set[rl_name] = []
        self.curr_atom_set[rl_name].append(attrs)

    def exitUndefined_part(self, ctx:DLV_OutParser.Undefined_partContext):
        self.undefined_set = self.curr_atom_set
        self.curr_atom_set = {}

    def exitTrue_part(self, ctx:DLV_OutParser.True_partContext):
        self.true_set = self.curr_atom_set
        self.curr_atom_set = {}

    def exitPw(self, ctx:DLV_OutParser.PwContext):
        for rl_name, rel_data_list in self.curr_atom_set.items():
            for rel_data in rel_data_list:
                self.curr_pw.add_relation(rl_name, rel_data)
        self.pws.append(self.curr_pw)
        self.curr_pw_id += 1
        self.curr_pw = None
        self.curr_atom_set = {}

    def exitOpt_model(self, ctx:DLV_OutParser.Opt_modelContext):
        for rl_name, rel_data_list in self.curr_atom_set.items():
            for rel_data in rel_data_list:
                self.curr_pw.add_relation(rl_name, rel_data)
        self.pws.append(self.curr_pw)
        self.curr_pw_id += 1
        self.curr_pw = None
        self.curr_atom_set = {}

    def exitOptimization_out(self, ctx:DLV_OutParser.Optimization_outContext):
        pass

    def exitWf_mode_out(self, ctx:DLV_OutParser.Wf_mode_outContext):
        pass

    def exitPws_out(self, ctx:DLV_OutParser.Pws_outContext):
        pass

    def exitDlvOutput(self, ctx:DLV_OutParser.DlvOutputContext):
        if self.soln_type in [AntlrDLVListener.OPT_SOLN, AntlrDLVListener.ASP_SOLN]:
            self.relations = AntlrDLVListener.create_rel_objs_from_pws(self.pws)
            self.dfs = AntlrDLVListener.load_pws_into_pandas(self.pws, self.relations)
            if not self.silent:
                print("Number of Models: {}".format(len(self.pws)))
        elif self.soln_type in [AntlrDLVListener.WFS_SOLN]:
            self.relations = AntlrDLVListener.create_rel_objs_from_atom_sets([self.true_set, self.undefined_set])
            self.dfs = AntlrDLVListener.load_wfs_soln_into_pandas(
                {AntlrDLVListener.WFS_TRUE_CATEGORY: self.true_set,
                 AntlrDLVListener.WFS_UNDEFINED_CATEGORY: self.undefined_set},
                self.relations)

    @staticmethod
    def create_rel_objs_from_pws(pws):
        rel_keys = []
        for pw in pws:
            rel_keys.extend(pw.rls.keys())
        rel_keys = list(set(rel_keys))
        rel_arities = [int(rl_name.rsplit('_', maxsplit=1)[-1]) for rl_name in rel_keys]
        rels = []
        for rl_id, (rl_name, rl_arity) in enumerate(zip(rel_keys, rel_arities)):
            rel = Relation(rl_name)
            rel.arity = rl_arity
            rel.r_id = rl_id
            rels.append(rel)
        return rels

    @staticmethod
    def create_rel_objs_from_atom_sets(atom_sets: list):
        rel_keys = []
        for atom_set in atom_sets:
            rel_keys.extend(atom_set.keys())
        rel_keys = list(set(rel_keys))
        rel_arities = [int(rl_name.rsplit('_', maxsplit=1)[-1]) for rl_name in rel_keys]
        rels = []
        for rl_id, (rl_name, rl_arity) in enumerate(zip(rel_keys, rel_arities)):
            rel = Relation(rl_name)
            rel.arity = rl_arity
            rel.r_id = rl_id
            rels.append(rel)
        return rels

    @staticmethod
    def load_pws_into_pandas(pws, relations):
        dfs = {}
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
        return dfs

    @staticmethod
    def load_wfs_soln_into_pandas(wfs_status_to_atom_set_dict, relations):
        dfs = {}
        for n, rl in enumerate(relations):
            cls = ['wfs_status']
            cls.extend([str('x' + str(i)) for i in range(1, rl.arity + 1)])

            rws = []  # could convert into numpy if sure it's all float/int
            for wfs_status, atom_set in wfs_status_to_atom_set_dict.items():
                if rl.relation_name in atom_set:
                    rl_data_pw = []
                    for rl_data in atom_set[rl.relation_name]:
                        rl_data_pw.append(rl_data.copy())
                        rl_data_pw[-1].insert(0, wfs_status)
                    rws.extend(rl_data_pw)

            df = pd.DataFrame(rws, columns=cls)
            dfs[rl.relation_name] = df
        return dfs


def parse_dlv_output(fname, silent=False, print_parse_tree=False):

    input_ = FileStream(fname)
    lexer = DLV_OutLexer(input_)

    # use this line to take input from the cmd line
    # lexer = DLV_OutLexer(StdinStream())

    stream = CommonTokenStream(lexer)
    parser = DLV_OutParser(stream)
    tree = parser.dlvOutput()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    pw_analyzer = AntlrDLVListener()
    pw_analyzer.silent = silent
    walker = ParseTreeWalker()
    walker.walk(pw_analyzer, tree)

    return pw_analyzer.dfs, pw_analyzer.relations, pw_analyzer.pws