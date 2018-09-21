#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import argparse
import importlib
from pwe_helper import PossibleWorld, Relation, load_from_temp_pickle, get_sql_conn, get_current_project_name, \
    set_current_project_name, get_save_folder, CUSTOM_VISUALIZATION_FUNCTIONS_FOLDER

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage
import networkx as nx
from sklearn.manifold import MDS
# from sklearn.decomposition import PCA


def dbscan_clustering(dist_matrix, save_to_file=None):

    fig, ax = plt.subplots()

    db = DBSCAN(metric='precomputed', eps=0.5, min_samples=1)
    labels = db.fit_predict(dist_matrix)

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    # dist_matrix = PCA(n_components = 2).fit_transform(dist_matrix)

    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)
        xy = dist_matrix[class_member_mask & core_samples_mask]
        ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)

        xy = dist_matrix[class_member_mask & ~core_samples_mask]
        ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)

    ax.title('Estimated number of clusters: %d' % n_clusters_)
    if save_to_file is not None:
        fig.savefig(save_to_file)
    return fig, labels


def linkage_dendrogram(dist_matrix, save_to_folder=None):

    X = squareform(dist_matrix)
    dendrogram_size = (max(25, int(np.sqrt(2 * len(X)) / 10)), 10)
    figs = []
    for dist_type in ['single', 'complete', 'average', 'weighted']:
        fig, ax = plt.subplots(figsize=dendrogram_size)
        linkage_matrix = linkage(X, dist_type)
        dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))], show_leaf_counts=True, ax=ax)
        ax.title("Dendrogram ({})".format(dist_type))
        if save_to_folder is not None:
            fig.savefig(os.path.join(save_to_folder, '{}_dendrogram.png'.format(dist_type)))
        figs.append(fig)
    return figs


def mds_graph_2(pws, A, scale_down_factor, save_to_file=True):

    dt = [('len', float)]
    A = A * len(A) / scale_down_factor
    A = A.view(dt)
    G = nx.from_numpy_matrix(A)
    G = nx.relabel_nodes(G,
                         dict(list(zip(list(range(len(G.nodes()))), ['pw-{}'.format(i) for i in range(0, len(pws))]))))

    G = nx.drawing.nx_agraph.to_agraph(G)

    G.node_attr.update(color="red", style="filled")
    G.edge_attr.update(color=None, width="0.1")
    # G.edge_attr.update(color="blue", width="0.1")

    if save_to_file is not None:
        G.draw(save_to_file, format='png', prog='neato')

    return G


def mds_sklearn(A, save_to_file=None):

    fig, ax = plt.subplots()
    mds = MDS(2, dissimilarity="precomputed")
    mds.fit(A)
    x = mds.embedding_[:, 0]
    y = mds.embedding_[:, 1]
    ax.scatter(x, y)
    if save_to_file is not None:
        fig.savefig(save_to_file)
    return fig


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
