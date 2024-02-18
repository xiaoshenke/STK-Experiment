#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/jingjia/cli.py start_engine_mode --mimic_open 0

nohup python engine/observe/jingjia/cli.py start_engine_mode --mimic_open 0 >>observe.jingjia.log 2>&1 &

