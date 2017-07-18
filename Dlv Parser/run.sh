#!/bin/bash
DLV=./dlv_bin/dlv.i386-apple-darwin.bin
# output ASP file
$DLV -silent -N=8 Mini\ Workflow/dlv_input/nqueens.dlv > Mini\ Workflow/dlv_output/nqueens.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/nqueens.asp --sql --csv --hdf --msg --pkl