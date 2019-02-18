#!/usr/bin/python
# coding=utf-8

CUR_PATH="/Users/wuxian/Desktop/STK-Experiment"
CSV_PATH="%s/data/csv_data/"%CUR_PATH
XLS_PATH="%s/data/xls_data/"%CUR_PATH
TOOL_PATH="%s/data/tool/"%CUR_PATH
REPORT_PATH="%s/data/report/"%CUR_PATH

INDEX_PATH="%s/data/csv_data/index/"%CUR_PATH

# inn.apply()返回的文件存储路径 -> 当前的功能其实..是下载远程文件
INN_APPLY="%s/data/inn/apply/"%CUR_PATH

# evaluater.evaluate()返回的文件存储路径 -> 实际的计算结果落地(其实没啥用,并不觉得需要存储->因为已经有了上面的下载文件,复盘的时候重新算就好了)
INN_EVALUATE="%s/data/inn/evaluate/"%CUR_PATH

# 每日的运行日志以及ignore codes(当前并没有启用)
INN_RUNNING="%s/data/inn/running/"%CUR_PATH

# 每日通过standby下载的所有文件路径
INN_FENSHI_CODES="%s/data/inn/fenshi_wholecodes/"%CUR_PATH

# 每日策略的filter source文件路径
INN_FILTER_SOURCE="%s/data/inn/filter_source/"%CUR_PATH

DEBUG_PATH="%s/data/debug/"%CUR_PATH

STRA_DATA_PATH="%s/data/strategy/"%CUR_PATH

# to run this, export PYTHONPATH=/Users/wuxian/Desktop/STK-Experiment:$PYTHONPATH

