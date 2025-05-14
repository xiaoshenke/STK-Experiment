#!/bin/bash

export PYTHONUNBUFFERED=1

echo 起数据下载器... sh/start_jingjia_advisor.sh
sh/start_jingjia_advisor.sh

echo 起观察组件... sh/start_jingjia_observe.sh
sh/observe/start_jingjia_observe.sh

echo 起buyer scheduler... sh/start_buyer_scheduler.sh
sh/start_buyer_scheduler.sh 

echo 起standby nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false 
nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false >>standby.log 2>&1 &

echo 起reporter server.. sh/start_reporter_server.sh
sh/start_reporter_server.sh

echo nohup python engine/observe/index/cli.py start_engine_mode 
nohup python engine/observe/index/cli.py start_engine_mode >>observe.index.log 2>&1 &

echo nohup python engine/observe/buyer/cli.py start_engine_mode
nohup python engine/observe/buyer/cli.py start_engine_mode >>observe.buyer.log 2>&1 &
