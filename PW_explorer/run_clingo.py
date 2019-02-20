import os
import subprocess as subprocess
from .pwe_helper import preprocess_clingo_output, parse_for_attribute_defs

def get_clingo_output(clingo_in_fnames: list, num_solutions: int=0):

    t = ['clingo', '-n {}'.format(num_solutions), '-Wnone']
    t.extend(clingo_in_fnames)
    process_ = subprocess.Popen(t, stdout=subprocess.PIPE)
    clingo_output = process_.communicate()[0]
    # clingo_output = subprocess.check_output()
    attribute_defs = {}
    for fname in clingo_in_fnames:
        with open(fname, 'r') as f:
            clingo_rules = f.read().splitlines()
            attribute_defs.update(parse_for_attribute_defs(clingo_rules))

    # print clingo_output
    cling_out_lines = clingo_output.splitlines()
    cling_out_lines = list(map(lambda x: str(x, 'utf-8'), cling_out_lines))
    # cling_out_lines = [l.decode('utf-8') for l in cling_out_lines]

    return cling_out_lines, attribute_defs


def run_clingo(clingo_rules: list, num_solutions: int=0):

    dummy_fname = 'svjsihkankjbyerhoihsyvgjnclsdihcysbfhcbygweincbsydgibwyebcsygdyc.lp4'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_rules))

    clingo_output, attr_defs = get_clingo_output([dummy_fname], num_solutions=num_solutions)
    os.remove(dummy_fname)

    return preprocess_clingo_output(clingo_output), attr_defs

