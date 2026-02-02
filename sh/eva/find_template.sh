#!/bin/bash

# 搜索当前所有可能的template文件

# 功能包括:
# 1, 搜索engine/eva-str/export下的.py模板
# 2, 搜索eva-str的计算结果 格式@/Desktop/stk_daily/2026-02-02//caozuo//RunEvaStrNode_xxx.txt

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
	echo Usage: sh/eva/find_template.sh template [--day ]
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
template_dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/
caozuo_dir=/Users/wuxian/Desktop/stk_daily/$day/caozuo/

#result=$( ls $template_dir | grep juben.properties|grep $template )
#if [ ${#result} -eq 0 ]
#then
#	echo 尝试寻找手工剧本$template_dir 下数据失败
#else
#	echo "开始进行搜索"
#	echo "## 手工剧本 find $template_dir | grep properties|grep $template"
#	echo 成功找到文件如下:
#	echo "$result"
#fi

result=$( find $cur_dir/engine/eva_str/export/ | grep $template | grep -v pyc )
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找$cur_dir/engine/eva_str/export/ 下数据失败
else
	echo ""
	echo "## 默认的模板文件 find $cur_dir/engine/eva_str/export/ | grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

result=$( ls $caozuo_dir | grep Run|grep RunEvaStr| grep $template )
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找$caozuo_dir 下的模板运算结果数据失败
else
	echo ""
	echo "## 模板文件的计算结果数据 find $caozuo_dir | grep Run|grep RunEvaStr | grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

echo ""

