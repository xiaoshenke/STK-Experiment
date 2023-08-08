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

mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.ERROR)
#mpl_logger.setLevel(logging.WARNING)

# 用于临时作用
tmp_logger = get_common_daily_logger('tmp','tmp')

# 用于分析性能问题
cost_logger = get_common_daily_logger('cost','cost')

# event logger
event_logger = get_common_daily_logger('event','event')

# report recorder日志,见@engine.record.report_recorder
report_recorder_logger = get_common_daily_logger('report_recorder','report_recorder')
report_recorder_detail_logger = get_common_daily_logger('report_recorder_detail','report_recorder_detail')

# codes-observe日志
codes_observe_logger = get_common_daily_logger('codes_observe','codes_observe')

# pool-observe日志
pool_observe_logger = get_common_daily_logger('pool_observe','pool_observe')

# xls-observe日志
xls_observe_logger = get_common_daily_logger('xls_observe','xls_observe')

# longhu-observe日志
longhu_observe_logger = get_common_daily_logger('longhu_observe','longhu_observe')

# shouban-observe日志
shouban_observe_logger = get_common_daily_logger('shouban_observe','shouban_observe')

# chaozuo-observe日志
chaozuo_observe_logger = get_common_daily_logger('chaozuo_observe','chaozuo_observe')

# stocks-observe日志
stocks_observe_logger = get_common_daily_logger('stocks_observe','stocks_observe')

# high-observe日志
high_observe_logger = get_common_daily_logger('high_observe','high_observe')

# zhz500-observe日志
zhz500_observe_logger = get_common_daily_logger('zhz500_observe','zhz500_observe')

# bind-observe日志
bind_observe_logger = get_common_daily_logger('bind_observe','bind_observe')

# mline-observe日志
mline_observe_logger = get_common_daily_logger('mline_observe','mline_observe')

# dig-observe日志
dig_observe_logger = get_common_daily_logger('dig_observe','dig_observe')

# change-observe日志
change_observe_logger = get_common_daily_logger('change_observe','change_observe')

# buyer_scheduler日志
buyer_scheduler_logger = get_common_daily_logger('buyer_scheduler','buyer_scheduler')

# upstp-observe日志
upstp_observe_logger = get_common_daily_logger('upstp_observe','upstp_observe')

# market-observe日志
market_observe_logger = get_common_daily_logger('market_observe','market_observe')

# buyer-observe日志
buyer_observe_logger = get_common_daily_logger('buyer_observe','buyer_observe')

# xls stage traing日志
xls_stage_tracing_logger = get_common_daily_logger('xls_stage','xls_stage')

# xls reporter 日志
xls_reporter_logger = get_common_daily_logger('xls_reporter','xls_reporter')

# plan reporter日志
plan_reporter_logger = get_common_daily_logger('plan_reporter','plan_reporter')

# xls opener日志
xls_opener_logger = get_common_daily_logger('xls_opener','xls_opener')

# observe opener日志
observe_opener_logger = get_common_daily_logger('observe_opener','observe_opener')

# prop-observer日志
prop_observer_logger = get_common_daily_logger('prop_observer','prop_observer')

# stock-scheduler日志
stock_scheduler_logger = get_common_daily_logger('stock_scheduler','stock_scheduler')

# 见@web.plan_report_handler
report_handler_logger = get_common_daily_logger('report_handler','report_handler')

# default_advisor 日志
default_advisor_logger = get_common_daily_logger('default_advisor','default_advisor')

# cli操作日志
cli_logger = get_common_daily_logger('cli','cli')

# operate日志
operate_logger = get_common_daily_logger('operate','operate')

# crontab日志
crontab_logger = get_common_daily_logger('crontab','crontab')

def log_slow(msg):
	try:
		slow_logger = get_common_daily_logger('slow','slow')
		slow_logger.warn(str(msg))
	except Exception,e:
		print "log_slow"
		print e

# 网络错误单独做成日志
net_error_logger = get_common_daily_logger('net_error','net_error')
def save_net_error(msg):
	try:
		net_error_logger.error(str(msg))
	except Exception,e:
		pass

# cpu issure单独做成日至
cpu_issure_logger = get_common_daily_logger('cpu_issure','cpu_issure')
def save_cpu_issure(msg):
	try:
		cpu_issure_logger.error(str(msg))
	except Exception,e:
		pass

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

