import sys
from antlr4 import *
from ClingoLexer import ClingoLexer
from ClingoParser import ClingoParser
from ClingoListener import ClingoListener
import pandas as pd
import numpy as np


#######################################################
#helper func
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
#######################################################


#######################################################

class PossibleWorld:

	n_pws = 0
	def _init__(self, num_relations):
		rls = [[] for i in range(num_relations)]
		pw_id = n_pws
		n_pws += 1
		pw_soln = 0


	def add_relation(self, relation_id, relation_data):
		if relation_id >= len(rls):
			rls.append([])
		rls[relation_id].append(relation_data)

#######################################################

#######################################################
class Relation:


	def __init__(self, relation_name):
		self.relation_name = relation_name
		self.arrity = 0
		r_id = 0
#######################################################

pws = []
relations = []
expected_pws = 0
curr_pw = None
curr_rl = None
curr_rl_data = None
n_rls = 0

###################################################################

class AntlrClingoListener(ClingoListener):

	#test function
	def enterModels(self, ctx):
		num_models = ctx.TEXT().getText()
		num_models = int(num_models)
		print "Number of Models:", num_models
		expected_pws = num_models

	def enterSolution(self, ctx):

		curr_pw = PossibleWorld(n_rls)
		assert curr_pw.pw_id == int(ctx.TEXT(0).getText())
		curr_pw.pw_soln = float(ctx.TEXT(1).getText()) if isfloat(ctx.TEXT(1).getText()) else ctx.TEXT(1).getText()

	def enterActual_soln(self, ctx):

		for i in range(): #need to figure out how to get number of *s
			curr_rl = Relation(ctx.TEXT(i).getText())

	def enterCustom_representation_soln(self, ctx):

		sol = ctx.TEXT().getText();
		curr_rl_data = sol.split(',')
		curr_rl.arrity = len(rl_data)
		rl_name_mod = str(curr_rl.relation_name + '_' + str(curr_rl.arrity))
		curr_rl.relation_name = rl_name_mod

	def exitCustom_representation_soln(self,ctx):

		foundMatch = False
		for rl in relations:
			if curr_rl.relation_name == rl.relation_name and curr_rl.arrity == rl.arrity:
				curr_rl.r_id = rl.r_id
				foundMatch = True
				break
		
		if not foundMatch:
			newRl = Relation(curr_rl.relation_name)
			newRl.arrity = curr_rl.arrity
			newRl.r_id = n_rls
			n_rls += 1
			relations.append()

		curr_pw.add_relation(curr_rl.r_id, curr_rl_data)
		curr_rl = None #could introduce bugs if passed by pointer in the upper statement, so be careful, use copy() if needed
		curr_rl_data = None 

	def exitActual_soln(self, ctx):

		curr_rl = None
		curr_rl_data = None

	def exitSolution(self, ctx):

		pws.append(curr_pw) #again be wary, else use .copy()
		curr_pw = None 




###################################################################




lexer = ClingoLexer(StdinStream())
stream = CommonTokenStream(lexer)
parser = ClingoParser(stream)
tree = parser.clingoOutput()
pw_analyzer = AntlrClingoListener()
walker = ParseTreeWalker()
walker.walk(pw_analyzer, tree)


######################################################################

#loading into pandas DF






