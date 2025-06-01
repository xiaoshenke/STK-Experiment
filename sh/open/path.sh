#!/bin/bash
# usage sh/open/path.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open/path.sh ABC
	exit 2
fi

day=#
dir=#

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo usage sh/open/path.sh time_str [--day abc] 
		exit 1
		;;
	*)
		dir=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/open_cli.py open --day $day "$dir" --back info
python realtime/open_cli.py open --day $day "$dir" --back info
