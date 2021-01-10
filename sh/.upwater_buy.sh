#!/bin/bash
# Usage: sh/upwater_buy.sh a(type) b(xls)

if [ $# -ne 2 ]
then
	echo Usage sh/upwater_buy.sh your-type your-xls
fi 

type=$1
xls=$2
echo python eva/cli.py do_eva $type upwater:mode=all:xls=$xls*buy:xls=$xls --realtime_type $xls


