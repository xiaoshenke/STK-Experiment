#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/juben/cli.py start_engine_mode log:observe.juben.log
nohup python engine/observe/juben/cli.py start_engine_mode --check_config_file 0 >>observe.juben.log 2>&1 &
