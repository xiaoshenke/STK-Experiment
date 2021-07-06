#!/bin/bash

if [ $# -ne 3 ]
then
	echo Usage:sh/build_apply.sh type day time_str
fi

type=$1
day=$2
time_str=$3

echo python cmd.py build_apply_by_fenshi $type $day $time_str
python cmd.py build_apply_by_fenshi $type $day $time_str

