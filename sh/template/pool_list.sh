#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi


echo ""
echo "行情列表 find engine/observe/juben/template/ |grep xx_|grep pool|grep [.]properties"
ls engine/observe/juben/template/|grep xx_|grep pool_|grep [.]properties|sort

echo ""

