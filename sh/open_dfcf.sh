#!/bin/bash
# Usage: ./open_dfcf.sh [code]

if [ $# -ne 1 ]
then
	url=https://stock.eastmoney.com/
	echo we will open dfcf main website: $url...
	open $url
	exit 1
fi

code=$1

if [[ $code =~ "zs" ]] || [[ $code =~ "sh" ]]
then
	url=https://quote.eastmoney.com/$code.html
	echo going to open url:$url ...
	open $url
	exit 1
fi

if [[ ${code:0:2} == "2." ]]
then
	url=https://quote.eastmoney.com/zz/$code.html
	echo going to open url:$url ...
	open $url
	exit 1
fi

url=http://quote.eastmoney.com/bk/90.$code.html
echo going to open url:$url ...
open $url

