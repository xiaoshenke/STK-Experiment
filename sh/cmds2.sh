#!/bin/bash

echo ATTENTION: BUYER-CMDS INFO

day=#
time_str=#
mode=#

type=''

while [ -n "$1" ]
do 
        case "$1" in 
        -day | --day)
                shift
                day=$1
                ;;
        -time_str | --time_str)
                shift
                time_str=$1
                ;;
        -mode | --mode)
                shift
                mode=$1
                ;;
        -help | --help)
		echo usage sh/realtime/cmds2.sh [--day abc] [--time_str xyz] [--mode aaa ] type
                exit 1
                ;;
        *)
		type=$1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

if [ ${#type} -eq 0 ]
then
	echo type empty.
	echo usage sh/realtime/cmds2.sh [--day abc] [--time_str xyz] [--mode aaa ] type
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/cmds_cli.py buyer_cmds $type --day $day --time_str $time_str --mode $mode
python realtime/cmds_cli.py buyer_cmds $type --day $day --time_str $time_str --mode $mode

