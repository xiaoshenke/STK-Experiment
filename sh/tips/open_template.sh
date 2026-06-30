#!/bin/bash

path=`pwd`

if [ $# -lt 1 ]
then
	echo Usage: sh/tips/open_template.sh template 
	exit 2
fi

template=$1

cur_dir=/Users/wuxian/Desktop/STK-Experiment
template_dir=engine/observe/tips/template/

caozuo_dir=/Users/wuxian/Desktop/stk_daily/$day/caozuo/

file="$cur_dir/$template_dir/$template"
echo $file
if [ -f "$file" ]
then
	open $file
else
	echo 不存在对应的文件
fi


echo ""

