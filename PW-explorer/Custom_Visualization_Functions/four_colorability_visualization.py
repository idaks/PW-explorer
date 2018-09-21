#!/usr/bin/env python3

from sklearn.cluster import DBSCAN
from pwe_helper import rel_id_from_rel_name, mkdir_p
import matplotlib.pyplot as plt
from collections import defaultdict
import os


def get_colors_list(df, id):
    idx = list(map(int, list(df[df.pw == id].x1)))
    clrs = list(df[df.pw == id].x2)

    ordered_clrs = [x for _, x in sorted(zip(idx, clrs))]
    return ordered_clrs


def visualize(**kwargs):

    kwargs = defaultdict(lambda: None, kwargs)
    dfs = kwargs['dfs']
    relations = kwargs['relations']
    save_to_folder = kwargs['save_to_folder']
    dist_matrix = kwargs['dist_matrix']

    if relations is None or dfs is None:
        print("No objects passed.")
        exit(1)

    db = DBSCAN(metric='precomputed', eps=0.5, min_samples=1)
    labels = db.fit_predict(dist_matrix)

    unique_indices = {}
    label_counts = {}
    for i, label in enumerate(labels):
        if label not in unique_indices:
            unique_indices[label] = i
            label_counts[label] = 1
        else:
            label_counts[label] += 1

    df = dfs[rel_id_from_rel_name('col_2', relations)]

    figs = []
    for label, idx in list(unique_indices.items()):
        fig, ax = plt.subplots()
        cols = get_colors_list(df, idx + 1)
        # print(cols)
        group_size = [1 for _ in cols]
        ax.pie(group_size, colors=cols)
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        ax.annotate(str(label_counts[label]), xy=(0, 0), ha='center', va='center', fontsize=35)
        figs.append(fig)

    if save_to_folder is not None:
        output_folder = os.path.join(save_to_folder, 'four_colorability_visualization')
        mkdir_p(output_folder)
        for i, fig in enumerate(figs):
            fig.savefig(os.path.join(output_folder, 'pattern_{}.png'.format(str(i))))

    return figs
