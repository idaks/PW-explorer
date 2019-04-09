import os
import subprocess as subprocess
from .meta_data_parser import parse_pwe_meta_data

def get_dlv_output(dlv_input_fnames: list, num_solutions: int=0, wfs_mode: bool=False,
                   dlv_max_int: int=None, other_args: list=None):
    """
    :param dlv_input_fnames: list of dlv filepaths
    :param num_solutions: number of solutions to generate. Default: 0 i.e. generate all solutions
    :param wfs_mode: Use the well-founded semantics form
    :param dlv_max_int: Set the -N parameter while running dlv
    :param other_args: Other arguments to pass to dlv. Provide a list of strings eg. ['-n=1', '-N=10', '-silent']
    :return: dlv output and parsed attribute definitions
    """
    t = ['dlv', '-n={}'.format(num_solutions), '-silent']
    if wfs_mode:
        t.append('-wf')
    if dlv_max_int:
        t.append('-N={}'.format(dlv_max_int))
    if other_args:
        t.extend(other_args)
    t.extend(dlv_input_fnames)
    process_ = subprocess.Popen(t, stdout=subprocess.PIPE)
    dlv_output = process_.communicate()[0]
    # dlv_output = subprocess.check_output()
    meta_data = {}
    #attribute_defs = {}
    #temporal_decs = {}
    for fname in dlv_input_fnames:
        with open(fname, 'r') as f:
            dlv_rules = f.read().splitlines()
            f_meta_data = parse_pwe_meta_data(dlv_rules)
            for md_type, md in f_meta_data.items():
                if md_type in meta_data:
                    meta_data[md_type].update(md)
                else:
                    meta_data[md_type] = md

    # print(dlv_output)
    dlv_out_lines = dlv_output.splitlines()
    dlv_out_lines = list(map(lambda x: str(x, 'utf-8'), dlv_out_lines))

    # dlv_out_lines = [l.decode('utf-8') for l in dlv_out_lines]

    # meta_data = {
    #     'attr_defs': attribute_defs,
    #     'temporal_decs': temporal_decs,
    # }

    return dlv_out_lines, meta_data


def run_dlv(dlv_rules, num_solutions: int=0, wfs_mode: bool=False,
            dlv_max_int: int=None, other_args: list=None):
    """
    :param dlv_rules: list of dlv rules as strings or a single string
    :param num_solutions: number of solutions to generate. Default: 0 i.e. generate all solutions
    :param wfs_mode: Use the well-founded semantics form
    :param dlv_max_int: Set the -N parameter while running dlv
    :param other_args: Other arguments to pass to dlv. Provide a list of strings eg. ['-n=1', '-N=10', '-silent']
    :return: dlv output and parsed attribute definitions
    """

    if isinstance(dlv_rules, str):
        dlv_rules = dlv_rules.splitlines()

    dummy_fname = 'svjsihkankjbyerhoihsyvgjnclsdihcysbfhcbygweincbsydgibwyebcsygdyc.lp4'
    with open(dummy_fname, 'w') as f:
        f.write('\n'.join(dlv_rules))

    dlv_output, meta_data = get_dlv_output([dummy_fname], num_solutions=num_solutions,
                                           wfs_mode=wfs_mode, dlv_max_int=dlv_max_int,
                                           other_args=other_args)
    os.remove(dummy_fname)

    return dlv_output, meta_data