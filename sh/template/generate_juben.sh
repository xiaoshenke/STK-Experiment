#!/bin/bash

# 用于(根据现存的模板文件)生成剧本文件,会依次尝试xx.template,xx.plan.xx.buyer
# 注意: 这里支持template2,此时会根据template2生成template的文件 即支持不同名文件的生成
# 注意: 不进行replace的操作

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
	echo Usage: sh/template/generate_juben.sh template [template2] [--day ]
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
	-help | --help)
		echo "Usage: sh/template/generate_juben.sh template [template2](支持名字不同)"
		exit 2
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

target="/Users/wuxian/Desktop/stk_daily/$day/template/$template.juben.properties"

if [ -f "$target" ]
then
	echo 目标文件:$target 已经存在 不做处理
	exit 2
fi

file=#
file0="$cur_dir/engine/observe/juben/template/$template2.juben.properties"
file1="$cur_dir/engine/observe/juben/template/$template2.template.properties"
file2="$cur_dir/engine/observe/plan/template/$template2.template.properties"
file3="$cur_dir/engine/caop/buyers/template/$template2.buyer.properties"

if [ -f "$file0" ]
then
	file=$file0
elif [ -f "$file1" ]
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

echo "复制文件 cp $file $target"
cp $file $target

echo ""
echo "最终生成的文件内容如下:"
cat $target

echo ""
echo 打开文件:open $target
