#!/bin/bash

export PYTHONUNBUFFERED=1

echo python engine/observe/code_types/cli.py start_engine_mode
nohup python engine/observe/code_types/cli.py start_engine_mode >>observe.code_types.log 2>&1 &

