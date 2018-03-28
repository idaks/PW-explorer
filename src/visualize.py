import pandas as pd
import numpy as np
import os
import sqlite3
import argparse
import pickle
import importlib
from .helper import PossibleWorld, Relation, load_from_temp_pickle, get_sql_conn, get_current_project_name, \
    set_current_project_name, get_save_folder

import matplotlib.pyplot as plt

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
parser.add_argument("-custom_visualisation_func", type=str,
                    help="provide the .py file (without the .py) containing your custom visualisation function. "
                         "The function signature should be visualize(dfs = None, pws = None, relations = None, "
                         "conn = None, project_name=None) where the four arguments refer to the data acquired "
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
expected_pws = len(pws)
dist_matrix = load_from_temp_pickle(project_name, 'dist_matrix')


def compute_dist_matrix(X=None):
    global dist_matrix
    return dist_matrix


def matplotlib_to_plotly(cmap, pl_entries):
    h = 1.0 / (pl_entries - 1) if pl_entries > 1 else 1
    pl_colorscale = []

    for k in range(pl_entries):
        C = list(map(np.uint8, np.array(cmap(k * h)[:3]) * 255))
        pl_colorscale.append([k * h, 'rgb' + str((C[0], C[1], C[2]))])

    return pl_colorscale


def dbscan_clustering(dist_matrix):
    global pws
    global relations
    global expected_pws
    global dfs

    db = DBSCAN(metric='precomputed', eps=0.5, min_samples=1)
    labels = db.fit_predict(dist_matrix)
    print('Cluster Labels:', str(labels))

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    # dist_matrix = PCA(n_components = 2).fit_transform(dist_matrix)

    # plt.xlim((-5,5))
    # plt.ylim((-5,5))

    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = dist_matrix[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = dist_matrix[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    save_folder = get_save_folder(project_name, 'visualization')
    plt.savefig(save_folder + str(project_name) + '_dbscan_clustering_.png')
    plt.figure()
    print('Clustering Output saved to: {}'.format(save_folder))


def dbscan_clustering_plotly(dist_matrix):
    global pws
    global relations
    global expected_pws
    global dfs

    db = DBSCAN(metric='precomputed', eps=0.5, min_samples=1)
    labels = db.fit_predict(dist_matrix)
    print('Cluster Labels:', str(labels))

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    unique_labels = set(labels)

    colors = matplotlib_to_plotly(plt.cm.Spectral, len(unique_labels))
    data = []

    for k, col in zip(unique_labels, colors):

        if k == -1:
            # Black used for noise.
            col = 'black'
        else:
            col = col[1]

        class_member_mask = (labels == k)

        xy = dist_matrix[class_member_mask & core_samples_mask]
        trace1 = go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers',
                            marker=dict(color=col, size=14,
                                        line=dict(color='black', width=1)))

        xy = dist_matrix[class_member_mask & ~core_samples_mask]
        trace2 = go.Scatter(x=xy[:, 0], y=xy[:, 1], mode='markers',
                            marker=dict(color=col, size=14,
                                        line=dict(color='black', width=1)))
        data.append(trace1)
        data.append(trace2)

    layout = go.Layout(showlegend=False,
                       title='Estimated number of clusters: %d' % n_clusters_,
                       xaxis=dict(showgrid=False, zeroline=False),
                       yaxis=dict(showgrid=False, zeroline=False))
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig)


def linkage_dendrogram(dist_matrix):
    global pws
    global relations
    global expected_pws
    global dfs

    # print str(dist_matrix)
    # print dist_matrix.shape

    X = squareform(dist_matrix)
    dendrogram_size = (max(25, int(np.sqrt(2 * len(X)) / 10)), 10)
    save_folder = get_save_folder(project_name, 'visualization')
    for dist_type in ['single', 'complete', 'average', 'weighted']:
        linkage_matrix = linkage(X, dist_type)
        plt.figure(figsize=dendrogram_size)
        dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))], show_leaf_counts=True)
        plt.title("Dendrogram ({})".format(dist_type))
        plt.savefig(save_folder + str(project_name) + '_{}_dendrogram.png'.format(dist_type))

    print('Dendrograms saved to:', save_folder)


def dendrogram_plotly(dist_matrix):
    global pws
    global relations
    global expected_pws
    global dfs

    pw_ids = [i for i in range(len(dist_matrix))]
    dendro = ff.create_dendrogram(dist_matrix, labels=pw_ids, distfun=compute_dist_matrix)
    dendro['layout'].update({'width': 800, 'height': 500})
    py.plot(dendro, filename='dendrogram')


def mds_graph_2(A):
    global pws
    global relations
    global expected_pws
    global dfs

    dt = [('len', float)]
    scale_down_factor = args.scale_down_factor
    A = A * len(A) / scale_down_factor
    A = A.view(dt)
    G = nx.from_numpy_matrix(A)
    # G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))
    G = nx.relabel_nodes(G,
                         dict(list(zip(list(range(len(G.nodes()))), ['pw-{}'.format(i) for i in range(0, len(pws))]))))

    G = nx.drawing.nx_agraph.to_agraph(G)

    G.node_attr.update(color="red", style="filled")
    G.edge_attr.update(color=None, width="0.1")
    # G.edge_attr.update(color="blue", width="0.1")

    save_folder = get_save_folder(project_name, 'visualization')
    G.draw(save_folder + str(project_name) + '_networkx_out.png', format='png', prog='neato')
    print('MDS Neato Graph saved to:', save_folder)


def mds_sklearn(A):
    from sklearn.manifold import MDS
    mds = MDS(2, dissimilarity="precomputed")
    mds.fit(A)
    x = mds.embedding_[:, 0]
    y = mds.embedding_[:, 1]
    plt.scatter(x, y)
    save_folder = get_save_folder(project_name, 'visualization')
    plt.savefig(save_folder + str(project_name) + '_mds_sklearn.png')
    plt.figure()


if args.mds:
    import networkx as nx
    mds_graph_2(dist_matrix)
if args.mds_sklearn:
    mds_sklearn(dist_matrix)
if len(pws) > 1:
    if args.clustering:
        from sklearn.cluster import DBSCAN
        from sklearn.decomposition import PCA

        dbscan_clustering(dist_matrix)
    # dbscan_clustering_plotly(dist_matrix)
    if args.dendrogram:
        from scipy.spatial.distance import squareform
        from scipy.cluster.hierarchy import dendrogram, linkage

        linkage_dendrogram(dist_matrix)
# dendrogram_plotly(np.array([i for i in range(len(pws))]))

if args.custom_visualisation_func:

    try:
        a = importlib.import_module(args.custom_visualisation_func, package='Custom_Visualization_Functions')
        visualisation_func = a.visualize
    except Exception as e:
        print("Error importing from the given file")
        print("Error: ", str(e))
        exit(1)

    visualisation_func(dfs, pws, relations, conn, project_name)

set_current_project_name(project_name)
conn.commit()
conn.close()
