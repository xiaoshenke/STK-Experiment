#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "find engine/observe/plan/template/ |grep pool_|grep [.]properties"
echo ""

ls engine/observe/plan/template/|grep pool|grep [.]properties|sort

echo ""

