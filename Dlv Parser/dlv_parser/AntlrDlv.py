import sys
from sys import argv
from antlr4 import *
from DlvLexer import DlvLexer
from DlvParser import DlvParser
from DlvListener import DlvListener
import pandas as pd
import numpy as np
import inspect
from antlr4.tree.Trees import Trees

class DlvPrintListener(DlvListener):
    def enterAtom(self, ctx):
        print(ctx.TEXT())
#    def enterAtom_vals(self, ctx):
#        print(ctx.val(0).TEXT())
def main():
    asp_file = sys.argv[1]
    input = FileStream(asp_file)
    lexer = DlvLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DlvParser(stream)
    #tree = parser.atom_vals()
    tree = parser.atom()
    printer = DlvPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
if __name__ == '__main__':
    main()
