#!/bin/bash
# usage sh/buyer/server/open_by_schedule_id.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/spacing/open_id.sh xx
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

type='0'
spacing='0'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
        -spacing | --spacing | -space | --space)
                shift
                spacing=$1
                ;;
	-help | --help)
		echo usage sh/spacing/open_id.sh xx
		exit 1
		;;
	*)
		if [ $now -eq 0 ]
		then
			type=$1
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

echo python engine/spacing/reg_cli.py manual_register $type --day $day --spacing $spacing
python engine/spacing/reg_cli.py manual_register $type --day $day --spacing $spacing
