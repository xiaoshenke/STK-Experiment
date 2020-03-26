#!/bin/bash
# used to show the latest apply file of [xls]
# TODO:

if [ $# -ne 1 ]
then
	echo Usage:./latest.sh xls
	exit 2
fi

day=`date +'%Y-%m-%d'`

xls=$1
ls ../stk_daily/$day/apply|grep $xls|tail -n 5

