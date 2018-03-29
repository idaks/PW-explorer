#!/usr/bin/env python3

import argparse
import pandas as pd
import pickle
import numpy as np
import os
from helper import lineno, isfloat, mkdir_p, rel_id_from_rel_name, get_save_folder, get_file_save_name
import sqlite3
from graphviz import Digraph

styles = {
    'graph': {
        'label': 'Taxonomy Alignment',
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': '#ffffff',
        'rankdir': 'LR',
    },
    'node_styles': {
        'node_equal': {
            'shape': 'box',
            'style': 'filled,rounded',
            'fontname': 'helvetica',
            'fillcolor': '#EEEEEE',
            'fontcolor': 'black',
        },
    },
    'edge_styles': {
        'overlap_edge': {
            'arrowhead': 'none',
            'style': 'dotted',
            'constraint': 'false',
            'penwidth': '1',
            'color': '#ce2118',
        },
        'proper_part_edge': {
            'arrowhead': 'normal',
            'style': 'solid',
            'color': 'black',
            'constraint': 'true',
            'penwidth': '1',
        },
    }
}


def remove_quotes(x):
    if x[0] == '"':
        x = x[1:]
    if x[-1] == '"':
        x = x[:-1]
    return x


def generate_node_style(fillcolor, fontcolor='black', shape='box', style='filled', fontname='helvetica'):
    return dict(fillcolor=fillcolor, fontcolor=fontcolor, shape=shape, style=style, fontname=fontname)


def find_set(ns, name):
    for i, ns_ in enumerate(ns):
        if name in ns_:
            return i


def visualize(dfs=None, pws=None, relations=None, conn=None, project_name=None):

    for pw_id in range(1, len(pws) + 1):

        graph = Digraph(graph_attr=styles['graph'])
        nodes_sets = []
        # Get the regions/concepts from the 'u' df
        df = dfs[rel_id_from_rel_name('u_1', relations)]
        df = df[df.pw == pw_id]
        for idx, row in df.iterrows():
            nodes_sets.append(set([row['x1']]))

        df = dfs[rel_id_from_rel_name('eq_2', relations)]
        df = df[df.pw == pw_id]

        for idx, row in df.iterrows():
            if row['x1'] == row['x2']:
                continue
            for i, set1 in enumerate(nodes_sets):
                if row['x1'] in set1:
                    for j, set2 in enumerate(nodes_sets):
                        if row['x2'] in set2:
                            if i != j:
                                nodes_sets[i] = nodes_sets[i].union(nodes_sets[j])
                                nodes_sets.pop(j)
                                break
                    break

        nodes_sets = list(map(list, nodes_sets))
        NODE_COLORS = ['#CCFFCC', '#FFFFCC', '#f4bf42', '#6346d6']
        NODE_COLORS_USED = 0
        for node_set in nodes_sets:
            node_set = list(map(remove_quotes, node_set))
            if len(node_set) == 1:
                tax = node_set[0].split('_')[0]
                if tax not in styles['node_styles']:
                    new_node_style = generate_node_style(NODE_COLORS[NODE_COLORS_USED])
                    NODE_COLORS_USED += 1
                    styles['node_styles'][tax] = new_node_style

                graph.node(node_set[0], _attributes=styles['node_styles'][tax])

            else:

                graph.node("\n".join(node_set), _attributes=styles['node_styles']['node_equal'])

        df = dfs[rel_id_from_rel_name('pp_2', relations)]
        df = df[df.pw == pw_id]

        pp_edges = []
        for idx, row in df.iterrows():
            node1 = list(map(remove_quotes, nodes_sets[find_set(nodes_sets, row['x1'])]))
            node2 = list(map(remove_quotes, nodes_sets[find_set(nodes_sets, row['x2'])]))
            if (node1, node2) not in pp_edges and (node2, node1) not in pp_edges:
                graph.edge("\n".join(node1), "\n".join(node2), _attributes=styles['edge_styles']['proper_part_edge'])
                pp_edges.append((node1, node2))

        df = dfs[rel_id_from_rel_name('po_2', relations)]
        df = df[df.pw == pw_id]

        overlap_edges = []
        for idx, row in df.iterrows():
            node1 = list(map(remove_quotes, nodes_sets[find_set(nodes_sets, row['x1'])]))
            node2 = list(map(remove_quotes, nodes_sets[find_set(nodes_sets, row['x2'])]))
            if (node1, node2) not in overlap_edges and (node2, node1) not in overlap_edges:
                graph.edge("\n".join(node1), "\n".join(node2), _attributes=styles['edge_styles']['overlap_edge'])
                overlap_edges.append((node1, node2))

        folder_name = get_save_folder(project_name, 'euler_visualization')
        graph.render(filename='{}/pw-{}'.format(folder_name, pw_id))
