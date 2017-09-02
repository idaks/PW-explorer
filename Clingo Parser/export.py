#EXPORT AND SCHEMA GENERATION SCRIPT:

import sys
from sys import argv
import pandas as pd
import numpy as np
import inspect
import sqlite3
import errno    
import os
import pickle
import argparse
import string
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project_name", type = str, help = "provide session/project name used while parsing")
parser.add_argument("-s", "--schema", action = "store_true", help= "generate sql schemas")
parser.add_argument("-sql", action = "store_true", help = "include if you want to export a sql db")
parser.add_argument("-csv", action = "store_true", help = "include if you want to export in csv")
parser.add_argument("-h5", action = "store_true", help = "include if you want to export in hdf5 format")
parser.add_argument("-msg", action = "store_true", help = "include if you want to export in msgpack format")
parser.add_argument("-pkl", action = "store_true", help = "include if you want to export in pickle format")
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

export_to_sql = args.sql
export_to_csv = args.csv
export_to_hdf = args.h5
export_to_msg = args.msg
export_to_pkl = args.pkl

#export_to_sql = True #making it true for querying purposes
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

o_fname = 'Mini Workflow/parser_output/'
conn = None

if export_to_sql:
	conn = sqlite3.connect("Mini Workflow/parser_output/sql_exports/" + str(project_name) + ".db")
if export_to_csv:
	mkdir_p(str(o_fname  + 'csv_exports/' + str(project_name)))
if export_to_hdf:
	mkdir_p(str(o_fname  + 'hdf_exports/' + str(project_name)))
if export_to_msg:
	mkdir_p(str(o_fname  + 'msg_exports/' + str(project_name)))
if export_to_pkl:
	mkdir_p(str(o_fname  + 'pkl_exports/' + str(project_name)))


for i, df in enumerate(dfs):
	if export_to_csv:
		df.to_csv(str(o_fname  + 'csv_exports/' + str(project_name) + '/' + str(relations[i].relation_name) + '.csv'))
	if export_to_hdf:
		df.to_hdf(str(o_fname  + 'hdf_exports/' + str(project_name) + '/' + str(relations[i].relation_name) + '.h5'), str(relations[i].relation_name), mode = 'w')
	if export_to_sql:
		df.to_sql(str(relations[i].relation_name), conn, if_exists = 'replace')
	if export_to_msg:
		df.to_msgpack(str(o_fname  + 'msg_exports/' + str(project_name) + '/' + str(relations[i].relation_name) + '.msg'))
	if export_to_pkl:
		df.to_pickle(str(o_fname  + 'pkl_exports/' + str(project_name) + '/' + str(relations[i].relation_name) + '.pkl'))

if export_to_csv:
	print "Successfully exported to csv"
if export_to_sql:
	print "Successfully exported to sql"
if export_to_msg:
	print "Successfully exported to msg"
if export_to_hdf:
	print "Successfully exported to hdf"
if export_to_pkl:
	print "Successfully exported to pkl"

#creating schemas for SQLite
#code to print schema of the tables created
if args.schema:
	schemas = []
	if export_to_sql:
		schema_q = conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
		print 'Sqlite Schema:'
		for row in schema_q.fetchall():
			print str(row[4])
			schemas.append(row[4])
	else:
		conn_t = sqlite3.connect("test.db")
		for i, df in enumerate(dfs):
			t = df.ix[0:0]
			t.to_sql(str(relations[i].relation_name), conn_t, if_exists = 'replace')
		schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
		print 'Sqlite Schema:'
		for row in schema_q.fetchall():
		 	print str(row[4])
		 	schemas.append(row[4])
		for i, df in enumerate(dfs):
			conn_t.execute('DROP TABLE ' + str(relations[i].relation_name))
		conn_t.commit()
		conn_t.close()
#this approach will take constant time since there is just one row in the exported database.

if export_to_sql:
	conn.commit()
	conn.close()