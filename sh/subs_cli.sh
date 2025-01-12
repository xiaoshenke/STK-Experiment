#!/bin/bash

echo ATTENTION: SUBS-CMDS CLI

day=#
time_str=#
mode=#

code_type=''
subs_type='basic'
operate='info'
ignore_cache=0

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
	-eva | --eva | --front | -front | --front_type | -front_type)
                shift
                operate=$1
                ;;
	-operate | --operate)
                shift
                operate=$1
                ;;
	-ignore_cache | --ignore_cache)
                shift
                ignore_cache=$1
                ;;
        -help | --help)
		echo usage sh/realtime/subs_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] code_type subs_type [info|flush|front-type]
                exit 1
                ;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then
			subs_type=$1
		else
			operate=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	code_type=$1
fi

if [ $# -eq 2 ]
then
	code_type=$1
	subs_type=$2
fi

if [ $# -eq 3 ]
then
	code_type=$1
	subs_type=$2
	operate=$3
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_eva=$(python realtime/subs_cli.py is_front_type $operate)
is_eva=${is_eva:0-1:1}

echo "sh/subs_cli.sh is_eva:$is_eva"

if [[ $operate == "info" ]] || [[ $operate == "trend" ]] || [[ $operate == "size" ]]
then
	echo python realtime/subs_cli.py info --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type
	python realtime/subs_cli.py info --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type

elif [[ ${operate:0:6} == "stage:" ]]
then
	echo python realtime/subs_cli.py stage --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type $operate
	python realtime/subs_cli.py stage --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type $operate

elif [[ $operate == "flush" ]]
then
	echo python realtime/subs_cli.py flush --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type
	python realtime/subs_cli.py flush --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type

elif [[ $is_eva == "1" ]]
then
	echo python realtime/subs_cli.py front --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type $operate
	python realtime/subs_cli.py front --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache $code_type $subs_type $operate

else

	echo python realtime/flush_cli.py flush_subs $code_type $subs_type --front_type $operate --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
        python realtime/flush_cli.py flush_subs $code_type $subs_type --front_type $operate --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
fi

