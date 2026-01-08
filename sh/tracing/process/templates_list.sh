#!/bin/bash

# 列举当前的tracing进程列表

silent=0

while [ -n "$1" ]
do 
	case "$1" in 
	-silent | --silent)
		shift
		silent=$1
		;;
	*)
		;;	
	esac
	shift
done

ps aux|grep python |grep entity_cli|grep start_engine_mode|grep "[temp|tmp]"|grep -v grep | awk '{print $14}'

temps=$(ps aux|grep python |grep entity_cli|grep start_engine_mode|grep "[temp|tmp]"|grep -v grep | awk '{print $14}')

temps=($temps)

echo 数据量: ${#temps[@]}

if [ ${#temps[@]} -eq 0 ]
then
	exit 2
fi

#for item in "${temps[@]}";do
#	echo 可以手工打开:  sh/buyer/open_file.sh ${item#*:}
#done 

