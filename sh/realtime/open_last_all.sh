#!/bin/bash
# usage sh/open_last_all.sh [-key xyz] [-day aaaa-bb-cc] [-time_str xx:yy:zz] [type]

day=`date +'%Y-%m-%d'`
time_str=`date +'%H:%M:%S'`
time_str='#'
key=#
type=''
mode='now'
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
	-mode | --mode)
		shift
		mode=$1
		;;
	-key | --key)
		shift
		key=$1
		;;
	-help | --help)
		echo usage sh/open_last_all.sh [-key xyz] [-day aaaa-bb-cc] [-time_str xx:yy:zz] [type]
		exit 1
		;;
	*)
		#break
		type=$1
		;;
	esac
	shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo 当前支持的type为chaozuo,market,pool,default,dapiao,style

if [[ $type == "chaozuo" ]]
then
	echo python realtime/observe/longhu.py open_last
	python realtime/observe/longhu.py open_last --day $day --time_str $time_str

	echo python realtime/observe/high.py open_last
	python realtime/observe/high.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/chaozuo.py open_last
	python realtime/observe/chaozuo.py open_last --day $day --time_str $time_str
elif [[ $type == "qingxu" ]]
then
	echo python realtime/observe/market.py open_last
	python realtime/observe/market.py open_last --day $day --time_str $time_str 

	echo python realtime/observe/mao.py open_last
	python realtime/observe/mao.py open_last --day $day --time_str $time_str

elif [[ $type == "pan" ]]
then
	echo python realtime/observe/upstp.py open_last --day $day --time_str $time_str
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str

	echo python realtime/observe/code_types.py open_last --day $day --time_str $time_str
	python realtime/observe/code_types.py open_last --day $day --time_str $time_str

	echo python realtime/observe/change.py open_last --day $day --time_str $time_str
	python realtime/observe/change.py open_last --day $day --time_str $time_str

	echo python realtime/observe/index.py open_last --day $day --time_str $time_str
	python realtime/observe/index.py open_last --day $day --time_str $time_str

	echo python realtime/observe/pan.py open_last --day $day --time_str $time_str
	python realtime/observe/pan.py open_last --day $day --time_str $time_str


elif [[ $type == "jingjia" ]] || [[ $type == "jj" ]]
then
	echo python realtime/observe/jingjia.py open_last
	python realtime/observe/jingjia.py open_last --day $day --time_str $time_str --mode $mode

elif [[ $type == "chaoduan" ]]
then
	echo python realtime/observe/chaoduan.py open_last
	python realtime/observe/chaoduan.py open_last --day $day --time_str $time_str 
elif [[ $type == "high" ]]
then
	echo python realtime/observe/high.py open_last
	python realtime/observe/high.py open_last --day $day --time_str $time_str --check_expire True
elif [[ $type == "style" ]]
then
	echo python realtime/observe/style.py open_last
	python realtime/observe/style.py open_last --day $day --time_str $time_str --check_expire True
elif [[ $type == "mao" ]]
then
	echo python realtime/observe/mao.py open_last
	python realtime/observe/mao.py open_last --day $day --time_str $time_str
elif [[ $type == "code_types" ]] || [[ $type == "code-types" ]] || [[ $type == "codetypes" ]]
then
	echo python realtime/observe/code_types.py open_last --mode $mode
	python realtime/observe/code_types.py open_last --day $day --time_str $time_str --mode $mode

elif [[ $type == "top_btw" ]]
then
	echo python realtime/observe/top_btw.py open_last
	python realtime/observe/top_btw.py open_last --day $day --time_str $time_str 
elif [[ $type == "shouban" ]]
then
	echo python realtime/observe/shouban.py open_last
	python realtime/observe/shouban.py open_last --day $day --time_str $time_str --check_expire True
elif [[ $type == "zhz500" ]]
then
	echo python realtime/observe/zhz500.py open_last
	python realtime/observe/zhz500.py open_last --day $day --time_str $time_str --check_expire True
elif [[ $type == "300" ]] || [[ $type == 'chuangye' ]]
then
	echo python realtime/observe/300.py open_last
	python realtime/observe/300.py open_last --day $day --time_str $time_str --check_expire True
elif [[ $type == "xls" ]]
then
	echo python realtime/observe/xls.py open_last
	python realtime/observe/xls.py open_last --day $day --time_str $time_str
elif [[ $type == "buyer" ]] || [[ $type == "buy" ]]
then
	#echo python realtime/buyer/observe_cli.py open_last
	#python realtime/buyer/observe_cli.py open_last --day $day --time_str $time_str
	echo python realtime/observe/buyer.py open_last
	python realtime/observe/buyer.py open_last --day $day --time_str $time_str

elif [[ $type == "index" ]]
then
	echo python realtime/observe/index.py open_last 
	python realtime/observe/index.py open_last --day $day --time_str $time_str --mode $mode

elif [[ $type == "stocks" ]]
then
	echo python realtime/observe/stocks.py open_last
	python realtime/observe/stocks.py open_last --day $day --time_str $time_str
elif [[ $type == "longhu" ]]
then
	echo python realtime/observe/longhu.py open_last
	python realtime/observe/longhu.py open_last --day $day --time_str $time_str

elif [[ $type == "dapiao" ]]
then
	echo python realtime/observe/zhz500.py open_last
	python realtime/observe/zhz500.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/dapiao.py open_last
	python realtime/observe/dapiao.py open_last --day $day --time_str $time_str  --check_expire True
elif [[ $type == "mline" ]]
then
	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str

	echo python realtime/observe/mline.py open_last
	python realtime/observe/mline.py open_last --day $day --time_str $time_str
elif [[ $type == "pools" ]]
then
	echo python realtime/observe/pools.py open_last --mode $mode
	python realtime/observe/pools.py open_last --day $day --time_str $time_str --key $key --mode $mode

elif [[ $type == "pool" ]]
then
	echo python realtime/observe/mao.py open_last --mode $mode
	python realtime/observe/mao.py open_last --day $day --time_str $time_str --mode $mode

	echo python realtime/observe/style.py open_last
	python realtime/observe/style.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/upstp.py open_last --mode $mode
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str --check_expire True --key $key --mode $mode

	echo python realtime/observe/bind.py open_last
	python realtime/observe/bind.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/mline.py open_last
	python realtime/observe/mline.py open_last --day $day --time_str $time_str --key $key

	echo python realtime/observe/pools.py open_last --mode $mode
	python realtime/observe/pools.py open_last --day $day --time_str $time_str --key $key --mode $mode

	echo python realtime/observe/change.py open_last --mode $mode
	python realtime/observe/change.py open_last --day $day --time_str $time_str --key $key --mode $mode

	echo python realtime/observe/top_btw.py open_last
	python realtime/observe/top_btw.py open_last --day $day --time_str $time_str --key $key

	echo python realtime/observe/chaoduan.py open_last
	python realtime/observe/chaoduan.py open_last --day $day --time_str $time_str 

	echo python realtime/observe/code_types.py open_last --mode $mode
	python realtime/observe/code_types.py open_last --day $day --time_str $time_str --check_expire True --mode $mode

elif [[ $type == "change" ]]
then
	echo python realtime/observe/change.py open_last --mode $mode
	python realtime/observe/change.py open_last --day $day --time_str $time_str --mode $mode

elif [[ $type == "bind" ]]
then
	echo python realtime/observe/longhu.py open_last
	python realtime/observe/longhu.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/bind.py open_last
	python realtime/observe/bind.py open_last --day $day --time_str $time_str
elif [[ $type == "upstp" ]]
then
	echo python realtime/observe/upstp.py open_last --mode $mode
	python realtime/observe/upstp.py open_last --day $day --time_str $time_str --check_expire True --mode $mode

elif [[ $type == "market" ]]
then
	echo python realtime/observe/market.py open_last
	python realtime/observe/market.py open_last --day $day --time_str $time_str --check_expire True

	echo python realtime/observe/change.py open_last
	python realtime/observe/change.py open_last --day $day --time_str $time_str
	
	echo python realtime/observe/style.py open_last
	python realtime/observe/style.py open_last --day $day --time_str $time_str --check_expire True

elif [[ $type == "default" ]]
then
	echo python realtime/observe/market.py open_last
	python realtime/observe/market.py open_last --day $day --time_str $time_str
	
	echo python realtime/observe/style.py open_last
	python realtime/observe/style.py open_last --day $day --time_str $time_str --check_expire True

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
	echo 不支持$type
fi
