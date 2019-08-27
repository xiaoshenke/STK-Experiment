#!/bin/bash

export PYTHONPATH=/home/xiaoshenke100/STK-Experiment:$PYTHONPATH

#cd /home/xiaoshenke100
#source env1/bin/activate
#cd /home/xiaoshenke100/STK-Experiment

echo generate report...
nohup python report/daily_generator.py >>nohup.out 2>&1 &

