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
has_changzhu=$(osascript sh/oscpt/has_changzhu_txt_window.scpt)
if [[ $has_changzhu == "1" ]]
then
	echo 当前存在常驻窗口 因此调用 osascript sh/oscpt/close_most_txt_has_changzhu.scpt
	osascript sh/oscpt/close_most_txt_has_changzhu.scpt
else
	osascript sh/oscpt/close_most_txt.scpt $keep
fi

cmd="sh/close_some.sh $keep"
sh/log/log_to_operate.sh "$cmd" "CLOSE_SOME"
