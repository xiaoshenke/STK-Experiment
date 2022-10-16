#!/bin/bash
# Usage: ./open_stock.sh -d|-w|-f -i [-ig] your-code

# open shangzheng index, sh/open_stock.sh -index 000001
# open shenzheng index, sh/open_stock.sh -f -i 399001
# open chuangye index,sh/open_stock.sh 399006

# 1:open website 2:open img
open_type=1
# 1:dk 2:wk 3:mk 4:f
stock_type=1
# 0:not index 1:index
is_index=0
ignore_local=0

appender="d"

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-h)
		echo Usage: sh/open_stock.sh "-d[k]|-w[k]|-f -i[mg]|-w -index" your-code
		echo '''for eg. 
open shangzheng index, sh/open_stock.sh -index 000001
open shenzheng index, sh/open_stock.sh 399001'''
		exit 2
		;;
	-d | -dk)
		stock_type=1
		appender="d"
		;;
	-w | -wk)
		stock_type=2
		appender="w"
		;;
	-f)
		stock_type=4
		appender="f"
		;;
	-i | -img)
		open_type=2
		;;
	-index)
		is_index=1
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

origin_code=$1
code=$1
if [ $is_index -eq 1 ] || [[ ${code:0:2} == "60" ]] || [[ ${code:0:2} == "68" ]]
then
	code=sh$code
else
	code=sz$code
fi

# if it is open browser,just open it
if [ $open_type -eq 1  ]
then
	url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml
	code=$1
	url=http://stockpage.10jqka.com.cn/$code
	echo going to open url:$url ...
	open $url
	exit 2
fi

# else,we will download and open image,carefully deal with -ignore parameter

url=""
local_code=$origin_code.$appender.jpg

if [ $stock_type -eq 1 ]
then
	url=http://image.sinajs.cn/newchart/daily/n/$code.gif
elif [ $stock_type -eq 2 ]
then
	url=http://image.sinajs.cn/newchart/weekly/n/$code.gif
elif [ $stock_type -eq 3 ]
then
	url=http://image.sinajs.cn/newchart/monthly/n/$code.gif
else
	url=http://image.sinajs.cn/newchart/min/n/$code.gif
fi

# check whether code is already exist
if [ -f $local_code ] && [ $ignore_local -eq 0 ]
then
	echo $local_code already exist!
	open $local_code
	exit 2
fi

# finally download and open
curl -s -o $local_code $url
open $local_code

exit 2
