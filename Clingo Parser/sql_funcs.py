import sys
from sys import argv
import pandas as pd
import numpy as np
import sqlite3
import os
import string
from helper import lineno, isfloat, mkdir_p, PossibleWorld, Relation

def rel_id_from_rel_name(rel_name, relations):

	for i, rel in enumerate(relations):
		if rel.relation_name == rel_name:
			if i != rel.r_id:
				print "Relations not in order"
			return rel.r_id

	return None

def union_panda(dfs, pws, relations, rl_id = 0, col_names = [], pws_to_consider = [], do_print = True):

	expected_pws = len(pws)

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
			out_file.write(str(s1) + '\n')
		else:
			out_file.write("NULL\n")

	return s1

#1: Intersection
def intersection_sqlite(dfs, pws, relations, conn, rl_id = 0, col_names = [], pws_to_consider = [], do_print = True):

	expected_pws = len(pws)

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]
	query_intersection = ''
	
	col_names = ', '.join(map(str,col_names))
	for j in pws_to_consider[:-1]:
		query_intersection += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(j) + ' intersect '
	query_intersection += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pws_to_consider[-1]) + ';'
	ik = pd.read_sql_query(query_intersection, conn)
	if do_print:
		print "Intersection for the relation " + str(relations[rl_id].relation_name) + " on features " + col_names + " for PWs " + str(', '.join(map(str, pws_to_consider)))
		if len(ik) > 0:
			print str(ik)
		else:
			print "NULL"

	return ik

#2: Union
def union_sqlite(dfs, pws, relations, conn, rl_id = 0, col_names = [], pws_to_consider = [], do_print = True):

	expected_pws = len(pws)

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]
	query_union = ''
	
	col_names = ', '.join(map(str,col_names))
	for j in pws_to_consider[:-1]:
		query_union += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(j) + ' union '
	query_union += 'select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pws_to_consider[-1]) + ';'
	ik = pd.read_sql_query(query_union, conn)
	if do_print:
		print "Union for the relation ", str(relations[rl_id].relation_name), " on features ", col_names, " for PWs ", str(', '.join(map(str, pws_to_consider)))
		if len(ik) > 0:
			print str(ik)
		else:
			print "NULL"

	return ik

#3: Frequency of a tuple
def freq_sqlite(dfs, pws, relations, conn, rl_id = 0, col_names = [], values = [], pws_to_consider = [], do_print = True):

	 
	expected_pws = len(pws)
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
		all_tuples = union_panda(dfs, pws, relations, rl_id, col_names, pws_to_consider, False)
	else:
		k = []
		k.append(values)
		all_tuples = pd.DataFrame(k, columns = col_names)

	for j in range(len(all_tuples)):
		query = 'select count(*) from ' + str(relations[rl_id].relation_name) + ' where '
		for k in range(len(col_names)):
			query += col_names[k] + '=' + "'" + all_tuples.ix[j][k] + "'" + ' and '

		query += 'pw in (' + str(', '.join(map(str,pws_to_consider))) + ');'
		#print query
		ik = pd.read_sql_query(query, conn)
		if do_print:
			print "Frequency of tuple " + str(tuple(all_tuples.ix[j])) + ' of the relation ' + str(relations[rl_id].relation_name) + ' for attributes ' + str(', '.join(map(str,col_names))) + ' in PWs ' + str(', '.join(map(str,pws_to_consider))) + " is: " + str(ik.ix[0][0])
		freqs.append(ik.ix[0][0])

	return all_tuples, freqs

#4: Number of tuples of a relation in a PW
def num_tuples_sqlite(relations, conn, rl_id, pw_id, do_print = True):

	 

	query = 'select count(*) from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pw_id) + ';'
	c = pd.read_sql_query(query, conn)

	if do_print:
		print "There exist " + str(c.ix[0][0]) + " tuples of relation " + str(relations[rl_id].relation_name) + " in PW " + str(pw_id)
	return c.ix[0][0]

#5: Difference Query
def difference_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	col_names = str(', '.join(map(str,col_names)))

	query = 'select * from (select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw =  ' + str(pw_id_1) + ') except select * from (select ' + col_names + ' from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(pw_id_2) + ');'
	diff = pd.read_sql_query(query, conn)

	if do_print:
		print "Following is the difference between PWs {} and {} in features {} of relation {}\n".format(pw_id_1, pw_id_2, col_names, str(relations[rl_id].relation_name))
		print str(diff)
	return diff

def difference_both_ways_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, col_names = [], do_print = True):

	 

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	x1 = difference_sqlite(dfs, relations, conn, rl_id, pw_id_1, pw_id_2, col_names, False)
	x2 = difference_sqlite(dfs, relations, conn, rl_id, pw_id_2, pw_id_1, col_names, False)

	diff = x1.append(x2, ignore_index = True)

	if do_print:
		print "Following tuples are in one of PW {} or {}, but not both, for relation {} and features {}\n".format(pw_id_1, pw_id_2, str(relations[rl_id].relation_name), str(', '.join(map(str,col_names))))
		print str(diff)
	return diff

#6: Redundant Column Query
def redundant_column_sqlite(dfs, pws, relations, conn, rl_id = 0, col_names = [], pws_to_consider = [], do_print = True):

	expected_pws = len(pws)

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	#PW specific:
	redundant_pw_specific = []
	for i in pws_to_consider:
		for ft in col_names:
			query = 'select count(distinct ' + str(ft) + ') from (select * from ' + str(relations[rl_id].relation_name) + ' where pw = ' + str(i) + ');'
			k = pd.read_sql_query(query, conn)
			if int(k.ix[0][0]) <= 1:
				redundant_pw_specific.append((i, rl_id, ft))
				if do_print:
					print 'Column' + str(ft) + 'is redundant in relation' + str(relations[rl_id].relation_name) + 'in PW' + str(i)

	#Across all PWs:
	redundant_across_pws = []
	for ft in col_names:
		query = 'select count(distinct ' + str(ft) + ') from (select * from ' + str(relations[rl_id].relation_name) + ' where pw in (' + str(', '.join(map(str,pws_to_consider))) + '));'
		k = pd.read_sql_query(query, conn)
		if int(k.ix[0][0]) <= 1:
			redundant_across_pws.append((pws_to_consider, rl_id, ft))
			if do_print:
				print 'Column ' + str(ft) + ' is redundant in relation ' + str(relations[rl_id].relation_name) + ' for PWs ' + str(', '.join(map(str,pws_to_consider)))

	return redundant_pw_specific, redundant_across_pws

#7: Tuples occuring in exactly one PW:
def unique_tuples_sqlite(dfs, pws, relations, conn, rl_id = 0, col_names = [], pws_to_consider = [], do_print = True):

	"""
	Used to ouput the unique tuples in a given solution set. These are the unique tuples (attributes) in the selected possible worlds and the selected columns in the relation.
	"""
	 
	expected_pws = len(pws)

	if pws_to_consider == []:
		pws_to_consider = [j for j in range(1, expected_pws+1)]

	if col_names == []:
		col_names = list(dfs[rl_id])[1:]

	relevant_tuples, freqs = freq_sqlite(dfs, pws, relations, conn, rl_id, col_names, [], pws_to_consider, False)
	unique_tuples = []

	for i, f in enumerate(freqs):
		if f == 1:
			query = 'select pw from ' + str(relations[rl_id].relation_name) + ' where '
			for k in range(len(col_names)):
				query += col_names[k] + '=' + "'" + relevant_tuples.ix[i][k] + "'" + ' and '

			query += 'pw in (' + str(', '.join(map(str,pws_to_consider))) + ');'

			unique_pw = pd.read_sql_query(query, conn)
			unique_pw = unique_pw.ix[0][0]

			unique_tuples.append((relevant_tuples.ix[i], unique_pw))

			if do_print:
				print 'The unique tuple ' + str(tuple(relevant_tuples.ix[i])) + ' occurs only in PW ' + str(unique_pw)

	return unique_tuples