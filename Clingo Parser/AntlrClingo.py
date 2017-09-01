import sys
from sys import argv
from antlr4 import *
from ClingoLexer import ClingoLexer
from ClingoParser import ClingoParser
from ClingoListener import ClingoListener
import pandas as pd
import numpy as np
import inspect
from antlr4.tree.Trees import Trees
import sqlite3
import errno    
import os
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import mpld3
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import networkx as nx
import string




###################################################################

#to help debug
def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

###################################################################

###################################################################

#helper funcs
#returns true if a value can be typecasted as a float, else false
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

#make a directory if it doesn't already exist
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

###################################################################

#global variables to use throughout the parsing process and further

pws = []
relations = []
expected_pws = 0
curr_pw = None
curr_rl = None
curr_rl_data = None
n_rls = 0
dfs = []

# global pws 
# global relations 
# global expected_pws 
# global curr_pw
# global curr_rl 
# global curr_rl_data 
# global n_rls
# global dfs
# global out_file

###################################################################

#Class to store details and solution relating to every possible world

class PossibleWorld:
	n_pws = 1
	def __init__(self, num_relations):
		self.rls = [[] for i in range(num_relations)]
		self.pw_id = PossibleWorld.n_pws
		PossibleWorld.n_pws += 1
		self.pw_soln = 0


	def add_relation(self, relation_id, relation_data):
		if relation_id >= len(self.rls):
			self.rls.append([])
		self.rls[relation_id].append(relation_data)

###################################################################

###################################################################

#Class to store description of each relation found in the clingo output

class Relation:
	def __init__(self, relation_name):
		self.relation_name = relation_name
		self.arrity = 0
		self.r_id = 0

###################################################################

######################################################################################


#Sort the possible worlds and relations by their ids
def rearrangePWSandRLS():

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file
	#sort PWs and Rls by their ids
	#print lineno()
	relations.sort(key = lambda x: x.r_id)
	pws.sort(key = lambda x: x.pw_id)

#Populate the Pandas DF, one for each relation
def loadIntoPandas():

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	#print lineno()
	for n, rl in enumerate(relations):
		cls = ['pw']
		cls.extend([str('x' + str(i)) for i in range(1, rl.arrity + 1)])

		rws = [] #could convert into numpy if sure it's all float/int
		for m, pw in enumerate(pws):
			#print rl.r_id
			if rl.r_id < len(pw.rls):
				rl_data_pw = pw.rls[rl.r_id]
				for i in range(len(rl_data_pw)):
					rl_data_pw[i].insert(0, pw.pw_id)
				rws.extend(rl_data_pw)

		df = pd.DataFrame(rws, columns = cls)
		dfs.append(df)

######################################################################################

######################################################################################

class AntlrClingoListener(ClingoListener):

	def enterClingoOutput(self, ctx):
		if ctx.OPTIMUM_FOUND() is not None:
			if ctx.OPTIMUM_FOUND().getText() == 'UNSATISFIABLE':
				print "The problem is unsatisfiable"
				out_file.write("The problem is unsatisfiable\n")

	def enterSolution(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file 
				
		curr_pw = PossibleWorld(n_rls)
		#assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
		if ctx.TEXT(1) is not None:
			curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()
		#print lineno()

	def enterActual_soln(self, ctx): 
		
		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		i = 0
		tmp = ''
		while ctx.TEXT(i) is not None:
			i += 1
		curr_rl = Relation(ctx.TEXT(i-1).getText())
		#print lineno()

	def enterCustom_representation_soln(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		sol = ctx.TEXT().getText();
		curr_rl_data = sol.split(',')
		curr_rl.arrity = len(curr_rl_data)
		rl_name_mod = str(curr_rl.relation_name + '_' + str(curr_rl.arrity))
		curr_rl.relation_name = rl_name_mod
		#print lineno()

	def exitCustom_representation_soln(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file
		
		foundMatch = False
		for rl in relations:
			if curr_rl.relation_name == rl.relation_name and curr_rl.arrity == rl.arrity:
				curr_rl.r_id = rl.r_id
				#print rl.r_id, lineno() ##for debugging purposes
				foundMatch = True
				break
		
		if not foundMatch:
			newRl = Relation(curr_rl.relation_name)
			newRl.arrity = curr_rl.arrity
			newRl.r_id = n_rls
			#print n_rls, lineno()
			n_rls += 1
			relations.append(newRl)
			curr_rl.r_id = newRl.r_id

		curr_pw.add_relation(curr_rl.r_id, curr_rl_data)
		curr_rl = None #could introduce bugs if passed by pointer in the upper statement, so be careful, use copy() if needed
		curr_rl_data = None 
		#print lineno()

	def exitActual_soln(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		curr_rl = None
		curr_rl_data = None

	def exitSolution(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		pws.append(curr_pw) #again be wary, else use .copy()
		curr_pw = None 

	def enterOptimum(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		optimum_found = ctx.TEXT().getText()
		if optimum_found == 'yes':
			print 'Optimum Solution was found'
			out_file.write('Optimum Solution was found\n')
		elif optimum_found == 'no':
			print 'Optimum Solution was not found'
			out_file.write('Optimum Solution was not found\n')
		else:
			print 'Unexpected Output:', optimum_found
			out_file.write(str('Unexpected Output: ' +  str(optimum_found) + '\n'))

	def enterOptimization(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		opt_soln = ctx.TEXT().getText()
		print 'Optimized Solution is', opt_soln
		out_file.write('Optimized Solution is ' + str(opt_soln) + '\n')

	def enterModels(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		num_models = ctx.TEXT().getText()
		num_models = int(num_models)
		print "Number of Models:", num_models
		out_file.write("Number of Models: " + str(num_models) + '\n')
		expected_pws = num_models

	def exitClingoOutput(self,ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs
		global out_file

		#print lineno()
		#loading into pandas DF
		rearrangePWSandRLS()
		loadIntoPandas()
		#for rl in relations: print rl.relation_name, rl.r_id, '\n'
		#for df in dfs: print df.head(5), '\n', list(df), '\n'

######################################################################################

#use these 3 lines if input is coming from a .txt file 
script, fname, project_name = argv
out_file = open('Mini Workflow/parser_output/{}.txt'.format(project_name), 'w')
input = FileStream(fname)
lexer = ClingoLexer(input)

#use this line to take input from the cmd line
#lexer = ClingoLexer(StdinStream())

stream = CommonTokenStream(lexer)
parser = ClingoParser(stream)
tree = parser.clingoOutput()
#Use (uncomment) the line below to see the parse tree of the given input
#print Trees.toStringTree(tree, None, parser)
pw_analyzer = AntlrClingoListener()
walker = ParseTreeWalker()
walker.walk(pw_analyzer, tree)
#print lineno()


#########################################################################################################

exp_formats = raw_input("Enter a comma-separated list of formats you want to export the project {} in. Options: sql, csv, h5, msg, pkl. Hit return to not export in any format.\n".format(project_name))
exp_formats = exp_formats.split(',')
# for i in range(len(exp_formats)):
# 	exp_formats[i] = exp_formats[i].strip()
exp_formats = map(str.strip, exp_formats)

export_to_sql = True if 'sql' in exp_formats else False
export_to_csv = True if 'csv' in exp_formats else False
export_to_hdf = True if 'h5' in exp_formats else False
export_to_msg = True if 'msg' in exp_formats else False
export_to_pkl = True if 'pkl' in exp_formats else False

export_to_sql = True #making it true for querying purposes

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
	
	out_file.write(relations[i].relation_name + '\n')
	out_file.write(str(df))
	out_file.write('\n\n')
	
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
	out_file.write("Successfully exported to csv\n")
if export_to_sql:
	print "Successfully exported to sql"
	out_file.write("Successfully exported to sql\n")
if export_to_msg:
	print "Successfully exported to msg"
	out_file.write("Successfully exported to msg\n")
if export_to_hdf:
	print "Successfully exported to hdf"
	out_file.write("Successfully exported to hdf\n")
if export_to_pkl:
	print "Successfully exported to pkl"
	out_file.write("Successfully exported to pkl\n")	

############################################################################################################

#creating schemas for SQLite
#code to print schema of the tables created

schemas = []
if export_to_sql:
	schema_q = conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
	out_file.write('Sqlite Schema:\n')
	for row in schema_q.fetchall():
		out_file.write(str(row[4]) + '\n')
		schemas.append(row[4])
else:
	conn_t = sqlite3.connect("test.db")
	for i, df in enumerate(dfs):
		t = df.ix[0:0]
		t.to_sql(str(relations[i].relation_name), conn_t, if_exists = 'replace')
	schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
	out_file.write('Sqlite Schema:\n')
	for row in schema_q.fetchall():
	 	out_file.write(str(row[4]) + '\n')
	 	schemas.append(row[4])
	for i, df in enumerate(dfs):
		conn_t.execute('DROP TABLE ' + str(relations[i].relation_name))
	conn_t.commit()
	conn_t.close()
#this approach will take constant time since there is just one row in the exported database.

#########################################################################################################


#Some Possible Queries:

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#1: Intersection

#SQLite Version:
def intersection_sqlite(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file
	global conn 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]
	query_intersection = ''
	
	col_names = ', '.join(map(str,col_names))
	for j in pws_to_consider[:-1]:
		query_intersection += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(j) + ' intersect '
	query_intersection += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pws_to_consider[-1]) + ';'
	ik = pd.read_sql_query(query_intersection, conn)
	if do_print:
		out_file.write("Intersection for the relation" + str(relations[rl_id].relation_name) + "on features" + col_names + "for PWs" + str(', '.join(map(str, pws_to_consider))) + '\n')
		if len(ik) > 0:
			out_file.write(str(ik) + '\n')
		else:
			out_file.write("NULL\n")

	return ik

	#old way:
	# for i, df in enumerate(dfs):
	# 	query_intersection = ''
	# 	col_names = list(df)[1:]
	# 	col_names = ', '.join(map(str,col_names))
	# 	for j in range(1, expected_pws):
	# 		query_intersection += 'select ' + col_names + ' from ' + str(relations[i].relation_name) + ' where pw = ' + str(j) + ' intersect '
	# 	query_intersection += 'select ' + col_names + ' from ' + str(relations[i].relation_name) + ' where pw = ' + str(expected_pws) + ';'
	# 	ik = pd.read_sql_query(query_intersection, conn)
	# 	if len(ik) > 0:
	# 		print "Intersection of all the PWs for the relation", str(relations[i].relation_name)
	# 		print ik


#Panda Version:
def intersection_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	s1 = df[df.pw == pws_to_consider[0]]
	for j in pws_to_consider[1:]:
		s1 = pd.merge(s1, df[df.pw == j], how = 'inner', on = col_names)
	s1 = s1[col_names]
	if do_print:
		print "Intersection for the relation", str(relations[rl_id].relation_name), "on features", str(', '.join(map(str,col_names))), "for PWs", str(', '.join(map(str, pws_to_consider)))
		if len(s1) > 0:
			out_file.write(str(s1) + '\n')
		else:
			out_file.write("NULL\n")

	return s1

	#old way:
	# for i, df in enumerate(dfs):
	# 	s1 = df[df.pw==1]
	# 	for j in range(1, expected_pws):
	# 		s1 = pd.merge(s1, df[df.pw == j+1], how = 'inner', on = list(df)[1:])
	# 	k = list(df)[1:]
	# 	s1 = s1[k]
	# 	if len(s1) > 0:
	# 		print "Intersection of all the PWs for the relation", str(relations[i].relation_name)
	# 		print s1


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#2: Union

#SQLite Version:
def union_sqlite(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]
	query_union = ''
	
	col_names = ', '.join(map(str,col_names))
	for j in pws_to_consider[:-1]:
		query_union += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(j) + ' union '
	query_union += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pws_to_consider[-1]) + ';'
	ik = pd.read_sql_query(query_union, conn)
	if do_print:
		print "Union for the relation", str(relations[rl_id].relation_name), "on features", col_names, "for PWs", str(', '.join(map(str, pws_to_consider)))
		if len(ik) > 0:
			out_file.write(str(ik) + '\n')
		else:
			out_file.write("NULL\n")

	return ik

	#old way:
	# for i, df in enumerate(dfs):
	# 	query_union = ''
	# 	col_names = list(df)[1:]
	# 	col_names = ', '.join(map(str,col_names))
	# 	for j in range(1, expected_pws):
	# 		query_union += 'select ' + col_names + ' from ' + str(relations[i].relation_name) + ' where pw = ' + str(j) + ' union '
	# 	query_union += 'select ' + col_names + ' from ' + str(relations[i].relation_name) + ' where pw = ' + str(expected_pws) + ';'
		
	# 	ik = pd.read_sql_query(query_union, conn)
	# 	if len(ik) > 0:
	# 		print "Union of all the PWs for the relation", str(relations[i].relation_name)
	# 		print ik


#Panda Version:
def union_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	s1 = df[df.pw == pws_to_consider[0]]
	for j in pws_to_consider[1:]:
		s1 = pd.merge(s1, df[df.pw == j], how = 'outer', on = col_names)
	s1 = s1[col_names]

	if do_print:
		print "Intersection for the relation", str(relations[rl_id].relation_name), "on features", str(', '.join(map(str,col_names))), "for PWs", str(', '.join(map(str, pws_to_consider)))
		if len(s1) > 0:
			out_file.write(str(s1) + '\n')
		else:
			out_file.write("NULL\n")

	return s1

	#old way
	# for i, df in enumerate(dfs):
	# 	s1 = df[df.pw==1]
	# 	for j in range(1, expected_pws):
	# 		s1 = pd.merge(s1, df[df.pw == j+1], how = 'outer', on = list(df)[1:])
	# 	k = list(df)[1:]
	# 	s1 = s1[k]
	# 	all_tuples.append(s1)
	# 	if len(s1) > 0:
	# 		print "Union of all the PWs for the relation", str(relations[i].relation_name)
	# 		print s1

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#3: Frequency of a tuple

#SQLite Version:
def freq_sqlite(rl_id = 0, col_names = [], values = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn 

	all_tuples = None
	freqs = []

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names != [] and values != [] and len(col_names) != len(values):
		print 'Lengths of col_names and values don\'t match.'
		return None

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	if values == []:
		all_tuples = union_panda(rl_id, col_names, pws_to_consider, False)
	else:
		k = []
		k.append(values)
		all_tuples = pd.DataFrame(k, columns = col_names)

	for j in range(len(all_tuples)):
		query = 'select count(*) from ' + str(relations[rl_id].relation_name) + ' where '
		for k in range(len(col_names)):
			query += col_names[k] + '=' + "'" + all_tuples.ix[j][k] + "'" + ' and '

		query += 'pw in (' + str(', '.join(map(str,pws_to_consider))) + ');'
		#print query
		ik = pd.read_sql_query(query, conn)
		if do_print:
			out_file.write("Frequency of tuple" + str(tuple(all_tuples.ix[j])) + 'of the relation' + str(relations[rl_id].relation_name) + 'for attributes' + str(', '.join(map(str,col_names))) + 'in PWs' + str(', '.join(map(str,pws_to_consider))) + "is:" + str(ik.ix[0][0]) + '\n')
		freqs.append(ik.ix[0][0])

	return all_tuples, freqs

	#old way:
	# for i, df in enumerate(dfs):
	# 	headers = list(df)[1:]
	# 	for j in range(len(all_tuples[i])):
	# 		query = 'select count(*) from ' + str(relations[i].relation_name) + ' where '
	# 		for k in range(len(headers) - 1):
	# 			query += headers[k] + '=' + "'" + all_tuples[i].ix[j][k] + "'" + ' and '
	# 		query += headers[-1] + '=' + "'" + all_tuples[i].ix[j][-1] + "'" + ';'
	# 		#print query
	# 		ik = pd.read_sql_query(query, conn)
	# 		print "Frequency of tuple", tuple(all_tuples[i].ix[j]), "of the relation", str(relations[i].relation_name), "is:", ik


#Panda Version:
def freq_panda(rl_id = 0, col_names = [], values = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	all_tuples = None
	freqs = []

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names != [] and values != [] and len(col_names) != len(values):
		print 'Lengths of col_names and values don\'t match.'
		return None

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	if values == []:
		all_tuples = union_panda(rl_id, col_names, pws_to_consider, False)
	else:
		k = []
		k.append(values)
		all_tuples = pd.DataFrame(k, columns = col_names)


	df = dfs[rl_id]
	for j in range(len(all_tuples)):
		expr = ''
		for k in range(len(col_names) - 1):
			expr += str(col_names[k]) + ' == ' + "'" + str(all_tuples.ix[j][k]) + "'" + ' and '
		expr += str(col_names[-1]) + ' == ' + "'" + str(all_tuples.ix[j][-1]) + "'"
		expr +=  ' and pw in [' + str(', '.join(map(str,pws_to_consider))) + ']'
		s3 = df.query(expr)
		tmp = len(s3)
		if do_print:
			out_file.write("Frequency of tuple" + str(tuple(all_tuples.ix[j])) + 'of the relation' + str(relations[rl_id].relation_name) + 'for attributes' + str(', '.join(map(str,col_names))) + 'in PWs' + str(', '.join(map(str,pws_to_consider))) + "is:" + str(tmp) + '\n')
		freqs.append(tmp)

	return all_tuples, freqs

	#old way:
	# for i, df in enumerate(dfs):
	# 	headers = list(df)[1:]
	# 	for j in range(len(all_tuples[i])):
	# 		expr = ''
	# 		for k in range(len(headers) - 1):
	# 			expr +=  str(headers[k]) + ' == ' + "'" + str(all_tuples[i].ix[j][k]) + "'" + ' and '
	# 		expr +=  str(headers[-1]) + ' == ' + "'" + str(all_tuples[i].ix[j][-1]) + "'"
	# 		#print expr
	# 		s3 = df.query(expr)
	# 		tmp = len(s3)
	# 		#print s3
	# 		print "Frequency of tuple", tuple(all_tuples[i].ix[j]), "of the relation", str(relations[i].relation_name), "is:", tmp


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#4: Number of tuples of a relation in a PW

#SQLite Version:
def num_tuples_sqlite(rl_id, pw_id, do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn 

	query = 'select count(*) from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pw_id) + ';'
	c = pd.read_sql_query(query, conn)

	if do_print:
		out_file.write("There exist" + str(c.ix[0][0]) + "tuples of relation" + str(relations[rl_id].relation_name) + "in PW" + str(pw_id) + '\n')
	return c.ix[0][0]

#Panda Version:
def num_tuples_panda(rl_id, pw_id, do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	df = dfs[rl_id]
	c = len(df[df.pw == pw_id])
	if do_print:
		out_file.write("There exist" + str(c) + "tuples of relation" + str(relations[rl_id].relation_name) + "in PW" + str(pw_id) + '\n')
	return c


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#5: Difference Query

#SQLite Version:
def difference_sqlite(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	col_names = str(', '.join(map(str,col_names)))

	query = 'select * from (select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw =  ' + str(pw_id_1) + ') except select * from (select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pw_id_2) + ');'
	diff = pd.read_sql_query(query, conn)

	if do_print:
		out_file.write("Following is the difference between PWs {} and {} in features {} of relation {}\n".format(pw_id_1, pw_id_2, col_names, str(relations[rl_id].relation_name)))
		out_file.write(str(diff) + '\n')
	return diff

def difference_both_ways_sqlite(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	x1 = difference_sqlite(rl_id, pw_id_1, pw_id_2, col_names, False)
	x2 = difference_sqlite(rl_id, pw_id_2, pw_id_1, col_names, False)

	diff = x1.append(x2, ignore_index = True)

	if do_print:
		out_file.write("Following tuples are in one of PW {} or {}, but not both, for relation {} and features {}\n".format(pw_id_1, pw_id_2, str(relations[rl_id].relation_name), str(', '.join(map(str,col_names)))))
		out_file.write(str(diff) + '\n')
	return diff

	#could also be implemented using union\intersection, but pretty sure that's what it does under the hood anyway

#Panda Version:
def difference_panda(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	x1 = df[df.pw == pw_id_1][col_names]
	x2 = df[df.pw == pw_id_2][col_names]

	diff = pd.concat([x1, x2, x2]).drop_duplicates(keep=False)
	if do_print:
		out_file.write("Following is the difference between PWs {} and {} in features {} of relation {}\n".format(pw_id_1, pw_id_2, str(', '.join(map(str,col_names))), str(relations[rl_id].relation_name)))
		out_file.write(str(diff) + '\n')
	return diff

def difference_both_ways_panda(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	x1 = difference_panda(rl_id, pw_id_1, pw_id_2, col_names, False)
	x2 = difference_panda(rl_id, pw_id_2, pw_id_1, col_names, False)

	diff = x1.append(x2, ignore_index = True)

	if do_print:
		out_file.write("Following tuples are in one of PW {} or {}, but not both, for relation {} and features {}\n".format(pw_id_1, pw_id_2, str(relations[rl_id].relation_name), str(', '.join(map(str,col_names)))))
		out_file.write(str(diff) + '\n')
	return diff


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


#6: Redundant Column Query

#SQLite Version:
def redundant_column_sqlite(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws + 1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	#PW specific:
	redundant_pw_specific = []
	for i in pws_to_consider:
		for ft in col_names:
			query = 'select count(distinct ' + str(ft) + ') from (select * from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(i) + ');'
			k = pd.read_sql_query(query, conn)
			if int(k.ix[0][0]) <= 1:
				redundant_pw_specific.append((i, rl_id, ft))
				if do_print:
					out_file.write('Column' + str(ft) + 'is redundant in relation' + str(relations[rl_id].relation_name) + 'in PW' + str(i) + '\n')

	#Across all PWs:
	redundant_across_pws = []
	for ft in col_names:
		query = 'select count(distinct ' + str(ft) + ') from (select * from ' + str(relations[rl_id].relation_name) + ' where pw in (' + str(', '.join(map(str,pws_to_consider))) + '));'
		k = pd.read_sql_query(query, conn)
		if int(k.ix[0][0]) <= 1:
			redundant_across_pws.append((pws_to_consider, rl_id, ft))
			if do_print:
				out_file.write('Column' + str(ft) + 'is redundant in relation' + str(relations[rl_id].relation_name) + 'for PWs' + str(', '.join(map(str,pws_to_consider))) + '\n')

	return redundant_pw_specific, redundant_across_pws

#Panda Version:
def redundant_column_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws + 1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	#PW specific:
	redundant_pw_specific = []

	df = dfs[rl_id]

	for ft in col_names:
		x1 = df.groupby('pw')[ft].nunique()
		for i in pws_to_consider:
			if x1.ix[i] <= 1:
				redundant_pw_specific.append((i, rl_id, ft))
				if do_print:
					out_file.write('Column' + str(ft) + 'is redundant in relation' + str(relations[rl_id].relation_name) + 'in PW' + str(i) + '\n')

	#Across all PWs:
	redundant_across_pws = []
	x1 = df[df.pw.isin(pws_to_consider)]
	for ft in col_names:
		if x1[ft].nunique() <= 1:
			redundant_across_pws.append((pws_to_consider, rl_id, ft))
			if do_print:
				out_file.write('Column' + str(ft) + 'is redundant in relation' + str(relations[rl_id].relation_name) + 'for PWs' + str(', '.join(map(str,pws_to_consider))) + '\n')

	return redundant_pw_specific, redundant_across_pws

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#7: Tuples occuring in exactly one PW:

#SQLite Version:
def unique_tuples_sqlite(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn 


	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	relevant_tuples, freqs = freq_sqlite(rl_id, col_names, [], pws_to_consider, False)
	unique_tuples = []

	for i, f in enumerate(freqs):
		if f == 1:
			query = 'select pw from ' + str(relations[rl_id].relation_name) + ' where '
			for k in range(len(col_names)):
				query += col_names[k] + '=' + "'" + relevant_tuples.ix[i][k] + "'" + ' and '

			query += 'pw in (' + str(', '.join(map(str,pws_to_consider))) + ');'

			unique_pw = pd.read_sql_query(query, conn)
			unique_pw = unique_pw.ix[0][0]

			unique_tuples.append((relevant_tuples.ix[i], unique_pw))

			if do_print:
				out_file.write('The unique tuple' + str(tuple(relevant_tuples.ix[i])) + 'occurs only in PW' + unique_pw + '\n')

	return unique_tuples

#Panda Version:
def unique_tuples_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	relevant_tuples, freqs = freq_panda(rl_id, col_names, [], pws_to_consider, False)
	unique_tuples = []
	df = dfs[rl_id]

	for i, f in enumerate(freqs):
		if f == 1:
			expr = ''
			for k in range(len(col_names) - 1):
				expr += str(col_names[k]) + ' == ' + "'" + str(relevant_tuples.ix[i][k]) + "'" + ' and '
			expr += str(col_names[-1]) + ' == ' + "'" + str(relevant_tuples.ix[i][-1]) + "'"
			expr +=  ' and pw in [' + str(', '.join(map(str,pws_to_consider))) + ']'
			s3 = df.query(expr)
			s3 = s3.reset_index(drop = True)
			unique_pw = s3.ix[0]['pw']

			unique_tuples.append((relevant_tuples.ix[i], unique_pw))

			if do_print:
				out_file.write('The unique tuple' + tuple(relevant_tuples.ix[i]) + 'occurs only in PW' + unique_pw + '\n')

	return unique_tuples


###########################################################################################

#prototype dist function:

def dist_sqlite(pw_id_1, pw_id_2):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	# if pw_id_1 == pw_id_2:
	# 	return 0

	dist = 0

	#based on number of tuples (complexity of soln):
	for i, rl in enumerate(relations):

		k = 1 #TBD
		wt = 1 #TBD
		dist += wt * abs(num_tuples_sqlite(i, pw_id_1, False) - num_tuples_sqlite(i, pw_id_2, False))**k 


	#based on difference in optimization value:
	soln_range = 1
	#find the max and min optimization value if it exists using a for loop across all pws
	curr_max = 0
	curr_min = 0
	for i, pw in enumerate(pws):
		if isfloat(pws[i].pw_soln):
			if pws[i].pw_soln > curr_max:
				curr_max = pws[i].pw_soln
			if pws[i].pw_soln < curr_min:
				curr_min = pws[i].pw_soln

	soln_range = curr_max - curr_min if curr_max - curr_min != 0 else 1


	if isfloat(pws[pw_id_1-1].pw_soln) and isfloat(pws[pw_id_2-1].pw_soln):
		wt = 1 #TBD
		k = 1 #TBD
		dist += wt * (abs(pws[pw_id_1-1].pw_soln - pws[pw_id_2-1].pw_soln)**k)/soln_range



	#based on number of similar and unique tuples:
	for i, rl in enumerate(relations):

		max_num_tuples = max(num_tuples_sqlite(i, pw_id_1, False), num_tuples_sqlite(i, pw_id_2, False))
		redundant_cols = redundant_column_sqlite(rl_id = i, pws_to_consider = [pw_id_1,pw_id_2], do_print = False)[0]
		cols_to_consider = set(list(dfs[i])[1:])
		for t in redundant_cols:
			if t in cols_to_consider:
				cols_to_consider.remove(t[2])

		k1 = 1 #TBD
		wt1 = 1 #TBD
		k2 = 1 #TBD
		wt2 = 1 #TBD

		x1 = difference_both_ways_sqlite(i, pw_id_1, pw_id_2, cols_to_consider, False)
		x2 = intersection_sqlite(i, cols_to_consider, [pw_id_1, pw_id_2], False)

		dist += wt1 * len(x1)**k1 if x1 is not None else 0
		dist -= wt2 * len(x2)**k2 if x2 is not None else 0


	return dist

def dist_panda(pw_id_1, pw_id_2):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	# if pw_id_1 == pw_id_2:
	# 	return 0

	dist = 0

	#based on number of tuples (complexity of soln):
	for i, rl in enumerate(relations):

		k = 1 #TBD
		wt = 1 #TBD
		dist += wt * abs(num_tuples_panda(i, pw_id_1, False) - num_tuples_panda(i, pw_id_2, False))**k 


	#based on difference in optimization value:
	soln_range = 1
	#find the max and min optimization value if it exists using a for loop across all pws
	curr_max = 0
	curr_min = 0
	for i, pw in enumerate(pws):
		if isfloat(pws[i].pw_soln):
			if pws[i].pw_soln > curr_max:
				curr_max = pws[i].pw_soln
			if pws[i].pw_soln < curr_min:
				curr_min = pws[i].pw_soln

	soln_range = curr_max - curr_min if curr_max - curr_min != 0 else 1


	if isfloat(pws[pw_id_1-1].pw_soln) and isfloat(pws[pw_id_2-1].pw_soln):
		wt = 1 #TBD
		k = 1 #TBD
		dist += wt * (abs(pws[pw_id_1-1].pw_soln - pws[pw_id_2-1].pw_soln)**k)/soln_range



	#based on number of similar and unique tuples:
	for i, rl in enumerate(relations):

		max_num_tuples = max(num_tuples_panda(i, pw_id_1, False), num_tuples_panda(i, pw_id_2, False))
		redundant_cols = redundant_column_panda(rl_id = i, pws_to_consider = [pw_id_1,pw_id_2], do_print = False)[0]
		cols_to_consider = set(list(dfs[i])[1:])
		for t in redundant_cols:
			if t in cols_to_consider:
				cols_to_consider.remove(t[2])
		cols_to_consider = list(cols_to_consider)

		k1 = 1 #TBD
		wt1 = 1 #TBD
		k2 = 1 #TBD
		wt2 = 1 #TBD

		x1 = difference_both_ways_panda(i, pw_id_1, pw_id_2, cols_to_consider, False)
		x2 = intersection_panda(i, cols_to_consider, [pw_id_1, pw_id_2], False)

		dist += wt1 * len(x1)**k1 if x1 is not None else 0
		dist -= wt2 * len(x2)**k2 if x2 is not None else 0


	return dist

def sym_diff_dist_sqlite(pw_id_1, pw_id_2, rls_to_use = []):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	if pw_id_1 == pw_id_2:
		return 0

	if rls_to_use == []:
		rls_to_use = [i for i in range(len(relations))]

	dist = 0
	for rl_id in rls_to_use:

		rl = relations[rl_id]
		max_num_tuples = max(num_tuples_sqlite(rl_id, pw_id_1, False), num_tuples_sqlite(rl_id, pw_id_2, False))
		redundant_cols = redundant_column_sqlite(rl_id = rl_id, pws_to_consider = [pw_id_1,pw_id_2], do_print = False)[0]
		cols_to_consider = set(list(dfs[rl_id])[1:])
		for t in redundant_cols:
			if t in cols_to_consider:
				cols_to_consider.remove(t[2])
		cols_to_consider = list(cols_to_consider)

		wt1 = 1 #TBD
		k1 = 1 #TBD

		x1 = difference_both_ways_sqlite(rl_id, pw_id_1, pw_id_2, cols_to_consider, False)
		dist += wt1 * len(x1)**k1 if x1 is not None else 0
		
	return dist

def euler_overlap_diff_dist(pw_id_1, pw_id_2, rl_id, col_name):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	# if rl_id is None:
	# 	for i, rl in enumerate(relations):
	# 		if rl.relation_name == 'rel_3':
	# 			rl_id = i
	# 			break

	x1 = freq_sqlite(rl_id, [col_name], ['"><"'], [pw_id_1], False)[1][0]
	x2 = freq_sqlite(rl_id, [col_name], ['"><"'], [pw_id_2], False)[1][0]

	return abs(x1-x2)





#How complex are these complex world relatively
def complexity_analysis(pws_to_consider = [] ,rls_to_use = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]
	if rls_to_use == []:
		rls_to_use = [i for i in range(len(relations))]

	complexities = np.zeros(len(pws_to_consider))

	#Do some computations

	for j, rl_id in enumerate(rls_to_use):

		uni = unique_tuples_sqlite(rl_id = rl_id, pws_to_consider = pws_to_consider, do_print = False)

		for i, pw_id in enumerate(pws_to_consider):
			#number of tuples
			complexities[i] += num_tuples_sqlite(rl_id, pw_id, False)
			#number of unique tuples
			complexities[i] += len(filter(lambda x: x[1] == pw_id, uni))
	
	if np.max(complexities) != np.min(complexities):
		complexities = (complexities - np.min(complexities))/(np.max(complexities) - np.min(complexities))

	if do_print:

		paired_pw_compl = zip(pws_to_consider, complexities)
		paired_pw_compl = sorted(paired_pw_compl, key = lambda x: x[1], reverse = True)

		out_file.write('PWs:         ' + str([x[0] for x in paired_pw_compl]) + '\n')
		out_file.write('Complexities:' + str([x[1].round(2) for x in paired_pw_compl]) + '\n')


	return complexities

def euler_complexity_analysis(rl_id, col_name, pws_to_consider = [], do_print = True):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file 
	global conn

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	complexities = np.zeros(len(pws_to_consider))

	for i, pw in enumerate(pws_to_consider):
		complexities[i] = freq_sqlite(rl_id, [col_name], ['"><"'], [pw], False)[1][0]
	
	if np.max(complexities) != np.min(complexities):
		complexities = (complexities - np.min(complexities))/(np.max(complexities) - np.min(complexities))
	if do_print:
		paired_pw_compl = zip(pws_to_consider, complexities)
		paired_pw_compl = sorted(paired_pw_compl, key = lambda x: x[1], reverse = True)
		out_file.write('PWs:         ' + str([x[0] for x in paired_pw_compl]) + '\n')
		out_file.write('Complexities:' + str([x[1].round(2) for x in paired_pw_compl]) + '\n')

	return complexities



###########################################################################################

#Interactive CMD Line UI for querying

query_db = raw_input('Do you want to query the database?\n')

def get_rl_id():
	rl_id = raw_input('Enter the relation id\n')
	rl_id = 0 if rl_id.strip() == '' else int(rl_id)
	return rl_id

def get_col_name():
	col_name = raw_input('Enter the column name\n')
	col_name = 'x1' if col_name.strip() == '' else str(col_name)
	return col_name

def get_rl_ids_list_dist():
	rl_ids = raw_input('Enter a comma-separated list of relation ids you want to use in the distance calculation. Press enter to use all relations.\n')
	rl_ids = [] if rl_ids.strip() == '' else rl_ids.split(',')
	rl_ids = map(str.strip, rl_ids)
	rl_ids = map(int, rl_ids)
	return rl_ids

def get_col_names():
	col_names = raw_input('Enter the columns you want to consider (comma separated). Press return to consider all columns.\n')
	col_names = [] if col_names.strip() == '' else col_names.split(',')
	col_names = map(str.strip, col_names)
	return col_names

def get_pws_to_consider():
	pws_to_consider = raw_input('Enter the PWs to consider (comma separated). Press return to consider all columns\n')
	pws_to_consider = [] if pws_to_consider.strip() == '' else pws_to_consider.split(',')
	pws_to_consider = map(str.strip, pws_to_consider)
	pws_to_consider = map(int, pws_to_consider)
	return pws_to_consider

while query_db in ['y', 'yes', '1', 1]:

	print 'Following are the parsed relation IDs and relation names:'
	for i, rl in enumerate(relations):
		print str(i) + ':', str(rl.relation_name)
	print '\n'
	print 'Following Queries are available:'
	print '1. Intersection\n 2. Union\n 3. Frequency\n 4. Number of Tuples\n 5. Difference\n 6. Redundant Column\n 7. Tuples occuring in exactly one PW\n 8. Show All Table Schemas\n 9. Show Table for a Relation\n'
	query_id = raw_input('Input the query id\n')
	sqlite_or_panda = raw_input("Do you want to use 'sqlite' or 'panda' to query?\n")
	query_id = int(query_id.strip())
	if query_id == 1:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pws_to_consider = get_pws_to_consider()

		if sqlite_or_panda.strip() == 'sqlite':
			print intersection_sqlite(rl_id, col_names, pws_to_consider, False)
		elif sqlite_or_panda.strip() == 'panda':
			print intersection_panda(rl_id, col_names, pws_to_consider, False)
	elif query_id == 2:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pws_to_consider = get_pws_to_consider()

		if sqlite_or_panda.strip() == 'sqlite':
			print union_sqlite(rl_id, col_names, pws_to_consider, False)
		elif sqlite_or_panda.strip() == 'panda':
			print union_panda(rl_id, col_names, pws_to_consider, False)
	elif query_id == 3:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pws_to_consider = get_pws_to_consider()
		vals = raw_input('Enter the specific values for the columns. Hit return to query frequency of all possible value combinations.\n')
		vals = [] if vals.strip() == '' else vals.split(',')
		vals = map(str.strip, vals)
		if sqlite_or_panda.strip() == 'sqlite':
			print freq_sqlite(rl_id, col_names, vals, pws_to_consider, False)
		elif sqlite_or_panda.strip() == 'panda':
			print freq_panda(rl_id, col_names, pws_to_consider, False)
	elif query_id == 4:
		rl_id = raw_input('Enter the relation id\n')
		rl_id = 0 if rl_id.strip() == '' else int(rl_id)
		pw_id = raw_input('Enter the PW ID for which to count the number of tuples.\n')
		pw_id = 0 if pw_id.strip() == '' else int(pw_id)
		if sqlite_or_panda.strip() == 'sqlite':
			print num_tuples_sqlite(rl_id, pw_id, False)
		elif sqlite_or_panda.strip() == 'panda':
			print num_tuples_panda(rl_id, pw_id, False)
	elif query_id == 5:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pw_id_1 = raw_input('Enter the PW ID of the first PW\n')
		pw_id_1 = 0 if pw_id_1.strip() == '' else int(pw_id_1)
		pw_id_2 = raw_input('Enter the PW ID of the second PW\n')
		pw_id_2 = 0 if pw_id_2.strip() == '' else int(pw_id_2)
		one_way_or_both = raw_input('Enter 1 for one-way difference and 2 for two-way difference.\n')
		one_way_or_both = 1 if one_way_or_both.strip() == '' else int(one_way_or_both)
		if sqlite_or_panda.strip() == 'sqlite':
			if one_way_or_both == 1:
				print difference_sqlite(rl_id, pw_id_1, pw_id_2, col_names, False)
			elif one_way_or_both == 2:
				print difference_both_ways_sqlite(rl_id, pw_id_1, pw_id_2, col_names, False)
		elif sqlite_or_panda.strip() == 'panda':
			if one_way_or_both == 1:
				print difference_panda(rl_id, pw_id_1, pw_id_2, col_names, False)
			elif one_way_or_both == 2:
				print difference_both_ways_panda(rl_id, pw_id_1, pw_id_2, col_names, False)
	elif query_id == 6:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pws_to_consider = get_pws_to_consider()
		if sqlite_or_panda.strip() == 'sqlite':
			print redundant_column_sqlite(rl_id, col_names, pws_to_consider, False)
		elif sqlite_or_panda.strip() == 'panda':
			print redundant_column_panda(rl_id, col_names, pws_to_consider, False)
	elif query_id == 7:
		rl_id = get_rl_id()
		col_names = get_col_names()
		pws_to_consider = get_pws_to_consider()
		if sqlite_or_panda.strip() == 'sqlite':
			print unique_tuples_sqlite(rl_id, col_names, pws_to_consider, False)
		elif sqlite_or_panda.strip() == 'panda':
			print unique_tuples_panda(rl_id, col_names, pws_to_consider, False)
	elif query_id == 8:
		for sch in schemas:
			print sch
	elif query_id == 9:
		rl_id = raw_input('Enter the relation id\n')
		rl_id = 0 if rl_id.strip() == '' else int(rl_id)
		print dfs[rl_id]
	else:
		print 'Invalid Query ID'

	query_db = raw_input('Do you want to query the database?\n')


#intersection_sqlite()#(0, ['x1', 'x2'], [1,5])
#intersection_panda()#(0, ['x1', 'x2'], [1,5])
#union_sqlite(0, ['x1', 'x2'], [1,5])
#union_panda(0, ['x1', 'x2'], [1,5])
#freq_sqlite(rl_id = 0, col_names = ['x1', 'x2'], values = ['4','5'], pws_to_consider = [1,4,5])
#freq_panda(rl_id = 1, col_names = ['x1'], values = ['30'], pws_to_consider = [1,2])
#num_tuples_sqlite(0, 3)
#num_tuples_panda(0, 3)
#difference_sqlite(0, 1, 2, ['x2'])
#difference_both_ways_sqlite(0, 1, 2, ['x2'])
#difference_panda(0, 1, 2, ['x2'])
#difference_both_ways_panda(0, 1, 2, ['x2'])
#redundant_column_sqlite(0, ['x1','x3'], [1,4,3])
#redundant_column_panda()
#unique_tuples_sqlite(0, ['x1', 'x2'], [1,3,5])
#unique_tuples_panda(0, ['x1', 'x2'], [1,3,5])

###########################################################################################

dist_matrix = None

def compute_dist_matrix(X):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file
	global dist_matrix

	if dist_matrix is not None:
		return dist_matrix

	print 'Distance Calculation:'
	print 'Following are the parsed relation IDs and relation names:'
	for i, rl in enumerate(relations):
		print str(i) + ':', str(rl.relation_name)

	#rl_ids = get_rl_ids_list_dist()
	rl_id = get_rl_id()
	col_name = get_col_name()
	dist_matrix = np.zeros((len(pws),len(pws)))
	for i in range(1, len(pws)+1):
		for j in range(i, len(pws)+1):
			#dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = dist_sqlite(i,j)
			#dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = dist_panda(i,j)
			#dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = sym_diff_dist_sqlite(i,j, rl_ids)
			dist_matrix[i-1, j-1] = dist_matrix[j-1,i-1] = euler_overlap_diff_dist(i, j, rl_id, col_name)
			#print 'Distance between PWs', i, 'and', j, 'is', dist_matrix[i-1,j-1]
	if np.max(dist_matrix) != np.min(dist_matrix):
		dist_matrix = (dist_matrix - np.min(dist_matrix))/(np.max(dist_matrix) - np.min(dist_matrix))
	return dist_matrix



def matplotlib_to_plotly(cmap, pl_entries):

    h = 1.0/(pl_entries-1) if pl_entries > 1 else 1
    pl_colorscale = []
    
    for k in range(pl_entries):
        C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])
        
    return pl_colorscale


def dbscan_clustering(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	db = DBSCAN(metric = 'precomputed', eps = 0.5, min_samples = 1)
	labels = db.fit_predict(dist_matrix)
	out_file.write('Cluster Labels: ' + str(labels) + '\n')


	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	unique_labels = set(labels)
	colors = [plt.cm.Spectral(each)
	          for each in np.linspace(0, 1, len(unique_labels))]
	

	#fig, ax = plt.subplots()

	for k, col in zip(unique_labels, colors):
	    if k == -1:
	        # Black used for noise.
	        col = [0, 0, 0, 1]

	    class_member_mask = (labels == k)

	    xy = dist_matrix[class_member_mask & core_samples_mask]
	    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
	             markeredgecolor='k', markersize=14)

	    xy = dist_matrix[class_member_mask & ~core_samples_mask]
	    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
	             markeredgecolor='k', markersize=6)

	#labels = ['point {0}'.format(i + 1) for i in range(expected_pws)]
	#fig.plugins = [mpld3.plugins.PointLabelTooltip(labels)]
	plt.title('Estimated number of clusters: %d' % n_clusters_)
	#mpld3.show()
	#plt.show()
	mkdir_p('Mini Workflow/parser_output/clustering_output/' + str(project_name))
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '.png')
	plt.figure()



def dbscan_clustering_plotly(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	db = DBSCAN(metric = 'precomputed', eps = 0.5, min_samples = 1)
	labels = db.fit_predict(dist_matrix)
	out_file.write('Cluster Labels: ' + str(labels) + '\n')


	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	unique_labels = set(labels)

	colors = matplotlib_to_plotly(plt.cm.Spectral, len(unique_labels))
	data = []

	for k, col in zip(unique_labels, colors):
    
	    if k == -1:
	        # Black used for noise.
	        col = 'black'
	    else:
	        col = col[1]
	    
	    class_member_mask = (labels == k)
	   
	    xy = dist_matrix[class_member_mask & core_samples_mask]
	    trace1 = go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers', 
	                        marker=dict(color=col, size=14,
	                                    line=dict(color='black', width=1)))

	    xy = dist_matrix[class_member_mask & ~core_samples_mask]
	    trace2 = go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers', 
	                        marker=dict(color=col, size=14,
	                                    line=dict(color='black', width=1)))
	    data.append(trace1)
	    data.append(trace2)

	layout = go.Layout(showlegend=False,
	                   title='Estimated number of clusters: %d' % n_clusters_,
	                   xaxis=dict(showgrid=False, zeroline=False),
	                   yaxis=dict(showgrid=False, zeroline=False))
	fig = go.Figure(data=data, layout=layout)

	py.plot(fig)



def linkage_dendrogram(dist_matrix):
	
	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	X = squareform(dist_matrix)
	Z = linkage(X, 'ward')
	
	plt.title('Hierarchical Clustering Dendrogram (Ward)')
	plt.xlabel('sample index')
	plt.ylabel('distance')
	dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
	#mpld3.show()
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_ward_dendrogram.png')
	plt.figure()
	
	linkage_matrix = linkage(X, "single")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Single)")
	#mpld3.show()
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_single_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "complete")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Complete)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_complete_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "average")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Average)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_average_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "weighted")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Weighted)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_weighted_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "centroid")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Centroid)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_centroid_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "median")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Median)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_median_dendrogram.png')
	plt.figure()


def dendrogram_plotly(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	pw_ids = [i for i in range(len(dist_matrix))]
	dendro = ff.create_dendrogram(dist_matrix, labels = pw_ids, distfun = compute_dist_matrix)
	dendro['layout'].update({'width':800, 'height':500})
	py.plot(dendro, filename='dendrogram')

def mds_graph(D):

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	global out_file

	G = nx.Graph()
	labels = {}
	for n in range(len(D)):
	    for m in range(len(D)-(n+1)):
	        G.add_edge(n,n+m+1)
	        labels[ (n,n+m+1) ] = str(D[n][n+m+1])
	pos=nx.spring_layout(G)

	nx.draw(G, pos)
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=30)
	mpld3.show()
	#plt.show()

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

	



dist_matrix = compute_dist_matrix(None)
#mds_graph(dist_matrix)
mds_graph_2(dist_matrix)





if len(pws) > 1:
	out_file.write(str(dist_matrix))
	out_file.write('\n')
	dbscan_clustering(dist_matrix)
	dbscan_clustering_plotly(dist_matrix)
	#linkage_dendrogram(dist_matrix)
	dendrogram_plotly(np.array([i for i in range(len(pws))]))

out_file.write('Complexity Analysis:\n')
print 'Complexity Analysis'
complexities = complexity_analysis()
out_file.write('Euler Complexity Analysis:\n')
print 'Euler Complexity Analysis'
complexities_euler = euler_complexity_analysis(get_rl_id(), get_col_name())


###########################################################################################

#closing SQLite Connection
if export_to_sql:
	conn.commit()
	conn.close()

#closing output file
out_file.close()



