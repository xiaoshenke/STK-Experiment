#!/bin/bash
# usage sh/open_last_all.sh [-day aaaa-bb-cc] [-time_str xx:yy:zz] [mode]

day=`date +'%Y-%m-%d'`
time_str=`date +'%H:%M:%S'`
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	*)
		break
		;;
	esac
	shift
done

mode=''
if [ $# -eq 1 ]
then
	mode=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo 当前支持的mode为chaozuo,market,pool,default,dapiao

if [[ $mode == "chaozuo" ]]
then
	echo python realtime/observe/high.py open_last
	python realtime/observe/high.py open_last --day $day --time_str $time_str

	echo python realtime/observe/chaozuo.py open_last
	python realtime/observe/chaozuo.py open_last --day $day --time_str $time_str
elif [[ $mode == "high" ]]
then
	echo python realtime/observe/high.py open_last
	python realtime/observe/high.py open_last --day $day --time_str $time_str
elif [[ $mode == "xls" ]]
then
	echo python realtime/observe/xls.py open_last
	python realtime/observe/xls.py open_last --day $day --time_str $time_str
elif [[ $mode == "buyer" ]] || [[ $mode == "buy" ]]
then
	echo python realtime/buyer/observe_cli.py open_last
	python realtime/buyer/observe_cli.py open_last --day $day --time_str $time_str
elif [[ $mode == "stocks" ]]
then
	echo python realtime/observe/stocks.py open_last
	python realtime/observe/stocks.py open_last --day $day --time_str $time_str
elif [[ $mode == "longhu" ]]
then
	echo python realtime/observe/longhu.py open_last
	python realtime/observe/longhu.py open_last --day $day --time_str $time_str

elif [[ $mode == "dapiao" ]]
then
	echo python realtime/observe/stocks.py open_last
	python realtime/observe/stocks.py open_last --day $day --time_str $time_str

	echo python realtime/observe/zhz500.py open_last
	python realtime/observe/zhz500.py open_last --day $day --time_str $time_str

	echo python realtime/observe/dapiao.py open_last
	python realtime/observe/dapiao.py open_last --day $day --time_str $time_str
elif [[ $mode == "mline" ]]
then
	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str

	echo python realtime/observe/mline.py open_last
	python realtime/observe/mline.py open_last --day $day --time_str $time_str
elif [[ $mode == "pools" ]]
then
	echo python realtime/observe/pools.py open_last
	python realtime/observe/pools.py open_last --day $day --time_str $time_str
elif [[ $mode == "pool" ]]
then
	echo python realtime/observe/upstp.py open_last
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str

	echo python realtime/observe/bind.py open_last
	python realtime/observe/bind.py open_last --day $day --time_str $time_str

	echo python realtime/observe/mline.py open_last
	python realtime/observe/mline.py open_last --day $day --time_str $time_str

	echo python realtime/observe/pools.py open_last
	python realtime/observe/pools.py open_last --day $day --time_str $time_str

	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str
elif [[ $mode == "change" ]]
then
	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str
elif [[ $mode == "bind" ]]
then
	echo python realtime/observe/longhu.py open_last
	python realtime/observe/longhu.py open_last --day $day --time_str $time_str

	echo python realtime/observe/bind.py open_last
	python realtime/observe/bind.py open_last --day $day --time_str $time_str
elif [[ $mode == "upstp" ]]
then
	echo python realtime/observe/upstp.py open_last
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str
elif [[ $mode == "market" ]]
then
	echo python realtime/observe/stocks.py open_last
	python realtime/observe/stocks.py open_last --day $day --time_str $time_str

	echo python realtime/observe/market.py open_last
	python realtime/observe/market.py open_last --day $day --time_str $time_str

	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str

elif [[ $mode == "default" ]]
then
	echo python realtime/observe/market.py open_last
	python realtime/observe/market.py open_last --day $day --time_str $time_str

	echo python realtime/observe/stocks.py open_last
	python realtime/observe/stocks.py open_last --day $day --time_str $time_str

	#echo python realtime/observe/longhu.py open_last
	#python realtime/observe/longhu.py open_last --day $day --time_str $time_str

	#echo python realtime/observe/chaozuo.py open_last
	#python realtime/observe/chaozuo.py open_last --day $day --time_str $time_str

	#echo python realtime/observe/pool.py open_last
	#python realtime/observe/pool.py open_last --day $day --time_str $time_str

	echo python realtime/observe/upstp.py open_last
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str

	echo python realtime/observe/bind.py open_last
	python realtime/observe/bind.py open_last --day $day --time_str $time_str

	echo python realtime/observe/xls.py open_last
	python realtime/observe/xls.py open_last --day $day --time_str $time_str

	echo python realtime/observe/mline.py open_last
	python realtime/observe/mline.py open_last --day $day --time_str $time_str

	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str

	echo python realtime/observe/pools.py open_last
	python realtime/observe/pools.py open_last --day $day --time_str $time_str

	echo python realtime/observe/dig.py open_last
	python realtime/observe/dig.py open_last --day $day --time_str $time_str

	#echo python realtime/buyer/observe_cli.py open_last
	#python realtime/buyer/observe_cli.py open_last --day $day --time_str $time_str
else
	echo 不支持$mode
fi
