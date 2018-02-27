#!/usr/bin/env bash

clingo circuit-4coloring-equiv-classes.lp4 -n0 -c n=4 -V0 | grep -v "SATISFIABLE" | sort -u | wc -l



