#!/usr/bin/env python3

from sklearn.cluster import DBSCAN
import pickle
from pwe_helper import rel_id_from_rel_name, get_save_folder, load_from_temp_pickle
import matplotlib.pyplot as plt

def get_colors_list(df, id):
    idx = list(map(int, list(df[df.pw == id].x1)))
    clrs = list(df[df.pw == id].x2)

    ordered_clrs = [x for _, x in sorted(zip(idx, clrs))]
    return ordered_clrs

def visualize(dfs=None, pws=None, relations=None, conn=None, project_name=None):
    if project_name is None or relations is None or dfs is None:
        print("None objects passed.")
        exit(1)

    dist_matrix = load_from_temp_pickle(project_name, 'dist_matrix')

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

    output_folder = get_save_folder(project_name, 'four_colorability_visualization')

    for label, idx in list(unique_indices.items()):
        cols = get_colors_list(df, idx + 1)
        # print(cols)
        group_size = [1 for _ in cols]

        plt.figure()
        plt.pie(group_size, colors=cols)
        # print(label_counts[label])
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.annotate(str(label_counts[label]), xy=(0, 0), ha='center', va='center', fontsize=35)
        plt.savefig(output_folder + '/pattern_' + str(label) + '.png')
