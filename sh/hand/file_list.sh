#!/bin/bash

# 打印当前的手工hand文件

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

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
echo "然后展示当前手工配置的hand文件"

dir=/Users/wuxian/Desktop/stk_daily/$day/juben/

echo "find $dir | grep hand | grep [.]properties"
ls $dir |grep [.]properties|grep hand|sort

echo ""
echo open $dir


#echo ""
#echo "================================================="
#echo "然后展示计算结果文件"

#dir=/Users/wuxian/Desktop/stk_daily/$day/hand/

#echo "find $dir "
#ls $dir | sort

#echo ""
#echo open $dir


