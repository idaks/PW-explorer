from .Input_Parsers.Meta_Data_Parser.meta_data_parser import (
    parse_meta_data_from_string,
    preprocess,
)


def parse_pwe_meta_data(asp_rules, silent=False, print_parse_tree=False):
    if isinstance(asp_rules, str):
        asp_rules = asp_rules.splitlines()
    md_comments = preprocess(asp_rules)
    md_comments = "\n".join(md_comments)
    parsed_meta_data = parse_meta_data_from_string(md_comments, silent, print_parse_tree)
    return parsed_meta_data


def parse_pwe_meta_data_from_file(fname, silent=False, print_parse_tree=False):
    with open(fname, 'r') as f:
        asp_rules = f.read()
    return parse_pwe_meta_data(asp_rules, silent, print_parse_tree)