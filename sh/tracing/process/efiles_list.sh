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

#if [ $silent -eq 0 ]
#then
#	echo "ps aux|grep python |grep entity_cli|grep -v grep"
#	ps aux|grep python |grep entity_cli|grep -v grep 

#	echo ""
#fi

ps aux|grep python |grep entity_cli|grep start_engine_mode|grep efile|grep -v grep | awk '{print $14}'

efiles=$(ps aux|grep python |grep entity_cli|grep start_engine_mode|grep efile|grep -v grep | awk '{print $14}')

efiles=($efiles)

echo 数据量: ${#efiles[@]}

if [ ${#efiles[@]} -eq 0 ]
then
	exit 2
fi

for item in "${efiles[@]}";do
	echo 可以手工打开:  sh/buyer/open_file.sh ${item#*:}
done 

