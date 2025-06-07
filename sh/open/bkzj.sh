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

if [[ $code == "zsHSI" ]]
then 
	url=http://quote.eastmoney.com/gb/zsHSI.html
	echo going to open url:$url ...
	open $url
	exit 1
fi

if [[ $code =~ "zs" ]] || [[ $code =~ "sh" ]] || [[ $code =~ "sz" ]]
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

if [[ ${code:0:3} == "47." ]]
then
	url=https://quote.eastmoney.com/uk/$code.html
	echo going to open url:$url ...
	open $url
	exit 1
fi

if [[ ${code:0:2} != "BK" ]] && [[ ${#code} == 4 ]]
then
	code=BK$code
fi

url=http://quote.eastmoney.com/bk/90.$code.html
echo going to open url:$url ...
open $url

