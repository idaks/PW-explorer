#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage
import networkx as nx
from sklearn.manifold import MDS
# from sklearn.decomposition import PCA
import seaborn as sns

from .Custom_Visualization_Functions.graphviz_meta_data_based_visualization import build_nx_from_metadata

class PWEVisualization:

    @staticmethod
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

        ax.set_title('Estimated number of clusters: %d' % n_clusters_)
        if save_to_file is not None:
            fig.savefig(save_to_file)
        return fig, labels

    @staticmethod
    def linkage_dendrogram(dist_matrix, pws_used: list=None, save_to_folder=None):

        if not pws_used:
            pws_used = range(1, len(dist_matrix)+1)

        pws_used = list(map(str, pws_used))

        X = squareform(dist_matrix)
        dendrogram_size = (max(25, int(np.sqrt(2 * len(X)) / 10)), 10)
        figs = []
        for dist_type in ['single', 'complete', 'average', 'weighted']:
            fig, ax = plt.subplots(figsize=dendrogram_size)
            linkage_matrix = linkage(X, dist_type)
            dendrogram(linkage_matrix, labels=pws_used, show_leaf_counts=True, ax=ax)
            ax.set_title("Dendrogram ({})".format(dist_type))
            if save_to_folder is not None:
                fig.savefig(os.path.join(save_to_folder, '{}_dendrogram.png'.format(dist_type)))
            figs.append(fig)
        return figs

    @staticmethod
    def mds_networkx(pws_used, A, scale_down_factor, save_to_file=True):

        dt = [('len', float)]
        A = A * len(A) / scale_down_factor
        A = A.view(dt)
        G = nx.from_numpy_matrix(A)
        G = nx.relabel_nodes(G,
                             dict(list(zip(list(range(len(G.nodes()))), ['pw-{}'.format(pw) for pw in pws_used]))))
        G = nx.drawing.nx_agraph.to_agraph(G)

        G.node_attr.update(color="red", style="filled")
        G.edge_attr.update(color=None, width="0.1")
        # G.edge_attr.update(color="blue", width="0.1")

        if save_to_file is not None:
            G.draw(save_to_file, format='png', prog='neato')

        return G

    @staticmethod
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

    @staticmethod
    def graphviz_from_meta_data(pw_rel_dfs, graphviz_meta_data):
        """
        Assumes a sliced pw_rel_dfs has been passed in.
        :param pw_rel_dfs:
        :param graphviz_meta_data:
        :return:
        """
        return build_nx_from_metadata(pw_rel_dfs, graphviz_meta_data)

    @staticmethod
    def cluster_map_viz(dist_matrix, pw_ids: list = None, cmap="mako"):

        if not pw_ids:
            pw_ids = range(1, dist_matrix.shape[0] + 1)

        pw_ids_mapper_key = lambda x: pw_ids[x]

        t = pd.DataFrame(dist_matrix)
        t = t.rename(pw_ids_mapper_key, axis='index')
        t = t.rename(pw_ids_mapper_key, axis='columns')
        cluster_map = sns.clustermap(t, cmap=cmap)
        fig = cluster_map.fig
        plt.show()
        return fig