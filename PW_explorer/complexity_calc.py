#!/usr/bin/env python3

import pandas as pd
import numpy as np
import argparse
import importlib
from pwe_helper import load_from_temp_pickle, get_sql_conn, get_current_project_name, set_current_project_name, \
    rel_id_from_rel_name
from pwe_query import PWEQuery


def euler_complexity_analysis(relations, expected_pws, dfs, rl_id, col_name, pws_to_consider: list=None, do_print=True):

    if not pws_to_consider:
        pws_to_consider = [j for j in range(1, expected_pws + 1)]

    complexities = np.zeros(len(pws_to_consider))

    for i, pw in enumerate(pws_to_consider):
        complexities[i] = PWEQuery.freq(relations, expected_pws, dfs, rl_id, [col_name], ['"><"'], [pw], False)[1][0]

    if np.max(complexities) != np.min(complexities):
        complexities = (complexities - np.min(complexities)) / (np.max(complexities) - np.min(complexities))
    if do_print:
        paired_pw_compl = list(zip(pws_to_consider, complexities))
        paired_pw_compl = sorted(paired_pw_compl, key=lambda x: x[1], reverse=True)
        print('PWs:         ', str([x[0] for x in paired_pw_compl]))
        print('Complexities:', str([x[1].round(2) for x in paired_pw_compl]))

    return complexities


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, help="provide session/project name used while parsing")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-euler_complexity_analysis", action='store_true', default=False,
                       help="use this if working with an euler result. This measures the complexity as the number of "
                            "overlaps (""><"") in two PWs. Provide the relation name or relation id to use using "
                            "the -rel_name or rel_id flag respectively. Provide the column name to use using the "
                            "-col flag. Calculates complexity on all PWs by default. Use the -pws flag to specify "
                            "the possible world ids if compexity of only a few are required.")
    group.add_argument("-custom_complexity_func", type=str,
                       help="provide the .py file (without the .py) containing your custom complexity function. The "
                            "function signature should be complexity(pw_id, dfs = None, pws = None, relations = None, "
                            "conn = None) where the latter four arguments refer to the data acquired from parsing the "
                            "ASP solutions and the connection to the generated sqlite database respectively. The function "
                            "should return a floating point number. Ensure that the file is in the same directory as this "
                            "script. You can use the functions in sql_funcs.py to design these dist functions")
    group.add_argument("-show_relations", action='store_true', default=False,
                       help="to get a list of relations and corresponding relation ids.")

    parser.add_argument("-rel_name", type=str,
                        help="provide the relation name to use in the distance calculation. Note that if both rel_id "
                             "and rel_name are provided, rel_name is disregarded.")
    parser.add_argument("-rel_id", type=int,
                        help="provide the relation id of the relation to use in the distance calculation. To view "
                             "relation ids, use -show_relations")
    parser.add_argument("-col", type=str,
                        help="provide the column to use for the complexity analysis, required with the "
                             "euler_complexity_analysis function")
    parser.add_argument("-pws", type=int, default=[], nargs='*',
                        help="provide the possible world ids of the possible world to calculate the complexity for. "
                             "Calculates for all PWs if not used.")

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

    if args.show_relations:

        print('Following are the parsed relation IDs and relation names:')
        for i, rl in enumerate(relations):
            print(str(i) + ':', str(rl.relation_name))

    elif args.euler_complexity_analysis:

        if args.rel_name is None and args.rel_id is None:
            print("Please include either the -rel_name or -rel_id flag along with the appropriate argument.")
            exit(0)

        r_id = args.rel_id
        if r_id is None:
            r_id = rel_id_from_rel_name(args.rel_name, relations)

        if args.col is None:
            print("-col is required")
            exit(0)

        pws_to_consider = args.pws
        if pws_to_consider == []:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        try:
            euler_complexity_analysis(r_id, args.col, pws_to_consider)
        except Exception as e:
            print("Error running the euler_complexity_analysis. Recheck your inputs.")
            print("Error: ", str(e))
            exit(1)

    elif args.custom_complexity_func:

        try:
            a = importlib.import_module(args.custom_dist_func)
            comp_func = a.complexity
        except Exception as e:
            print("Error importing from the given file")
            print("Error: ", str(e))
            exit(1)

        pws_to_consider = args.pws
        if pws_to_consider == []:
            pws_to_consider = [j for j in range(1, expected_pws + 1)]

        complexities = np.zeros(len(pws_to_consider))

        try:
            for i, pw in enumerate(pws_to_consider):
                complexities[i] = comp_func(pw, dfs, pws, relations, conn)
        except Exception as e:
            print("Error running the given function. Recheck your inputs.")
            print("Error: ", str(e))
            exit(1)

        if np.max(complexities) != np.min(complexities):
            complexities = (complexities - np.min(complexities)) / (np.max(complexities) - np.min(complexities))

        paired_pw_compl = list(zip(pws_to_consider, complexities))
        paired_pw_compl = sorted(paired_pw_compl, key=lambda x: x[1], reverse=True)
        print('PWs:         ', str([x[0] for x in paired_pw_compl]))
        print('Complexities:', str([x[1].round(2) for x in paired_pw_compl]))

    set_current_project_name(project_name)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    __main__()
