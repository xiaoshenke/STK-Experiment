#!/bin/bash

day=`date +'%Y-%m-%d'`
time_str=#
mode='now'

msg=''

# update 2026-01-22: ignore_cache:1->0
ignore_cache=0
debug=0
open=0
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/log/hand_log.sh msg
	exit 2
fi

msg=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo sh/log/hand_log.sh msg
		exit 1
		;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			msg="$1"
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [[ -z $msg ]]
then
	echo msg empty.
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

python realtime/operate2.py log "$msg" "HAND-SAVE" --day $day

