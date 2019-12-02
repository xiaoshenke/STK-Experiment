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

def get_common_daily_logger(appender,save_name,day=''):
	day = day if day else str(today())
        _logger = logging.getLogger(appender)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        fh = logging.FileHandler("%s%s.log"%(get_daily_dir(day),save_name))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        _logger.handlers = []
        _logger.addHandler(fh)
        _logger.setLevel(logging.DEBUG)
        return _logger

# cal manager日志,记录了cal manager处理的所有event
cal_manager_report_logger = get_common_daily_logger('cal_manager_report','cal_manager_report')

# 单次file刷新时的算子组日志,记录了实际上cal manager所有发生的计算
cals_report_logger = get_common_daily_logger('cals_report','cals_report')

# 单次file刷新时,这个file对应的股票池数据的表现,当前主要是涨停表现
cal_file_codes_report_logger = get_common_daily_logger('file_codes_report','file_codes_report')

# cal manager计算出来过的历史结果股票数据的表现,当前主要是涨停表现
cal_hist_codes_report_logger = get_common_daily_logger('cal_hist_report','hist_codes_report')

# 单次file刷新时的算子组中的stage-数据,用于挖掘优秀个股买点
stage_minus_logger = get_common_daily_logger('stage_minus','stage-')

# hit process的日志
hprocesser_logger = get_common_daily_logger('hit_processer','hit_processer')

ecli_logger = get_common_daily_logger('eva_cli','eva_cli')
schcli_logger = get_common_daily_logger('sch_cli','cal_scheduler_cli')
slow_logger = get_common_daily_logger('slow','slow')
error_logger = get_common_daily_logger('error','error')

def log_slow(msg):
	try:
		slow_logger.warn(str(msg))
	except Exception,e:
		print "log_slow"
		print e

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

INN_CAL_MANAGER = 'cal_manager'

INN_DYNA_SCHEDULR = 'dyna_scheduler'

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

CAL_INTEGRATION = 'cal_integration'
