#!/bin/bash

echo 起flush-code-types... sh/start_code_types_observe.sh --mode pan
sh/start_code_types_observe.sh --mode pan

echo 起buyer scheduler... sh/start_buyer_scheduler.sh --mode pan
sh/start_buyer_scheduler.sh --mode pan

echo 起pan observe.. python engine/observe/pan/cli.py start_engine_mode
nohup python engine/observe/pan/cli.py start_engine_mode >>observe.pan.log 2>&1 &

echo 起xls observe.. python engine/observe/xls/cli.py start_engine_mode
nohup python engine/observe/xls/cli.py start_engine_mode >>observe.xls.log 2>&1 &

