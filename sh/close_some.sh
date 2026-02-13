#!/bin/bash
# only work in mac os

# 保留的窗口数量默认为2
# 2->1
keep=1
if [ $# -eq 1 ]
then
	keep=$1
fi

echo ">>>>>>> before call osascript sh/oscpt/close_most_jpg.scpt $keep"
osascript sh/oscpt/close_most_jpg.scpt $keep

echo ""

echo ">>>>>>> before call osascript sh/oscpt/close_most_txt.scpt $keep"
osascript sh/oscpt/close_most_txt.scpt $keep

cmd="sh/close_some.sh $keep"
sh/log/log_to_operate.sh "$cmd" "CLOSE_SOME"
