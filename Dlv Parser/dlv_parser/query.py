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
    def intersection_sqlite(self, relation):
        self.c.execute("SELECT * FROM META WHERE relation_name=?", (relation,))
        meta = self.c.fetchone()
        relation_name = meta[0]
        pw_num = meta[1]
        field_num = meta[2]

        # list of pws number
        pws_to_consider = [j for j in range(1, pw_num +1)]
        #"x1, x2, ..."
        col_names = ', '.join(["x"+str(i) for i in range(1, field_num+1)])
        query_intersection = ''
        for j in pws_to_consider[:-1]:
            query_intersection += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(j) + ' intersect '
        query_intersection += 'select ' + col_names + ' from ' + relation_name + ' where pw = ' + str(pws_to_consider[-1]) + ';'
        self.c.execute(query_intersection)
        print (self.c.fetchall())
        """
        if do_print:
            out_file.write("Intersection for the relation" + str(relations[rl_id].relation_name) + "on features" + col_names + "for PWs" + str(', '.join(map(str, pws_to_consider))) + '\n')
            if len(ik) > 0:
                out_file.write(str(ik) + '\n')
            else:
                out_file.write("NULL\n")

        return ik
        """
    def displaySchema(self):
        for row in self.conn.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;"):
            print row[4]

    def query(self,q):
        for row in self.conn.execute(q):
            print row

def main():
    # TODO only output query result
    if args.o:
        sys.stdout = open(args.o[0], 'w')
    if args.sql:
        sqlQuery = SqlQuery(args.sql[0])
        if args.intersection:
            sqlQuery.intersection_sqlite(args.intersection[0])
        if args.display:
            sqlQuery.displaySchema()
        if args.query:
            sqlQuery.query(args.query[0])
            
    """
    if args.csv:
        pass
    """
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dlv parse to other data formats.')
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_sql = subparsers.add_parser('sqlQuery', help='sqlQuery help')
    parser_sql.add_argument('sql', nargs = 1, help='Input SQLite database location')
    parser_sql.add_argument('-d', '--display', action='store_true', help='Display Schema')
    parser_sql.add_argument('--intersection', nargs = 1, help='intersection relation name')
    parser_sql.add_argument('-query', nargs = 1, help='query input')
    parser_sql.add_argument('-o', nargs = 1, help='Output file location')
    
    parser_csv = subparsers.add_parser('pandasQuery', help='pandasQuery help')
    parser_csv.add_argument('csv', nargs = 1, help='Input csv file location')
    #parser.add_argument("")
    args = parser.parse_args()
    main()
