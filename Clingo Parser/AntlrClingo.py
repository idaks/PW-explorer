import sys
from antlr4 import *
from ClingoLexer import ClingoLexer
from ClingoParser import ClingoParser
from ClingoListener import ClingoListener

class PossibleWorld:

	def _init__(self, num_relations):
		rls = [[] for i in range(num_relations)]


	def add_relation(self, relation_id, relation_data):

		rls[relation_id].append(relation_data)



class Relation:

	n_relations = 0

	def __init__(self, relation_name, arrity):
		self.relation_name = relation_name
		self.arrity = arrity
		r_id = n_relations
		n_relations += 1






class AntlrClingoListener(ClingoListener):

	def enterModels(self, ctx):
		num_models = ctx.TEXT().getText()
		num_models = int(num_models)
		print "Number of Models:", num_models

	def 




#def main():
	#input_file = open(fname)
	#print (input_file.readlines())
pws = []
relations = []
lexer = ClingoLexer(StdinStream())
#lexer = ClingoLexer(input_file)
stream = CommonTokenStream(lexer)
parser = ClingoParser(stream)
tree = parser.clingoOutput()
pw_analyzer = AntlrClingoListener()
walker = ParseTreeWalker()
walker.walk(pw_analyzer, tree)

#script, fname = sys.argv
#main()