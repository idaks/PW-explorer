#!/usr/bin/env python3

from .Input_Parsers.Clingo_Parser.clingo_parser import parse_clingo_output
from .Input_Parsers.DLV_Parser.dlv_parser import parse_dlv_output
from .pwe_helper import rel_id_from_rel_name
import pandas as pd
import numpy as np

import os


def parse_solution(fname, meta_data: dict=None, reasoner='clingo'):

    if not meta_data:
        meta_data = {}

    reasoner_parser_map = {'clingo': parse_clingo_output, 'dlv': parse_dlv_output}
    parser_to_use = None
    if reasoner in reasoner_parser_map:
        parser_to_use = reasoner_parser_map[reasoner]
    else:
        print("Unrecognized reasoner selected")
        exit(1)

    dfs, relations, pws = parser_to_use(fname)

    if 'attr_defs' in meta_data:
        attr_defs = meta_data['attr_defs']
        for rel_name, df in dfs.items():
            if rel_name in attr_defs:
                mapper = dict(zip(list(df.columns)[1:], attr_defs[rel_name]))
                df.rename(index=str, columns=mapper, inplace=True)
                rel_obj = relations[rel_id_from_rel_name(rel_name=rel_name, relations=relations)]
                rel_obj.meta_data['attr_defs'] = attr_defs[rel_name]

    if 'temporal_decs' in meta_data:
        temporal_decs = meta_data['temporal_decs']
        for rl in relations:
            rl_name = rl.relation_name
            if rl_name in temporal_decs:
                rl.meta_data['temporal_decs'] = temporal_decs[rl_name]

    return dfs, relations, pws


def load_worlds(asp_output: list, meta_data: dict=None, reasoner='clingo'):

    if not meta_data:
        meta_data = {}
    # TODO Add functionality to generate random file name
    dummy_fname = 'sjbcbshlpowieiohbcjhsbnckibubkjcnaiuhwyegvjcbwscuawhbnckbuveyrb.txt'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(asp_output))
    dfs, relations, pws = parse_solution(dummy_fname, meta_data, reasoner)
    os.remove(dummy_fname)
    return dfs, relations, pws
