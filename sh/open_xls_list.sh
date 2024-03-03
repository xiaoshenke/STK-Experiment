#!/bin/bash
# usage sh/open_xls_list.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open_xls_list.sh ABC
	exit 2
fi

xls_list=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/xls/open_cli.py open_xls_list $xls_list
python engine/xls/open_cli.py open_xls_list $xls_list

