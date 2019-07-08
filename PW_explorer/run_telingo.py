import os
import subprocess as subprocess
from .helper import (
    preprocess_telingo_output,
)
from .meta_data_parser import parse_pwe_meta_data

def get_telingo_output(telingo_in_fnames: list, num_solutions: int=0):

    t = ['telingo', '-n {}'.format(num_solutions), '-Wnone']
    t.extend(telingo_in_fnames)
    process_ = subprocess.Popen(t, stdout=subprocess.PIPE)
    telingo_output = process_.communicate()[0]
    # clingo_output = subprocess.check_output()
    meta_data = {}
    #attribute_defs = {}
    #temporal_decs = {}
    for fname in telingo_in_fnames:
        with open(fname, 'r') as f:
            telingo_rules = f.read().splitlines()
            f_meta_data = parse_pwe_meta_data(telingo_rules)
            for md_type, md in f_meta_data.items():
                if md_type in meta_data:
                    meta_data[md_type].update(md)
                else:
                    meta_data[md_type] = md

    teling_out_lines = telingo_output.splitlines()
    teling_out_lines = list(map(lambda x: str(x, 'utf-8'), teling_out_lines))


    return teling_out_lines, meta_data


def run_telingo(telingo_rules, num_solutions: int=0):
    """
    :param telingo_rules: string or list of strings
    :param num_solutions:
    :return:
    """

    if isinstance(telingo_rules, str):
        telingo_rules = telingo_rules.splitlines()

    dummy_fname = 'svjsihkankjbyerhoihsyvgjnclsdihcysbfhcbygweincbsydgibwyebcsygdyc.lp4'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(telingo_rules))

    telingo_output, meta_data = get_telingo_output([dummy_fname], num_solutions=num_solutions)
    os.remove(dummy_fname)

    return preprocess_telingo_output(telingo_output), meta_data ## TODO Change preprocess_clingo_output
