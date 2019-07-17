#!/bin/bash

# WSL: when scheduled by crontab,must specify PYTHONPATH
export PYTHONPATH=/home/xiaoshenke100/STK-Experiment:$PYTHONPATH

cd /home/xiaoshenke100
source env1/bin/activate
cd /home/xiaoshenke100/STK-Experiment

echo start standby...
# WSL: when scheduled by crontab,must specify >>nohup.out,otherwise no log
nohup python inn_strategy/standby_cli.py schedule-standby-and-merge >>nohup.out 2>&1 &

echo start engine...
nohup python engine/cli.py start-engine >>nohup.out 2>&1 &

