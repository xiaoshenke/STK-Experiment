#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "find engine/observe/plan/template/ |grep [.]properties"
echo ""

ls engine/observe/plan/template/|grep [.]properties|sort

echo ""
echo "然后是手工配置的plan"
echo "find /Users/wuxian/Desktop/stk_daily/$day/template/|grep plan.properties"
ls /Users/wuxian/Desktop/stk_daily/$day/template/|grep "plan.properties"

