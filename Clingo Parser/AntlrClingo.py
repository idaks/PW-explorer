import sys
from antlr4 import *
from ClingoLexer import ClingoLexer
from ClingoParser import ClingoParser
from ClingoListener import ClingoListener

class AntlrClingoListener(DrinkListener):
	




def main(argv):
	lexer = ClingoLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = ClingoParser(stream)
	tree = parser.hi()
	pw_analyzer = AntlrClingoListener()
	walker = ParseTreeWalker()
	walker.walk(pw_analyzer, tree)

if __name__ == '__main__':
    main(sys.argv)