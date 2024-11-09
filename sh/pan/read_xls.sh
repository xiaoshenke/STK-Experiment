#!/bin/bash

key=''

now=0
while [ -n "$1" ]
do 
        case "$1" in 
        -help | --help)
		echo usage sh/config/read_xls.sh key
                exit 1
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
	echo usage sh/config/read_xls.sh key
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/pan_config_cli.py read_xls $key
python realtime/pan_config_cli.py read_xls $key 

