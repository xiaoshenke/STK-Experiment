#!/bin/bash

key=''

now=0
while [ -n "$1" ]
do 
        case "$1" in 
        -help | --help)
		echo usage sh/config/read_pool.sh key
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
	echo usage sh/config/read_pool.sh key
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py read_pool $key
python realtime/properties_cli.py read_pool $key 

