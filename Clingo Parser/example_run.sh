#!/bin/sh

python clingo_out.py Clingo\ Examples/CEN-NDC-regions_pw.lp4 Clingo\ Examples/CEN-NDC-regions_pwswitch.lp4 cen_ndc_example

python parse.py cen_ndc_example

python export.py -sql -csv

python sql_query.py -show_relations

python sql_query.py -unique_tuples -rel_id 0

python sql_query.py -num_tuples -pws 1 2 4 23 -rel_name rel_3

python sql_query.py -intersection -rel_id 0 -pws 2 23 -cols x1 x2 x3

python dist_calc.py -euler_num_overlaps_diff -rel_name rel_3 -col x3 -calc_dist_matrix

python complexity_calc.py -euler_complexity_analysis -rel_name rel_3 -col x3

python visualize.py -mds -dendrogram -clustering


#Expected Output:

# Copied files into the clingo_input folder
# Preprocessed clingo output written to clingo_output/cen_ndc_example.txt
# Number of Models: 30
# Successfully exported to csv
# Successfully exported to sql
# Following are the parsed relation IDs and relation names:
# 0: rel_3
# The unique tuple (u'cCEN_USA', u'cNDC_USA', u'"="') occurs only in PW 1
# There exist 30 tuples of relation rel_3 in PW 1
# There exist 30 tuples of relation rel_3 in PW 2
# There exist 30 tuples of relation rel_3 in PW 4
# There exist 30 tuples of relation rel_3 in PW 23
# Intersection for the relation rel_3 on features x1, x2, x3 for PWs 2, 23
#                 x1              x2    x3
# 0     cCEN_Midwest    cNDC_Midwest   "="
# 1     cCEN_Midwest  cNDC_Northeast   "!"
# 2     cCEN_Midwest  cNDC_Southeast   "!"
# 3     cCEN_Midwest  cNDC_Southwest   "!"
# 4     cCEN_Midwest        cNDC_USA   "<"
# 5     cCEN_Midwest       cNDC_West   "!"
# 6   cCEN_Northeast    cNDC_Midwest   "!"
# 7   cCEN_Northeast  cNDC_Northeast   "<"
# 8   cCEN_Northeast  cNDC_Southeast   "!"
# 9   cCEN_Northeast  cNDC_Southwest   "!"
# 10  cCEN_Northeast        cNDC_USA   "<"
# 11  cCEN_Northeast       cNDC_West   "!"
# 12      cCEN_South    cNDC_Midwest   "!"
# 13      cCEN_South  cNDC_Southeast   ">"
# 14      cCEN_South  cNDC_Southwest  "><"
# 15      cCEN_South       cNDC_West   "!"
# 16        cCEN_USA    cNDC_Midwest   ">"
# 17        cCEN_USA  cNDC_Southeast   ">"
# 18        cCEN_USA  cNDC_Southwest  "><"
# 19        cCEN_USA       cNDC_West   ">"
# 20       cCEN_West    cNDC_Midwest   "!"
# 21       cCEN_West  cNDC_Northeast   "!"
# 22       cCEN_West  cNDC_Southeast   "!"
# 23       cCEN_West  cNDC_Southwest  "><"
# 24       cCEN_West        cNDC_USA   "<"
# 25       cCEN_West       cNDC_West   ">"
# Distance Matrix:
# [[ 0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.4  0.6  0.4  0.6  0.6
#    0.8  0.4  0.6  0.4  0.6  0.6  0.8  0.6  0.6  0.8  0.6  0.8  0.6  0.8
#    0.8  1. ]
#  [ 0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.2  0.4  0.2  0.4  0.4
#    0.6  0.2  0.4  0.2  0.4  0.4  0.6  0.4  0.4  0.6  0.4  0.6  0.4  0.6
#    0.6  0.8]
#  [ 0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.4  0.6  0.4  0.6  0.6
#    0.8  0.4  0.6  0.4  0.6  0.6  0.8  0.6  0.6  0.8  0.6  0.8  0.6  0.8
#    0.8  1. ]
#  [ 0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.2  0.4  0.2  0.4  0.4
#    0.6  0.2  0.4  0.2  0.4  0.4  0.6  0.4  0.4  0.6  0.4  0.6  0.4  0.6
#    0.6  0.8]
#  [ 0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.2  0.4  0.2  0.4  0.4
#    0.6  0.2  0.4  0.2  0.4  0.4  0.6  0.4  0.4  0.6  0.4  0.6  0.4  0.6
#    0.6  0.8]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.2  0.4  0.2  0.4  0.4
#    0.6  0.2  0.4  0.2  0.4  0.4  0.6  0.4  0.4  0.6  0.4  0.6  0.4  0.6
#    0.6  0.8]
#  [ 0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.2  0.4  0.2  0.4  0.4
#    0.6  0.2  0.4  0.2  0.4  0.4  0.6  0.4  0.4  0.6  0.4  0.6  0.4  0.6
#    0.6  0.8]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.   0.2  0.   0.2  0.2
#    0.4  0.   0.2  0.   0.2  0.2  0.4  0.2  0.2  0.4  0.2  0.4  0.2  0.4
#    0.4  0.6]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.2  0.   0.2  0.   0.   0.2
#    0.2  0.   0.2  0.   0.   0.2  0.   0.   0.2  0.   0.2  0.   0.2  0.2
#    0.4]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 0.8  0.6  0.8  0.6  0.6  0.4  0.6  0.6  0.4  0.4  0.2  0.4  0.2  0.2  0.
#    0.4  0.2  0.4  0.2  0.2  0.   0.2  0.2  0.   0.2  0.   0.2  0.   0.   0.2]
#  [ 1.   0.8  1.   0.8  0.8  0.6  0.8  0.8  0.6  0.6  0.4  0.6  0.4  0.4
#    0.2  0.6  0.4  0.6  0.4  0.4  0.2  0.4  0.4  0.2  0.4  0.2  0.4  0.2
#    0.2  0. ]]
# PWs:          [30, 15, 21, 24, 26, 28, 29, 11, 13, 14, 17, 19, 20, 22, 23, 25, 27, 6, 9, 10, 12, 16, 18, 2, 4, 5, 7, 8, 1, 3]
# Complexities: [1.0, 0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.59999999999999998, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.0, 0.0]
# MDS Neato Graph saved to: Mini Workflow/parser_output/clustering_output/cen_ndc_example
# Cluster Labels: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# Clustering Output saved to: Mini Workflow/parser_output/clustering_output/cen_ndc_example
# Dendrograms saved to: Mini Workflow/parser_output/clustering_output/cen_ndc_example
