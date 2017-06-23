import sys
from antlr4 import *
from ClingoLexer import ClingoLexer
from ClingoParser import ClingoParser
from ClingoListener import ClingoListener

class AntlrClingoListener(ClingoListener):

	def enterModels(self, ctx):
		num_models = ctx.NUM_MODELS().getText()
		num_models = int(num_models)
		print "Number of Models: ", num_models





def main():
	#input_file = open(fname)
	#print (input_file.readlines())
	lexer = ClingoLexer(StdinStream())
	#lexer = ClingoLexer(input_file)
	stream = CommonTokenStream(lexer)
	parser = ClingoParser(stream)
	tree = parser.clingoOutput()
	pw_analyzer = AntlrClingoListener()
	walker = ParseTreeWalker()
	walker.walk(pw_analyzer, tree)

#script, fname = sys.argv
main()