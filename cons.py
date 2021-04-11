#!/usr/bin/python
# coding=utf-8

SERVER_PORT = 1234
SH_DOWNLOADER_SERVER_PORT = 1236
MANUAL_CODES_SERVER_PORT = 1235
MANUAL_BUYER_SERVER_PORT = 1237
MANUAL_PLANER_SERVER_PORT = 1238
PLAN_REPORTER_SERVER_PORT = 1239
OBSERVE_SCHEDULER_SERVER_PORT = 1240

# 创业板涨跌幅限制
CHUANGYE_10_TO_20 = True

# derive算子暂时忽略创业板个股
FILTER_CHUANGYE = False

CUR_PATH="/Users/wuxian/Desktop/STK-Experiment"
CSV_PATH = "%s/data/csv_data/"%CUR_PATH
XLS_PATH = "%s/data/xls_data/"%CUR_PATH
STK_DAILY_PATH="/Users/wuxian/Desktop/stk_daily/"

# to run this, export PYTHONPATH=/Users/wuxian/Desktop/STK-Experiment:$PYTHONPATH
