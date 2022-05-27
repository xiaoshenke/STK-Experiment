#!/bin/bash

nohup python inn_strategy/standby_cli.py schedule_standby_and_merge2 --enable_merger false >>standby.log 2>&1 &
nohup python engine/advise/node/cli.py start_node_engine_mode update >>node.log 2>&1 &
nohup python engine/tracing/xls/cli.py start_tracing_engine_mode >>tracing.log 2>&1 &
nohup python engine/tracing/market/cli.py start_tracing_engine_mode >>tracing.market.log 2>&1 &

