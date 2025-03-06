#!/bin/bash

echo ATTENTION: MANUAL-BUYER-CMDS CLI

day=#
time_str=#
mode='now'

operate=''
branch=#
codes=#
clear=0
ignore_cache=1

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
	-branch | --branch)
		shift
		branch=$1
		;;
        -clear | --clear)
		shift
		clear=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/manual/buyer_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			operate=$1
		elif [ $now -eq 1 ]
		then
			branch=$1
			codes=$1
		elif [ $now -eq 2 ]
		then
			branch=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [[ $operate == "saveto" ]] || [[ $operate == "save_to" ]]
then

	echo python realtime/manual_buyer_cli.py save_to $branch --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --clear $clear
	python realtime/manual_buyer_cli.py save_to $branch --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --clear $clear

elif [[ $operate == "checkout" ]] 
then
	echo python realtime/manual_buyer_cli.py checkout $branch --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/manual_buyer_cli.py checkout $branch --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 

elif [[ $operate == "version" ]] || [[ $operate =~ "cur" ]]
then
	echo python realtime/manual_buyer_cli.py version  --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/manual_buyer_cli.py version  --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo 当前不支持类型$operate,branch:$branch
fi

