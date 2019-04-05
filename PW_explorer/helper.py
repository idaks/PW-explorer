#!/usr/bin/env python3

import errno
import inspect
import os
import pickle
import sqlite3
import importlib
import copy

import pandas as pd

from .meta_data_parser import (
    META_DATA_TEMPORAL_DEC_KEYWORD,
)

###################################################################

# to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


###################################################################

###################################################################

# helper funcs

def isfloat(value):
    """returns true if a value can be typecasted as a float, else false"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def mkdir_p(path):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def preprocess_clingo_output(clingo_raw_output: list):

    start = 0
    for i, line in enumerate(clingo_raw_output):
        if line.strip() == 'Solving...':
            start = i + 1
            break

    return clingo_raw_output[start:]

###################################################################


###################################################################

class PossibleWorld:
    """
    Class to store details and solution relating to every possible world
    """
    def __init__(self, pw_id):
        self.rls = {} #[[] for i in range(num_relations)]
        self.pw_id = pw_id
        self.pw_soln = None

    def add_relation(self, relation_name, relation_data):
        if relation_name not in self.rls:
            self.rls[relation_name] = []
        self.rls[relation_name].append(relation_data)


###################################################################

class Relation:
    """
    Class to store description of each relation found in the clingo output
    """

    def __init__(self, relation_name):
        self.relation_name = relation_name
        self.arity = None
        self.r_id = None
        self.meta_data = {}


###################################################################

###################################################################

def make_temporal_columns_numeric(rel_schemas, pw_rels_dfs):
    for rel in rel_schemas:
        rl_name = rel.relation_name
        if META_DATA_TEMPORAL_DEC_KEYWORD in rel.meta_data:
            for temporal_index in rel.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD]:
                col_name = pw_rels_dfs[rl_name].columns[temporal_index + 1]  # +1 is to a/c for the 'pw' column
                pw_rels_dfs[rl_name][col_name] = pd.to_numeric(pw_rels_dfs[rl_name][col_name])

###################################################################


###################################################################

def pw_slicer(dfs, pws, pws_to_use):
    sliced_pws = list(filter(lambda x: x.pw_id in pws_to_use, pws)) if pws else None
    sliced_dfs = {rl_name: df[df['pw'].isin(pws_to_use)] for rl_name, df in dfs.items()} if dfs else None
    return sliced_dfs, sliced_pws


def rel_slicer(dfs, rels, pws, rels_to_use):
    """
    A new copy of pws is returned (although the underlying rl details are shared).
    """
    sliced_dfs = {rl_name: df for rl_name, df in dfs.items() if rl_name in rels_to_use} if dfs else None
    sliced_rels = list(filter(lambda x: x.relation_name in rels_to_use, rels)) if rels else None
    sliced_pws = None
    if pws:
        sliced_pws = []
        for pw_obj in pws:
            new_pw_obj = PossibleWorld(pw_obj.pw_id)
            new_pw_obj.pw_soln = pw_obj.pw_soln
            new_pw_obj.rls = {rl_name: pw_obj.rls[rl_name] for rl_name in rels_to_use if rl_name in pw_obj.rls}
            sliced_pws.append(new_pw_obj)

    return sliced_dfs, sliced_rels, sliced_pws

###################################################################

###################################################################

def pw_id_remapper(dfs, pws, pw_id_map: dict, dfs_inplace=False, pws_inplace=False):
    if not pws:
        pws = []
    if not dfs:
        dfs = {}

    if not pws_inplace:
        pws = copy.deepcopy(pws)
    if not dfs_inplace:
        dfs = {rl_name: df.copy(deep=True) for rl_name, df in dfs.items()}

    for pw in pws:
        if pw.pw_id in pw_id_map:
            pw.pw_id = pw_id_map[pw.pw_id]
    for rl_name, df in dfs.items():
        df['pw'] = df['pw'].map(pw_id_map).fillna(df['pw'])

    return dfs, pws


def rel_name_remapper(dfs, pws, rels, rel_name_map, pws_inplace=False, rels_inplace=False):
    """
    No guarantees if map is weird i.e. if a and b are both keys in dfs (& PossibleWorld.rls) and
    a --> b but b is not mapped to anything else. Hence, exhaustive maps are recommended.
    Also no merges are supported, i.e. if a --> b and c --> b, that doesn't imply that there will be
    a merging of any of the elements of dfs, pws.rls or rels.
    """
    if not pws:
        pws = []
    if not dfs:
        dfs = {}
    if not rels:
        rels = []

    dfs = {(rel_name_map[rl_name] if rl_name in rel_name_map else rl_name): df
           for rl_name, df in dfs.items()}

    if not pws_inplace:
        pws = copy.deepcopy(pws)
    if not rels_inplace:
        rels = copy.deepcopy(rels)

    for pw in pws:
        pw.rls = {(rel_name_map[rl_name] if rl_name in rel_name_map else rl_name): facts
                  for rl_name, facts in pw.rls.items()}

    for rel in rels:
        if rel.relation_name in rel_name_map:
            rel.relation_name = rel_name_map[rel.relation_name]

    return dfs, pws, rels


###################################################################




def rel_id_from_rel_name(rel_name, relations):
    for i, rel in enumerate(relations):
        if rel.relation_name == rel_name:
            if i != rel.r_id:
                print("Relations not in order")
            return rel.r_id
    return None
