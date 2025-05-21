#!/bin/bash

export PYTHONUNBUFFERED=1

echo 起pan observe.. python engine/observe/pan/cli.py start_engine_mode
nohup python engine/observe/pan/cli.py start_engine_mode >>observe.pan.log 2>&1 &

