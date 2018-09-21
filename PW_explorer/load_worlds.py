#!/usr/bin/env python3

from Input_Parsers.Clingo_Parser.clingo_parser import parse_clingo_output
import pandas as pd
import numpy as np

import os
import argparse
import pickle
from pwe_helper import get_asp_output_folder, set_current_project_name, get_save_folder, get_file_save_name, \
    preprocess_clingo_output


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fname", type=str,
                        help="provide the preprocessed clingo output .txt file to parse. "
                             "Need not provide one if it already exists in the asp_output folder as $project_name.txt")
    parser.add_argument("project_name", type=str,
                        help="provide a suitable session/project name to reference these results in future scripts")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-clingo", action='store_true', default=True)
    group.add_argument("-dlv", action='store_true', default=False)
    args = parser.parse_args()

    fname = args.fname
    project_name = args.project_name

    if fname is None:
        fname = get_asp_output_folder(project_name) + '/' + str(project_name) + '.txt'
    if not os.path.exists(fname):
        print("No file by the name {}.txt exists in the asp_output folder. "
              "Please recheck the project name.".format(project_name))
        exit(1)

    dfs, relations, pws = parse_solution(fname, 'clingo' if args.clingo else 'dlv')

    for data, data_type in [(dfs, 'dfs'), (relations, 'relations'), (pws, 'pws')]:
        with open(get_save_folder(project_name, 'temp_pickle_data') + '/' +
                  get_file_save_name(project_name, data_type), 'wb') as f:
            pickle.dump(data, f)
    set_current_project_name(project_name)


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

    dummy_fname = 'sjbcbshlpowieiohbcjhsbnckibubkjcnaiuhwyegvjcbwscuawhbnckbuveyrb.txt'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_output))
    dfs, relations, pws = parse_solution(dummy_fname, reasoner)
    os.remove(dummy_fname)
    return dfs, relations, pws


if __name__ == '__main__':
    __main__()
