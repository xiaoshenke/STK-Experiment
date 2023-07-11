#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/scheduler/buyer/cli.py start_engine_mode >>scheduler.buyer.log 2>&1 &
nohup python engine/scheduler/buyer/cli.py start_engine_mode --debug 0 >>scheduler.buyer.log 2>&1 &

