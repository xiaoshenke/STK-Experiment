#!/bin/bash

#echo "$@"
if [ $# -ne 1 ]
then
	echo usage: sh/open_in_qview.sh abc.jpg
	exit 0
fi

jpg=$1
if [[ ! $jpg =~ "jpg" ]]
then
	echo $jpg not valid jpg dir
	exit 0
fi

if [[ $jpg =~ "/*.jpg" ]]
then
	dir=${jpg%/*}
	code=`ls $dir|grep jpg|head -n 1`
	jpg=$dir/$code
fi

echo open -a /Applications/qView.app/ $jpg
open -a /Applications/qView.app/ $jpg

