#!/bin/bash
# Usage: ./open_xueqiu.sh code

if [ $# -ne 1 ]
then
	echo Usage:./open_xueqiu.sh code
	exit 2
fi

code=$1

url=https://xueqiu.com/S/$code
echo going to open url:$url ...
open $url

