#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo 版块模版列表
ls engine/observe/buyer/template/|grep xx_|grep [.]properties|sort

echo ""
echo "行情列表 find engine/observe/buyer/template/|grep -v xx_|grep [.]properties"
ls engine/observe/buyer/template/|grep -v xx_|grep [.]properties|sort

echo ""
echo "find engine/observe/buyer/template/"

echo ""
echo "手写的剧本列表"
echo "find /Users/wuxian/Desktop/stk_daily/$day/template/|grep juben.properties"
ls /Users/wuxian/Desktop/stk_daily/$day/template/|grep "juben.properties"
