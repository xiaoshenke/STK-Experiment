#!/bin/bash

mode="jpg"
back=""
#echo "$@"
id=0
force=1
debug=0
day=`date +'%Y-%m-%d'`

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-mode|--mode)
		mode=$2
		shift
		;;
	-day | --day)
		shift
		day=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-back|--back)
		back=$2
		shift
		;;
	-debug|--debug)
		shift
		debug=$1
		;;
	*)
		#break
		id=$1
		;;
	esac
	shift
done

#if [ $# -ne 1 ]
#then
#	echo usage: sh/openid.sh 123
#	exit 0
#fi

if [ $# -eq 1 ]
then
	id=$1
fi

if [ $id -lt 1 ]
then
	echo usage: sh/openid.sh 123
	exit 0
fi

if [ ${#back} -gt 1 ]
then
	echo python realtime/query_cli.py open $id --day $day --open_mode $mode --back $back --force $force --debug $debug
	python realtime/query_cli.py open $id --day $day --open_mode $mode --back $back --force $force --debug $debug
else
	echo python realtime/query_cli.py open $id --day $day --open_mode $mode --force $force --debug $debug
	python realtime/query_cli.py open $id --day $day --open_mode $mode --force $force --debug $debug
fi
