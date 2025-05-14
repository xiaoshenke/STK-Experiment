#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/buyer/cli.py start_engine_mode
nohup python engine/observe/buyer/cli.py start_engine_mode >>observe.buyer.log 2>&1 &
