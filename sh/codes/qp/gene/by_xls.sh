#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

xls=#
template=#
now=0
time_str=#
mode='now'
operate='flush'
with_logic=-1
ignore_cache=0
chain_id=-1

if [ $# -lt 2 ]
then
	echo Usage: sh/codes/qp/gene/by_xls.sh xls template [--day ] 
	exit 2
fi

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
	-ignore_cache | --ignore_cache | -ignore | --ignore)
		shift
		ignore_cache=$1
		;;
        -chain_id | --chain_id | --chain)
		shift
		chain_id=$1
		;;
	-operate| --operate)
		shift
		operate=$1
		;;
        -with_logic | --with_logic | -logic| --logic)
		shift
		with_logic=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			template=$1
		elif [ $now -eq 2 ]
		then
			#operate=$1
			day=$1
		elif [ $now -eq 3 ]
		then
			mode=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done


echo python engine/gene/qp/xls/cli.py generate $xls $template --day $day --mode $mode --time_str $time_str --chain_id $chain_id
python engine/gene/qp/xls/cli.py generate $xls $template --day $day --mode $mode --time_str $time_str --chain_id $chain_id
