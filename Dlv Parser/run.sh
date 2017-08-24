#!/bin/bash
DLV=./dlv_bin/dlv.i386-apple-darwin.bin

# 8-queen
echo "8-queen"
# output ASP file
$DLV -silent -N=8 Mini\ Workflow/dlv_input/nqueens.dlv > Mini\ Workflow/dlv_output/nqueens.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/nqueens.asp -sql -csv 

# 4-coloring
echo "4-coloring"
# output ASP file
$DLV -silent Mini\ Workflow/dlv_input/coloring.dlv -filter=color > Mini\ Workflow/dlv_output/coloring.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/coloring.asp -sql -csv

# TEST_SWITCH
echo "region_switch"
# output ASP file
$DLV -silent $TEST_FOLDER/CEN-NDC-regions_pw.dlv $TEST_FOLDER/CEN-NDC-regions_ixswitch.dlv $TEST_FOLDER/CEN-NDC-regions_pwswitch.dlv -filter=rel > Mini\ Workflow/dlv_output/region_switch.asp
# parse the ASP file and output files in other common format
python dlv_parser/AntlrDlv.py Mini\ Workflow/dlv_output/region_switch.asp -sql -csv

