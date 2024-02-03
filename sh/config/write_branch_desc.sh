#!/bin/bash

if [ $# -ne 2 ]
then
	echo usage sh/config/write_branch_desc.sh branch desc
	exit 1
fi

val=$1
desc=$2

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_branch_desc $val $desc
python realtime/properties_cli.py write_branch_desc $val $desc

