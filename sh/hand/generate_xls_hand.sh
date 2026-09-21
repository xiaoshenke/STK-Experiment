#!/bin/bash

# Usage: sh/hand/template/generate_xls_hand.sh xls [type] [to-name] [--day]

# 定位: 用于根据@observe/hand/template下的模板文件生成hand文件
# 注意: 会做replace的操作

# copy from @sh/buyer/template/generate_xls_buyer.sh 

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)
now=0
xls=#
type='default'
to_name=#
force=0

# 标志位=1的话 会去刷新一下tracing observe
flush=0

if [ $# -lt 1 ]
then
	echo Usage: sh/hand/generate_xls_hand.sh xls [type] [to-name] [--day]
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
			xls=$1
			to_name=$1
		elif [ $now -eq 1 ]
		then
			type=$1
		elif [ $now -eq 2 ]
		then
			to_name=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/hand/gene/gene_two_files.py gene_xls_hand $xls $type $to_name $day
python engine/observe/hand/gene/gene_two_files.py gene_xls_hand $xls $type $to_name $day

