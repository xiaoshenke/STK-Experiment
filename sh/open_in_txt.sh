#!/bin/bash

#echo "$@"
if [ $# -ne 1 ]
then
	echo usage: sh/open_in_txt.sh abc.log
	exit 0
fi
txt=$1
echo open -a /Applications/TextEdit.app/ $txt
open -a /Applications/TextEdit.app/ $txt

