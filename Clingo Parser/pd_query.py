#Pandas QUERY SCRIPT:

import sys
from sys import argv
import pandas as pd
import numpy as np
import os
import string
import argparse
import pickle
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--project_name", type = str, help = "provide session/project name used while parsing")
group = parser.add_mutually_exclusive_group()
group.add_argument("-intersection", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
group.add_argument("-union", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
group.add_argument("-freq", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag, possible worlds to consider using the -pws flag and the values for the columns (in the mentioned order) using the -vals flag (optional).")
group.add_argument("-num_tuples", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively and the possible world ids to count the tuples in using the -pws flag.")
group.add_argument("-difference", choices = ('one-way', 'symmetric'), help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag and the two possible world ids using the -pws flag.")
group.add_argument("-redundant_column", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
group.add_argument("-unique_tuples", action = 'store_true', default = False, help = "provide either relation name or relation_id using the -rel_name or -rel_id flag respectively, columns to consider using the -cols flag and possible worlds to consider using the -pws flag.")
group.add_argument("-custom", type = str, help = "provide the query enclosed in '' and either relation name or relation_id using the -rel_name or -rel_id flag respectively.")
group.add_argument("-show_relations", action = 'store_true', default = False, help = "to get a list of relations and corresponding relation ids.")

parser.add_argument("-rel_name", type = str, help = "provide the relation name to query. Note that if both rel_id and rel_name are provided, rel_name is disregarded.")
parser.add_argument("-rel_id", type = int, help = "provide the relation id of the relation to query. To view relation ids, use -show_relations")
parser.add_argument("-cols", type = str, nargs = '*', default = [], help = "provide the columns of the selected relations to consider for the chosen query. If you want to consider all the columns, do not include this flag.")
parser.add_argument("-pws", type = int, nargs = '*', default = [], help = "provide the possible world ids of the possible world to consider for this query. If you want to consider all the possible worlds, do not include this flag. Please note that difference query requires exactly 2 arguments for this flag.") 
parser.add_argument("-vals", nargs = '*', default = [], type = str, help = "provide the values for the freq query in the same order as the mentioned columns. If you want to query all possible tuples, do not include this flag.")

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

expected_pws = len(pws)

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

def intersection_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	s1 = df[df.pw == pws_to_consider[0]]
	for j in pws_to_consider[1:]:
		s1 = pd.merge(s1, df[df.pw == j], how = 'inner', on = col_names)
	s1 = s1[col_names]
	if do_print:
		print "Intersection for the relation", str(relations[rl_id].relation_name), "on features", str(', '.join(map(str,col_names))), "for PWs", str(', '.join(map(str, pws_to_consider)))
		if len(s1) > 0:
			print str(s1)
		else:
			print "NULL"

	return s1

def union_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	s1 = df[df.pw == pws_to_consider[0]]
	for j in pws_to_consider[1:]:
		s1 = pd.merge(s1, df[df.pw == j], how = 'outer', on = col_names)
	s1 = s1[col_names]

	if do_print:
		print "Intersection for the relation", str(relations[rl_id].relation_name), "on features", str(', '.join(map(str,col_names))), "for PWs", str(', '.join(map(str, pws_to_consider)))
		if len(s1) > 0:
			print str(s1) 
		else:
			print "NULL"

	return s1

def freq_panda(rl_id = 0, col_names = [], values = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	all_tuples = None
	freqs = []

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names != [] and values != [] and len(col_names) != len(values):
		print 'Lengths of col_names and values don\'t match.'
		return None

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	if values == []:
		all_tuples = union_panda(rl_id, col_names, pws_to_consider, False)
	else:
		k = []
		k.append(values)
		all_tuples = pd.DataFrame(k, columns = col_names)


	df = dfs[rl_id]
	for j in range(len(all_tuples)):
		expr = ''
		for k in range(len(col_names) - 1):
			expr += str(col_names[k]) + ' == ' + "'" + str(all_tuples.ix[j][k]) + "'" + ' and '
		expr += str(col_names[-1]) + ' == ' + "'" + str(all_tuples.ix[j][-1]) + "'"
		expr +=  ' and pw in [' + str(', '.join(map(str,pws_to_consider))) + ']'
		s3 = df.query(expr)
		tmp = len(s3)
		if do_print:
			print "Frequency of tuple " + str(tuple(all_tuples.ix[j])) + ' of the relation ' + str(relations[rl_id].relation_name) + ' for attributes ' + str(', '.join(map(str,col_names))) + ' in PWs ' + str(', '.join(map(str,pws_to_consider))) + " is: " + str(tmp)
		freqs.append(tmp)

	return all_tuples, freqs

def num_tuples_panda(rl_id, pw_id, do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	df = dfs[rl_id]
	c = len(df[df.pw == pw_id])
	if do_print:
		print "There exist " + str(c) + " tuples of relation " + str(relations[rl_id].relation_name) + " in PW " + str(pw_id)
	return c

def difference_panda(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	df = dfs[rl_id]
	x1 = df[df.pw == pw_id_1][col_names]
	x2 = df[df.pw == pw_id_2][col_names]

	diff = pd.concat([x1, x2, x2]).drop_duplicates(keep=False)
	if do_print:
		print "Following is the difference between PWs {} and {} in features {} of relation {}\n".format(pw_id_1, pw_id_2, str(', '.join(map(str,col_names))), str(relations[rl_id].relation_name))
		print str(diff)
	return diff

def difference_both_ways_panda(rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	x1 = difference_panda(rl_id, pw_id_1, pw_id_2, col_names, False)
	x2 = difference_panda(rl_id, pw_id_2, pw_id_1, col_names, False)

	diff = x1.append(x2, ignore_index = True)

	if do_print:
		print "Following tuples are in one of PW {} or {}, but not both, for relation {} and features {}\n".format(pw_id_1, pw_id_2, str(relations[rl_id].relation_name), str(', '.join(map(str,col_names))))
		print str(diff)
	return diff

def redundant_column_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws + 1)], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	#PW specific:
	redundant_pw_specific = []

	df = dfs[rl_id]

	for ft in col_names:
		x1 = df.groupby('pw')[ft].nunique()
		for i in pws_to_consider:
			if x1.ix[i] <= 1:
				redundant_pw_specific.append((i, rl_id, ft))
				if do_print:
					print 'Column ' + str(ft) + ' is redundant in relation ' + str(relations[rl_id].relation_name) + ' in PW ' + str(i)

	#Across all PWs:
	redundant_across_pws = []
	x1 = df[df.pw.isin(pws_to_consider)]
	for ft in col_names:
		if x1[ft].nunique() <= 1:
			redundant_across_pws.append((pws_to_consider, rl_id, ft))
			if do_print:
				print 'Column ' + str(ft) + ' is redundant in relation ' + str(relations[rl_id].relation_name) + ' for PWs ' + str(', '.join(map(str,pws_to_consider)))

	return redundant_pw_specific, redundant_across_pws

def unique_tuples_panda(rl_id = 0, col_names = [], pws_to_consider = [j for j in range(1, expected_pws+1)], do_print = True):

	global relations 
	global expected_pws 
	global dfs
	global conn
	global pws 

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	relevant_tuples, freqs = freq_panda(rl_id, col_names, [], pws_to_consider, False)
	unique_tuples = []
	df = dfs[rl_id]

	for i, f in enumerate(freqs):
		if f == 1:
			expr = ''
			for k in range(len(col_names) - 1):
				expr += str(col_names[k]) + ' == ' + "'" + str(relevant_tuples.ix[i][k]) + "'" + ' and '
			expr += str(col_names[-1]) + ' == ' + "'" + str(relevant_tuples.ix[i][-1]) + "'"
			expr +=  ' and pw in [' + str(', '.join(map(str,pws_to_consider))) + ']'
			s3 = df.query(expr)
			s3 = s3.reset_index(drop = True)
			unique_pw = s3.ix[0]['pw']

			unique_tuples.append((relevant_tuples.ix[i], unique_pw))

			if do_print:
				print 'The unique tuple ', tuple(relevant_tuples.ix[i]), 'occurs only in PW', unique_pw

	return unique_tuples



if args.intersection:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	soln = None
	try:
		soln = intersection_panda(r_id, args.cols, args.pws, True)
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.union:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	soln = None
	try:
		soln = union_panda(r_id, args.cols, args.pws, True)
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.freq:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	soln = None
	try:
		soln = freq_panda(r_id, args.cols, args.vals, args.pws, True)
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.num_tuples:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	pws_to_consider = args.pws
	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	soln = []
	try:
		for i in pws_to_consider:
			soln.append(num_tuples_panda(r_id, i, True))
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.difference is not None:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	if len(args.pws) != 2:
		print "Please provide exactly 2 possible world ids."
		exit(0)

	soln = None

	if args.difference == 'one-way':
		try:
			soln = difference_panda(r_id, args.pws[0], args.pws[1], args.cols, True)
		except Exception, e:
			print "Query failed. Please check the provided arguments to make sure they are valid."
			print "Error: ", str(e)
			exit(1)
	elif args.difference == 'symmetric':
		try:
			soln = difference_both_ways_panda(r_id, args.pws[0], args.pws[1], args.cols, True)
		except Exception, e:
			print "Query failed. Please check the provided arguments to make sure they are valid."
			print "Error: ", str(e)
			exit(1)

elif args.redundant_column:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	soln = None
	try:
		soln = redundant_column_panda(r_id, args.cols, args.pws, True)
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.unique_tuples:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	soln = None
	try:
		soln = unique_tuples_panda(r_id, args.cols, args.pws, True)
	except Exception, e:
		print "Query failed. Please check the provided arguments to make sure they are valid."
		print "Error: ", str(e)
		exit(1)

elif args.show_relations:

	print 'Following are the parsed relation IDs and relation names:'
	for i, rl in enumerate(relations):
		print str(i) + ':', str(rl.relation_name)

elif args.custom is not None:

	if args.rel_name is None and args.rel_id is None:
		print "Please include either the -rel_name or -rel_id flag along with the appropriate argument."
		exit(0)

	r_id = args.rel_id
	if r_id is None:
		r_id = rel_id_from_rel_name(args.rel_name)

	ik = None 
	try:
		ik = dfs[r_id].query(args.custom)
		print str(ik)
		if len(ik) <= 0 :
			print "NULL"
	except Exception, e:
		print "Query failed. Please check the provided query to make sure it is valid."
		print "Error: ", str(e)
		exit(1)






