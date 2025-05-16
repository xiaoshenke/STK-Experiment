#!/bin/bash

export PYTHONUNBUFFERED=1

echo 起flush-code-types... 

echo python engine/observe/code_types/cli.py start_engine_mode --mode pull
nohup python engine/observe/code_types/cli.py start_engine_mode --mode pull >>observe.pull.log 2>&1 &
