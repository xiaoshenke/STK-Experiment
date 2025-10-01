#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo "find engine/caop/buyers/template/ |grep [.]properties"
ls engine/caop/buyers/template/|grep xx_i|grep [.]properties|sort

echo ""


