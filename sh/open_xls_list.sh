#!/bin/bash
# usage sh/open_xls_list.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open_xls_list.sh ABC
	exit 2
fi

open_mode=jpg
time_str=#
fenshi_type=#

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-mode | --mode | -open_mode | --open_mode)
		shift
		open_mode=$1
		;;
	-type | --type)
		shift
		open_mode=$1
		;;
	-fenshi_type | --fenshi_type)
		shift
		fenshi_type=$1
		;;


	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-help | --help)
		echo usage sh/open_xls_list.sh [--day abc] [--type xyz] xls_list
		exit 1
		;;
	*)
		xls_list=$1
		;;
	esac
	shift
done

#xls_list=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/xls/open_cli.py open_xls_list $xls_list --open_mode $open_mode --time_str $time_str --fenshi_type $fenshi_type
python engine/xls/open_cli.py open_xls_list $xls_list --open_mode $open_mode --time_str $time_str --fenshi_type $fenshi_type

