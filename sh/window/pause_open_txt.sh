#!/bin/bash

# 暂停open-txt-manager,此时所有的open txt的请求会全部被拒绝

export PYTHONUNBUFFERED=1

pause=1

if [ $# -eq 1 ]
then
	pause=$1
fi       

echo python engine/ecore/window/web_txt_cli.py pause $pause
python engine/ecore/window/web_txt_cli.py pause $pause

