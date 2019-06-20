#!/usr/bin/python
# coding=utf-8

CUR_PATH="/Users/wuxian/Desktop/STK-Experiment"

# 除了日内产生的csv的保存路径
CSV_PATH="%s/data/csv_data/"%CUR_PATH

# xls保存路径
XLS_PATH="%s/data/xls_data/"%CUR_PATH

# 每日生成的复盘文件路径
REPORT_PATH="%s/data/report/"%CUR_PATH

# ------------------------------- 下面是日内文件的保存路径 -----------------------

BASE_INN_PATH = "%s/data/inn/"%CUR_PATH

# inn.apply()返回的文件存储路径 
INN_APPLY="%s/apply/"%BASE_INN_PATH

# evaluater.evaluate()返回的文件存储路径 
INN_EVALUATE="%s/evaluate/"%BASE_INN_PATH

# 每日通过standby下载的所有文件路径
INN_FENSHI_CODES="%s/fenshi_wholecodes/"%BASE_INN_PATH

# 每日策略的filter source文件路径
INN_FILTER_SOURCE="%s/filter_source/"%BASE_INN_PATH

# 每日的运行日志保存路径
INN_RUNNING="%s/running/"%BASE_INN_PATH

# eventloop framework的df文件路径
INN_RUNNING_DAILY="%s/daily/"%INN_RUNNING

# -----------------

# 暂时没有被使用
TOOL_PATH="%s/data/tool/"%CUR_PATH

# 暂时没有被使用
INDEX_PATH="%s/data/csv_data/index/"%CUR_PATH

# to run this, export PYTHONPATH=/Users/wuxian/Desktop/STK-Experiment:$PYTHONPATH
