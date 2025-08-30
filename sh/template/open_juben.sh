#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#
do_log=1

if [ $# -lt 1 ]
then
	echo Usage: sh/template/open_juben.sh juben [day]
	exit 2
fi

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-juben | --juben)
		shift
		juben=$1
		;;
        -do_log | --do_log)
		shift
		do_log=$1
		;;
	-help | --help)
		echo Usage: sh/template/open_juben.sh juben [day]
		exit 2
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			juben=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben --do_log $do_log
python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben --do_log $do_log
