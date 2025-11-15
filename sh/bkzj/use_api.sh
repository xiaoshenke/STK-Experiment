#!/bin/bash
# usage sh/ls_apply.sh [day]

if [ $# -ne 1 ]
then
	echo Usage: sh/bkzj/use_api.sh xxx
	exit 2
fi

version=$1

if [ $version -eq 0 ]
then
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_bkzj_version "$version" 
python realtime/properties_cli.py write_bkzj_version $version

