import sys
from sys import argv
import pandas as pd
import numpy as np
import os
import string
import sqlite3
import argparse
import pickle
import importlib
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation
from sql_funcs import rel_id_from_rel_name, union_panda, intersection_sqlite, union_sqlite, freq_sqlite, num_tuples_sqlite, difference_sqlite, difference_both_ways_sqlite, redundant_column_sqlite, unique_tuples_sqlite

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project_name", type = str, help = "provide session/project name used while parsing")
group = parser.add_mutually_exclusive_group()
group.add_argument("-symmetric_difference", action = 'store_true', default = False, help = "this option measures distance by measuring the size of the symmetric difference set of two PWs. Use either the -rel_ids or -rel_names flag to specify the relations to use in this calculation.")
group.add_argument("-euler_num_overlaps_diff", action = 'store_true', default = False, help = "use this if working with an euler result. This measures the distance as the absolute difference in the number of overlaps (""><"") in two PWs. Provide the relation name or relation id to use using the -rel_name or rel_id flag respectively. Provide the column name to use using the -col flag.")
group.add_argument("-custom_dist_func", type = str, help = "provide the .py file (without the .py) containing your custom distance function. The function signature should be dist(pw_id_1, pw_id_2, dfs = None, pws = None, relations = None, conn = None) where the latter four arguments refer to the data acquired from parsing the ASP solutions and the connection to the generated sqlite database respectively. The function should return a floating point number. Ensure that the file is in the same directory as this script. You can use the functions in sql_funcs.py to design these dist functions")
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

def rel_id_from_rel_name(rel_name):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	for i, rel in enumerate(relations):
		if rel.relation_name == rel_name:
			if i != rel.r_id:
				print "Relations not in order"
			return rel.r_id

	return None


def sym_diff_dist_sqlite(pw_id_1, pw_id_2, rls_to_use = []):

	global pws 
	global relations 
	global expected_pws 
	global dfs
	global conn

	if pw_id_1 == pw_id_2:
		return 0

	if rls_to_use == []:
		rls_to_use = [i for i in range(len(relations))]

	dist = 0
	for rl_id in rls_to_use:

		rl = relations[rl_id]
		max_num_tuples = max(num_tuples_sqlite(relations, conn, rl_id, pw_id_1, False), num_tuples_sqlite(relations, conn, rl_id, pw_id_2, False))
		redundant_cols = redundant_column_sqlite(dfs, pws, relations, conn, rl_id = rl_id, pws_to_consider = [pw_id_1,pw_id_2], do_print = False)[0]
		cols_to_consider = set(list(dfs[rl_id])[1:])
		for t in redundant_cols:
			if t in cols_to_consider:
				cols_to_consider.remove(t[2])
		cols_to_consider = list(cols_to_consider)

		wt1 = 1 #TBD
		k1 = 1 #TBD

		x1 = difference_both_ways_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, cols_to_consider, False)
		dist += wt1 * len(x1)**k1 if x1 is not None else 0
		
	return dist

def euler_overlap_diff_dist(pw_id_1, pw_id_2, rl_id, col_name):

	global pws 
	global relations 
	global expected_pws 
	global dfs
	global conn

	# if rl_id is None:
	# 	for i, rl in enumerate(relations):
	# 		if rl.relation_name == 'rel_3':
	# 			rl_id = i
	# 			break

	x1 = freq_sqlite(dfs, pws, relations, conn, rl_id, [col_name], ['"><"'], [pw_id_1], False)[1][0]
	x2 = freq_sqlite(dfs, pws, relations, conn, rl_id, [col_name], ['"><"'], [pw_id_2], False)[1][0]

	return abs(x1-x2)


dist_func_to_use = None


if args.symmetric_difference:

	arg_ids = args.rel_ids

	if arg_ids is [] and args.rel_names is not []:
		for i in args.rel_names:
			arg_ids.append(rel_id_from_rel_name(i))
	if args.pws is None and args.calc_dist_matrix == False:
		print "Include atleast one of -pws or -calc_dist_matrix flags."
		exit(0)

	if args.pws is not None and len(args.pws) == 2:
		pw1 = args.pws[0]
		pw2 = args.pws[1]
		print "Distance between PWs {} and {} is {}".format(pw1, pw2, sym_diff_dist_sqlite(pw1, pw2, arg_ids))
	
	dist_matrix = None

	if args.calc_dist_matrix:
		dist_matrix = np.zeros((len(pws),len(pws)))
	
		for i in range(1, len(pws)+1):
			for j in range(i, len(pws)+1):
				dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = sym_diff_dist_sqlite(i,j, arg_ids)
		
		if np.max(dist_matrix) != np.min(dist_matrix):
			dist_matrix = (dist_matrix - np.min(dist_matrix))/(np.max(dist_matrix) - np.min(dist_matrix))

		mkdir_p('Mini Workflow/temp_pickle_data/' + str(project_name))
		with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'wb') as f:
			pickle.dump(dist_matrix, f)

elif args.euler_num_overlaps_diff:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)
	
	if args.col is None:
		print "-col is required"
		exit(0)
	
	if args.pws is None and args.calc_dist_matrix == False:
		print "Include atleast one of -pws or -calc_dist_matrix flags."
		exit(0)

	if args.pws is not None and len(args.pws) == 2:
		pw1 = args.pws[0]
		pw2 = args.pws[1]
		print "Distance between PWs {} and {} is {}".format(pw1, pw2, euler_overlap_diff_dist(pw1, pw2, r_id, args.col))
	
	dist_matrix = None

	if args.calc_dist_matrix:
		dist_matrix = np.zeros((len(pws),len(pws)))
	
		for i in range(1, len(pws)+1):
			for j in range(i, len(pws)+1):
				dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = euler_overlap_diff_dist(i, j, r_id, args.col)
		
		if np.max(dist_matrix) != np.min(dist_matrix):
			dist_matrix = (dist_matrix - np.min(dist_matrix))/(np.max(dist_matrix) - np.min(dist_matrix))

		mkdir_p('Mini Workflow/temp_pickle_data/' + str(project_name))
		with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'wb') as f:
			pickle.dump(dist_matrix, f)

elif args.show_relations:

	print 'Following are the parsed relation IDs and relation names:'
	for i, rl in enumerate(relations):
		print str(i) + ':', str(rl.relation_name)

elif args.custom_dist_func:

	try:
		a=importlib.import_module(args.custom_dist_func)
		dist_func = a.dist
	except Exception, e:
		print "Error importing from the given file"
		print "Error: ", str(e)
		exit(1)
	
	if args.pws is None and args.calc_dist_matrix == False:
		print "Include atleast one of -pws or -calc_dist_matrix flags."
		exit(0)

	
	if args.pws is not None and len(args.pws) == 2:
		pw1 = args.pws[0]
		pw2 = args.pws[1]
		print "Distance between PWs {} and {} is {}".format(pw1, pw2, dist_func(pw1, pw2, dfs, pws, relations, conn))
	
	if args.calc_dist_matrix:
		dist_matrix = np.zeros((len(pws),len(pws)))
	
		for i in range(1, len(pws)+1):
			for j in range(i, len(pws)+1):
				dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = dist_func(i, j, dfs, pws, relations, conn)
		
		if np.max(dist_matrix) != np.min(dist_matrix):
			dist_matrix = (dist_matrix - np.min(dist_matrix))/(np.max(dist_matrix) - np.min(dist_matrix))

		mkdir_p('Mini Workflow/temp_pickle_data/' + str(project_name))
		with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'wb') as f:
			pickle.dump(dist_matrix, f)



	

	





	







