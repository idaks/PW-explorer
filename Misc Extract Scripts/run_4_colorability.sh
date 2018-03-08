#!/bin/bash

PROJECT_NAME=$1

#Go into the PW-E directory
cd ../Clingo\ Parser/

#Run clingo on the circuit-4-coloring file. This produces a clingo output and stores it in the Mini Workflow/clingo_out folder. Also store a copy of input file in clingo_in folder
python run_clingo.py ../Colorability_Examples/circuit-4coloring.lp4 $PROJECT_NAME

#Runs the Clingo Parser on the generated clingo output and stores the solution as Pandas DataFrames in Mini Workflow/temp_pickle_data folder
python load_worlds.py $PROJECT_NAME

#Exports the generated Pandas Dataframes in csv and sql dbs in the Mini Workflow/parser_output/csv_exports and Mini Workflow/parser_output/sql_exports folder
python export.py -p $PROJECT_NAME -csv -sql

#Compute a distance matrix with distance between each pair of possible worlds. Stores this distance matrix in pickle format for future use if needed.
python dist_calc.py -p $PROJECT_NAME -custom_dist_func colorability_dist -calc_dist_matrix

#Makes the interesting visualisations and stores them in the Mini Workflow/parser_output/colorability_visualizations/$PROJECT_NAME folder.
#Contains the principle patters with the count of each of these patterns.
python visualize.py -p $PROJECT_NAME -custom_visualisation_func four_colorability_visualization