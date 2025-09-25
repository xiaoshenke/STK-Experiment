#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi


echo ""
echo "行情列表 find engine/observe/buyer/template/ |grep maoding|grep [.]properties|sort"
ls engine/observe/buyer/template/|grep maoding|grep [.]properties|sort

echo ""

