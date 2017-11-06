import sys
from sys import argv
import pandas as pd
import numpy as np
import os
import string
import sqlite3
import argparse
import pickle
import importlib
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation
from sql_funcs import rel_id_from_rel_name, union_panda, intersection_sqlite, union_sqlite, freq_sqlite, num_tuples_sqlite, difference_sqlite, difference_both_ways_sqlite, redundant_column_sqlite, unique_tuples_sqlite


import matplotlib.pyplot as plt


#from scipy.cluster.hierarchy import cophenet
#from scipy.spatial.distance import pdist


# import mpld3
# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as ff


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project_name", type = str, help = "provide session/project name used while parsing")
parser.add_argument("-mds", action = 'store_true', default = False, help = "produce a Multidimensional Scaling Graph Output using the Neato Program")
parser.add_argument("-clustering", action = 'store_true', default = False, help = "use DBScan Algorithm to cluster the Possible Worlds")
parser.add_argument("-dendrogram", action = 'store_true', default = False, help = "create various dendrograms using scipy")
args = parser.parse_args()

project_name = ''
if args.project_name == None:
	try:
		with open('Mini Workflow/temp_pickle_data/' + 'current_project' + '/curr_proj_name.pkl', 'rb') as f:
			project_name = pickle.load(f)
	except IOError:
		print "Could not automatically find the current project/session. Please provide a project name explicitly using the -p flag"
		exit(1)
else:
	project_name = args.project_name

dfs = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dfs.pkl', 'rb') as input_file:
		dfs = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

relations = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/relations.pkl', 'rb') as input_file:
		relations = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

pws = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/pws.pkl', 'rb') as input_file:
		pws = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered."
	exit(1)

if not os.path.exists("Mini Workflow/parser_output/sql_exports/" + str(project_name) + ".db"):
	print "No file by the name {}.db exists in the clingo_output/sql_exports folder. Please recheck the project name.".format(project_name)
	exit(1)

conn = None
try:
	conn = sqlite3.connect("Mini Workflow/parser_output/sql_exports/" + str(project_name) + ".db")
except sqlite3.Error:
	print "Could not find the associated sqlite databse. Please recheck project_name or make sure a sql db has been exported using export.py module"
	exit(1)

expected_pws = len(pws)

dist_matrix = None
try:
	with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'rb') as input_file:
		dist_matrix = pickle.load(input_file)
except IOError:
	print "Could not find the project, check project/session name entered. Ensure you have run the dist_calc script and computed a distance matrix."
	exit(1)



def rel_id_from_rel_name(rel_name):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	for i, rel in enumerate(relations):
		if rel.relation_name == rel_name:
			if i != rel.r_id:
				print "Relations not in order"
			return rel.r_id

	return None

def compute_dist_matrix(X = None):
	global dist_matrix
	return dist_matrix

def matplotlib_to_plotly(cmap, pl_entries):

    h = 1.0/(pl_entries-1) if pl_entries > 1 else 1
    pl_colorscale = []
    
    for k in range(pl_entries):
        C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])
        
    return pl_colorscale

def dbscan_clustering(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global dfs

	db = DBSCAN(metric = 'precomputed', eps = 0.5, min_samples = 1)
	labels = db.fit_predict(dist_matrix)
	print 'Cluster Labels:', str(labels)

	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	unique_labels = set(labels)
	colors = [plt.cm.Spectral(each)
	          for each in np.linspace(0, 1, len(unique_labels))]
	

	#fig, ax = plt.subplots()

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

	#labels = ['point {0}'.format(i + 1) for i in range(expected_pws)]
	#fig.plugins = [mpld3.plugins.PointLabelTooltip(labels)]
	plt.title('Estimated number of clusters: %d' % n_clusters_)
	#mpld3.show()
	#plt.show()
	mkdir_p('Mini Workflow/parser_output/clustering_output/' + str(project_name))
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '.png')
	plt.figure()
	print 'Clustering Output saved to:', ('Mini Workflow/parser_output/clustering_output/' + str(project_name))

def dbscan_clustering_plotly(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global dfs

	db = DBSCAN(metric = 'precomputed', eps = 0.5, min_samples = 1)
	labels = db.fit_predict(dist_matrix)
	print 'Cluster Labels:', str(labels)


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

	#print str(dist_matrix)
	#print dist_matrix.shape

	X = squareform(dist_matrix)

	#print X
	#print X.shape
	# Z = linkage(X, method='ward', metric='euclidean')
	
	# plt.title('Hierarchical Clustering Dendrogram (Ward)')
	# plt.xlabel('sample index')
	# plt.ylabel('distance')
	# dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
	# #mpld3.show()
	# plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_ward_dendrogram.png')
	# plt.figure()
	
	linkage_matrix = linkage(X, "single")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Single)")
	#mpld3.show()
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_single_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "complete")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Complete)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_complete_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "average")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Average)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_average_dendrogram.png')
	plt.figure()

	linkage_matrix = linkage(X, "weighted")
	dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	plt.title("Dendrogram (Weighted)")
	plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_weighted_dendrogram.png')
	plt.figure()

	# linkage_matrix = linkage(X, "centroid")
	# dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	# plt.title("Dendrogram (Centroid)")
	# plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_centroid_dendrogram.png')
	# plt.figure()

	# linkage_matrix = linkage(X, "median")
	# dendrogram(linkage_matrix, labels=[str(i) for i in range(len(dist_matrix))])
	# plt.title("Dendrogram (Median)")
	# plt.savefig('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_median_dendrogram.png')
	# plt.figure()

	print 'Dendrograms saved to:', ('Mini Workflow/parser_output/clustering_output/' + str(project_name))

def dendrogram_plotly(dist_matrix):

	global pws 
	global relations 
	global expected_pws 
	global dfs

	pw_ids = [i for i in range(len(dist_matrix))]
	dendro = ff.create_dendrogram(dist_matrix, labels = pw_ids, distfun = compute_dist_matrix)
	dendro['layout'].update({'width':800, 'height':500})
	py.plot(dendro, filename='dendrogram')

def mds_graph_2(A):

	global pws 
	global relations 
	global expected_pws
	global dfs

	dt = [('len', float)]
	A = A*len(A)/5
	A = A.view(dt)
	G = nx.from_numpy_matrix(A)
	#G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))
	G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),['pw-{}'.format(i) for i in range(1, len(pws)+1)])))     

	G = nx.drawing.nx_agraph.to_agraph(G)

	G.node_attr.update(color="red", style="filled")
	G.edge_attr.update(color=None, width="0.1")
	#G.edge_attr.update(color="blue", width="0.1")

	mkdir_p('Mini Workflow/parser_output/clustering_output/' + str(project_name))
	G.draw('Mini Workflow/parser_output/clustering_output/' + str(project_name) + '/' + str(project_name) + '_networkx_out.png', format='png', prog='neato')
	print 'MDS Neato Graph saved to:', ('Mini Workflow/parser_output/clustering_output/' + str(project_name))

if args.mds:
	import networkx as nx
	mds_graph_2(dist_matrix)
if len(pws) > 1:
	if args.clustering:
		from sklearn.cluster import DBSCAN
		dbscan_clustering(dist_matrix)
	#dbscan_clustering_plotly(dist_matrix)
	if args.dendrogram:
		from scipy.spatial.distance import squareform
		from scipy.cluster.hierarchy import dendrogram, linkage

		linkage_dendrogram(dist_matrix)
	#dendrogram_plotly(np.array([i for i in range(len(pws))]))







conn.commit()
conn.close()	