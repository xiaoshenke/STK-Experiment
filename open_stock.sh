
#!/bin/bash 
# Usage: ./open_stock.sh -d[k]|-w[k]|-m[k]|-f -i[mg]|-w your-code 
# -f:fenshitu -i:open img -w:open website(default)
# -dk day kline,-wk week kline,-mk month kline

# 1:open website 2:open img
open_type=1

# 1:dk 2:wk 3:mk 4:f
stock_type=1

while [ -n "$1" ]
do
	case "$1" in
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
	-w)
		open_type=1
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
if [[ ${code:0:2} == "30" ]]
then
	code=sz$code
else
	code=sh$code
fi

if [ $open_type -eq 1  ]
then
	url=http://finance.sina.com.cn/realstock/company/$code/nc.shtml
	echo going to open url:$url ...
	open $url
	exit 2
fi

url=""
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

echo downloading img:$url ...
curl -s -o $code.jpg $url

open $code.jpg

