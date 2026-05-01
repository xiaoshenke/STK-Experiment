#!/bin/bash

# 定位:分析版块池的bkzj数据

# TODO:

#if [ $# -lt 1 ]
#then
#	echo Usage: sh/pool/analyze_bkzj.sh xxx
#	exit 2
#fi

day=`date +'%Y-%m-%d'`
time_str='0'
mode='now'

xls='use_pool'

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
	*)
		xls=$1
		;;
	esac
	shift
done

cmd="sh/bkzj/analyze_bkzj.sh $xls --day $day --time_str $time_str --mode $mode"
sh/log/log_to_operate.sh "$cmd" "ANALYZE-BKZJ"

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

pool_type=$(python realtime/pool_cli.py get_realtime_pool $xls --day $day --mode $mode)

if [ ${#pool_type} -lt 1 ]
then
	echo python realtime/pool_cli.py get_realtime_pool 返回空数据
	exit 2
fi

#echo $pool_type

echo sh/template/run_pool_template.sh $pool_type pool_bkzj --mode $mode
sh/template/run_pool_template.sh $pool_type pool_bkzj --mode $mode
