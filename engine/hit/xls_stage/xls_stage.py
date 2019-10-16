#!/usr/bin/python
# coding=utf-8

# TODO: 版块所处的阶段,xt,warm,hot,cold

from engine.hit.xls_stage.stage_cons import *

def get_stage_from_df(df,day,xls):
	from engine.codes_builder import g_codes_builder
	if df.empty:
		return STAGE_NOT_KNOWN
	codes = g_codes_builder.safe_get_codes(xls,day)
	if len(codes) == 0:
		return STAGE_NOT_KNOWN

	from util.mini import to_float2
	from inn_strategy.icore.inn_util import full_df_to_bounch
	df = df.drop_duplicates('code')
	df = full_df_to_bounch(df,day,codes,-1)
	df['pchg'] = df['trade'] - df['pre_c']
	df['pchg'] = 100.0*df['pchg']/df['pre_c']
	df['pchg'] = df['pchg'].map(to_float2)

	from engine.emotion.emotion import XlsEmotion
	emotion = XlsEmotion().set_type(xls).set_day(day)
	
	top = df[df['pchg']>=8.0].index.size
	normal = df[df['pchg']>=0.1].index.size
	crash = df[df['pchg']<=-6.0].index.size

	emotion.set_top(top).set_normal(normal).set_crash(crash).set_total(df.index.size)
	return get_stage_from_emotion(emotion)

# TODO: 根据crash top normal这几个数据综合计算出一个stage结果
def get_stage_from_emotion(emotion):
	return STAGE_NOT_KNOWN

