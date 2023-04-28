#!/bin/bash

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
                echo usage sh/open_last_all.sh [-key xyz] [-day aaaa-bb-cc] [-time_str xx:yy:zz] [mode]
                exit 1
                ;;
        *)
                #break
		type=$1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/cmds_cli.py cmds $type --day $day --time_str $time_str --mode $mode
python realtime/cmds_cli.py cmds $type --day $day --time_str $time_str --mode $mode

