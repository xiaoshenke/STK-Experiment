#!/usr/bin/python
# coding=utf-8
from util.time_util import today
from util.dir_util import get_daily_dir,init_dirs
init_dirs()

import logging, sys, os
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,filemode='a')
logger = logging.getLogger('stock')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger.setLevel(logging.DEBUG)

def get_daily_flogger(day):
        _logger = logging.getLogger('fstock')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),day))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger

def get_daily_eva_cli_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('eva_cli')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'eva_cli'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger

ecli_logger = get_daily_eva_cli_logger()

f_logger = None
def update_flogger(day=''):
    day = day if day else str(today())
    global f_logger
    init_dirs(day)
    f_logger = get_daily_flogger(day)

# 当日期变化的时候,调一下这个函数
update_flogger()

INN_EVA_LOG_NAME="inn_eva"

INN_CAL_SCHEDULE = "cal_schedule"

INN_DOWNLOADER_NAME="inn_downloader"

INN_SERVER = "inn_server"

INN_CODES_BUILDER = "codes_builder"

INN_CODES_MERGER = "codes_merger"

INN_PRESCHEDULER = "prescheduler"

INN_MARKET = 'market'

INN_RAPID_UP_TRACING = 'rapid_up_tracing'

INN_XLS_DOWNLOADER = 'xls_downloader'

INN_LAST_TOP = 'last_top'

INN_UPSTP_HOT = 'upstp_hot'
