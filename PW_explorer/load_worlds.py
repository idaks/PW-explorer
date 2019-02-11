#!/usr/bin/env python3

from .Input_Parsers.Clingo_Parser.clingo_parser import parse_clingo_output
import pandas as pd
import numpy as np

import os



def parse_solution(fname, attr_defs: dict={}, reasoner='clingo'):

    parser_to_use = None
    if reasoner == 'clingo':
        parser_to_use = parse_clingo_output
    else:
        print("Unrecognized reasoner selected")
        exit(1)

    dfs, relations, pws = parser_to_use(fname)

    for rel_name, df in dfs.items():
        if rel_name in attr_defs:
            mapper = dict(zip(list(df.columns)[1:], attr_defs[rel_name]))
            df.rename(index=str, columns=mapper, inplace=True)

    return dfs, relations, pws


def load_worlds(clingo_output: list, attr_defs: dict={}, reasoner='clingo'):

    # TODO Add functionality to generate random file name
    dummy_fname = 'sjbcbshlpowieiohbcjhsbnckibubkjcnaiuhwyegvjcbwscuawhbnckbuveyrb.txt'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_output))
    dfs, relations, pws = parse_solution(dummy_fname, attr_defs, reasoner)
    os.remove(dummy_fname)
    return dfs, relations, pws
