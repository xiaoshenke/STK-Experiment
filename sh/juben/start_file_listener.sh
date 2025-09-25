#!/bin/bash

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/juben/cli.py start_juben_file_listener
nohup python engine/observe/juben/cli.py start_juben_file_listener >>juben_file_change.log 2>&1 &
