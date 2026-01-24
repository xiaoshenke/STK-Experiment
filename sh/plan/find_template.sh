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
	echo Usage: sh/template/find_template.sh template [--day ]
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
template_dir=/Users/wuxian/Desktop/stk_daily/$day/template/
caozuo_dir=/Users/wuxian/Desktop/stk_daily/$day/caozuo/
plan_dir=/Users/wuxian/Desktop/stk_daily/$day/plan/

result=$( ls $template_dir | grep plan.properties|grep $template )
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找plan手工文件 $template_dir 数据失败
else
	echo ""
	echo "## plan手工文件 find $template_dir | grep plan.properties|grep $template"
	echo 成功找到文件如下:
	echo "$result"
fi

result=$( ls $cur_dir/engine/observe/plan/template/| grep $template)
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找plan模板文件 $cur_dir/engine/observe/plan/template/ 数据失败
else
	echo ""
	echo "## plan模板文件 find $cur_dir/engine/observe/plan/template/ | grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

result=$( ls $plan_dir |grep Run|grep Template| grep $template)
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找plan计算结果文件 $plan_dir 数据失败
else
	echo ""
	echo "## plan计算结果文件 find $plan_dir |grep Run|grep Template| grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

echo ""

