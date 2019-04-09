from .Input_Parsers.Meta_Data_Parser.meta_data_parser import (
    parse_meta_data,
    preprocess,
)

import os


def parse_pwe_meta_data(asp_rules, silent=False, print_parse_tree=False):
    if isinstance(asp_rules, str):
        asp_rules = asp_rules.splitlines()
    md_comments = preprocess(asp_rules)
    # TODO Ability to generate random filenames for one time use
    dummy_fname = 'skfjnjdshviiuhvdjnfiu.txt'
    with open(dummy_fname, 'w') as f:
        f.write("\n".join(md_comments))
    parsed_meta_data = parse_meta_data(dummy_fname, silent, print_parse_tree)
    os.remove(dummy_fname)
    return parsed_meta_data