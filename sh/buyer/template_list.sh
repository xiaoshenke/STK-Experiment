#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "find engine/caop/buyers/template/ |grep [.]properties"
ls engine/caop/buyers/template/|grep [.]properties|sort

echo ""
echo "手工配置的文件"

echo "find /Users/wuxian/Desktop/stk_daily/$day/template/|grep evafile.properties"
ls /Users/wuxian/Desktop/stk_daily/$day/template/|grep "evafile.properties"

