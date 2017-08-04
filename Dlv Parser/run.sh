#!/bin/bash
DLV=./dlv_bin/dlv.i386-apple-darwin.bin

# 8-queen
# output ASP file
$DLV -silent -N=8 Mini\ Workflow/dlv_input/nqueens.dlv > Mini\ Workflow/dlv_output/nqueens.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/nqueens.asp --sql --csv --hdf --msg --pkl

# 4-coloring
# output ASP file
$DLV -silent Mini\ Workflow/dlv_input/coloring.dlv -filter=color > Mini\ Workflow/dlv_output/coloring.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/coloring.asp --sql --csv  --msg --pkl
