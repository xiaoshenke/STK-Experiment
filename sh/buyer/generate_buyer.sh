#!/bin/bash

# Usage: sh/buyer/generate_buyer.sh type [to-name] [--day]
# 定位: 用于根据@observe/buyer/template下的模板文件生成buyer文件

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
xls=#
type='default'
to_name=#
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/generate_buyer.sh type [to-name] [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
			to_name=$1
		elif [ $now -eq 1 ]
		then
			to_name=$1
		elif [ $now -eq 2 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment

to_file="/Users/wuxian/Desktop/stk_daily/$day/buyer/$to_name.properties"
file1="$cur_dir/engine/observe/buyer/template/$type.buyer.properties"

# 检验file1是否已经存在
if [ -f "$to_file" ]
then
	echo 想要生成的buyer文件已经存在,无须操作: $to_file
	exit 2
fi

if [ ! -f "$file1" ]
then
	echo 模板剧本文件: $file1 不存在,是否输入错误?
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo "复制文件 cp $file1 $to_file"
cp $file1 $to_file

echo ""
echo "最终生成的文件内容如下:"
cat $to_file

echo ""
echo 手工打开文件:  open $to_file
