#!/bin/bash

mode="jpg"
back=""
#echo "$@"
id=0

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-mode|--mode)
		mode=$2
		shift
		;;
	-back|--back)
		back=$2
		shift
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
	echo python realtime/query_cli.py open $id --open_mode $mode --back $back
	python realtime/query_cli.py open $id --open_mode $mode --back $back
else
	echo python realtime/query_cli.py open $id --open_mode $mode
	python realtime/query_cli.py open $id --open_mode $mode
fi
