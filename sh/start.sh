#!/bin/bash

# WSL: when scheduled by crontab,must specify PYTHONPATH
export PYTHONPATH=/home/xiaoshenke100/STK-Experiment:$PYTHONPATH

echo start standby...
# WSL: when scheduled by crontab,must specify >>nohup.out,otherwise no log
nohup /usr/bin/python inn_strategy/standby_cli.py schedule-standby-and-merge >>nohup.out 2>&1 &

echo start engine...
nohup /usr/bin/python engine/cli.py start-engine >>nohup.out 2>&1 &

