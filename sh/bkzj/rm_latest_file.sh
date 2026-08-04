#!/bin/bash
# usage sh/bkzj/rm_latest_file.sh [ aa:bb:cc ] --force 

day=#
time_str=#
now=0
force=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	*)
		if [ $now -eq 0 ]
		then
			time_str=$1
		elif [ $now -eq 1 ]
		then 
			force=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python util/bkzj_util.py remove $day $time_str --force $force
python util/bkzj_util.py remove $day $time_str --force $force
