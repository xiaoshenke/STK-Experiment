#!/bin/bash
# only work in mac os

force=0

if [ $# -eq 1 ]
then
	force=$1
fi

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-force | --force)
		shift
		force=$1
		;;
	*)
		force=$1
		;;
	esac
	shift
done

if [ $force -eq 1 ]
then
	echo 指定了force=1 因此关闭全部窗口
	osascript -e 'quit app "TextEdit"'
	exit 2
fi

has_changzhu=$(osascript sh/oscpt/has_changzhu_txt_window.scpt)
echo has_changzhu:$has_changzhu

if [[ $has_changzhu == "1" ]]
then
	echo 当前存在常驻窗口 因此调用 osascript sh/oscpt/close_txt2.scpt
	osascript sh/oscpt/close_txt2.scpt
else
	osascript -e 'quit app "TextEdit"'
fi

#osascript -e 'quit app "TextEdit"'

#cmd="sh/close_txt.sh"
#sh/log/log_to_operate.sh "$cmd" "CLOSE_TXT"

#osascript sh/oscpt/close_txt2.scpt 
