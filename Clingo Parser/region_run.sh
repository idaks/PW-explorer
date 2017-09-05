#!/bin/bash
#region_run.sh

echo "region_switch"

PROJECT_NAMES=(2017-08-29-21:48:22-cen-ndc-regions_1pw 2017-08-29-21:48:50-cen-ndc-regions_30pw 2017-08-29-21:49:40-cen-ndc-regions_3pw 2017-08-29-21:49:58-CEN-NDC-regions_3PW 2017-08-29-21:50:12-CEN-NDC-regions_2PW 2017-08-29-21:56:48-CEN-NDC-regions_3PW 2017-08-29-21:57:02-CEN-NDC-regions_51PW 2017-08-29-21:57:29-CEN-NDC-regions_5PW)
QUERY_FOLDER="sqlQuery"
for PROJECT_NAME in ${PROJECT_NAMES[*]}
do
	echo $PROJECT_NAME
	PROJECT_FOLDER="Regions_Example_Clingo/$PROJECT_NAME/1-ASP-input-code"
	python clingo_out.py $PROJECT_FOLDER/CEN-NDC-regions_pw.clingo $PROJECT_FOLDER/CEN-NDC-regions_pwswitch.clingo $PROJECT_NAME -n 0
	python parse.py $PROJECT_NAME
	python export.py -p $PROJECT_NAME -sql -csv
	echo "overlapped regions, followed by subset regions, followed by all not equal relations"
	python sql_query.py -p $PROJECT_NAME -custom_file $QUERY_FOLDER/allThree.sql > $PROJECT_FOLDER/sqlQuery_results.txt
done

#Regions_Example_Clingo/2017-08-29-21:48:22-cen-ndc-regions_1pw