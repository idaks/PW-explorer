#!/usr/bin/env python3

from pwe_helper import rel_id_from_rel_name, mkdir_p
from nxpd import draw
import networkx as nx
import os
from collections import defaultdict


def get_styles(project_name, pw_id):
    return {
        'graph': {
            'label': '{}_pw_{}'.format(str(project_name), str(pw_id)),
            'fontsize': '16',
            'fontcolor': 'black',
            'bgcolor': '#ffffff',
            'rankdir': 'RL',
        },
        'node_styles': {
            'node_equal': {
                'shape': 'box',
                'style': '"filled,rounded"',
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

# Utility functions


def remove_quotes(x):
    if x[0] == '"':
        x = x[1:]
    if x[-1] == '"':
        x = x[:-1]
    return x


def generate_node_style(fillcolor, fontcolor='black', shape='box', style='filled', fontname='helvetica'):
    return dict(fillcolor=fillcolor, fontcolor=fontcolor, shape=shape, style=style, fontname=fontname)


# Disjoint Sets Utility Functions

def get_parent(node, djs):
    if djs[node] == node:
        return node
    parent = get_parent(djs[node], djs)
    djs[node] = parent
    return parent


def union(node1, node2, djs):
    node1 = get_parent(node1, djs)
    node2 = get_parent(node2, djs)
    if node1 != node2:
        djs[node2] = node1
    return node1


def setup_djs(djs):
    for child, parent in djs.items():
        djs[child] = get_parent(child, djs)

# Nodes merge function


def merge_nodes(G,nodes, new_node, attr):
    G_ = nx.contracted_nodes(G, *nodes)
    G__ = nx.relabel.relabel_nodes(G_, {nodes[0] : new_node})
    G__.nodes[new_node].update(attr)
    return G__


# Visualization function

def visualize(**kwargs):

    kwargs = defaultdict(lambda: None, kwargs)
    dfs = kwargs['dfs']
    pws = kwargs['pws']
    relations = kwargs['relations']
    save_to_folder = kwargs['save_to_folder']
    project_name = kwargs['project_name']
    Gs = []

    for pw_id in range(1, len(pws) + 1):

        styles = get_styles(project_name, pw_id)
        G = nx.DiGraph(**styles['graph'])

        # Add all the units to the graph
        df = dfs[rel_id_from_rel_name('u_1', relations)]
        df = df[df.pw == pw_id]
        NODE_COLORS = ['#CCFFCC', '#FFFFCC', '#f4bf42', '#6346d6']
        NODE_COLORS_USED = 0

        for idx, row in df.iterrows():
            node_name = remove_quotes(row['x1'])
            tax = node_name.split('_')[0]
            if tax not in styles['node_styles']:
                new_node_style = generate_node_style(NODE_COLORS[NODE_COLORS_USED])
                NODE_COLORS_USED += 1
                styles['node_styles'][tax] = new_node_style
            G.add_node(node_name, **styles['node_styles'][tax])

        # Add proper part edges
        df = dfs[rel_id_from_rel_name('pp_2', relations)]
        df = df[df.pw == pw_id]
        for idx, row in df.iterrows():
            G.add_edge(remove_quotes(row['x1']), remove_quotes(row['x2']), **styles['edge_styles']['proper_part_edge'])

        # Remove the redundant edges i.e. edges that go to ancestors of a parent
        for node in G.nodes:
            pred = list(G.predecessors(node))
            succ = list(G.successors(node))
            # print('node: {}'.format(node))
            for pred_ in pred:
                # print('predecessor: {}'.format(pred_))
                for succ_ in succ:
                    # print('successor: {}'.format(succ_))
                    if G.has_edge(pred_, succ_):
                        #  print('removing edge {} {}'.format(pred_, succ_))
                        G.remove_edge(pred_, succ_)

        # Add partial overlap edges
        df = dfs[rel_id_from_rel_name('po_2', relations)]
        df = df[df.pw == pw_id]

        for idx, row in df.iterrows():
            n1 = remove_quotes(row['x1'])
            n2 = remove_quotes(row['x2'])
            if not G.has_edge(n2, n1):
                G.add_edge(n1, n2, **styles['edge_styles']['overlap_edge'])

        # Merge the equivalent nodes
        df = dfs[rel_id_from_rel_name('eq_2', relations)]
        df = df[df.pw==pw_id]

        # Find the equivalent sets
        nodes = list(G.nodes)
        dj_sets = dict(zip(nodes, nodes))
        for idx, row in df.iterrows():
            n1 = remove_quotes(row['x1'])
            n2 = remove_quotes(row['x2'])
            if n1 == n2:
                continue
            else:
                union(n1, n2, dj_sets)
        setup_djs(dj_sets)

        final_djs = {}
        for child, parent in dj_sets.items():
            if parent not in final_djs:
                final_djs[parent] = set([])
            final_djs[parent].add(child)
        final_djs = list(map(list, final_djs.values()))

        final_djs = list(filter(lambda x: len(x) > 1, final_djs))

        # Merge equivalent nodes
        for final_djs_ in final_djs:
            G = merge_nodes(G, final_djs_, '\n'.join(final_djs_), styles['node_styles']['node_equal'])

        Gs.append(G)

    if save_to_folder is not None:
        folder_name = os.path.join(save_to_folder, 'euler_visualization')
        mkdir_p(folder_name)
        for i, G in enumerate(Gs):
            draw(G, format='gv', filename='{}/pw-{}'.format(folder_name, i+1))
            draw(G, format='pdf', filename='{}/pw-{}.pdf'.format(folder_name, i+1))

    return Gs








