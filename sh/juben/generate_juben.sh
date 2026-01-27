#!/bin/bash

# Usage: sh/juben/generate_juben.sh type from_type [--day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
type=''
from_type=''
force=0

if [ $# -lt 2 ]
then
	echo Usage: sh/juben/generate_juben.sh type from_type [--day]
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
			from_type=$1
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

to_file="/Users/wuxian/Desktop/stk_daily/$day/juben/$type.properties"

# 检验file1是否已经存在 且force标志位 != 1
if [ -f "$to_file" ] && [ $force -ne 1 ]
then
	echo 想要生成的juben文件已经存在,无须操作: $to_file
	exit 2
fi

file1="$cur_dir/engine/observe/tracing/template/$from_type.tracing.properties"
file2="$cur_dir/engine/observe/juben/template/$from_type.juben.properties"
file3="$cur_dir/engine/observe/juben/template/$from_type.properties"

file=#
if [ -f "$file1" ]
then
	file=$file1
elif [ -f "$file2" ]
then
	file=$file2
elif [ -f "$file3" ]
then
	file=$file3
fi

if [[ $file == "#" ]]
then
	echo 找不到模板文件,生成文件失败
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo "复制文件 cp $file $to_file"
cp $file $to_file

echo "" >> $to_file
echo "from_template=$file" >> $to_file

echo ""
echo "最终生成的文件内容如下:"
cat $to_file


echo ""
echo 手工打开文件:  open $to_file

open $to_file
