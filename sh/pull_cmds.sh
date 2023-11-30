#!/bin/bash

day=#
time_str=#
mode=#

type='market'
t2='#'
fix=0
now=0
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
	-t2 | --t2)
		shift
		t2=$1
		;;
	-fix | --fix)
		shift
		fix=$1
		;;	
        -help | --help)
		echo usage sh/realtime/cmds.sh [--day abc] [--time_str xyz] [--mode aaa ] type
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
	echo usage sh/realtime/cmds.sh [--day abc] [--time_str xyz] [--mode aaa ] type
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH
	
echo python realtime/cmds_cli.py pull_cmds $type --t2 $t2 --day $day --time_str $time_str --mode $mode
	
python realtime/cmds_cli.py pull_cmds $type --t2 $t2 --day $day --time_str $time_str --mode $mode
