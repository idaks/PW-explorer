#!/usr/bin/env python3
# SQLite QUERY SCRIPT:

import pandas as pd
import numpy as np
import sqlite3
import os
import argparse
from .helper import get_current_project_name, set_current_project_name, \
    load_from_temp_pickle, get_sql_conn, rel_id_from_rel_name
from . import sql_funcs


def union_panda(relations, expected_pws, dfs, pws, rl_id=0, col_names=[], pws_to_consider=[], do_print=True):

    if not pws_to_consider:
        pws_to_consider = [j for j in range(1, expected_pws + 1)]

    if not col_names:
        col_names = list(dfs[rl_id])[1:]

    return sql_funcs.union_panda(dfs, pws, relations, rl_id, col_names, pws_to_consider, do_print)


# 1: Intersection
def intersection_sqlite(relations, expected_pws, dfs, conn, pws, rl_id=0, col_names=[],
                        pws_to_consider=[], do_print=True):

    if not pws_to_consider:
        pws_to_consider = [j for j in range(1, expected_pws + 1)]

    if not col_names:
        col_names = list(dfs[rl_id])[1:]
    return sql_funcs.intersection_sqlite(dfs, pws, relations, conn, rl_id, col_names, pws_to_consider, do_print)


# 2: Union
def union_sqlite(relations, expected_pws, dfs, conn, pws, rl_id=0, col_names=[], pws_to_consider=[], do_print=True):

    if not pws_to_consider:
        pws_to_consider = [j for j in range(1, expected_pws + 1)]

    if not col_names:
        col_names = list(dfs[rl_id])[1:]

    return sql_funcs.union_sqlite(dfs, pws, relations, conn, rl_id, col_names, pws_to_consider, do_print)


# 3: Frequency of a tuple
def freq_sqlite(relations, dfs, conn, pws, rl_id=0, col_names=[], values=[], pws_to_consider=[],
                do_print=True):

    return sql_funcs.freq_sqlite(dfs, pws, relations, conn, rl_id, col_names, values, pws_to_consider, do_print)


# 4: Number of tuples of a relation in a PW
def num_tuples_sqlite(relations, conn, rl_id, pw_id, do_print=True):

    return sql_funcs.num_tuples_sqlite(relations, conn, rl_id, pw_id, do_print)


# 5: Difference Query
def difference_sqlite(relations, conn, dfs, rl_id, pw_id_1, pw_id_2, col_names=[], do_print=True):

    return sql_funcs.difference_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, col_names, do_print)


def difference_both_ways_sqlite(relations, conn, dfs, rl_id, pw_id_1, pw_id_2, col_names=[], do_print=True):

    return sql_funcs.difference_both_ways_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, col_names, do_print)


# 6: Redundant Column Query
def redundant_column_sqlite(relations, expected_pws, dfs, conn, pws, rl_id=0, col_names=[], pws_to_consider=[],
                            do_print=True):

    if not pws_to_consider:
        pws_to_consider = [j for j in range(1, expected_pws + 1)]

    return sql_funcs.redundant_column_sqlite(dfs, pws, relations, conn, rl_id, col_names, pws_to_consider, do_print)


# 7: Tuples occuring in exactly one PW:
def unique_tuples_sqlite(relations, pws, dfs, conn, rl_id=0, col_names=None, pws_to_consider=None, do_print=True):

    return sql_funcs.unique_tuples_sqlite(dfs, pws, relations, conn, rl_id, col_names, pws_to_consider, do_print)


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, help="provide session/project name used while parsing")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-intersection", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
    group.add_argument("-union", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
    group.add_argument("-freq", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag, possible worlds to consider using the -pws flag and "
                            "the values for the columns (in the mentioned order) using the -vals flag (optional).")
    group.add_argument("-num_tuples", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively "
                            "and the possible world ids to count the tuples in using the -pws flag.")
    group.add_argument("-difference", choices=('one-way', 'symmetric'),
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag and the two possible world ids using the -pws flag.")
    group.add_argument("-redundant_column", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
    group.add_argument("-unique_tuples", action='store_true', default=False,
                       help="provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, "
                            "columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
    group.add_argument("-custom", type=str, help="provide the query enclosed in '' .")
    group.add_argument("-custom_file", type=str, help="provide the .sql file containing the query.")
    group.add_argument("-show_relations", action='store_true', default=False,
                       help="to get a list of relations and corresponding relation ids.")

    parser.add_argument("-rel_name", type=str,
                        help="provide the relation name to query. Note that if both rel_id and rel_name are provided, "
                             "rel_name is disregarded.")
    parser.add_argument("-rel_id", type=int,
                        help="provide the relation id of the relation to query. To view relation ids, use -show_relations")
    parser.add_argument("-cols", type=str, nargs='*', default=[],
                        help="provide the columns of the selected relations to consider for the chosen query. If you want "
                             "to consider all the columns, do not include this flag.")
    parser.add_argument("-pws", type=int, nargs='*', default=[],
                        help="provide the possible world ids of the possible world to consider for this query. If you want "
                             "to consider all the possible worlds, do not include this flag. Please note that difference "
                             "query requires exactly 2 arguments for this flag.")
    parser.add_argument("-vals", nargs='*', default=[], type=str,
                        help="provide the values for the freq query in the same order as the mentioned columns. If you "
                             "want to query all possible tuples, do not include this flag.")

    args = parser.parse_args()

    project_name = ''
    if args.project_name is None:
        project_name = get_current_project_name()
        if project_name is None:
            print("Couldn't find current project. Please provide a project name.")
            exit(1)
    else:
        project_name = args.project_name

    dfs = load_from_temp_pickle(project_name, 'dfs')
    relations = load_from_temp_pickle(project_name, 'relations')
    pws = load_from_temp_pickle(project_name, 'pws')
    conn = get_sql_conn(project_name)
    expected_pws = len(pws)
    # print "pws: ", args.pws
    # print "cols: ", args.cols

    if args.intersection:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        soln = None
        try:
            soln = intersection_sqlite(r_id, args.cols, args.pws, True)
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.union:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        soln = None
        try:
            soln = union_sqlite(r_id, args.cols, args.pws, True)
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.freq:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        soln = None
        try:
            soln = freq_sqlite(r_id, args.cols, args.vals, args.pws, True)
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.num_tuples:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        pws_to_consider = args.pws
        if pws_to_consider == []:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        soln = []
        try:
            for i in pws_to_consider:
                soln.append(num_tuples_sqlite(r_id, i, True))
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.difference is not None:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        if len(args.pws) != 2:
            print("Please provide exactly 2 possible world ids.")
            exit(0)

        soln = None

        if args.difference == 'one-way':
            try:
                soln = difference_sqlite(r_id, args.pws[0], args.pws[1], args.cols, True)
            except Exception as e:
                print("Query failed. Please check the provided arguments to make sure they are valid.")
                print("Error: ", str(e))
                exit(1)
        elif args.difference == 'symmetric':
            try:
                soln = difference_both_ways_sqlite(r_id, args.pws[0], args.pws[1], args.cols, True)
            except Exception as e:
                print("Query failed. Please check the provided arguments to make sure they are valid.")
                print("Error: ", str(e))
                exit(1)

    elif args.redundant_column:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        soln = None
        try:
            soln = redundant_column_sqlite(r_id, args.cols, args.pws, True)
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.unique_tuples:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        soln = None
        try:
            soln = unique_tuples_sqlite(r_id, args.cols, args.pws, True)
        except Exception as e:
            print("Query failed. Please check the provided arguments to make sure they are valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.show_relations:

        print('Following are the parsed relation IDs and relation names:')
        for i, rl in enumerate(relations):
            print(str(i) + ':', str(rl.relation_name))

    elif args.custom is not None:

        ik = None
        try:
            ik = pd.read_sql_query(args.custom, conn)
            print(str(ik))
            if len(ik) <= 0:
                print("NULL")
        except Exception as e:
            print("Query failed. Please check the provided query to make sure it is valid.")
            print("Error: ", str(e))
            exit(1)

    elif args.custom_file is not None:

        if not os.path.exists(args.custom_file):
            print("No file by the name {} exists. Please recheck the .sql file location".format(args.custom_file))
            exit(1)

        f = open(args.custom_file, 'r')
        f = f.read()

        sqlQueries = f.split(';')
        soln = []
        # print sqlQueries
        for q in sqlQueries:
            if q.strip() == '':
                continue
            try:
                soln.append(pd.read_sql_query(q, conn))
                print(str(soln[-1]))
                if len(soln[-1]) <= 0:
                    print("NULL")
            except Exception as e:
                print("Query failed. Please check the provided query to make sure it is valid.")
                print("Error: ", str(e))
                exit(1)

    conn.commit()
    conn.close()
    set_current_project_name(project_name)


if __name__ == '__main__':
    __main__()