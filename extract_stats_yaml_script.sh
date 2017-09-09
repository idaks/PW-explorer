#!/bin/bash

PROJECT_NAMES=(2017-09-07-22:53:56-figure4C_1PW_key 2017-09-07-22:54:41-figure4C_4PW 2017-09-07-22:55:05-figure4C_5PW 2017-09-07-22:55:28-figure4C_5PW 2017-09-07-22:55:48-figure4C_5PW 2017-09-07-22:56:05-figure4C_1PW 2017-09-07-22:56:17-figure4C_1PW 2017-09-07-22:56:29-figure4C_1PW)
for PROJECT_NAME in ${PROJECT_NAMES[*]}
do
	PROJECT_FOLDER=Nico_Examples_DLV/Original/$PROJECT_NAME
	python3 extract_stats_from_yaml.py "$PROJECT_FOLDER" "figure4C"
done