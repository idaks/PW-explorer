#!/usr/bin/env python3

from .Input_Parsers.Clingo_Parser.clingo_parser import parse_clingo_output
import pandas as pd
import numpy as np

import os
from .pwe_helper import preprocess_clingo_output


def parse_solution(fname, reasoner='clingo'):

    parser_to_use = None
    if reasoner == 'clingo':
        parser_to_use = parse_clingo_output
    else:
        print("Unrecognized reasoner selected")
        exit(1)

    dfs, relations, pws = parser_to_use(fname)
    return dfs, relations, pws


def load_worlds(clingo_output: list, reasoner='clingo', preprocessed: bool=True):

    if not preprocessed:
        clingo_output = preprocess_clingo_output(clingo_output)

    # TODO Add functionality to generate random file name
    dummy_fname = 'sjbcbshlpowieiohbcjhsbnckibubkjcnaiuhwyegvjcbwscuawhbnckbuveyrb.txt'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_output))
    dfs, relations, pws = parse_solution(dummy_fname, reasoner)
    os.remove(dummy_fname)
    return dfs, relations, pws
