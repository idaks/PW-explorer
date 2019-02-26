#!/usr/bin/env python3

import errno
import inspect
import os
import pickle
import sqlite3
import importlib
import re
import copy

import pandas as pd

###################################################################

# to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


###################################################################

###################################################################

# helper funcs

def isfloat(value):
    """returns true if a value can be typecasted as a float, else false"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def mkdir_p(path):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def preprocess_clingo_output(clingo_raw_output: list):

    start = 0
    for i, line in enumerate(clingo_raw_output):
        if line.strip() == 'Solving...':
            start = i + 1
            break

    return clingo_raw_output[start:]

###################################################################

META_DATA_KEYWORD = 'meta_data'
META_DATA_TEMPORAL_DEC_KEYWORD = 'temporal_dec'
META_DATA_ATTRIBUTE_DEF_KEYWORD = 'attr_def'
ASP_SYNTAX_TEMPORAL_DEC_KEYWORD = 'temporal'
ASP_SYNTAX_ATTRIBUTE_DEF_KEYWORD = 'schema'


TEMPORAL_FIELD_DEF_REGEX="temporal\s*\w+\(\s*[_T]+\s*(,\s*[_T]+\s*)*\)"
def parse_for_temporal_declarations(clingo_rules: list):
    temporal_decs = {}
    pattern = re.compile(TEMPORAL_FIELD_DEF_REGEX)
    for i, line in enumerate(clingo_rules):
        comment_start_idx = line.find('%')
        if comment_start_idx != -1:
            comment = line[comment_start_idx + 1:].strip()
            pattern_object = pattern.search(comment)
            if pattern_object is not None:
                declaration = comment[pattern_object.span()[0]:pattern_object.span()[1]]
                declaration = declaration.split(ASP_SYNTAX_TEMPORAL_DEC_KEYWORD, maxsplit=1)[1].strip()
                temp = declaration.split('(', maxsplit=1)
                rel_name = temp[0]
                attrs = temp[1].rsplit(')', maxsplit=1)[0].split(',')
                attrs = list(map(str.strip, attrs))
                rel_name = "{}_{}".format(rel_name, len(attrs))
                temporal_indices = [i for i, attr in enumerate(attrs) if attr == 'T']
                temporal_decs[rel_name] = temporal_indices

    return temporal_decs


ATTRIBUTES_DEF_REGEX = "define\s*\w+\(\s*\w+\s*(,\s*\w+\s*)*\)"
def parse_for_attribute_defs(clingo_rules: list):
    attribute_defs = {}
    pattern = re.compile(ATTRIBUTES_DEF_REGEX)
    for i, line in enumerate(clingo_rules):
        comment_start_idx = line.find('%')
        if comment_start_idx != -1:
            comment = line[comment_start_idx + 1:].strip()
            pattern_object = pattern.search(comment)
            if pattern_object is not None:
                definition = comment[pattern_object.span()[0]:pattern_object.span()[1]]
                definition = definition.split('define', maxsplit=1)[1].strip()
                temp = definition.split('(', maxsplit=1)
                rel_name = temp[0]
                attrs = temp[1].rsplit(')', maxsplit=1)[0].split(',')
                attrs = list(map(str.strip, attrs))
                attribute_defs["{}_{}".format(rel_name, len(attrs))] = attrs

    return attribute_defs


###################################################################

class PossibleWorld:
    """
    Class to store details and solution relating to every possible world
    """
    def __init__(self, pw_id):
        self.rls = {} #[[] for i in range(num_relations)]
        self.pw_id = pw_id
        self.pw_soln = None

    def add_relation(self, relation_name, relation_data):
        if relation_name not in self.rls:
            self.rls[relation_name] = []
        self.rls[relation_name].append(relation_data)


###################################################################

class Relation:
    """
    Class to store description of each relation found in the clingo output
    """

    def __init__(self, relation_name):
        self.relation_name = relation_name
        self.arity = None
        self.r_id = None
        self.meta_data = {}


###################################################################

###################################################################

def make_temporal_columns_numeric(rel_schemas, pw_rels_dfs):
    for rel in rel_schemas:
        rl_name = rel.relation_name
        if META_DATA_TEMPORAL_DEC_KEYWORD in rel.meta_data:
            for temporal_index in rel.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD]:
                col_name = pw_rels_dfs[rl_name].columns[temporal_index + 1]  # +1 is to a/c for the 'pw' column
                pw_rels_dfs[rl_name][col_name] = pd.to_numeric(pw_rels_dfs[rl_name][col_name])

###################################################################


###################################################################

def pw_slicer(dfs, pws, pws_to_use):
    sliced_pws = list(filter(lambda x: x.pw_id in pws_to_use, pws)) if pws else None
    sliced_dfs = {rl_name: df[df['pw'].isin(pws_to_use)] for rl_name, df in dfs.items()} if dfs else None
    return sliced_dfs, sliced_pws


def rel_slicer(dfs, rels, pws, rels_to_use):
    """
    A new copy of pws is returned (although the underlying rl details are shared).
    """
    sliced_dfs = {rl_name: df for rl_name, df in dfs.items() if rl_name in rels_to_use} if dfs else None
    sliced_rels = list(filter(lambda x: x.relation_name in rels_to_use, rels)) if rels else None
    sliced_pws = None
    if pws:
        sliced_pws = []
        for pw_obj in pws:
            new_pw_obj = PossibleWorld(pw_obj.pw_id)
            new_pw_obj.pw_soln = pw_obj.pw_soln
            new_pw_obj.rls = {rl_name: pw_obj.rls[rl_name] for rl_name in rels_to_use if rl_name in pw_obj.rls}
            sliced_pws.append(new_pw_obj)

    return sliced_dfs, sliced_rels, sliced_pws

###################################################################

###################################################################

def pw_id_remapper(dfs, pws, pw_id_map: dict, dfs_inplace=False, pws_inplace=False):
    if not pws:
        pws = []
    if not dfs:
        dfs = {}

    if not pws_inplace:
        pws = copy.deepcopy(pws)
    if not dfs_inplace:
        dfs = {rl_name: df.copy(deep=True) for rl_name, df in dfs.items()}

    for pw in pws:
        if pw.pw_id in pw_id_map:
            pw.pw_id = pw_id_map[pw.pw_id]
    for rl_name, df in dfs.items():
        df['pw'] = df['pw'].map(pw_id_map).fillna(df['pw'])

    return dfs, pws


def rel_name_remapper(dfs, pws, rels, rel_name_map, pws_inplace=False, rels_inplace=False):
    """
    No guarantees if map is weird i.e. if a and b are both keys in dfs (& PossibleWorld.rls) and
    a --> b but b is not mapped to anything else. Hence, exhaustive maps are recommended.
    Also no merges are supported, i.e. if a --> b and c --> b, that doesn't imply that there will be
    a merging of any of the elements of dfs, pws.rls or rels.
    """
    if not pws:
        pws = []
    if not dfs:
        dfs = {}
    if not rels:
        rels = []

    dfs = {(rel_name_map[rl_name] if rl_name in rel_name_map else rl_name): df
           for rl_name, df in dfs.items()}

    if not pws_inplace:
        pws = copy.deepcopy(pws)
    if not rels_inplace:
        rels = copy.deepcopy(rels)

    for pw in pws:
        pw.rls = {(rel_name_map[rl_name] if rl_name in rel_name_map else rl_name): facts
                  for rl_name, facts in pw.rls.items()}

    for rel in rels:
        if rel.relation_name in rel_name_map:
            rel.relation_name = rel_name_map[rel.relation_name]

    return dfs, pws, rels


###################################################################

# File Location Constants:


SRC_TEMP_PICKLE_LOC = '.temp_pickle_data/'
CURRENT_PROJECT_NAME_LOC = SRC_TEMP_PICKLE_LOC + 'current_project_name.pkl'
PROJECT_RESULTS_LOC = 'PWE_Results/'
PROJECT_ASP_INPUT_FOLDER = 'ASP_Input/'
PROJECT_ASP_OUTPUT_FOLDER = 'ASP_Output/'
PROJECT_EXPORTS_FOLDER = 'Exports/'
PROJECT_VISUALIZATIONS_FOLDER = 'Visualizations/'
PROJECT_TEMP_PICKLE_DATA_FOLDER = 'temp_pickle_data/'
CUSTOM_DISTANCE_FUNCTIONS_FOLDER = 'Custom_Distance_Functions'
CUSTOM_VISUALIZATION_FUNCTIONS_FOLDER = 'Custom_Visualization_Functions'


def get_asp_input_folder(project_name):
    """
    :type project_name: string
    """
    loc = PROJECT_RESULTS_LOC + project_name + '/' + PROJECT_ASP_INPUT_FOLDER
    mkdir_p(loc)
    return os.path.abspath(loc)


def get_asp_output_folder(project_name):
    """
    :type project_name: string
    """
    loc = PROJECT_RESULTS_LOC + project_name + '/' + PROJECT_ASP_OUTPUT_FOLDER
    mkdir_p(loc)
    return os.path.abspath(loc)


def get_current_project_name():
    project_name = None
    try:
        with open(CURRENT_PROJECT_NAME_LOC, 'rb') as f:
            project_name = pickle.load(f)
    except IOError:
        project_name = None
    return project_name


def set_current_project_name(project_name):
    mkdir_p(SRC_TEMP_PICKLE_LOC)
    with open(CURRENT_PROJECT_NAME_LOC, 'wb') as f:
        pickle.dump(project_name, f)


def get_save_folder(project_name, data_type):
    data_types_dict = {
        'csv_export': PROJECT_EXPORTS_FOLDER+'csv/',
        'sql_export': PROJECT_EXPORTS_FOLDER+'sql/',
        'msg_export': PROJECT_EXPORTS_FOLDER + 'msg/',
        'h5_export': PROJECT_EXPORTS_FOLDER + 'h5/',
        'pkl_export': PROJECT_EXPORTS_FOLDER + 'pkl/',
        'temp_pickle_data': PROJECT_TEMP_PICKLE_DATA_FOLDER,
        'visualization': PROJECT_VISUALIZATIONS_FOLDER,
        'asp_simple': PROJECT_EXPORTS_FOLDER+'asp_simple/',
        'asp_triples': PROJECT_EXPORTS_FOLDER+'asp_triples/',
    }

    relative_loc = PROJECT_RESULTS_LOC + project_name + '/'

    if data_type in data_types_dict:
        relative_loc += data_types_dict[data_type]
    else:
        relative_loc += data_type + '/'

    mkdir_p(relative_loc)

    return os.path.abspath(relative_loc)


PICKLE_FILE_TYPES = ['dist_matrix', 'dfs', 'relations', 'pws', 'complexities', 'attr_defs', 'meta_data']

def get_file_save_name(project_name, file_type):

    if file_type in PICKLE_FILE_TYPES:
        return file_type + '.pkl'
    return None


def load_from_temp_pickle(project_name, file_type):
    if file_type in PICKLE_FILE_TYPES:
        try:
            with open(get_save_folder(project_name, 'temp_pickle_data') + '/' +
                      get_file_save_name(project_name, file_type), 'rb') as input_file:
                f = pickle.load(input_file)
            return f
        except IOError:
            print("Could not find the project, check project/session name entered.")
            exit(1)


def save_to_temp_pickle(project_name, data, file_type):
    if file_type in PICKLE_FILE_TYPES:
        try:
            with open(get_save_folder(project_name, 'temp_pickle_data') + '/'
                      + get_file_save_name(project_name, file_type), 'wb') as f:
                pickle.dump(data, f)
        except IOError:
            print("Could not find the project, check project/session name entered.")
            exit(1)


def save_to_txt_file(lines, fname):
    with open(fname, 'w') as f:
        f.write('\n'.join(lines))


def get_sql_conn(project_name):
    try:
        conn = sqlite3.connect(get_save_folder(project_name, 'sql_export') + '/' +str(project_name) + ".db")
        return conn
    except sqlite3.Error:
        print("Could not find the associated sqlite database. Please recheck project_name " \
              "or make sure a sql db has been exported using export module")
        exit(1)


def rel_id_from_rel_name(rel_name, relations):
    for i, rel in enumerate(relations):
        if rel.relation_name == rel_name:
            if i != rel.r_id:
                print("Relations not in order")
            return rel.r_id
    return None


def import_custom_module(module_name, module_path):
    """
    Reference: https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    :param module_name: Name of the module to import
    :param module_path: Expected to be an absolute path
    :return: custom_module
    """
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    custom_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_module)
    return custom_module