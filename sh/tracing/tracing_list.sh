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

if [ $silent -eq 0 ]
then
	echo "ps aux|grep python |grep entity_cli|grep -v grep"
	ps aux|grep python |grep entity_cli|grep -v grep 

	echo ""
	ps aux|grep python |grep entity_cli|grep start_engine_mode|grep -v grep | awk '{print $14 ,$18}'
	echo ""
else
	ps aux|grep python |grep entity_cli|grep start_engine_mode|grep -v grep | awk '{print $14}'
fi

