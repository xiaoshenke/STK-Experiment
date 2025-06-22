#!/bin/bash

# 封装了@realtime/observe/caozuo.py
echo ATTENTION: realtime/observe/caozuo-CMDS CLI

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str=#
mode=#

operate_type='get'
type2='#'
ignore_cache=0
desc=#

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
	-desc | --desc | --reason | -reason)
		shift
		desc=$1
		;;
	-eva | --eva | --front | -front | --front_type | -front_type)
		shift
		front_type=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/caozuo_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		# set value to type|operate_type by now-flag
		if [ $now -eq 0 ]
		then
			operate_type=$1
		elif [ $now -eq 1 ]
		then
			type2=$1
			desc=$1
			day=$1
		else
			type2=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

is_xls=$(python realtime/manual_cli.py is_xls $operate_type)
# reset value to last character
is_xls=${is_xls:0-1:1}

#echo "sh/flush_cli.sh is_code_types:$is_code_types is_eva:$is_eva is_operate:$is_operate can_be_stage:$can_be_stage"

#if [[ $is_code_types != "1" ]] 
#then
#	echo $type 不是切片池,当前仅支持切片池类型
#	exit 2
#fi

# 特殊处理fronts fenbu
if [[ $operate_type == "get" ]]
then
	echo python realtime/observe/caozuo.py get --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get --day $day --time_str $time_str --mode $mode

elif [[ $operate_type =~ "get_oper" ]] || [[ $operate_type =~ "oper" ]]
then
	echo python realtime/observe/caozuo.py get_operate --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_operate --day $day --time_str $time_str --mode $mode

elif [[ $operate_type =~ "get_cod" ]] || [[ $operate_type =~ "codes" ]]
then
	echo python realtime/observe/caozuo.py get_codes --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_codes --day $day --time_str $time_str --mode $mode

elif [[ ${operate_type:0:3} == "qpc" ]]
then
	echo python realtime/observe/caozuo.py get_qpc $operate_type --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_qpc $operate_type --day $day --time_str $time_str --mode $mode

elif [[ $operate_type =~ "pool_silu" ]] || [[ $operate_type =~ "poolsilu" ]]
then
	echo python realtime/observe/caozuo.py get_pool_silu $operate_type --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_pool_silu $operate_type --day $day --time_str $time_str --mode $mode --do_log 1

elif [[ $operate_type =~ "message" ]] || [[ $operate_type =~ "msg" ]]
then
	echo python realtime/observe/caozuo.py get_message $operate_type --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_message $operate_type --day $day --time_str $time_str --mode $mode 
#--do_log 1

elif [[ ${operate_type:0:3} == "eva" ]]
then
	echo python realtime/observe/caozuo.py get_eva $operate_type --day $day --time_str $time_str --mode $mode --reason $desc
	python realtime/observe/caozuo.py get_eva $operate_type --day $day --time_str $time_str --mode $mode --reason $desc --do_log 1

elif [[ $operate_type =~ "buyer_silu" ]] || [[ $operate_type =~ "buyersilu" ]]
then
	echo python realtime/observe/caozuo.py get_buyer_silu $operate_type --day $day --time_str $time_str --mode $mode --reason $desc
	python realtime/observe/caozuo.py get_buyer_silu $operate_type --day $day --time_str $time_str --mode $mode --reason $desc --do_log 1

elif [[ ${operate_type:0:3} == "buy" ]]
then
	echo python realtime/observe/caozuo.py get_buyer $operate_type --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_buyer $operate_type --day $day --time_str $time_str --mode $mode

elif [[ $operate_type == "get_xls" ]]
then
	echo python realtime/observe/caozuo.py get_xls $type2 --day $day --time_str $time_str --mode $mode
 	python realtime/observe/caozuo.py get_xls $type2 --day $day --time_str $time_str --mode $mode

elif [[ $is_xls == "1" ]]
then
	echo python realtime/observe/caozuo.py get_xls $operate_type --day $day --time_str $time_str --mode $mode
	python realtime/observe/caozuo.py get_xls $operate_type --day $day --time_str $time_str --mode $mode


elif [[ $operate_type =~ "list" ]]
then
	#echo python realtime/observe/caozuo.py last --day $day 
	#python realtime/observe/caozuo.py last --day $day 
	
	echo find ../stk_daily/$day/caozuo/
	find ../stk_daily/$day/caozuo/
else
	echo 不支持operate_type:$operate_type type2:$type2

fi
