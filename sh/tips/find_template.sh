#!/bin/bash

# 搜索当前所有可能的template文件

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
template=#
now=0
time_str=#
mode='plan'
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/tips/find_template.sh template [--day ]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			template=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment
template_dir=engine/observe/tips/template/
caozuo_dir=/Users/wuxian/Desktop/stk_daily/$day/caozuo/

result=$( ls $cur_dir/$template_dir | grep tips.properties | grep $template )
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找tips模板文件 $template_dir 数据失败
else
	echo ""
	echo "## tips模板文件 find $template_dir | grep tips.properties | grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

result=$( ls $caozuo_dir |grep tips| grep $template)
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找caozuo计算结果文件 $caozuo_dir 数据失败
else
	echo ""
	echo "## caozuo计算结果文件 find $caozuo_dir |grep tips| grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

echo ""

