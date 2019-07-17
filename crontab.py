#!/usr/bin/python
# coding=utf-8

# start engine
15 9 * * *  cd /home/xiaoshenke100/STK-Experiment && /bin/bash sh/start.sh
# stop engine
9 15 * * * cd /home/xiaoshenke100/STK-Experiment && /bin/bash sh/stop.sh
# generate report
11 15 * * * cd /home/xiaoshenke100/STK-Experiment && /bin/bash sh/gene_report.sh

