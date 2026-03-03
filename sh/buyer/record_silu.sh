#!/bin/bash

# 定位: 实时记录一下临盘的时候 并顺便打开对应的properties文件 便于手工进行编写思路

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
xls=#

type=#
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/record_silu.sh type [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-force | --force)
                shift
                force=$1
                ;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
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

to_file="/Users/wuxian/Desktop/stk_daily/$day/buyer/$type.properties"
file1="$cur_dir/engine/observe/buyer/template/silu.buyer.properties"

# 检验file1是否已经存在 且force标志位 != 1
if [ -f "$to_file" ] && [ $force -ne 1 ]
then
	echo 想要生成的buyer文件已经存在,无须操作: $to_file
	open $to_file
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

# 落日志
cmd="sh/buyer/record_silu.sh $type"
sh/log/log_to_operate.sh "$cmd" "RECORD-BUYER-SILU"


open $to_file
