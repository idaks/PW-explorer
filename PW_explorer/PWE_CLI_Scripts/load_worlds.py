#!/usr/bin/env python3

from PW_explorer.pwe_helper import (
    get_asp_output_folder,
    get_save_folder,
    get_file_save_name,
    set_current_project_name,
)
from PW_explorer.load_worlds import  *

import argparse
import pickle
import os


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


if __name__ == '__main__':
    __main__()
