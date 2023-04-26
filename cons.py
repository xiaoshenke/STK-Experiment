#!/usr/bin/python
# coding=utf-8

SERVER_PORT = 1234
PLAN_REPORTER_SERVER_PORT = 1222
SH_DOWNLOADER_SERVER_PORT = 1236
MANUAL_CODES_SERVER_PORT = 1235
MANUAL_BUYER_SERVER_PORT = 1237
MANUAL_PLANER_SERVER_PORT = 1238
OBSERVE_SCHEDULER_SERVER_PORT = 1240
MARKET_OBSERVER_SERVER_PORT = 1241
STOCK_SCHEDULER_SERVER_PORT = 1242
XLS_SCHEDULER_SERVER_PORT = 1243
CAOP_SCHEDULER_SERVER_PORT = 1245
XLS_TRACING_SERVER_PORT = 1246
POOL_OBSERVE_SERVER_PORT = 1251
LONGHU_OBSERVE_SERVER_PORT = 1252
MARKET_OBSERVE_SERVER_PORT = 1253
ZHZ500_OBSERVE_SERVER_PORT = 1254
HIGH_OBSERVE_SERVER_PORT = 1255
XLS_OBSERVE_SERVER_PORT = 1256
CODES_OBSERVE_SERVER_PORT = 1257
STOCKS_OBSERVE_SERVER_PORT = 1258
UPSTP_OBSERVE_SERVER_PORT = 1259
BIND_OBSERVE_SERVER_PORT = 1260
CHAOZUO_OBSERVE_SERVER_PORT = 1261
MLINE_OBSERVE_SERVER_PORT = 1262
BUYER_OBSERVE_SERVER_PORT = 1263
DIG_OBSERVE_SERVER_PORT = 1264
CHANGE_OBSERVE_SERVER_PORT = 1265
POOLS_OBSERVE_SERVER_PORT = 1266
DAPIAO_OBSERVE_SERVER_PORT = 1267
SHOUBAN_OBSERVE_SERVER_PORT = 1268
CHUANGYE_OBSERVE_SERVER_PORT = 1269
PROP_OBSERVE_SERVER_PORT = 1270
STYLE_OBSERVE_SERVER_PORT = 1271
TOPBTW_OBSERVE_SERVER_PORT = 1272
TOP_BTW_OBSERVE_SERVER_PORT = 1272

# @update_advisor对应的port
NODE_UPDATER_SERVER_PORT = 1281

# properties文件名称
REALTIME_PROPERTIES_FILE = 'realtime/realtime.properties'

USER = 'wuxian'

# 认为cpu issure的时间
CPU_ISSURE_TIME = 40.0

# 出龙虎榜的时间
LONGHUBANG_TIME = '16:35:00'

# 创业板涨跌幅限制
CHUANGYE_10_TO_20 = True

# derive算子暂时忽略创业板个股
FILTER_CHUANGYE = False

CUR_PATH="/Users/wuxian/Desktop/STK-Experiment"
CSV_PATH = "%s/data/csv_data/"%CUR_PATH
XLS_PATH = "%s/data/xls_data/"%CUR_PATH
STK_DAILY_PATH="/Users/wuxian/Desktop/stk_daily/"

# to run this, export PYTHONPATH=/Users/wuxian/Desktop/STK-Experiment:$PYTHONPATH
