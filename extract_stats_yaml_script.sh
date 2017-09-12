#!/bin/bash

PROJECT_NAMES=(2017-09-11-20:24:04-figure4C_minart_0_1PWmncb 2017-09-11-20:25:17-figure4C_minart_0_25PWmncb 2017-09-11-20:26:09-figure4C_minart_0_7PWmncb 2017-09-11-20:27:05-figure4C_minart_0_25PWmncb 2017-09-11-20:28:29-figure4C_minart_0_25PWmncb)
for PROJECT_NAME in ${PROJECT_NAMES[*]}
do
	PROJECT_FOLDER=Andropogon-ZOOM_IN/$PROJECT_NAME
	python3 extract_stats_from_yaml.py "$PROJECT_FOLDER" "figure4C_minart_0"
done