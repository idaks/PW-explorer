#!/bin/sh

#clingo_input_fname = $1
#project_name = $2

cp $1 /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_input/$2.lp4

echo "Copying Done"

# if [[-z $3]]; 
# then
# 	clingo -n $3 /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_input/$2.lp4 > /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_output/$2.txt
# else
# 	clingo -n 0 /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_input/$2.lp4 > /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_output/$2.txt
# fi

clingo -n ${3:-0} /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_input/$2.lp4 > /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_output/$2.txt

echo "Clingo Ouput Done"

python Preprocessing.py /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_output/$2.txt

echo "Preprocessing Done"

python AntlrClingo.py /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/clingo_output/$2.txt 2 > /Users/sahil1105/PW-explorer/Clingo\ Parser/Mini\ Workflow/parser_output/$2.txt

