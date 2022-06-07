#!/bin/bash

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

nohup python engine/observe/xls/cli.py start_engine_mode >>observe.xls.log 2>&1 &

nohup python engine/observe/chaozuo/cli.py start_engine_mode >>observe.chaozuo.log 2>&1 &
