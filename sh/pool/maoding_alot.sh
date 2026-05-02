#!/bin/bash

# 定位:分析版块池的20cm数据

day=`date +'%Y-%m-%d'`
time_str='0'
mode='now'

xls='use_pool'
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
	*)
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

pool_type=$(python realtime/pool_cli.py get_realtime_pool $xls --day $day --mode $mode)

if [ ${#pool_type} -lt 1 ]
then
	echo python realtime/pool_cli.py get_realtime_pool 返回空数据
	exit 2
fi

cmd="sh/pool/maoding_alot.sh $xls --day $day --time_str $time_str --mode $mode"
sh/log/log_to_operate.sh "$cmd" "POOL-ANALYZE-MAODING-ALOT"

#echo $pool_type

echo sh/template/run_pool_template.sh $pool_type pool_maoding_alot --day $day --mode $mode
sh/template/run_pool_template.sh $pool_type pool_maoding_alot --day $day --mode $mode
