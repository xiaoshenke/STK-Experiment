#!/bin/bash
# only work in mac os

has_changzhu=$(osascript sh/oscpt/has_changzhu_txt_window.scpt)
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
