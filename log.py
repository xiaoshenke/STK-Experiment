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

# 用于临时作用
tmp_logger = get_common_daily_logger('tmp','tmp')

# event logger
event_logger = get_common_daily_logger('event','event')

# observer-xls 日志
observer_xls_logger = get_common_daily_logger('observer_xls','observer_xls')

# xls-tracing-observer日志
xls_tracing_observer_logger = get_common_daily_logger('xls_tracing_observer','xls_tracing_observer')

# market-observer日志
market_observer_logger = get_common_daily_logger('market_observer','market_observer')

# result_observer日志
result_observer_logger = get_common_daily_logger('result_observer','result_observer')

# market->xls candidate observer日志
xls_observer_logger = get_common_daily_logger('xls_observer','xls_observer')

# xls-reporter-observer日志
xls_reporter_observer_logger = get_common_daily_logger('xls_reporter_observer','xls_reporter_observer')

# xls stage traing日志
xls_stage_tracing_logger = get_common_daily_logger('xls_stage','xls_stage')

# codes merger日志
codes_merger_logger = get_common_daily_logger('codes_merger','codes_merger')

# dyna scheduler日志
dyna_scheduler_logger = get_common_daily_logger('dyna_scheduler','dyna_scheduler')

# preview_scheduler日志
preview_scheduler_logger = get_common_daily_logger('preview_scheduler','preview_scheduler')

# preview_score_observer日志
preview_score_observer_logger = get_common_daily_logger('preview_score_observer','preview_score_observer')

# dyna candidate日志
dyna_candidate_logger = get_common_daily_logger('dyna_candidate','dyna_candidate')

# dyna derive日志
dyna_derive_logger = get_common_daily_logger('dyna_derive','dyna_derive')

# xls_shape_codes日志
xls_shape_codes_logger = get_common_daily_logger('xls_shape_codes','xls_shape_codes')

# candi-top-codes日志
candi_top_codes_logger = get_common_daily_logger('candi_top_codes','candi_top_codes')

# candi-shape-codes日志
candi_shape_codes_logger = get_common_daily_logger('candi_shape_codes','candi_shape_codes')

# candi-compete-codes日志
candi_compete_codes_logger = get_common_daily_logger('candi_compete_codes','candi_compete_codes')

# comp_shape_codes日志
comp_shape_codes_logger = get_common_daily_logger('comp_shape_codes','comp_shape_codes')

# query_xls日志
query_xls_logger = get_common_daily_logger('query_xls','query_xls')

# @dyna_xls_codes
dyna_xls_logger = get_common_daily_logger('dyna_xls','dyna_xls')

# xls scheduler调度日志
xls_scheduler_logger = get_common_daily_logger('xls_scheduler','xls_scheduler')

# shape scheduler调度日志
shape_scheduler_logger = get_common_daily_logger('shape_scheduler','shape_scheduler')

# xls reporter 日志
xls_reporter_logger = get_common_daily_logger('xls_reporter','xls_reporter')

# xls opener日志
xls_opener_logger = get_common_daily_logger('xls_opener','xls_opener')

# realtime_reporter日志
realtime_reporter_logger = get_common_daily_logger('realtime_reporter','realtime_reporter')

# manual_reporter日志
manual_reporter_logger = get_common_daily_logger('manual_reporter','manual_reporter')

# shape reporter日志
shape_reporter_logger = get_common_daily_logger('shape_reporter','shape_reporter')

# prebuild_candi日志
prebuild_candi_logger = get_common_daily_logger('prebuild_candi','prebuild_candi')

# pretracing_xls日志
pretracing_xls_logger = get_common_daily_logger('pretracing_xls','pretracing_xls')

# risk0_advisor日志
risk0_advisor_logger = get_common_daily_logger('risk0_advisor','risk0_advisor')

# safe_advisor日志
safe_advisor_logger = get_common_daily_logger('safe_advisor','safe_advisor')

# default_advisor 日志
default_advisor_logger = get_common_daily_logger('default_advisor','default_advisor')

# cli操作日志
cli_logger = get_common_daily_logger('cli','cli')

# operate日志
operate_logger = get_common_daily_logger('operate','operate')

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

INN_SERVER = "inn_server"

