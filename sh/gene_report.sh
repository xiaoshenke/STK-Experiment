#!/bin/bash

export PYTHONPATH=/home/xiaoshenke100/STK-Experiment:$PYTHONPATH

echo generate report...
nohup /usr/bin/python report/daily_generator.py >>nohup.out 2>&1 &

