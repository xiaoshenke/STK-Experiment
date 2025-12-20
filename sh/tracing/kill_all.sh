#!/bin/bash

type=''
pid=0
force=0
day=`date +'%Y-%m-%d'`

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
		echo usage sh/tracing/kill_all.sh [force] [--day]
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			force=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

# 打印当前的所有listener进程
ps aux|grep python |grep entity_cli|grep -v grep 

listens=$(ps aux|grep python |grep entity_cli|grep -v grep | awk '{print $2 "," $14}')
listens=($listens)

if [ ${#listens[@]} -eq 0 ]
then
	echo 不存在tracing-entity,不需要kill任何进程
	echo ""
	exit 2
fi

echo ""

for item in "${listens[@]}";do
	type=$(echo $item | awk -F',' '{print $2}')
	pid=$(echo $item | awk -F',' '{print $1}')

	if [[ $force == '1' ]]
	then
		echo kill $pid ..
		kill $pid
	else
		# 否则 调用web接口
		echo 找到了pid:$pid

		echo python engine/observe/tracing/port_cli.py kill_by_name $type --day $day
		python engine/observe/tracing/port_cli.py kill_by_name $type --day $day

		sleep 1.0
	fi
done 

