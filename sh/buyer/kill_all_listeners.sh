#!/bin/bash

type=''
pid=0

# 打印当前的所有listener进程
ps aux|grep python |grep listener_cli|grep -v grep 

listens=$(ps aux|grep python |grep listener_cli|grep -v grep | awk '{print $2 "," $14}')
listens=($listens)

if [ ${#listens[@]} -eq 0 ]
then
	echo 不存在listener,不需要kill任何进程
	echo ""
	exit 2
fi

echo ""

for item in "${listens[@]}";do
	_type=$(echo $item | awk -F',' '{print $2}')
	pid=$(echo $item | awk -F',' '{print $1}')

	echo kill $pid ..
	kill $pid
done 

