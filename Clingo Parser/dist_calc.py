import sys
from sys import argv
import pandas as pd
import numpy as np
import os
import string
import argparse
import pickle
import importlib
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project_name", type = str, help = "provide session/project name used while parsing")
group = parser.add_mutually_exclusive_group()
group.add_argument("-symmetric_difference", action = 'store_true', default = False, help = "this option measures distance by measuring the size of the symmetric difference set of two PWs. Use either the -rel_ids or -rel_names flag to specify the relations to use in this calculation.")
group.add_argument("-euler_num_overlaps_diff", action = 'store_true', default = False, help = "use this if working with an euler result. This measures the distance as the absolute difference in the number of overlaps ("><") in two PWs. Provide the relation name or relation id to use using the -rel_name or rel_id flag respectively. Provide the column name to use using the -col flag.")
group.add_argument("-custom_dist_func", type = str, help = "provide the .py file containing your custom distance function. The function signature should be dist(pw_id_1, pw_id_2, dfs = None, pws = None, relations = None, conn = None) where the latter four arguments refer to the data acquired from parsing the ASP solutions and the connection to the generated sqlite database respectively. The function should return a floating point number.")
group.add_argument("-show_relations", action = 'store_true', default = False, help = "to get a list of relations and corresponding relation ids.")

parser.add_argument("-rel_names", nargs = '*', default = [], type = str, help = "provide the relation names to use in the distance calculation. Note that if both rel_ids and rel_names are provided, rel_names is disregarded.")
parser.add_argument("-rel_ids", nargs = '*', default = [], type = int, help = "provide the relation ids of the relation to use in the distance calculation. To view relation ids, use -show_relations")
parser.add_argument("-rel_name", type = str, help = "provide the relation name to use in the distance calculation. Note that if both rel_id and rel_name are provided, rel_name is disregarded.")
parser.add_argument("-rel_id", type = int, help = "provide the relation id of the relation to use in the distance calculation. To view relation ids, use -show_relations")
parser.add_argument("-calc_dist_matrix", action = 'store_true', default = False, help = "specify this flag to calculate the distance matrix")
parser.add_argument("-pws", type = int, nargs = 2, help = "provide the two possible world ids of the possible world to calculate the distance between. At least one of -pws and -calc_dist_matrix must be used.")
parser.add_argument("-col", type = str, help = "provide the column to use for the distance calculation, required with the euler_num_overlaps_diff distance metric.")

args = parser.parse_args()

project_name = ''
if args.project_name == None:
	try:
		with open('Mini Workflow/temp_pickle_data/' + 'current_project' + '/curr_proj_name.pkl', 'rb') as f:
			project_name = pickle.load(f)
	except IOError:
		print "Could not automatically find the current project/session. Please provide a project name explicitly using the -p flag"
		exit(1)
else:
	project_name = args.project_name

dfs = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dfs.pkl', 'rb') as input_file:
		dfs = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

relations = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/relations.pkl', 'rb') as input_file:
		relations = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

pws = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/pws.pkl', 'rb') as input_file:
		pws = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

if not os.path.exists("Mini Workflow/parser_output/sql_exports/" + str(project_name) + ".db"):
	print "No file by the name {}.db exists in the clingo_output/sql_exports folder. Please recheck the project name.".format(project_name)
	exit(1)

conn = None
try:
	conn = sqlite3.connect("Mini Workflow/parser_output/sql_exports/" + str(project_name) + ".db")
except sqlite3.Error:
	print "Could not find the associated sqlite databse. Please recheck project_name or make sure a sql db has been exported using export.py module"
	exit(1)

expected_pws = len(pws)


