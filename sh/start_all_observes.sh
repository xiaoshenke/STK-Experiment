#!/bin/bash

nohup python engine/observe/market/cli.py start_engine_mode >>observe.market.log 2>&1 &
nohup python engine/observe/upstp/cli.py start_engine_mode >>observe.upstp.log 2>&1 &
nohup python engine/observe/dig/cli.py start_engine_mode >>observe.dig.log 2>&1 &

nohup python engine/observe/xls/cli.py start_engine_mode >>observe.xls.log 2>&1 &
nohup python engine/observe/mline/cli.py start_engine_mode >>observe.mline.log 2>&1 &
nohup python engine/observe/bind/cli.py start_engine_mode >>observe.bind.log 2>&1 &

nohup python engine/observe/chaozuo/cli.py start_engine_mode >>observe.chaozuo.log 2>&1 &
nohup python engine/observe/stocks/cli.py start_engine_mode >>observe.stocks.log 2>&1 &

nohup python engine/observe/zhz500/cli.py start_engine_mode >>observe.zhz500.log 2>&1 &
nohup python engine/observe/longhu/cli.py start_engine_mode >>observe.longhu.log 2>&1 &
nohup python engine/observe/high/cli.py start_engine_mode >>observe.high.log 2>&1 &

