#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/buyer/cli.py start_engine_mode
nohup python engine/observe/buyer/cli.py start_engine_mode --check_config_file 0 >>observe.juben.log 2>&1 &
