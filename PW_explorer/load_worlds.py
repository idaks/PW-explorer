from .Input_Parsers.Clingo_Parser.clingo_parser import (
    parse_clingo_output_from_file,
    parse_clingo_output_from_string,
)
from .Input_Parsers.DLV_Parser.dlv_parser import (
    parse_dlv_output_from_file,
    parse_dlv_output_from_string,
)
from .helper import (
    rel_id_from_rel_name,
    turn_list_into_str,
)
from .Input_Parsers.Meta_Data_Parser.meta_data_parser import (
    META_DATA_ATTRIBUTE_DEF_KEYWORD,
    META_DATA_TEMPORAL_DEC_KEYWORD,
)

import pandas as pd


def parse_solution(data, file_or_string='string', meta_data: dict=None, reasoner='clingo', silent=False,
                   print_parse_tree=False, internal_facts_as_string=True):
    """
    :param data:
    :param file_or_string: If 'file' then 'data' must be a filename, if 'string' then 'data' must be a string.
                           Default: 'string'
    :param meta_data:
    :param reasoner:
    :param silent:
    :param print_parse_tree:
    :param internal_facts_as_string: If true, the facts inside facts are turned into string.
    They are stored as list within lists otherwise. Default: True.
    :return:
    """

    if not meta_data:
        meta_data = {}

    reasoner_parser_map = {}

    if file_or_string == 'string':
        reasoner_parser_map = {'clingo': parse_clingo_output_from_string, 'dlv': parse_dlv_output_from_string}
    elif file_or_string == 'file':
        reasoner_parser_map = {'clingo': parse_clingo_output_from_file, 'dlv': parse_dlv_output_from_file}
    else:
        print("Unrecognized argument to 'file_or_string' argument.")
        exit(1)

    parser_to_use = None
    if reasoner in reasoner_parser_map:
        parser_to_use = reasoner_parser_map[reasoner]
    else:
        print("Unrecognized reasoner selected")
        exit(1)

    dfs, relations, pws = parser_to_use(data, silent=silent, print_parse_tree=print_parse_tree)

    if META_DATA_ATTRIBUTE_DEF_KEYWORD in meta_data:
        attr_defs = meta_data[META_DATA_ATTRIBUTE_DEF_KEYWORD]
        for rel_name, df in dfs.items():
            if rel_name in attr_defs:
                mapper = dict(zip(list(df.columns)[1:], attr_defs[rel_name]))
                df.rename(index=str, columns=mapper, inplace=True)
                rel_obj = relations[rel_id_from_rel_name(rel_name=rel_name, relations=relations)]
                rel_obj.meta_data[META_DATA_ATTRIBUTE_DEF_KEYWORD] = attr_defs[rel_name]

    if META_DATA_TEMPORAL_DEC_KEYWORD in meta_data:
        temporal_decs = meta_data[META_DATA_TEMPORAL_DEC_KEYWORD]
        for rl in relations:
            rl_name = rl.relation_name
            if rl_name in temporal_decs:
                temporal_indices = temporal_decs[rl_name]
                rl.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD] = temporal_indices
                for temporal_index in temporal_indices:
                    col_name = dfs[rl_name].columns[temporal_index + 1]  # To a/c for the pw column
                    dfs[rl_name][col_name] = pd.to_numeric(dfs[rl_name][col_name])

    if internal_facts_as_string:
        for df in dfs.values():
            if len(df.columns) > 1:
                cols = df.columns[1:]
                for col in cols:
                    df[col] = df[col].apply(lambda x: turn_list_into_str(x) if isinstance(x, list) else x)

    return dfs, relations, pws


def load_worlds(asp_output, meta_data: dict=None, reasoner='clingo', silent=False, print_parse_tree=False,
                internal_facts_as_string=True):
    """
    :param asp_output: single string or a list of strings
    :param meta_data:
    :param reasoner:
    :param silent:
    :param print_parse_tree:
    :param internal_facts_as_string: If true, the facts inside facts are turned into string.
    They are stored as list within lists otherwise. Default: True.
    :return:
    """

    if not meta_data:
        meta_data = {}

    if isinstance(asp_output, list):
        asp_output = '\n'.join(asp_output)

    dfs, relations, pws = parse_solution(asp_output, file_or_string='string', meta_data=meta_data, reasoner=reasoner,
                                         silent=silent, print_parse_tree=print_parse_tree,
                                         internal_facts_as_string=internal_facts_as_string)
    return dfs, relations, pws


def load_worlds_from_file(fname, meta_data: dict=None, reasoner='clingo', silent=False, print_parse_tree=False,
                          internal_facts_as_string=True):
    """
    :param fname: filename to load worlds from
    :param meta_data:
    :param reasoner:
    :param silent:
    :param print_parse_tree:
    :param internal_facts_as_string: If true, the facts inside facts are turned into string.
    They are stored as list within lists otherwise. Default: True.
    :return:
    """

    if not meta_data:
        meta_data = {}

    dfs, relations, pws = parse_solution(fname, file_or_string='file', meta_data=meta_data, reasoner=reasoner,
                                         silent=silent, print_parse_tree=print_parse_tree,
                                         internal_facts_as_string=internal_facts_as_string)
    return dfs, relations, pws
