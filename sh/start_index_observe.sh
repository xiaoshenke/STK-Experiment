#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/index/cli.py start_engine_mode 

nohup python engine/observe/index/cli.py start_engine_mode >>observe.index.log 2>&1 &

