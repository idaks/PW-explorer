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

dist_matrix = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'rb') as input_file:
		dist_matrix = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered. Ensure you have run the dist_calc script and computed a distance matrix."
	exit(1)

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


def mds_graph_2(A):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	dt = [('len', float)]
	A = A*len(A)/5
	A = A.view(dt)
	G = nx.from_numpy_matrix(A)
	#G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))
	G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),['pw-{}'.format(i) for i in range(1, len(pws)+1)])))     

	G = nx.drawing.nx_agraph.to_agraph(G)

	G.node_attr.update(color="red", style="filled")
	G.edge_attr.update(color=None, width="0.1")
	#G.edge_attr.update(color="blue", width="0.1")

	mkdir_p('Mini Workflow/parser_output/clustering_output/' + str(project_name))
	G.draw('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_networkx_out.png', format='png', prog='neato')









conn.commit()
conn.close()	