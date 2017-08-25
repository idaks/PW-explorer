#!/bin/bash
DLV=./dlv_bin/dlv.i386-apple-darwin.bin

echo "region_switch"
# list of project names of CEN-NDC-regions with exactly one restriction being removed
PROJECT_NAMES=(2017-05-31-16:47:24-CEN-NDC-regions 2017-05-31-16:47:53-CEN-NDC-regions 2017-05-31-16:49:19-CEN-NDC-regions 2017-05-31-16:50:20-CEN-NDC-regions 2017-05-31-16:51:01-CEN-NDC-regions 2017-05-31-16:51:38-CEN-NDC-regions 2017-05-31-16:52:17-CEN-NDC-regions 2017-05-31-16:53:02-CEN-NDC-regions)
for PROJECT_NAME in ${PROJECT_NAMES[*]}
do
    echo $PROJECT_NAME
    # output ASP file
    TEST_FOLDER="../iConference/$PROJECT_NAME/1-ASP-input-code"
    $DLV -silent $TEST_FOLDER/CEN-NDC-regions_pw.dlv $TEST_FOLDER/CEN-NDC-regions_ixswitch.dlv $TEST_FOLDER/CEN-NDC-regions_pwswitch.dlv -filter=rel > Mini\ Workflow/dlv_output/$PROJECT_NAME.asp
    # parse the ASP file and output files in other common format
    dlv_parser/pwe export Mini\ Workflow/dlv_output/$PROJECT_NAME.asp -sql -csv
    dlv_parser/pwe sqlQuery Mini\ Workflow/parser_output/sql_exports/$PROJECT_NAME/$PROJECT_NAME.db -f dlv_parser/test.sql
done
