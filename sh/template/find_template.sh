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

echo "开始进行搜索"
echo "## 手工剧本 find $template_dir | grep juben.properties|grep $template"
result=$( ls $template_dir | grep juben.properties|grep $template )
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi

echo ""
echo "## 默认的模板文件 find $cur_dir/engine/observe/buyer/template/ | grep $template"
result=$( ls $cur_dir/engine/observe/buyer/template/ | grep $template )
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi

echo ""
echo "## plan手工文件 find $template_dir | grep plan.properties|grep $template"
result=$( ls $template_dir | grep plan.properties|grep $template )
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi

echo ""
echo "## plan模板文件 find $cur_dir/engine/observe/plan/template/ | grep $template"
result=$( ls $cur_dir/engine/observe/plan/template/| grep $template)
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi


echo ""
echo "## buyer手工文件 find $template_dir | grep evafile.properties|grep $template"
result=$( ls $template_dir | grep evafile.properties|grep $template )
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi

echo ""
echo "## buyer模板文件 find $cur_dir/engine/caop/buyers/template/ |grep $template"
result=$( ls $cur_dir/engine/caop/buyers/template/|grep $template)
if [ ${#result} -eq 0 ]
then
	echo 寻找失败
else
	echo 成功找到文件如下:
	echo "$result"
fi

