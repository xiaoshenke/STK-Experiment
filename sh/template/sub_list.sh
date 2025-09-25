#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi


echo ""
echo "行情列表 find engine/observe/juben/template/ |grep xx_i|grep [.]properties|sort"
ls engine/observe/juben/template/|grep xx_i|grep [.]properties|sort

echo ""

