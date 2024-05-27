#!/bin/bash
# usage sh/open_xls_list.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open_xls_list.sh ABC
	exit 2
fi

key=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo open "https://so.eastmoney.com/news/s?sort=time&keyword=$key"
open "https://so.eastmoney.com/news/s?sort=time&keyword=$key"

