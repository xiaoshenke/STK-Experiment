#!/bin/bash 
# Usage:
# 1 ./open_stock.sh -name your-stock-name
# 2 ./open_stock.sh 000001

# here we open sina stock website,eg. http://finance.sina.com.cn/realstock/company/sz300722/nc.shtml

# 0:not name,but code 1:name
is_name=0
while [ -n "$1" ]
do
	case "$1" in
	-n | -name)
		is_name=1
		;;
	*)
		break
		;;
	esac
	shift
done

if [ $# -ne 1 ]
then
	echo Usage:./open_stock.sh -name your-stock-name or ./open_stock.sh 000001
	exit2
fi

code=""
if [ $is_name -eq 1 ]
then
	code=$(python cli.py get_code_by_name_exact $1)
else
	code=$1
fi

if [ ${#code} -eq 0 ]
then
	echo code is empty
	exit 2
fi

if [[ ${code:0:2} == "30" ]]
then
	code=sz$code
else
	code=sh$code
fi

url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml

echo going to open url:$url ...

open $url
