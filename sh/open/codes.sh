#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: ./open_codes.sh aaa,bbb,ccc
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

codes=$1
open_mode='jpg'
now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-open_mode | --open_mode | -openmode | --openmode)
		shift
		open_mode=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			codes=$1
		elif [ $now -eq 1 ]
		then
			open_mode=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python realtime/code/cli.py open $codes --open_mode $open_mode
python realtime/code/cli.py open $codes --open_mode $open_mode

