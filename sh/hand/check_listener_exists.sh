#!/bin/bash

export PYTHONUNBUFFERED=1

day=`date +'%Y-%m-%d'`
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/hand/check_listener_exists.sh type 
	exit 2
fi

type=$1

ps aux|grep python |grep hand|grep listener_cli|grep -v grep 

echo ""

listens=$(ps aux|grep python |grep hand|grep listener_cli|grep -v grep | awk '{print $14}')
listens=($listens)

for item in "${listens[@]}";do
	if [[ $item == $type ]]
	then
		echo 1
		exit 
	fi
done 

echo 0

