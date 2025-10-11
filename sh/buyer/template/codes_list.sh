#!/bin/bash

day=`date +'%Y-%m-%d'`

if [ $# -gt 0 ]
then
	day=$1
fi

echo ""
echo "find engine/caop/buyers/template/ |grep [.]properties"
ls engine/caop/buyers/template/|grep -v xx_|grep [.]properties|grep -v test|sort

echo ""


