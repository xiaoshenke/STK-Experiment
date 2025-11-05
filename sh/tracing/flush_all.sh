#!/bin/bash

type=''
pid=0

# 打印当前的所有listener进程
ps aux|grep python |grep entity_cli|grep -v grep 

listens=$(ps aux|grep python |grep entity_cli|grep -v grep | awk '{print $14}')
listens=($listens)

if [ ${#listens[@]} -eq 0 ]
then
	echo 不存在entity,不需要flush任何进程
	echo ""
	exit 2
fi

echo ""
echo "tracing列表"
ps aux|grep python |grep entity_cli|grep start_engine_mode|grep -v grep | awk '{print $14}'
echo ""

for item in "${listens[@]}";do
	echo "开始刷新 $item ..."
	sh/tracing/flush_one.sh $item
	sleep 0.2

	echo ""
done 

