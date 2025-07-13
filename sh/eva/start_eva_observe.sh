#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/oeva/cli.py start_engine_mode
nohup python engine/observe/oeva/cli.py start_engine_mode --test 1 --check_config_file 0 >>observe.eva.log 2>&1 &
