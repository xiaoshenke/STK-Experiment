#!/bin/bash
# only work in mac os

# 保留的窗口数量默认为2
keep=2
if [ $# -eq 1 ]
then
        keep=$1
fi

echo osascript sh/oscpt/close_most_jpg.scpt $keep
osascript sh/oscpt/close_most_jpg.scpt $keep

echo ""

echo osascript sh/oscpt/close_most_txt.scpt $keep
osascript sh/oscpt/close_most_txt.scpt $keep
