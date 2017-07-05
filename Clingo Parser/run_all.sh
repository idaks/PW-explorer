#!/bin/sh

# $1 = source folder
# $2 = num_PWs

for filename in $1/*.lp4; do
	#echo $filename
	k=${filename##*/}
	#echo $k
	#echo ${k%.*}
	sh ./run_file.sh $filename ${k%.*} ${2:-0}
done

