import sys, os
from sys import argv
import pandas as pd
import numpy as np
import inspect
import string
import argparse
import sqlite3
import errno  
import logging
FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT)

class SqlQuery:
    def __init__(self, location):
        self.location = location
        if os.path.exists(location):
            try:
                self.conn = sqlite3.connect(location)
                self.c = self.conn.cursor()
            except sqlite3.Error:
                logging.error(traceback.format_exc())
                exit()
        
        else:
            logging.error("location \"" + location + "\" doesn't exist")
            exit()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    #Some Possible Queries:

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

    #1: Intersection

    #SQLite Version:
    def intersection_sqlite():
    #def intersection_sqlite(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):
        # number of lines
        """
        if pws_to_consider == []:
            pws_to_consider = [j for j in range(1, expected_pws+1)]
        """
        # "x1", "x2"...
        """
        if col_names == []:
            col_names = list(dfs[rl_id])[1:]
        query_intersection = ''
        """
        #"x1, x2, ..."
        """
        col_names = ', '.join(map(str,col_names))
        """
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

def main():
    if args.sql:
        with SqlQuery(args.sql[0]) as sqlQuery:

    if args.csv:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dlv parse to other data formats.')

    parser.add_argument('-sql', '--sql', nargs = 1, help='Input SQLite database location')
    parser.add_argument('-csv', '--csv', nargs = 1, help='Input csv file location')
    args = parser.parse_args()
    main()
