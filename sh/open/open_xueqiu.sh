#!/bin/bash
# Usage: ./open_xueqiu.sh [code]

if [ $# -ne 1 ]
then
	url=https://xueqiu.com/hq
	echo we will open xueqiu main website: $url...
	open $url
	exit 1
fi

code=$1

url=https://xueqiu.com/S/$code
echo going to open url:$url ...
open $url

