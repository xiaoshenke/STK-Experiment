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

# manual xls logger,见@engine.manual.xls.manual_xls
manual_xls_logger = get_common_daily_logger('manual_xls','manual_xls')

# watch recorder
watch_recorder_logger = get_common_daily_logger('watch_recorder','watch_recorder')

# manual codes logger,见@engine.manual.codes.manual_codes
manual_codes_logger = get_common_daily_logger('manual_codes','manual_codes')

# report recorder日志,见@engine.record.report_recorder
report_recorder_logger = get_common_daily_logger('report_recorder','report_recorder')

# buyer id日志,见@engine.record.buyer_recorder
buyer_id_logger = get_common_daily_logger('buyer_id','buyer_id')

# time-observer日志
time_observer_logger = get_common_daily_logger('time_observer','time_observer')

# xls-tracing-observer日志
xls_tracing_observer_logger = get_common_daily_logger('xls_tracing_observer','xls_tracing_observer')

# xls stage traing日志
xls_stage_tracing_logger = get_common_daily_logger('xls_stage','xls_stage')

# plan scheduler日志
plan_scheduler_logger = get_common_daily_logger('plan_scheduler','plan_scheduler')

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

# manual_shape_codes日志
manual_shape_codes_logger = get_common_daily_logger('manual_shape_codes','manual_shape_codes')

# manual-buyer日志
manual_buyer_logger = get_common_daily_logger('manual_buyer','manual_buyer')

# observe_scheduler日志
observe_scheduler_logger = get_common_daily_logger('observe_scheduler','observe_scheduler')

# query_xls日志
query_xls_logger = get_common_daily_logger('query_xls','query_xls')

# xls reporter 日志
xls_reporter_logger = get_common_daily_logger('xls_reporter','xls_reporter')

# plan reporter日志
plan_reporter_logger = get_common_daily_logger('plan_reporter','plan_reporter')

# xls opener日志
xls_opener_logger = get_common_daily_logger('xls_opener','xls_opener')

# realtime_reporter日志
realtime_reporter_logger = get_common_daily_logger('realtime_reporter','realtime_reporter')

# market-observer日志
market_observer_logger = get_common_daily_logger('market_observer','market_observer')

# 实际是在@market-observer中,分出market的部分 分开再写一遍日志
market_logger = get_common_daily_logger('market','market')

# market plan日志
market_plan_logger = get_common_daily_logger('market_plan','market_plan')

# shouban plan日志
shouban_plan_logger = get_common_daily_logger('shouban_plan','shouban_plan')

# ban24 plan日志
ban24_plan_logger = get_common_daily_logger('ban24_plan','ban24_plan')

# chaozuo plan日志
chaozuo_plan_logger = get_common_daily_logger('chaozuo_plan','chaozuo_plan')

# strongs plan日志
strongs_plan_logger = get_common_daily_logger('strongs_plan','strongs_plan')

# strongest plan日志
strongest_plan_logger = get_common_daily_logger('strongest_plan','strongest_plan')

# weakest plan日志
weakest_plan_logger = get_common_daily_logger('weakest_plan','weakest_plan')

# monitor_plan日志
monitor_plan_logger = get_common_daily_logger('monitor_plan','monitor_plan')

# lifecycle_plan日志
lifecycle_plan_logger = get_common_daily_logger('lifecycle_plan','lifecycle_plan')

# upscore_plan日志
upscore_plan_logger = get_common_daily_logger('upscore_plan','upscore_plan')

# xls plan日志
xls_plan_logger = get_common_daily_logger('xls_plan','xls_plan')

# pretraces list plan日志
pretraces_list_logger = get_common_daily_logger('pretraces_list','pretraces_list')

# manual_list 日志
manual_list_logger = get_common_daily_logger('manual_list','manual_list')

# pretraces plan日志
pretraces_plan_logger = get_common_daily_logger('pretraces_plan','pretraces_plan')

# guxing plan日志
guxing_plan_logger = get_common_daily_logger('guxing_plan','guxing_plan')

# guxing list plan日志
guxing_list_logger = get_common_daily_logger('guxing_list','guxing_list')

# manual_reporter日志
manual_reporter_logger = get_common_daily_logger('manual_reporter','manual_reporter')

# 见@web.plan_report_handler
report_handler_logger = get_common_daily_logger('report_handler','report_handler')

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

# rotate_advisor 日志
rotate_advisor_logger = get_common_daily_logger('rotate_advisor','rotate_advisor')

# rotate_env日志
rotate_env_logger = get_common_daily_logger('rotate_env','rotate_env')

# cli操作日志
cli_logger = get_common_daily_logger('cli','cli')

# operate日志
operate_logger = get_common_daily_logger('operate','operate')

# crontab日志
crontab_logger = get_common_daily_logger('crontab','crontab')

# plan-list日志
plan_list_logger = get_common_daily_logger('plan_list','plan_list')

# realtime_plan日志
realtime_plan_logger = get_common_daily_logger('realtime_plan','realtime_plan')

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

