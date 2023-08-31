#!/bin/bash
# Usage: sh/open_timestr.sh aa:bb:cc [xls]

mode="jpg"

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-mode|--mode)
		mode=$2
		shift
		;;
	*)
		break
		;;
	esac
	shift
done

#echo "$@"
if [ $# -lt 1 ]
then
	echo usage: sh/open_timestr.sh aa:bb:cc [xls]
	exit 0
fi

time_str=$1
xls=""
if [ $# -eq 2 ]
then
	xls=$2
	echo python realtime/query_cli.py open_timestr $time_str --xls $xls --open_mode $mode --no_backend true
	python realtime/query_cli.py open_timestr $time_str --xls $xls --open_mode $mode --no_backend true
else
	echo python realtime/query_cli.py open_timestr $time_str --open_mode $mode --no_backend true
	python realtime/query_cli.py open_timestr $time_str --open_mode $mode --no_backend true
fi

