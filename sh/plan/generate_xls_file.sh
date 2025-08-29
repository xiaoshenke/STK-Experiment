#!/bin/bash

# 用于根据模板生成题材的配置文件 比如sh/plan/generate_xls_file.sh jungong xx_normal,那么就会根据xx_normal.template.properties文件生成一下jungong.plan.properties文件
# Usage: sh/plan/generate_xls_file.sh xls template_name [--day ]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
template=#
now=0
time_str=#
mode='plan'
xls=#
template=#
force=0

if [ $# -lt 2 ]
then
	echo Usage: sh/plan/generate_xls_file.sh xls template_name [--day ] 
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
			template=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment

file1="/Users/wuxian/Desktop/stk_daily/$day/template/$xls.plan.properties"
file2="$cur_dir/engine/observe/plan/template/$template.template.properties"

# 检验file1是否已经存在
if [ -f "$file1" ]
then
	echo 想要生成的xls文件已经存在: $file1
	exit 2

fi

if [ ! -f "$file2" ]
then
	echo xx_模版文件不存在: $file2  ,检查一下输入是否正确?
	exit 2
fi

echo "复制文件 cp $file2 $file1"
cp $file2 $file1

echo "进行内容替换 sed -i 's/xx/$xls/g' $file1"
sed -i "" "s/xx/$xls/g" $file1

echo ""
echo "最终生成的文件内容如下:"
cat $file1
