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
import os
import errno
import string
import argparse
import pickle

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
out_file = None

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
#script, fname, project_name = argv

parser = argparse.ArgumentParser()
parser.add_argument("fname", type = str, help = "provide the preprocessed clingo output .txt file to parse")
parser.add_argument("project_name", type = str, help = "provide a suitable session/project name to reference these results in future scripts")
args = parser.parse_args()

fname = args.fname
project_name = args.project_name

out_file = open('Mini Workflow/parser_output/{}.txt'.format(project_name), 'w+')
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

#Add pickling commands here.
mkdir_p('Mini Workflow/temp_pickle_data/' + str(project_name))
with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dfs.pkl', 'wb') as f:
	pickle.dump(dfs, f)
with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/relations.pkl', 'wb') as f:
	pickle.dump(relations, f)
with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/pws.pkl', 'wb') as f:
	pickle.dump(pws, f)

with open('Mini Workflow/temp_pickle_data/' + 'current_project' + '/dfs.pkl', 'wb') as f:
	pickle.dump(dfs, f)
with open('Mini Workflow/temp_pickle_data/' + 'current_project' + '/relations.pkl', 'wb') as f:
	pickle.dump(relations, f)
with open('Mini Workflow/temp_pickle_data/' + 'current_project' + '/pws.pkl', 'wb') as f:
	pickle.dump(pws, f)


out_file.close()
