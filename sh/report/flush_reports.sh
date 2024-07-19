#!/bin/bash
# usage sh/less_error.sh [day]

day=`date +'%Y-%m-%d'`
time_str=`date +'%H:%M:%S'`
id=0
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
		#break
		id=$1
		;;
	esac
	shift
done


path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ $id -gt 0 ]
then
	echo python realtime/query_cli.py report $id
	python realtime/query_cli.py report $id
	exit 2
fi
echo python realtime/query_cli.py report_last --force $force
python realtime/query_cli.py report_last --day $day --time_str $time_str --force $force

