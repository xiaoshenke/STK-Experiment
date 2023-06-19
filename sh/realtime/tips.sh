#!/bin/bash

day=#
time_str=#
mode=#

operate='write'
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
		echo usage sh/realtime/tips.sh [--day abc] [--time_str xyz] [--mode aaa ] [operate]
                exit 1
                ;;
        *)
		operate=$1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	operate=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ "$operate" = "write" ]
then
	echo python realtime/tips_cli.py write --day $day --time_str $time_str --mode $mode
	python realtime/tips_cli.py write --day $day --time_str $time_str --mode $mode
	exit 1
else
	echo python realtime/tips_cli.py read --day $day --time_str $time_str --mode $mode
	python realtime/tips_cli.py read --day $day --time_str $time_str --mode $mode
fi


