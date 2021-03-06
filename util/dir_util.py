#!/usr/bin/python
# coding=utf-8
# 当前所有日志都在daily/xxxx-aa-bb/文件夹下

from util.time_util import today

def get_cur_dir():
	from cons import CUR_PATH
	return CUR_PATH

def get_daily_dir(day=''):
	from cons import STK_DAILY_PATH
	day = day if day else str(today())
	return "%s%s/"%(STK_DAILY_PATH,day)


def get_crontab_dir(day=''):
	return '%s/crontab/'%get_daily_dir(day)

def get_plan_dir(day=''):
	return '%s/plan/'%get_daily_dir(day)

def get_buyer_dir(day=''):
	return '%s/buyer/'%get_daily_dir(day)

def get_suma_dir(day=''):
	return '%s/suma/'%get_daily_dir(day)

def get_codes_dir(day=''):
	return "%s/codes/"%get_daily_dir(day)

def get_xls_dir(day=''):
	return "%s/xls/"%get_daily_dir(day)

# 用于engine.stage.xls的cache
def get_xls_stage_dir(day=''):
	return '%s/xls_stage/'%get_daily_dir(day)

# engine.stage.market的cache
def get_market_stage_dir(day=''):
	return '%s/market_stage/'%get_daily_dir(day)

def get_shizhan_dir(day=''):
	return '%s/shizhan/'%(get_daily_dir(day))

def get_realtime_report_dir(day=''):
        return "%s/realtime_report/"%get_daily_dir(day)

def get_shape_report_dir(day=''):
	return "%s/shape_report/"%get_daily_dir(day)

def get_manual_report_dir(day=''):
	return "%s/manual_report/"%get_daily_dir(day)

def get_xls_report_dir(day=''):
	return "%s/xls_report/"%get_daily_dir(day)

def get_open2_report_dir(day=''):
	return "%s/open2_report/"%get_daily_dir(day)

def get_rapid_up_dir(day=''):
	return "%s/rapid_up/"%get_daily_dir(day)

def get_open_dir(day=''):
	return "%s/open/"%get_daily_dir(day)

def get_hot_xls_dir(day=''):
	return "%s/hot_xls/"%get_daily_dir(day)

def get_apply_dir(day=''):	
	return "%s/apply/"%get_daily_dir(day)

def get_env_dir(day=''):
	return "%s/env/"%get_daily_dir(day)

def get_advise_dir(day=''):
	return '%s/advise/'%get_daily_dir(day)

def get_evaluate_dir(day=''):
	return "%s/evaluate/"%get_daily_dir(day)

def get_df_merger_source_dir(day=''):
	return "%s/df_merger_source/"%get_daily_dir(day)

def get_filter_source_dir(day=''):
	return "%s/filter_source/"%get_daily_dir(day)

def get_create_source_dir(day=''):
	return "%s/create_source/"%get_daily_dir(day)

def get_candi_source_dir(day=''):
	return '%s/candi_source/'%get_daily_dir(day)

def get_eva_dir(day=''):
	return "%s/eva/"%get_daily_dir(day)

# 处理cross+inner类型的strategy的cache路径
def get_create_cache_dir(day=''):
	return "%s/create_cache/"%get_daily_dir(day)

def get_dfa_source_dir(day=''):
	return '%s/dfa_source/'%get_daily_dir(day)

def get_cal_manager_source_dir(day=''):
	return '%s/cm_source/'%get_daily_dir(day)

def get_queryable_source_dir(day=''):
	return '%s/queryable_source/'%get_daily_dir(day)

def get_tracing_dir(day=''):
	return '%s/tracing/'%get_daily_dir(day)

def get_stage_source_dir(day=''):
	return "%s/stage_source/"%get_daily_dir(day)

def get_fenshi_wholecodes_dir(day=''):
	return "%s/fenshi_wholecodes/"%get_daily_dir(day)

def get_report_dir(day=''):
	return "%s/report/"%get_daily_dir(day)

def get_report2_dir(day=''):
	return "%s/report2/"%get_daily_dir(day)

def get_noon_report_dir(day=''):
	return '%s/noon_report/'%get_daily_dir(day)

def get_yidong_dir(day=''):
	return "%s/yidong/"%get_daily_dir(day)

def get_prebuild_dir(day=''):
	return "%s/prebuild/"%get_daily_dir(day)

def get_csv_path():
	return "%s/data/csv_data/"%get_cur_dir()

def init_dirs(day=''):
	dirs = [get_daily_dir,get_apply_dir,get_filter_source_dir,get_fenshi_wholecodes_dir,get_report_dir,get_open_dir,get_create_source_dir,get_stage_source_dir,get_queryable_source_dir,get_shape_report_dir,get_tracing_dir,get_dfa_source_dir,get_xls_report_dir,get_hot_xls_dir,get_noon_report_dir,get_create_cache_dir,get_candi_source_dir,get_env_dir,get_advise_dir,get_plan_dir,get_suma_dir,get_xls_stage_dir,get_market_stage_dir,get_crontab_dir,get_buyer_dir,get_shizhan_dir]
	dirs = [ dir(day) for dir in dirs ]
	import os
	for dir in dirs:
		if not os.path.exists(dir):
			print "we will mkdir:%s"%dir
			try:
				os.mkdir(dir)
			except Exception,e:
				print e
	return

import click
@click.group()
def cli():
	"""DIR UTIL CLI"""
	pass

@cli.command()
@click.argument('day')
def init(day):
	""" init day """
	init_dirs(day)

if __name__ == "__main__":
	cli()
