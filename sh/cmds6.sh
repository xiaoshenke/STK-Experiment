#!/bin/bash

echo ATTENTION: CORE-CMDS INFO

day=#
time_str=#
mode=#

type=''
code_sub=#

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
        -help | --help)
		echo usage sh/realtime/cmds6.sh [--day abc] [--time_str xyz] [--mode aaa ] type
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		else
			code_sub=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

if [ $# -eq 2 ]
then
	type=$1
	code_sub=$2
fi

if [ ${#type} -eq 0 ]
then
	echo type empty.
	echo usage sh/realtime/cmds6.sh [--day abc] [--time_str xyz] [--mode aaa ] type
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/cmds_cli.py core_cmds $type --day $day --time_str $time_str --mode $mode --code_sub $code_sub
	
python realtime/cmds_cli.py core_cmds $type --day $day --time_str $time_str --mode $mode --code_sub $code_sub

