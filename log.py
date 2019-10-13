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

def get_daily_hit_processer_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('hit_processer')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'hit_processer'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger

hprocesser_logger = get_daily_hit_processer_logger()


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

def get_daily_prescheduler_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('prescheduler')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'prescheduler'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger
presch_logger = get_daily_prescheduler_logger()

def get_daily_cal_scheduler_cli_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('sch_cli')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'cal_scheduler_cli'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger
schcli_logger = get_daily_cal_scheduler_cli_logger()

def get_daily_slow_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('slow')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'slow'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger
slow_logger = get_daily_slow_logger()

def log_slow(msg):
	try:
		slow_logger.warn(str(msg))
	except Exception,e:
		print "log_slow"
		print e

def get_daily_error_logger(day=''):
	day = day if day else str(today())
        _logger = logging.getLogger('error')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        # 配置文件路径
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),'error'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger
error_logger = get_daily_error_logger()

def save_error(msg):
	try:
		error_logger.error(str(msg))
	except Exception,e:
		pass

f_logger = None
def update_flogger(day=''):
    day = day if day else str(today())
    global f_logger
    init_dirs(day)
    f_logger = get_daily_flogger(day)

# 当日期变化的时候,调一下这个函数
update_flogger()

HIT_PROCESSER = 'hit_processer'

HIT_HOT_XLS = 'hit_hot_xls'

INN_EVA_LOG_NAME="inn_eva"

INN_TYPE_GROUPED_EVA = 'type_grouped_eva'

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

INN_RAPID_XLS = 'rapid_xls'
