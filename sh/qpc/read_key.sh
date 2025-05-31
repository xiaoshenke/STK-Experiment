#!/bin/bash

key=''
day=`date +'%Y-%m-%d'`

now=0
while [ -n "$1" ]
do 
        case "$1" in 
        -help | --help)
		echo usage sh/qpc/read_key.sh key
                exit 1
                ;;	
	-day | --day)
                shift
                day=$1
                ;;
        *)
		key=$1
		;;
        esac
        shift
done

if [ ${#key} -eq 0 ]
then
	echo key empty.
	echo usage sh/qpc/read_key.sh key
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/qpc_cli.py read_name $key --day $day
python realtime/qpc_cli.py read_name $key --day $day
