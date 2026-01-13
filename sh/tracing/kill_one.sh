#!/bin/bash

type=''
pid=0
force=0
day=`date +'%Y-%m-%d'`

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/kill_listener.sh type [force]
	exit 2
fi

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-help | --help)
		echo usage sh/tracing/kill_entity.sh type [force] [--day]
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			force=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

#if [ $# -gt 1 ]
#then
#	force=$2
#fi

# 打印当前的所有listener进程
#ps aux|grep python |grep entity_cli|grep -v grep 
#echo ""

listens=$(ps aux|grep python |grep entity_cli|grep -v grep | awk '{print $2 "," $14}')
listens=($listens)

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

for item in "${listens[@]}";do
	_type=$(echo $item | awk -F',' '{print $2}')
	pid=$(echo $item | awk -F',' '{print $1}')

	# force=1的时候 直接调用kill
	if [[ $type == $_type ]] && [[ $force == '1' ]]
	then
		echo 找到了pid:$pid 
		echo kill $pid ..
		kill $pid
		exit 2
	# 否则 调用web接口
	elif [[ $type == $_type ]]
	then
		echo 找到了pid:$pid

		echo python engine/observe/tracing/port_cli.py kill_by_name $type --day $day
		python engine/observe/tracing/port_cli.py kill_by_name $type --day $day

		sleep 1.0
		exit 2
	fi
done 

echo 尝试找到$type 代表的entity失败.

