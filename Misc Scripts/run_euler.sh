#!/bin/bash

#Provide the name of the project and the clingo file location
CLINGO_FILE=$1
PROJECT_NAME=$2

#Go to the PWE-directory with all the relevant python files
cd ../Clingo\ Parser/

#Run clingo on the file generated by Lean Euler. It goes to the Lean Euler directory and finds the clingo file named $PROJECT_NAME.lp4 and runs clingo on it
python2.7 run_clingo.py $CLINGO_FILE $PROJECT_NAME

#Parse the clingo output and store the produced Pandas Dataframes
python2.7 load_worlds.py $PROJECT_NAME

#Export the dataframes to sql and csv formats
python2.7 export.py -p $PROJECT_NAME -csv -sql

#Need to run this to use the visualisation script. Calls a dummy distance function which does no computation.
python2.7 dist_calc.py -p $PROJECT_NAME -custom_dist_func dummy_dist_func -calc_dist_matrix

#Produce the visualisations for the generated PWs. Stores these in Mini Workflow/parser_output/euler_visualizations/$PROJECT_NAME/
python2.7 visualize.py -p $PROJECT_NAME -custom_visualisation_func euler_visualization
