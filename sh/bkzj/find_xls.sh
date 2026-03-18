#!/bin/bash
# usage sh/bkzj/get_xls.sh BKxxx

if [ $# -ne 1 ]
then
	echo Usage: sh/bkzj/get_xls.sh BKxxx
	exit 2
fi

code=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/xls/bk/bk_loader.py find_xls $code
python engine/xls/bk/bk_loader.py find_xls $code
