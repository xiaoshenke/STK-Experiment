#!/usr/bin/python
# coding=utf-8

# 判断是否是@strategy.tuxing 包下的类,语义为: 调试良好的图形

import re
from util.df_util import empty
from util.param_util import fix_time_str

def is_tuxing_type(type,debug=False):
	if is_tuxing_type2(type):
		return True

	tmp = type[:3]

	# 只要符合开头的格式 那么就认为是图形算子
	if tmp in [ 'tx:','tx_','tx-','tt:','tt_','tt-' ]:
		return True
	return False

def is_tuxing_type2(type,debug=False):
	from eva.parser.builder.youzi_tuxing_builder import is_yz_tuxing_type
	return is_yz_tuxing_type(type)

def build_tuxing_one(type,debug=False):
	if is_tuxing_type2(type):
		from eva.parser.builder.youzi_tuxing_builder import build_yz_tuxing_one
		return build_yz_tuxing_one(type)

	# 去除前置符
	type = type[3:]
	origin = type

	type = type.replace('_fr_','_').replace('-fr-','_').replace('_from_','_').replace('-from-','_')
	type = type.replace('-','_')
	name = type.split(':')[0]

	eva = None

	if name in [ 'jjrzq_weak' ]:
		eva = try_parse_jjrzq_from_weak_1(type)	

	# 竞价弱转强+前日大阴线
	elif name in [ 'jjrzq_yin' ]:
		eva = try_parse_jjrzq_from_yin_1(type)

	# 竞价弱转强+当前处于箱体底部
	elif name in [ 'jjrzq_dibu' ]:
		eva = try_parse_jjrzq_from_dibu_1(type)

	elif name in [ 'jjrzq_yznianhe','jjrzq_yz_nianhe' ]:
		eva = try_parse_jjrzq_from_yz_nianhe_1(type)

	if name in [ 'shouri_tupo','srtupo','shouritupo' ]:
		eva = try_parse_shouri_tupo_1(type)

	if name == 'good':
		eva = try_parse_good_1(type)
	elif name == 'good2':
		eva = try_parse_good_2(type)

	elif name == 'zhusheng':
		eva = try_parse_zhusheng_1(type)
	elif name in [ 'gw_zhusheng','gaowei_zhusheng' ]:
		eva = try_parse_gaowei_zhusheng_1(type)

	elif name == 'newhigh':
		eva = try_parse_newhigh_1(type)
	elif name == 'reach_btw':
		eva = try_parse_reach_btw_1(type)

	# update 2026-01-16: 添加try_single逻辑
	if not eva and may_try_single_type(origin):  
		from eva.parser.builder.single_builder import build_single_one
		return build_single_one(origin)

	if not eva:	
		return eva
	return eva

# 当前不做任何逻辑判断 直接返回true
def may_try_single_type(type):
        return True

# example: tx:gaowei_zhusheng
def try_parse_gaowei_zhusheng_1(type):
	from eva.tuxing.zhushengs_1 import GaoweiZhusheng_1Eva
	return GaoweiZhusheng_1Eva()

# example: tx:zhusheng
def try_parse_zhusheng_1(type):
	from eva.tuxing.zhushengs_1 import Zhusheng_1Eva
	return Zhusheng_1Eva()

# example: tx:good
def try_parse_good_1(type):
	from eva.tuxing.goods_1 import Good_1Eva
	return Good_1Eva()

# example: tx:good2
def try_parse_good_2(type):
	from eva.tuxing.goods_1 import Good_2Eva
	return Good_2Eva()

# example: tx:shouritupo
def try_parse_shouri_tupo_1(type):
	from eva.tuxing.shouri_tupos_1 import ShouriTupo_1Eva
	eva = ShouriTupo_1Eva()
	return eva

# example: tx:jjrzq_yin
def try_parse_jjrzq_from_yin_1(type):
	from eva.tuxing.jjrzqs_1 import JJrzqFromYin_1Eva
	eva = JJrzqFromYin_1Eva()

	return eva

# example: tx:jjrzq_from_dibu
def try_parse_jjrzq_from_dibu_1(type):
	from eva.tuxing.jjrzqs_1 import JJrzqFromDibu_1Eva
	eva = JJrzqFromDibu_1Eva()
	
	return eva

# example: tx:jjrzq_yznianhe
def try_parse_jjrzq_from_yz_nianhe_1(type):
	from eva.tuxing.jjrzqs_1 import JJrzqFromYzNianhe_1Eva
	eva = JJrzqFromYzNianhe_1Eva()
	
	return eva

# example: tx:jjrzq_weak
def try_parse_jjrzq_from_weak_1(type):
	from eva.tuxing.jjrzqs_1 import JJrzqFromWeak_1Eva
	eva = JJrzqFromWeak_1Eva()

	return eva

# example: tx:newhigh:len=xx
def try_parse_newhigh_1(type):
	from eva.tuxing.newhighs_1 import Newhigh_1Eva
	eva = Newhigh_1Eva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			eva.set_day_len(int(k[1]))
	return eva

def try_parse_reach_btw_1(type):
	from eva.tuxing.reach_btws_1 import ReachBtw_1Eva
	eva = ReachBtw_1Eva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			eva.set_day_len(int(k[1]))
	return eva

if __name__ == "__main__":
	pass

