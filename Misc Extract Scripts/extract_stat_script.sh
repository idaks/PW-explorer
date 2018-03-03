#!/bin/bash

PROJECT_NAMES=(2017-08-29-21:48:22-cen-ndc-regions_1pw 2017-08-29-21:48:50-cen-ndc-regions_30pw 2017-08-29-21:49:40-cen-ndc-regions_3pw 2017-08-29-21:49:58-CEN-NDC-regions_3PW 2017-08-29-21:50:12-CEN-NDC-regions_2PW 2017-08-29-21:56:48-CEN-NDC-regions_3PW 2017-08-29-21:57:02-CEN-NDC-regions_51PW 2017-08-29-21:57:29-CEN-NDC-regions_5PW)
for PROJECT_NAME in ${PROJECT_NAMES[*]}
do
	PROJECT_FOLDER=Clingo\ Parser/Regions_Example_Clingo/$PROJECT_NAME/4-PWs
	OUTPUT_FOLDER=Clingo\ Parser/Regions_Example_Clingo/$PROJECT_NAME
	python3 extract_from_gv.py "$PROJECT_FOLDER" > "$OUTPUT_FOLDER/extracted_stats.txt"
done