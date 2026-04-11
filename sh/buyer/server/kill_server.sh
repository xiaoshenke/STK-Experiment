#!/bin/bash

pid=0

# 打印当前的所有listener进程
ps aux|grep python |grep buyer|grep server|grep start_engine_mode|grep -v grep
echo ""

listens=$(ps aux|grep python |grep buyer|grep server|grep start_engine_mode|grep -v grep | awk '{print $2}')
listens=($listens)

for item in "${listens[@]}";do
	pid=$item

	echo 找到了pid:$pid 
	echo kill $pid ..
	kill $pid
done 

