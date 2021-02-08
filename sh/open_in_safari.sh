#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage: sh/open_in_safari.sh abc.jpg
	exit 0
fi

jpg=$1
if [[ ! $jpg =~ "jpg" ]]
then
	echo $jpg not valid jpg dir
	exit 0
fi

#echo open -a /Applications/Safari.app/ $jpg
open -a /Applications/Safari.app/ $jpg

