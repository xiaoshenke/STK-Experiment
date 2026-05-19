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
	echo Usage: sh/buyer/find_template.sh template [--day ]
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

template_dir=engine/observe/buyer/template/
buyer_dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/
eva_str_dir=engine/eva_str/export/buyer/

result=$( ls $template_dir | grep [.]properties|grep $template )
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找buyer模版文件 $template_dir 数据失败
else
	echo ""
	echo "## buyer模版文件 find $template_dir | grep [.]properties|grep $template"
	echo 成功找到文件如下:
	echo "$result"
fi

result=$( ls $eva_str_dir | grep [.]py |grep -v pyc|grep $template )
if [ ${#result} -eq 0 ]
then	
	echo 尝试寻找buyer+eva-str文件 $eva_str_dir 数据失败
else
	echo ""
	echo "## uyer+eva-str文件 find $eva_str_dir| grep [.]py |grep -v pyc|grep $template "
	echo 成功找到文件如下:
	echo "$result"
fi

result=$( ls $buyer_dir| grep $template)
if [ ${#result} -eq 0 ]
then
	echo 尝试寻找buyer手工文件 $buyer_dir 数据失败
else
	echo ""
	echo "## buyer手工文件 find $buyer_dir | grep $template"
	echo 成功找到文件如下:
	echo "$result"
	echo ""
fi

echo ""

