#!/usr/bin/env python3

import argparse
import pandas as pd
import pickle
import numpy as np
import os
from helper import lineno, isfloat, mkdir_p
from sql_funcs import rel_id_from_rel_name
import sqlite3
from graphviz import Digraph


styles = {
	'graph': {
		'label' : 'Taxonomy Alignment',
		'fontsize' : '16',
		'fontcolor' : 'black',
		'bgcolor' : '#ffffff',
		'rankdir' : 'LR',
	},
	'node_equal' : {
		'shape' : 'box',
		'style' : 'filled,rounded',
		'fontname' : 'helvetica',
		'fillcolor' : '#1fce0c',
		'fontcolor' : 'black',
	},
	'node_tax1' : {
		'shape' : 'box',
		'style' : 'filled',
		'fontname' : 'helvetica',
		'fillcolor' : '#f4bf42',
		'fontcolor' : 'black',
	},
	'node_tax2' : {
		'shape' : 'box',
		'style' : 'filled',
		'fontname' : 'helvetica',
		'fillcolor' : '#6346d6',
		'fontcolor' : 'black',
	},
	'overlap_edge' : {
		'arrowhead' : 'none',
		'style' : 'dotted',
		'constraint' : 'false',
		'penwidth' : '1',
		'color' : '#ce2118',
	},
	'proper_part_edge' : {
		'arrowhead' : 'normal',
		'style' : 'solid',
		'color' : 'black',
		'constraint' : 'true',
		'penwidth' : '1',
	},
}

def find_set(ns, name):
    for i, ns_ in enumerate(ns):
        if name in ns_:
            return i


def visualize(dfs=None, pws=None, relations=None, conn=None, project_name=None):

	for pw_id in range(1, len(pws)+1):

		graph = Digraph(graph_attr = styles['graph'])
		nodes_sets = []
		# Get the regions/concepts from the 'u' df
		df = dfs[rel_id_from_rel_name('u_1', relations)]
		df = df[df.pw == pw_id]
		for idx, row in df.iterrows():
			nodes_sets.append(set([row['x1']]))

		df = dfs[rel_id_from_rel_name('eq_2', relations)]
		df = df[df.pw == pw_id]

		for idx, row in df.iterrows():
		    if (row['x1'] == row['x2']):
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
		for node_set in nodes_sets:
		    if len(node_set) == 1:
		        if node_set[0][0] == 'a':
		            graph.node(node_set[0], _attributes = styles['node_tax1'])
		        else:
		            graph.node(node_set[0], _attributes = styles['node_tax2'])
		    else:
		        graph.node("\n".join(node_set), _attributes = styles['node_equal'])

		
		df = dfs[rel_id_from_rel_name('pp_2', relations)]
		df = df[df.pw==pw_id]

		pp_edges = []
		for idx, row in df.iterrows():
		    node1 = nodes_sets[find_set(nodes_sets, row['x1'])]
		    node2 = nodes_sets[find_set(nodes_sets, row['x2'])]
		    if (node1, node2) not in pp_edges and (node2, node1) not in pp_edges:
		        graph.edge("\n".join(node1), "\n".join(node2), _attributes = styles['proper_part_edge'])
		        pp_edges.append((node1, node2))

		df = dfs[rel_id_from_rel_name('po_2', relations)]
		df = df[df.pw==pw_id]

		overlap_edges = []
		for idx, row in df.iterrows():
		    node1 = nodes_sets[find_set(nodes_sets, row['x1'])]
		    node2 = nodes_sets[find_set(nodes_sets, row['x2'])]
		    if (node1,node2) not in overlap_edges and (node2, node1) not in overlap_edges:
		        graph.edge("\n".join(node1), "\n".join(node2), _attributes = styles['overlap_edge'])
		        overlap_edges.append((node1, node2))

		mkdir_p('Mini Workflow/parser_output/euler_visualizations/{}/'.format(project_name))
		graph.render(filename='Mini Workflow/parser_output/euler_visualizations/{}/pw-{}'.format(project_name, pw_id))




