#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

export PYTHONUNBUFFERED=1

echo nohup python engine/report/plan/flush/report_flusher.py 

nohup python engine/report/plan/flush/report_flusher.py >>report_flusher.log 2>&1 &
