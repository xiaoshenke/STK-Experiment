#!/bin/bash

# 打印当前的手工buyer文件

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/

echo "find $dir |grep [.]properties"
ls $dir |grep [.]properties|sort

echo ""
echo open $dir

