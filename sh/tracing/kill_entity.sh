#!/bin/bash

type=''
pid=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/kill_listener.sh type
	exit 2
fi

type=$1

# 打印当前的所有listener进程
ps aux|grep python |grep entity_cli|grep -v grep 
echo ""

listens=$(ps aux|grep python |grep entity_cli|grep -v grep | awk '{print $2 "," $14}')
listens=($listens)

for item in "${listens[@]}";do
	_type=$(echo $item | awk -F',' '{print $2}')
	pid=$(echo $item | awk -F',' '{print $1}')

	if [[ $type == $_type ]]
	then
		echo 找到了pid:$pid 
		echo kill $pid ..
		kill $pid
		exit 2
	fi
done 

echo 尝试找到$type 代表的entity失败.

