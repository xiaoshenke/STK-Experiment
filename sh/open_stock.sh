#!/bin/bash 
# Usage: ./open_stock.sh -d[k]|-w[k]|-m[k]|-f -i[mg]|-w [-ig] your-code 
# -f:fenshitu -i:open img -w:open website(default)
# -dk day kline,-wk week kline,-mk month kline

# open shangzheng index, sh/open_stock.sh -index 000001
# open shenzheng index, sh/open_stock.sh -f -i 399001

JPG_PATH="data/jpg_data"

# 1:open website 2:open img
open_type=1

# 1:dk 2:wk 3:mk 4:f
stock_type=1
is_index=0
ignore_local=0
while [ -n "$1" ]
do
	case "$1" in
	-h)
		echo Usage: ./open_stock.sh "-d[k]|-w[k]|-m[k]|-f -i[mg]|-w -index" your-code
		echo '''for eg. 
open shangzheng index, ./open_stock.sh -f -index -i 000001
open shenzheng index, ./open_stock.sh -f -i 399001'''
		exit 2
		;;
	-d | -dk)
		stock_type=1
		;;
	-w | -wk)
		stock_type=2
		;;
	-m | -mk)
		stock_type=3
		;;
	-f)
		stock_type=4
		;;
	-i | -img)
		open_type=2
		;;
	-index)
		is_index=1
		;;
	-w)
		open_type=1
		;;
	-ig)
		ignore_local=1
		;;
	-*)
		echo $1 arg not supported!
		exit 2
		;;	
	*)
		break
		;;
	esac
	shift
done

if [ $# -ne 1 ]
then
	echo Usage:./open_stock.sh -d[k]|-w[k]|-m[k]|-f -i[mg]|-w your-code
	exit 2
fi

code=$1
if [ $is_index -eq 1 ] || [[ ${code:0:2} == "60" ]]
then
	code=sh$code
else
	code=sz$code
fi

if [ $open_type -eq 1  ]
then
	url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml
	echo going to open url:$url ...
	open $url
	exit 2
fi

url=""
local=""
local_code=""
if [ $stock_type -eq 1 ]
then
	url=http://image.sinajs.cn/newchart/daily/n/$code.gif
	local=`find $JPG_PATH|grep $code.jpg|head -n 1`
	local_code=$code.jpg
elif [ $stock_type -eq 2 ]
then
	url=http://image.sinajs.cn/newchart/weekly/n/$code.gif
	local=`find $JPG_PATH|grep w_$code.jpg|head -n 1`
	local_code=w_$code.jpg
elif [ $stock_type -eq 3 ]
then
	url=http://image.sinajs.cn/newchart/monthly/n/$code.gif
	local=`find $JPG_PATH|grep m_$code.jpg|head -n 1`
	local_code=m_$code.jpg
else
	url=http://image.sinajs.cn/newchart/min/n/$code.gif
	local=`find $JPG_PATH|grep $code.jpg|head -n 1`
	local_code=$code.jpg
fi

if [ -f $local_code ]
then
	echo $local_code already exist!
	open $local_code
	exit 2
fi

if [ ${#local} -gt 6 ] && [ $ignore_local -eq 0 ]
then
	echo $local_code already exist at $local 
	open $local
	exit 2
fi

#echo downloading img:$url to $local_code
curl -s -o $local_code $url
open $local_code

exit 2


