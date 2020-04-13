#!/bin/bash
# used to open dir codes

if [ $# -gt 1 ]
then
	echo Usage: ./open_codes.sh dir
	exit 2
fi

dir=`pwd`
if [ $# -eq 1 ]
then
	dir=$1
fi

echo open $dir/*.jpg
open $dir/*.jpg

