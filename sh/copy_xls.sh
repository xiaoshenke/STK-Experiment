#!/bin/bash

# Usage: ./copy_xls.sh -d|-w|-f -i [-ig] -sub your-code
# -sub(sub-dir): copy stock to current-dir/sub_dir/

# 1:copy website 2:copy img
open_type=2

# 1:dk 2:wk 3:mk 4:f 5:all
stock_type=1

ignore_local=0

appender="d"
sub_dir=""

# extract parameters
while [ -n "$1" ]
do
	case "$1" in
	-h)
		echo Usage: sh/copy_xls.sh "-d[k]|-w[k]|-f -i[mg]|-w -index -sub" your-code
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
	echo Usage:./copy_xls.sh -d[k]|-w[k]|-m[k]|-f -i[mg]|-w your-code
	exit 2
fi

xls=$1

nid=$(python engine/xls/open_cli.py get_dfcf_code $xls)

if [[ $nid == '#' ]]
then
	echo 找不到版块:$xls对应的东方财富code
	exit 2
fi

# if it is open browser,just open it
if [ $open_type -eq 1  ]
then
	echo 暂时不支持打开web类型
	#url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml
	#echo going to open url:$url ...
	#open $url
	exit 2
fi

# else,we will download and open image,carefully deal with -ignore parameter

url=""
cur_dir=`pwd`
local_code=$xls.$appender.jpg

# has sub-dir
if [ ${#sub_dir} -gt 0 ]
then
	local_code=$cur_dir/$sub_dir/$xls.$appender.jpg
fi

if [ $stock_type -eq 5 ]
then
	echo sh/copy_xls -i $xls
	sh/copy_xls.sh -i $xls

	echo sh/copy_xls -i -f $xls
	sh/copy_xls.sh -i -f $xls
	exit 2
fi

if [ $stock_type -eq 1 ]
then
	url="http://webquotepic.eastmoney.com/GetPic.aspx?imageType=KXL&type=&nid=$nid"
else
	url="http://webquotepic.eastmoney.com/GetPic.aspx?imageType=r&type=&nid=$nid"
fi

#echo url: $url
#echo local_code: $local_code

# check whether code is already exist
if [ -f $local_code ] && [ $ignore_local -eq 0 ]
then
	echo $local_code already exist!
	exit 2
fi

# finally download and open
curl --max-time 1.0 -s -o $local_code $url

exit 2
