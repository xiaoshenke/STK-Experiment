#!/bin/bash

# Usage: sh/hand/generate_hand.sh type [to-name] [--day]   -> 语义:根据样本字符串生成文件 默认生成的名字和样本名字相同
# 定位: 用于根据@observe/hand/template下的模板文件生成hand文件

# 会生成2个文件 1个hand 1个tmp

# copy from @sh/buyer/template/generate_buyer.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

now=0
xls=#
type=#
to_name=#
force=0

if [ $# -lt 2 ]
then
	echo Usage: sh/hand/generate_hand.sh type [to-name] [--day]
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

echo python engine/observe/hand/gene/gene_next_file.py gene_next $type $to_name $day
python engine/observe/hand/gene/gene_next_file.py gene_next $type $to_name $day

from_file="/Users/wuxian/Desktop/stk_daily/$day/juben/$type.hand.properties"
to_file="/Users/wuxian/Desktop/stk_daily/$day/juben/$to_name.hand.properties"
if [ ! -f "$to_file" ]
then
	echo 生成失败!
	exit 2
fi

# 接下来还要对文本内容进行一些修改

line=$(grep -n -m 1 "模板:" $to_file | cut -d: -f1)

if [ -n "$line" ] 
then
	# 替换原先的存储本文
	sed -i '' "${line}d" $to_file
	declare -i line=$line-1
	sed -i '' "${line}a\\
# 模板: ${from_file}\\
" $to_file
fi


line=$(grep -n -m 1 "存储:" $to_file | cut -d: -f1)

if [ -n "$line" ] 
then
	# 替换原先的存储本文
	sed -i '' "${line}d" $to_file
	declare -i line=$line-1
	sed -i '' "${line}a\\
# 存储: ${to_file}\\
" $to_file
fi

line=$(grep -n -m 1 "可以继续启动对应的监听器" $to_file | cut -d: -f1)
if [ -n "$line" ]
then
	declare -i line2=$line+1	
	# 替换原先的存储本文
	sed -i '' "${line2}d" $to_file
	sed -i '' "${line}d" $to_file

	declare -i line=$line-1
	sed -i '' "${line}a\\
可以继续启动对应的监听器: sh/hand/start_file_listener.sh $to_name --only 0\\
对应的日志在 ../stk_daily/$day/observe.hand.xx_$to_name.log\\
\\
" $to_file
fi


open $to_file
