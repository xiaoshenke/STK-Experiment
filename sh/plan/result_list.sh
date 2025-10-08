#!/bin/bash

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo "先给出通过模板计算生成的结果文件"
echo "ls ../stk_daily/$day/plan//  |grep Run |grep Temp"
ls ../stk_daily/$day/plan//|grep Run|grep Temp

echo ""
echo "open \"../stk_daily/$day/plan/\""
echo "open ../stk_daily/$day/plan/"
echo ""

echo "下面是手工的plan: 即通过sh/plan/open_file.sh xx 生成的文件"
echo "ls ../stk_daily/$day/plan//  |grep -v Run"
ls ../stk_daily/$day/plan//|grep -v Run|grep Manu
