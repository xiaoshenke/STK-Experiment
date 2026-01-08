#!/bin/bash

# 打印当前的手工buyer文件

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "先展示当前的模板文件"
echo "find engine/observe/tracing/template/ |grep [.]properties"
ls engine/observe/tracing/template/ | grep tracing[.]properties | sort

echo ""
echo "然后展示当前手工配置的buyer文件"

dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/

echo "find $dir |grep [.]properties"
ls $dir |grep [.]properties|sort

echo ""
echo open $dir

