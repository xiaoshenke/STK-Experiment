#!/bin/bash
# usage sh/open/path.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open/path.sh ABC
	exit 2
fi

day=#
dir=#
back='info'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-back | --back)
		shift
		back=$1
		;;
	-help | --help)
		echo usage sh/open/path.sh path [day] [--day abc] 
		exit 1
		;;
	*)
		if [ $now -eq 0 ]
		then
			dir=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/open_cli.py open --day $day "$dir" --back $back
python realtime/open_cli.py open --day $day "$dir" --back $back --do_log 1
