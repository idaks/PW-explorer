#!/usr/bin/env python3

from sql_funcs import rel_id_from_rel_name
from sklearn.cluster import DBSCAN
from colorability_dist import *
import pickle
from helper import mkdir_p
import matplotlib.pyplot as plt



def visualize(dfs=None, pws=None, relations=None, conn=None, project_name=None):

	if project_name == None or relations == None or dfs == None:
		print("None objects passed.")
		exit(1)

	dist_matrix = None
	try:
		with open('Mini Workflow/temp_pickle_data/' + str(project_name) + '/dist_matrix.pkl', 'rb') as input_file:
			dist_matrix = pickle.load(input_file)
	except IOError:
		print("Could not find the distance matrix for the project, check project/session name entered. Ensure you have run the dist_calc script and computed a distance matrix.")
		exit(1)

	
	db = DBSCAN(metric = 'precomputed', eps = 0.5, min_samples = 1)
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

	OUTPUT_FOLDER = 'Mini Workflow/parser_output/colorability_visualizations/{}'.format(project_name)
	mkdir_p(OUTPUT_FOLDER)

	for label, idx in list(unique_indices.items()):
		
		cols = get_colors_list(df, idx+1)
		#print(cols)
		group_size = [1 for _ in cols]

		plt.figure()
		plt.pie(group_size, colors = cols)
		#print(label_counts[label])
		my_circle=plt.Circle((0,0), 0.7, color='white')
		p=plt.gcf()
		p.gca().add_artist(my_circle)
		plt.annotate(str(label_counts[label]), xy=(0,0), ha='center', va='center', fontsize=35)
		plt.savefig(OUTPUT_FOLDER + '/pattern' + str(label) + '.png')



