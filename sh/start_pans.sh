#!/bin/bash

# Usage: sh/start_pans.sh [mode]

export PYTHONUNBUFFERED=1

mode='download'
if [ $# -eq 1 ]
then
	mode=$1
fi

if [[ $mode == "download" ]]
then
	echo "仅起一些下载相关的组件,standby,node updater,xls tracing"

	echo nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false 
	nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false >>standby.log 2>&1 &

	echo nohup python engine/advise/node/cli.py start_node_engine_mode update
	# 轻量级运行default advisor(下载热门版块数据) 
	nohup python engine/advise/node/cli.py start_node_engine_mode update >>node.log 2>&1 &

	# 轻量级运行xls stage tracing
	echo nohup python engine/tracing/xls/cli.py start_tracing_engine_mode
	nohup python engine/tracing/xls/cli.py start_tracing_engine_mode >>tracing.log 2>&1 &

	echo 起reporter server sh/start_reporter_server.sh
	sh/start_reporter_server.sh 

	echo 起index observe sh/start_index_observe.sh 
	sh/start_index_observe.sh
 
elif [[ $mode == "light" ]]
then
	echo "[轻量级模式]:依次起standby,node updater,xls tracing,market tracing,style observe,change observe."

	echo nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false 
	nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false >>standby.log 2>&1 &

	echo nohup python engine/advise/node/cli.py start_node_engine_mode update
	# 轻量级运行default advisor(下载热门版块数据) 
	nohup python engine/advise/node/cli.py start_node_engine_mode update >>node.log 2>&1 &

	# 轻量级运行xls stage tracing
	echo nohup python engine/tracing/xls/cli.py start_tracing_engine_mode
	nohup python engine/tracing/xls/cli.py start_tracing_engine_mode >>tracing.log 2>&1 &

	# 轻量级运行market stage tracing
	echo nohup python engine/tracing/market/cli.py start_tracing_engine_mode
	nohup python engine/tracing/market/cli.py start_tracing_engine_mode >>tracing.market.log 2>&1 &

	# 轻量级运行style observe
	echo nohup python engine/observe/style/cli.py start_engine_mode
	nohup python engine/observe/style/cli.py start_engine_mode --mimic_open true >>observe.style.log 2>&1 &

	echo nohup python engine/observe/mao/cli.py start_engine_mode
	nohup python engine/observe/mao/cli.py start_engine_mode --mimic_open false >>observe.mao.log 2>&1 &

	echo python engine/observe/change/cli.py start_engine_mode
	nohup python engine/observe/change/cli.py start_engine_mode --running_mode light --mimic_open true >>observe.change.log 2>&1 &

elif [[ $mode == "default" ]]
then
	echo "依次起standby,node updater,xls tracing,market tracing,change observe,mline observe"

	nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false >>standby.log 2>&1 &

	# 轻量级运行default advisor(下载热门版块数据) 
	nohup python engine/advise/node/cli.py start_node_engine_mode update >>node.log 2>&1 &

	# 轻量级运行xls stage tracing
	nohup python engine/tracing/xls/cli.py start_tracing_engine_mode >>tracing.log 2>&1 &

	# 轻量级运行market stage tracing
	nohup python engine/tracing/market/cli.py start_tracing_engine_mode >>tracing.market.log 2>&1 &

	nohup python engine/observe/change/cli.py start_engine_mode >>observe.change.log 2>&1 &

	nohup python engine/observe/mline/cli.py start_engine_mode >>observe.mline.log 2>&1 &

	#nohup python engine/observe/xls/cli.py start_engine_mode >>observe.xls.log 2>&1 &

	nohup python engine/observe/longhu/cli.py start_engine_mode --mimic_open true >>observe.longhu.log 2>&1 &

	nohup python engine/observe/chaozuo/cli.py start_engine_mode >>observe.chaozuo.log 2>&1 &

	nohup python engine/observe/chuangye/cli.py start_engine_mode >>observe.chuangye.log 2>&1 &

	nohup python engine/observe/pools/cli.py start_engine_mode >>observe.pools.log 2>&1 &

	nohup python engine/scheduler/buyer/cli.py start_engine_mode >>scheduler.buyer.log 2>&1 &
	
	nohup python engine/observe/style/cli.py start_engine_mode >>observe.style.log 2>&1 &

	nohup python engine/observe/top_btw/cli.py start_engine_mode >>observe.top_btw.log 2>&1 &
else
        echo 不支持$mode
fi


