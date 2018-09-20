#!/usr/bin/env python3

import errno
import inspect
import os
import pickle
import sqlite3


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

class PossibleWorld:
    """
    Class to store details and solution relating to every possible world
    """
    def __init__(self, num_relations, pw_id):
        self.rls = [[] for i in range(num_relations)]
        self.pw_id = pw_id
        self.pw_soln = 0

    def add_relation(self, relation_id, relation_data):
        if relation_id >= len(self.rls):
            self.rls.append([])
        self.rls[relation_id].append(relation_data)


###################################################################

class Relation:
    """
    Class to store description of each relation found in the clingo output
    """

    def __init__(self, relation_name):
        self.relation_name = relation_name
        self.arity = 0
        self.r_id = 0


###################################################################

# File Location Constants:


SRC_TEMP_PICKLE_LOC = 'temp_pickle_data/'
CURRENT_PROJECT_NAME_LOC = SRC_TEMP_PICKLE_LOC + 'current_project_name.pkl'
PROJECT_RESULTS_LOC = 'Results/'
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
    }

    relative_loc = PROJECT_RESULTS_LOC + project_name + '/'

    if data_type in data_types_dict:
        relative_loc += data_types_dict[data_type]
    else:
        relative_loc += data_type + '/'

    mkdir_p(relative_loc)

    return os.path.abspath(relative_loc)


def get_file_save_name(project_name, file_type):

    if file_type in ['dist_matrix', 'dfs', 'relations', 'pws', 'complexities']:
        return file_type + '.pkl'
    return None


def load_from_temp_pickle(project_name, file_type):
    if file_type in ['dfs', 'pws', 'relations', 'dist_matrix', 'complexities']:

        try:
            with open(get_save_folder(project_name, 'temp_pickle_data') + '/' +
                      get_file_save_name(project_name, file_type), 'rb') as input_file:
                return pickle.load(input_file)
        except IOError:
            print("Could not find the project, check project/session name entered.")
            exit(1)


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
