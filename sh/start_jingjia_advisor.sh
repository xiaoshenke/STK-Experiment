#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/advise/node/cli.py start_jingjia_engine_mode >>node.log 2>&1 &
nohup python engine/advise/node/cli.py start_jingjia_engine_mode >>node.log 2>&1 &
