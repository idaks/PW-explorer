#!/usr/bin/env bash

for i in `seq 2 7`; do
    echo "Number of 4-colorings of circuit with" $i "nodes:"
    clingo circuit-4coloring.lp4 -n0 -c n=$i -V0 | grep -v "SATISFIABLE" | wc -l             
done    


