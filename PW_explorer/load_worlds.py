#!/usr/bin/env python3

from .Input_Parsers.Clingo_Parser.clingo_parser import parse_clingo_output
from .Input_Parsers.DLV_Parser.dlv_parser import parse_dlv_output
from .helper import (
    rel_id_from_rel_name,
)
from .meta_data_parser import (
    META_DATA_ATTRIBUTE_DEF_KEYWORD,
    META_DATA_TEMPORAL_DEC_KEYWORD,
)
import pandas as pd
import numpy as np

import os


def parse_solution(fname, meta_data: dict=None, reasoner='clingo', silent=False, print_parse_tree=False):

    if not meta_data:
        meta_data = {}

    reasoner_parser_map = {'clingo': parse_clingo_output, 'dlv': parse_dlv_output}
    parser_to_use = None
    if reasoner in reasoner_parser_map:
        parser_to_use = reasoner_parser_map[reasoner]
    else:
        print("Unrecognized reasoner selected")
        exit(1)

    dfs, relations, pws = parser_to_use(fname, silent=silent, print_parse_tree=print_parse_tree)

    if META_DATA_ATTRIBUTE_DEF_KEYWORD in meta_data:
        attr_defs = meta_data[META_DATA_ATTRIBUTE_DEF_KEYWORD]
        for rel_name, df in dfs.items():
            if rel_name in attr_defs:
                mapper = dict(zip(list(df.columns)[1:], attr_defs[rel_name]))
                df.rename(index=str, columns=mapper, inplace=True)
                rel_obj = relations[rel_id_from_rel_name(rel_name=rel_name, relations=relations)]
                rel_obj.meta_data[META_DATA_ATTRIBUTE_DEF_KEYWORD] = attr_defs[rel_name]

    if META_DATA_TEMPORAL_DEC_KEYWORD in meta_data:
        temporal_decs = meta_data[META_DATA_TEMPORAL_DEC_KEYWORD]
        for rl in relations:
            rl_name = rl.relation_name
            if rl_name in temporal_decs:
                temporal_indices = temporal_decs[rl_name]
                rl.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD] = temporal_indices
                for temporal_index in temporal_indices:
                    col_name = dfs[rl_name].columns[temporal_index + 1]  # To a/c for the pw column
                    dfs[rl_name][col_name] = pd.to_numeric(dfs[rl_name][col_name])


    return dfs, relations, pws


def load_worlds(asp_output, meta_data: dict=None, reasoner='clingo', silent=False, print_parse_tree=False):
    """
    :param asp_output: single string or a list of strings
    :param meta_data:
    :param reasoner:
    :return:
    """

    if not meta_data:
        meta_data = {}
    # TODO Add functionality to generate random file name
    dummy_fname = 'sjbcbshlpowieiohbcjhsbnckibubkjcnaiuhwyegvjcbwscuawhbnckbuveyrb.txt'
    with open(dummy_fname, 'w') as f:
        if isinstance(asp_output, list):
            f.write('\n'.join(asp_output))
        elif isinstance(asp_output, str):
            f.write(asp_output)
    dfs, relations, pws = parse_solution(dummy_fname, meta_data, reasoner, silent, print_parse_tree)
    os.remove(dummy_fname)
    return dfs, relations, pws
