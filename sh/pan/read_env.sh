#!/bin/bash

now=0
while [ -n "$1" ]
do 
        case "$1" in 
        -help | --help)
		echo usage sh/config/read_env.sh 
                exit 1
                ;;
        *)
		;;
        esac
        shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/pan_config_cli.py read_env 
python realtime/pan_config_cli.py read_env 

