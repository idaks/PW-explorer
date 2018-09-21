#!/usr/bin/env python3

import argparse
import os
import subprocess as subprocess
from pwe_helper import get_asp_input_folder, get_asp_output_folder, set_current_project_name, preprocess_clingo_output

"""
This script is used to run clingo on given clingo files, pre-process the output and then
save it to the appropriate location.
"""


def __main__():

    parser = argparse.ArgumentParser()
    parser.add_argument("fnames", type=str, help="provide the clingo files", nargs='+')
    parser.add_argument("project_name", type=str,
                        help='provide a suitable session/project name to reference these results in future scripts')
    parser.add_argument("-n", "--num_solutions", type=int, default=0,
                        help="number of solutions to generate using clingo, optional, generates all by default")
    args = parser.parse_args()

    fnames = args.fnames
    project_name = args.project_name

    for fname in fnames:
        if not os.path.exists(fname):
            print("Could not find the file {}".format(str(fname)))
            exit(1)

    clingo_in_files = []

    for i, fname in enumerate(fnames):
        clingo_in_files.append(
            get_asp_input_folder(project_name) + '/{}{}.lp4'.format(project_name, ('_' + str(i)) if len(fnames) > 1 else ''))
        subprocess.check_call(['cp', fname, clingo_in_files[-1]])
    print("Copied files into {}".format(get_asp_input_folder(project_name)))

    clingo_output = get_clingo_output(clingo_in_files, args.num_solutions)
    preprocessed_clingo_output = preprocess_clingo_output(clingo_output)

    temp_data = open(get_asp_output_folder(project_name) + '/{}.txt'.format(project_name), 'w')
    temp_data.writelines('\n'.join(preprocessed_clingo_output))
    print("Preprocessed clingo output written to {}".format(get_asp_output_folder(project_name)))

    temp_data.close()
    set_current_project_name(project_name)


def get_clingo_output(clingo_in_fnames: list, num_solutions: int=0):

    t = ['clingo', '-n {}'.format(num_solutions), '-Wnone']
    t.extend(clingo_in_fnames)
    process_ = subprocess.Popen(t, stdout=subprocess.PIPE)
    clingo_output = process_.communicate()[0]
    # clingo_output = subprocess.check_output()

    # print clingo_output
    cling_out_lines = clingo_output.splitlines()
    cling_out_lines = list(map(lambda x: str(x, 'utf-8'), cling_out_lines))
    # cling_out_lines = [l.decode('utf-8') for l in cling_out_lines]
    return cling_out_lines


def run_clingo(clingo_rules: list) -> list:

    dummy_fname = 'svjsihkankjbyerhoihsyvgjnclsdihcysbfhcbygweincbsydgibwyebcsygdyc.lp4'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_rules))

    clingo_output = get_clingo_output([dummy_fname])
    os.remove(dummy_fname)
    return preprocess_clingo_output(clingo_output)


if __name__ == '__main__':
    __main__()
