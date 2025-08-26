#!/bin/bash

# 用于生成非题材的文件 比如sh/plan/generate_file_not_xls.sh xxx,那么就会根据xxx.template.properties文件生成一下xxx.plan.properties文件(即默认模式下会生成同名的文件)
# 注意: 这里支持template2,此时会根据template2生成template的文件 即支持不同名文件的生成

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
template=#
now=0
time_str=#
mode='plan'
template2=#
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/plan/generate_file_not_xls.sh template [template2] [--day ]
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
			template2=$1
		elif [ $now -eq 1 ]
		then
			template2=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment

file1="/Users/wuxian/Desktop/stk_daily/$day/plan/$template.plan.properties"
file2="$cur_dir/engine/observe/plan/template/$template2.template.properties"

# 检验file1是否已经存在
if [ -f "$file1" ]
then
	echo 想要生成的文件已经存在: $file1
	exit 2

fi

if [ ! -f "$file2" ]
then
	echo 模版文件不存在: $file2  ,检查一下输入是否正确?
	exit 2
fi

echo "复制文件 cp $file2 $file1"
cp $file2 $file1

echo ""
echo "最终生成的文件内容如下:"
cat $file1
