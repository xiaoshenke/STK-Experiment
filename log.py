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

market_stage_logger = get_common_daily_logger('market_stage','market_stage')

# cal manager日志,记录了cal manager处理的所有event
cal_manager_report_logger = get_common_daily_logger('cal_manager_report','cal_manager_report')

# 单次file刷新时的算子组日志,记录了实际上cal manager所有发生的计算
cals_report_logger = get_common_daily_logger('cals_report','cals_report')

# 单次file刷新时,这个file对应的股票池数据的表现,当前主要是涨停表现
cal_file_codes_report_logger = get_common_daily_logger('file_codes_report','file_codes_report')

# cal manager计算出来过的历史结果股票数据的表现,当前主要是涨停表现
cal_hist_codes_report_logger = get_common_daily_logger('cal_hist_report','hist_codes_report')

# hit.xls_stage.hit_all_xls的盘面全版块信息,当前主要是涨停表现
all_xls_logger = get_common_daily_logger('all_xls','all_xls')

# xls dfastr tracing的日志
xls_dfastr_tracing_logger = get_common_daily_logger('xls_dfastr','xls_dfastr')

# 单次file刷新时的算子组中的stage-数据,用于挖掘优秀个股买点
stage_minus_logger = get_common_daily_logger('stage_minus','stage-')

# hot xls的log,实质当前是被我用来做hit算子HIT_XLS_EFFECT_NORMAL_1记录操作用的
hot_xls_logger = get_common_daily_logger('hot_xls','hot_xls')

# hit process的日志
hprocesser_logger = get_common_daily_logger('hit_processer','hit_processer')

# codes merger日志
codes_merger_logger = get_common_daily_logger('codes_merger','codes_merger')

# market configer日志
mkt_configer_logger = get_common_daily_logger('market_configer','market_configer')

# dyna scheduler日志
dyna_scheduler_logger = get_common_daily_logger('dyna_scheduler','dyna_scheduler')

# xls scheduler调度日志
xls_scheduler_logger = get_common_daily_logger('xls_scheduler','xls_scheduler')

# shape scheduler调度日志
shape_scheduler_logger = get_common_daily_logger('shape_scheduler','shape_scheduler')

# open2 scheduler调度日志
open2_scheduler_logger = get_common_daily_logger('open2_scheduler','open2_scheduler')

# opening_xls scheduler调度日志
opening_xls_scheduler_logger = get_common_daily_logger('opening_xls','opening_xls')

# scheduler reporter日志
scheduler_reporter_logger = get_common_daily_logger('scheduler_reporter','scheduler_reporter')

# realtime_reporter日志
realtime_reporter_logger = get_common_daily_logger('realtime_reporter','realtime_reporter')

# manual_reporter日志
manual_reporter_logger = get_common_daily_logger('manual_reporter','manual_reporter')

# shape reporter日志
shape_reporter_logger = get_common_daily_logger('shape_reporter','shape_reporter')

# cli操作日志
cli_logger = get_common_daily_logger('cli','cli')

def log_slow(msg):
	try:
		slow_logger = get_common_daily_logger('slow','slow')
		slow_logger.warn(str(msg))
	except Exception,e:
		print "log_slow"
		print e

error_logger = get_common_daily_logger('error','error')
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

INN_PRESCHEDULER = "prescheduler"

INN_MARKET = 'market'

INN_RAPID_UP_TRACING = 'rapid_up_tracing'

INN_XLS_DOWNLOADER = 'xls_downloader'

INN_LAST_TOP = 'last_top'

INN_UPSTP_HOT = 'upstp_hot'

INN_RAPID_XLS = 'rapid_xls'

CAL_INTEGRATION = 'cal_integration'
