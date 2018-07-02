#!/bin/bash 
# Usage: ./cat_index.sh your-index-csv-file

if [ $# -ne 1 ]
then
	echo Usage:./cat_index.sh your-index-csv-file
	exit 2
fi

cat $1 |gawk 'BEGIN{FS=","} {print $1, $3, $2}'

