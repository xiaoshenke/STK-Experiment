#!/bin/bash

TO_PATH="/Users/wuxian/Desktop"

if [ $# -ne 1 ]
then
	echo Usage: ./copy_to.sh your-file
	exit 2
fi

cp $1 $TO_PATH

