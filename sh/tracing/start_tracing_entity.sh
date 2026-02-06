#!/bin/bash

export PYTHONUNBUFFERED=1

type='eva'

day=`date +'%Y-%m-%d'`
start_at=#
end_at=#
now=0
sort=0

if [ $# -lt 1 ]
then
	echo Usage: sh/tracing/start_file_listener.sh type [--day ]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-end | -end_at | --end | --end_at)
		shift
		end_at=$1
		;;
	-start | -start_at | --start | --start_at)
		shift
		start_at=$1
		;;
	-sort | --sort)
		shift
		sort=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			end_at=$1
		elif [ $now -eq 2 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

alread_exists=$( sh/tracing/check_entity_exists.sh $type )
# reset value to last character
alread_exists=${alread_exists:0-1:1}

if [[ $alread_exists == "1" ]]
then
	echo 尝试启动对买点文件类型:$type 的监听器 但是检查到系统中已经存在对应的进程 因此无视本次调度.
	exit 2
fi

valid=$(python engine/observe/tracing/entity_cli.py check_valid_type $type $day 09:30:00)
_valid=${valid:0-1:1}
if [[ $_valid == "0" ]]
then
	echo 尝试启动对买点文件类型:$type 的监听器 但是python engine/observe/tracing/entity_cli.py check_valid_type 返回false

	echo ""
	echo ""
	
	python engine/observe/tracing/entity_cli.py check_valid_type $type $day 09:30:00
	exit 2
else
	echo 通过了python engine/observe/tracing/entity_cli.py check_valid_type 的校验 可以成功启动...
	echo ""
	echo ""
fi

dir=/Users/wuxian/Desktop/stk_daily/$day/

echo "python engine/observe/tracing/entity_cli.py start_engine_mode $type --day $day --end_at $end_at --sort $sort --start_at $start_at log: $dir/observe.tracing.xx_$type.log"
nohup python engine/observe/tracing/entity_cli.py start_engine_mode $type --day $day --end_at $end_at --sort $sort --start_at $start_at >>$dir/observe.tracing.xx_$type.log 2>&1 &

cmd="sh/tracing/start_tracing_entity.sh $type --start_at $start_at --end_at $end_at"
sh/log/log_to_operate.sh "$cmd" "START-TRACING"

