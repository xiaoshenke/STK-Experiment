#!/bin/bash

key=''
val=''
force=0
reason=#
day=`date +'%Y-%m-%d'`

now=0
while [ -n "$1" ]
do 
        case "$1" in 
	-day | --day)
                shift
                day=$1
                ;;
	-force | --force | --froce)
		shift
		force=$1
		;;	
	-reason | --reason | -desc | --desc)
		shift
		reason=$1
		;;
        -help | --help)
		echo usage sh/qpc/write_key.sh key val
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			key=$1
		elif [ $now -eq 1 ]
		then
			val=$1
		elif [ $now -eq 2 ]
		then
			reason=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ ${#key} -eq 0 ]
then
	echo key empty.
	echo usage sh/qpc/write_key.sh key val
	exit 1
fi

if [ ${#val} -eq 0 ]
then
	echo val empty.
	echo usage sh/qpc/write_key.sh key val
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/qpc_cli.py add --day $day $key $val --force $force --reason $reason
python realtime/qpc_cli.py add --day $day $key $val --force $force --reason $reason

