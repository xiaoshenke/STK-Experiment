#!/bin/bash

export PYTHONUNBUFFERED=1

type='eva'

day=`date +'%Y-%m-%d'`
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/start_file_listener.sh type [--day ]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

alread_exists=$( sh/buyer/check_listener_exists.sh $type )
# reset value to last character
alread_exists=${alread_exists:0-1:1}
dir=/Users/wuxian/Desktop/stk_daily/$day/

if [[ $alread_exists == "1" ]]
then
	echo 尝试启动对买点文件类型:$type 的监听器 但是检查到系统中已经存在对应的进程 因此无视本次调度. 
	echo 可以手工查看日志: $dir/observe.buyer.xx_$type.log
	exit 2
fi

dir=/Users/wuxian/Desktop/stk_daily/$day/

echo "python engine/observe/buyer/listener_cli.py start_engine_mode $type --day $day  log: $dir/observe.buyer.xx_$type.log"
nohup python engine/observe/buyer/listener_cli.py start_engine_mode $type --day $day >>$dir/observe.buyer.xx_$type.log 2>&1 &
