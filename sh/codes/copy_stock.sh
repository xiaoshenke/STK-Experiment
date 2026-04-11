#!/bin/bash
# Usage: ./copy_stock.sh -d|-w|-f -i [-ig] -sub your-code
# copy shangzheng index, sh/copy_stock.sh -index 000001
# copy shenzheng index, sh/copy_stock.sh -f -i 399001
# copy chuangye index,sh/copy_stock.sh 399006
# -sub(sub-dir): copy stock to current-dir/sub_dir/

# 1:copy website 2:copy img
open_type=1
# 1:dk 2:wk 3:mk 4:f 5:all
stock_type=1
# 0:not index 1:index
is_index=0
ignore_local=0

appender="d"
sub_dir=""

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-h)
		echo Usage: sh/copy_stock.sh "-d[k]|-w[k]|-f -i[mg]|-w -index -sub" your-code
		echo '''for eg. 
copy shangzheng index, sh/copy_stock.sh -index 000001
copy shenzheng index, sh/copy_stock.sh 399001'''
		exit 2
		;;
	-d | -dk)
		stock_type=1
		appender="d"
		;;
	-a | -all)
		stock_type=5
		open_type=2
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
	-sub)
		sub_dir=$2
		shift
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
	echo Usage:./copy_stock.sh -d[k]|-w[k]|-m[k]|-f -i[mg]|-w your-code
	exit 2
fi

origin_code=$1
code=$1
if [ $is_index -eq 1 ] || [[ ${code:0:2} == "60" ]] || [[ ${code:0:2} == "68" ]]
then
	code=sh$code
elif [ $is_index -eq 1 ] || [[ ${code:0:1} == "4" ]] || [[ ${code:0:1} == "8" ]]
then
	code=bj$code
else
	code=sz$code
fi

# if it is open browser,just open it
if [ $open_type -eq 1  ]
then
	url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml
	echo going to open url:$url ...
	open $url
	exit 2
fi

# else,we will download and open image,carefully deal with -ignore parameter

url=""
cur_dir=`pwd`
local_code=$origin_code.$appender.jpg
# has sub-dir
if [ ${#sub_dir} -gt 0 ]
then
	local_code=$cur_dir/$sub_dir/$origin_code.$appender.jpg
fi

if [ $stock_type -eq 5 ]
then
	echo sh/copy_stock -i $origin_code
	sh/copy_stock.sh -i $origin_code
	echo sh/copy_stock -i -f $origin_code
	sh/copy_stock.sh -i -f $origin_code
	exit 2
fi

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
	exit 2
fi

# finally download and open
curl --max-time 1.0 -s -o $local_code $url

exit 2
