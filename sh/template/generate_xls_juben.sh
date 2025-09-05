#!/bin/bash

# 仅用于根据模板(observe/buyer/template/xls.juben.properties)生成题材的剧本文件(即stk_daily/template/xxx.juben.properties) 
# Usage: sh/template/generate_xls_juben.sh xls [--day ]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
time_str=#
mode='plan'
xls=#
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/template/generate_xls_juben.sh xls [--day ]
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
			xls=$1
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

file1="/Users/wuxian/Desktop/stk_daily/$day/template/$xls.juben.properties"
file2="$cur_dir/engine/observe/buyer/template/xls.juben.properties"

# 检验file1是否已经存在
if [ -f "$file1" ]
then
	echo 想要生成的xls文件已经存在: $file1
	exit 2
fi

echo "复制文件 cp $file2 $file1"
cp $file2 $file1

echo "进行内容替换 sed -i 's/xx/$xls/g' $file1"
sed -i "" "s/xx/$xls/g" $file1

echo ""
echo "最终生成的文件内容如下:"
cat $file1

echo ""
echo 手工打开文件:  open $file1
