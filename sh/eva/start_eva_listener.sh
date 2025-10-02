#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/oeva/cli.py start_engine_mode --only_listener 1 log:observe.eva.log
nohup python engine/observe/oeva/cli.py start_engine_mode --test 1 --only_listener 1 --check_config_file 0 >>observe.eva.log 2>&1 &
