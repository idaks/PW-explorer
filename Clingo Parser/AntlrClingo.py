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

class Relation:
	def __init__(self, relation_name):
		self.relation_name = relation_name
		self.arrity = 0
		self.r_id = 0

###################################################################

######################################################################################

def rearrangePWSandRLS():

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs
	#sort PWs and Rls by their ids
	#print lineno()
	relations.sort(key = lambda x: x.r_id)
	pws.sort(key = lambda x: x.pw_id)


def loadIntoPandas():

	global pws 
	global relations 
	global expected_pws 
	global curr_pw
	global curr_rl 
	global curr_rl_data 
	global n_rls
	global dfs

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

	def enterSolution(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs 
				
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

		curr_rl = Relation(ctx.TEXT().getText())
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

		#print lineno()
		optimum_found = ctx.TEXT().getText()
		if optimum_found == 'yes':
			print 'Optimum Solution was found'
		elif optimum_found == 'no':
			print 'Optimum Solution was not found'
		else:
			print 'Unexpected Output:', optimum_found

	def enterOptimization(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs

		#print lineno()
		opt_soln = ctx.TEXT().getText()
		print 'Optimized Solution is', opt_soln

	def enterModels(self, ctx):

		global pws 
		global relations 
		global expected_pws 
		global curr_pw
		global curr_rl 
		global curr_rl_data 
		global n_rls
		global dfs

		#print lineno()
		num_models = ctx.TEXT().getText()
		num_models = int(num_models)
		print "Number of Models:", num_models
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

		#print lineno()
		#loading into pandas DF
		rearrangePWSandRLS()
		loadIntoPandas()

######################################################################################

#use these 3 lines if input is coming from a .txt file 
script, fname, project_name = argv
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

exp_formats = raw_input()
exp_formats = exp_formats.split(',')
for i in range(len(exp_formats)):
	exp_formats[i] = exp_formats[i].strip()

export_to_sql = True if 'sql' in exp_formats else False
export_to_csv = True if 'csv' in exp_formats else False
export_to_hdf = True if 'h5' in exp_formats else False
export_to_msg = True if 'msg' in exp_formats else False
export_to_pkl = True if 'pkl' in exp_formats else False

#export_to_sql = True #making it true for querying purposes

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
	
	print relations[i].relation_name
	print df
	
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

############################################################################################################

#creating schemas for SQLite
#code to print schema of the tables created

schemas = []
if export_to_sql:
	schema_q = conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
	print 'Sqlite Schema:'
	for row in schema_q.fetchall():
		print row[4]
		schemas.append(row[4])
else:
	conn_t = sqlite3.connect("test.db")
	for i, df in enumerate(dfs):
		t = df.ix[0:0]
		t.to_sql(str(relations[i].relation_name), conn_t, if_exists = 'replace')
	schema_q = conn_t.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")
	print 'Sqlite Schema:'
	for row in schema_q.fetchall():
	 	print row[4]
	 	schemas.append(row[4])
	for i, df in enumerate(dfs):
		conn_t.execute('DROP TABLE ' + str(relations[i].relation_name))
	conn_t.commit()
	conn_t.close()
#this approach will take constant time since there is just one row in the exported database.

#########################################################################################################


#Some Possible Queries:

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#1: does a relation occur in all the PWs:

#SQLite Version:
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
# for i, df in enumerate(dfs):
# 	s1 = df[df.pw==1]
# 	for j in range(1, expected_pws):
# 		s1 = pd.merge(s1, df[df.pw == j+1], how = 'inner', on = list(df)[1:])
# 	k = list(df)[1:]
# 	s1 = s1[k]
# 	if len(s1) > 0:
# 		print "Intersection of all the PWs for the relation", str(relations[i].relation_name)
# 		print s1

#something like this could also be used to find intersection of a particular set of PWs
#both in pandas and SQLite

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#2: list of unique relations across all the PWs:

#SQLite Version:
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

all_tuples = []
#Panda Version:
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

#something like this could also be used to find intersection of a particular set of PWs
#both in pandas and SQLite

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#3: found out how many worlds a particluar relation occurs:

#SQLite Version:
#Pandas version of query #2 must be run before this to be able to run this query
# for i, df in enumerate(dfs):
# 	headers = list(df)[1:]
# 	for j in range(len(all_tuples[i])):
# 		query = 'select count(*) from ' + str(relations[i].relation_name) + ' where '
# 		for k in range(len(headers) - 1):
# 			query += headers[k] + '=' + all_tuples[i].ix[j][k] + ' and '
# 		query += headers[-1] + '=' + all_tuples[i].ix[j][-1] + ';'
# 		#print query
# 		ik = pd.read_sql_query(query, conn)
# 		print "Frequency of tuple", tuple(all_tuples[i].ix[j]), "of the relation", str(relations[i].relation_name), "is:", ik


#Panda Version:
#Pandas version of query #2 must be run before this to be able to run this query
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

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


###########################################################################################

#closing SQLite Connection
if export_to_sql:
	conn.commit()
	conn.close()



