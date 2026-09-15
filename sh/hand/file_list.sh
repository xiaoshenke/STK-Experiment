#!/bin/bash

# 打印当前的手工hand文件

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "先展示当前的模板文件"
echo "find engine/observe/hand/template/ |grep [.]properties"
ls engine/observe/hand/template/ | grep hand[.]properties | sort

# =================================================

echo ""
echo "================================================="
echo "然后展示当前手工配置的buyer文件"

dir=/Users/wuxian/Desktop/stk_daily/$day/juben/

echo "find $dir |grep [.]properties"
ls $dir |grep [.]properties|sort

echo ""
echo open $dir


