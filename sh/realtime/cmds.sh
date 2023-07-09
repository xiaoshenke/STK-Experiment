#!/bin/bash

echo "ATTENTION: DEFAULT(INFO)-CMDS INFO"

day=#
time_str=#
mode=#

type='market'
front=''
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
	-fix | --fix)
		shift
		fix=$1
		;;	
        -help | --help)
		echo usage sh/realtime/cmds.sh [--day abc] [--time_str xyz] [--mode aaa ] type
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		else
			front=$1
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

if [ ${#type} -eq 0 ]
then
	echo type empty.
	echo usage sh/realtime/cmds.sh [--day abc] [--time_str xyz] [--mode aaa ] type
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ ${#front} -eq 0 ]
then
	echo python realtime/cmds_cli.py cmds $type --day $day --time_str $time_str --fix $fix --mode $mode
	python realtime/cmds_cli.py cmds $type --day $day --time_str $time_str --fix $fix --mode $mode
	exit 1
fi

echo python realtime/caop/front.py cmds --day $day --time_str $time_str --mode $mode $type $front
python realtime/caop/front.py cmds --day $day --time_str $time_str --mode $mode $type $front
