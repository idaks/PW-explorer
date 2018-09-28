#!/usr/bin/env python3

import argparse
import importlib

from PW_explorer.pwe_helper import (
    load_from_temp_pickle,
    get_sql_conn,
    get_save_folder,
    set_current_project_name,
    CUSTOM_VISUALIZATION_FUNCTIONS_FOLDER,
    get_current_project_name,
)
from PW_explorer.visualize import *


def __main__():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--project_name", type=str, help="provide session/project name used while parsing")
    parser.add_argument("-mds", action='store_true', default=False,
                        help="produce a Multidimensional Scaling Graph Output using the Neato Program. Provide a "
                             "scale-down-factor for graph generation. Default factor is 5.0")
    parser.add_argument("-mds_sklearn", action='store_true', default=False,
                        help="produce a MDS graph in 2D using skelearn's MDS package.")
    parser.add_argument("-sdf", "--scale_down_factor", type=float, default=5.0,
                        help="provide a scale factor for the Multidimensional Scaling Graph. Deafults to 5.0")
    parser.add_argument("-clustering", action='store_true', default=False,
                        help="use DBScan Algorithm to cluster the Possible Worlds")
    parser.add_argument("-dendrogram", action='store_true', default=False, help="create various dendrograms using scipy")
    parser.add_argument("-custom_visualization_func", type=str,
                        help="provide the .py file (without the .py) containing your custom visualisation function. "
                             "The function signature should be visualize(**kwargs) the following arguments are provided:\n"
                             "dfs, relations, pws, project_name, dist_matrix, save_to_folder, of which the visualization function may use any subset"
                             "from parsing the ASP solutions and the connection to the generated sqlite database "
                             "respectively. The function should create the visualization and may or may not return "
                             "anything. Ensure that the file is in the same directory as this script. You can use the "
                             "functions in sql_funcs.py to design these visualisation functions")

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
    dist_matrix = load_from_temp_pickle(project_name, 'dist_matrix')

    if args.mds:
        file_to_save_to = get_save_folder(project_name, 'visualization') + '/' + 'networkx_out.png'
        mds_graph_2(pws, dist_matrix, args.sdf, file_to_save_to)
        print('MDS Neato Graph saved to:', file_to_save_to)
    if args.mds_sklearn:
        file_to_save_to = get_save_folder(project_name, 'visualization') + '/' + 'mds_sklearn.png'
        mds_sklearn(dist_matrix, file_to_save_to)
        print('MDS Graph saved to: {}'.format(file_to_save_to))
    if len(pws) > 1:
        if args.clustering:
            file_to_save_to = get_save_folder(project_name, 'visualization') + '/' + 'dbscan_clustering_.png'
            dbscan_clustering(dist_matrix, file_to_save_to)
            print('Clustering Output saved to: {}'.format(file_to_save_to))
        if args.dendrogram:
            folder_to_save_to = get_save_folder(project_name, 'visualization')
            linkage_dendrogram(dist_matrix, folder_to_save_to)
            print('Dendrograms saved to:', folder_to_save_to)
    if args.custom_visualization_func:
        try:
            a = importlib.import_module(CUSTOM_VISUALIZATION_FUNCTIONS_FOLDER + '.' + args.custom_visualization_func)
            visualization_func = a.visualize
            visualization_func(dfs=dfs, pws=pws, relations=relations, dist_matrix=dist_matrix,
                               save_to_folder=get_save_folder(project_name, 'visualization'),
                               project_name=project_name)
        except Exception as e:
           print("Error importing from the given file")
           print("Error: ", str(e))
           exit(1)

    set_current_project_name(project_name)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    __main__()
