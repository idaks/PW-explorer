import sys, os
from sys import argv
from antlr4 import *
from DlvLexer import DlvLexer
from DlvParser import DlvParser
from DlvListener import DlvListener
import pandas as pd
import numpy as np
import inspect
from antlr4.tree.Trees import Trees
import string
from sets import Set
import argparse
import sqlite3
import errno  

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

class PossibleWorld:
    def __init__(self):
        self.pw = 0
        self.row_val = []
###################################################################

#Class to store details and solution relating to every possible world

dfs = {}
possibleWorlds = []
class PossibleWorld:
    n_pws = 0
    def __init__(self):
        self.rls = []
        self.rls_types = set() 
        PossibleWorld.n_pws += 1
        self.pw_id = PossibleWorld.n_pws


    def add_relation(self, relation_id, relation_data):
        if relation_id >= len(self.rls):
            self.rls.append([])
        self.rls[relation_id].append(relation_data)

###################################################################

###################################################################

#Class to store description of each relation found in the dlv output

class Relation:
    def __init__(self, relation_name):
        self.relation_name = relation_name
        self.vals = []
        self.arrity = 0
        self.r_id = 0

###################################################################

class DlvPrintListener(DlvListener): 
    parseStr = lambda s, x: x.isalpha() and x or x.isdigit() and \
            int(x) or x.isalnum() and x or \
            len(set(string.punctuation).intersection(x)) == 1 and \
        x.count('.') == 1 and float(x) or x
    def __init__(self):
        self.row_val = []
    def enterSolution(self, ctx):
        self.curr_pw = PossibleWorld() 
#        print("curr_pw.pw_id", self.curr_pw.pw_id)

    def enterAtom(self, ctx):
        self.curr_rel = Relation(ctx.TEXT().getText())

    def enterVal(self, ctx):
        self.row_val.append(self.parseStr(ctx.TEXT().getText()))

    def exitAtom_vals(self, ctx):
        self.curr_rel.vals = self.row_val
        self.curr_rel.arrity = len(self.row_val)
        self.curr_rel.rls_type = (self.curr_rel.relation_name, len(self.row_val))
        self.curr_pw.rls.append(self.curr_rel)
        self.row_val = []

#        print("rel name: ", self.curr_rel.relation_name)
#        print("rel val: ", self.curr_rel.vals)
        
    def exitSolution(self, ctx):
        # find all relation types
        for rel in self.curr_pw.rls:
            self.curr_pw.rls_types.update([rel.rls_type]) 
        possibleWorlds.append(self.curr_pw)

def loadIntoPandas(possibleWorlds):
    # find all relation types
    # a set of tuples (rel_name, rel_arrity)
    all_rls_types = set() 
    for pw in possibleWorlds:
        all_rls_types.update(pw.rls_types)
    # initialize dictionary 
    # with key : (rel_name, rel_arrity)
    # with value : Dataframe of all possible worlds
    for rls in all_rls_types:
        dfs[rls] = []
    
    # insert value from possibleWorlds to the dataframe
    for pw in possibleWorlds:
        for rel in pw.rls:
            dfs[rls].append([pw.pw_id]+rel.vals)

    # 2D array to dataframe
    for rls in all_rls_types:
        # assign column names
        cls = ['pw']
        cls.extend([str('x' + str(i)) for i in range(1, rls[1] + 1)])
        dfs[rls] = pd.DataFrame(np.array(dfs[rls]), columns=cls) 

def parseDlvToPws():
    asp_file = args.fileName
    input = FileStream(asp_file)
    lexer = DlvLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DlvParser(stream)
    #tree = parser.atom_vals()
    tree = parser.dlvOutput()
    printer = DlvPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
def getProjectName(fileName):
    filePath = args.fileName.split("/")
    fileCoreName = filePath[len(filePath)-1].split(".")[0]
    return fileCoreName
def pandasToOutputFiles():
    #TODO: change project name to project folder/file
    project_name = getProjectName(args.fileName)
    output_dir = os.path.dirname(os.path.realpath(__file__)) + '/../Mini Workflow/parser_output/'
    conn = None

    if args.sql:
        output_folder = str(output_dir + 'sql_exports/' + str(project_name))
        mkdir_p(output_folder)
        print(output_folder)
        conn = sqlite3.connect(output_folder + '/' + str(project_name) + ".db")
        for rsl_type, df in dfs.iteritems():
            df.to_sql(str(rsl_type[0]), conn, if_exists = 'replace')
        conn.close()
    if args.csv:
        output_folder = str(output_dir + 'csv_exports/' + str(project_name))
        mkdir_p(output_folder)
        for rsl_type, df in dfs.iteritems():
            df.to_csv(output_folder + '/' + str(rsl_type[0]) + '.csv')
    if args.hdf:
        output_folder = str(output_dir + 'hdf_exports/' + str(project_name))
        mkdir_p(output_folder)
        for rsl_type, df in dfs.iteritems():
            df.to_hdf(output_folder + '/' + str(rsl_type[0]) + '.h5', str(rsl_type[0]), mode = 'w')
    if args.msg:
        output_folder = str(output_dir + 'msg_exports/' + str(project_name))
        mkdir_p(output_folder)
        for rsl_type, df in dfs.iteritems():
            df.to_msgpack(output_folder + '/' + str(rsl_type[0]) + '.msg')
    if args.pkl:
        output_folder = str(output_dir + 'pkl_exports/' + str(project_name))
        mkdir_p(output_folder)
        for rsl_type, df in dfs.iteritems():
            df.to_pickle(output_folder + '/' + str(rsl_type[0]) + '.pkl')

def main():

    parseDlvToPws()
    loadIntoPandas(possibleWorlds)
    pandasToOutputFiles()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dlv parse to other data formats.')
    parser.add_argument('fileName', help='ASP file location')

    parser.add_argument('--sql', action='store_true', help='Output SQLite database')
    parser.add_argument('--csv', action='store_true', help='Output csv format')
    parser.add_argument('--hdf', action='store_true', help='Output hdf format')
    parser.add_argument('--msg', action='store_true', help='Output msg format')
    parser.add_argument('--pkl', action='store_true', help='Output pkl format')
    args = parser.parse_args()
    main()
