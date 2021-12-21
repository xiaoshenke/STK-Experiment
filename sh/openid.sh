#!/bin/bash

mode="jpg"

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-mode)
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
if [ $# -ne 1 ]
then
	echo usage: sh/openid.sh 123
	exit 0
fi

id=$1

echo python realtime/query_cli.py open $id --open_mode $mode
python realtime/query_cli.py open $id --open_mode $mode

