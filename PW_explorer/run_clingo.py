import os
import subprocess as subprocess
from .helper import (
    preprocess_clingo_output,
)
from .meta_data_parser import parse_meta_data

def get_clingo_output(clingo_in_fnames: list, num_solutions: int=0):

    t = ['clingo', '-n {}'.format(num_solutions), '-Wnone']
    t.extend(clingo_in_fnames)
    process_ = subprocess.Popen(t, stdout=subprocess.PIPE)
    clingo_output = process_.communicate()[0]
    # clingo_output = subprocess.check_output()
    meta_data = {}
    #attribute_defs = {}
    #temporal_decs = {}
    for fname in clingo_in_fnames:
        with open(fname, 'r') as f:
            clingo_rules = f.read().splitlines()
            f_meta_data = parse_meta_data(clingo_rules)
            for md_type, md in f_meta_data.items():
                if md_type in meta_data:
                    meta_data[md_type].update(md)
                else:
                    meta_data[md_type] = md
            #attribute_defs.update(parse_for_attribute_defs(clingo_rules))
            #temporal_decs.update(parse_for_temporal_declarations(clingo_rules))

    cling_out_lines = clingo_output.splitlines()
    cling_out_lines = list(map(lambda x: str(x, 'utf-8'), cling_out_lines))

    # cling_out_lines = [l.decode('utf-8') for l in cling_out_lines]

    # meta_data = {
    #     'attr_defs': attribute_defs,
    #     'temporal_decs': temporal_decs,
    # }

    return cling_out_lines, meta_data


def run_clingo(clingo_rules, num_solutions: int=0):
    """
    :param clingo_rules: string or list of strings
    :param num_solutions:
    :return:
    """

    if isinstance(clingo_rules, str):
        clingo_rules = clingo_rules.splitlines()

    dummy_fname = 'svjsihkankjbyerhoihsyvgjnclsdihcysbfhcbygweincbsydgibwyebcsygdyc.lp4'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(clingo_rules))

    clingo_output, meta_data = get_clingo_output([dummy_fname], num_solutions=num_solutions)
    os.remove(dummy_fname)

    return preprocess_clingo_output(clingo_output), meta_data
