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
	from strategy.stra.builder.youzi_tuxing_builder import is_yz_tuxing_type
	return is_yz_tuxing_type(type)

def build_tuxing_one(type,debug=False):
	# 游资类型的图形
	if is_tuxing_type2(type):
		from strategy.stra.builder.youzi_tuxing_builder import build_yz_tuxing_one
		return build_yz_tuxing_one(type)

	# 去除前置符
	type = type[3:]
	origin = type

	# 处理一下.bf参数
	from strategy.stra.builder.param_util import get_bf_len_from
	bf_len = get_bf_len_from(type)
	if '.bf' in type:
		type = type.split('.bf')[0]

	stra = None
	name = type.split(':')[0]

	if name == 'duotrd':
		stra = try_parse_duotrd_1(type)
	elif name in [ 'duoyang','duoyang1','duoyang_1' ]:
		stra = try_parse_duoyang_1(type)
	elif name in [ 'duoyang2','duoyang_2' ]:
		stra = try_parse_duoyang_2(type)

	elif name in [ 'break5','break5_1' ]:
		stra = try_parse_break5_1(type)

	elif name in [ 'tie' ]:
		stra = try_parse_tie_1(type)
	elif name == 'tie2':
		stra = try_parse_tie2_1(type)

	elif name == 'dibu':
		stra = try_parse_dibu_1(type)
	elif name == 'xt':
		stra = try_parse_xt_1(type)
	elif name in [ 'kuan_xt','kuan_xt1' ]:
		stra = try_parse_kuan_xt_1(type)
		
	elif name in [ 'huoli','huoli1' ]:
		stra = try_parse_huoli_1(type) 
	elif name == 'huoli_alot':
		stra = try_parse_huoli_alot_1(type)	
	
	elif name in [ 'zouqiang' ]:
		stra = try_parse_zouqiang_1(type)
	elif name == 'qushi':
		stra = try_parse_qushi_1(type)
	elif name == 'qushi2':
		stra = try_parse_qushi_2(type)

	elif name in [ 'qiangshi','qiangs','qiangsh','qs' ]:
		stra = try_parse_qiangshi_1(type)
	elif name in [ 'qiangshi2','qiangs2','qiangsh2','qs2' ]:
		stra = try_parse_qiangshi_2(type)

	elif name in [ 'good','gd' ]:
		stra = try_parse_good_1(type)
	elif name in [ 'good2','gd2' ]:
                stra = try_parse_good_2(type)

	# 不强	
	elif name in [ 'buqiang','buq' ]:
		stra = try_parse_buqiang_1(type)

	elif name == 'quanzhong':
		stra = try_parse_quanzhong_1(type)

	elif name in [ 'guxing2','gx2','dgx2' ]:
		stra = try_parse_guxing_2(type)
	elif name in [ 'guxing','gx','dgx' ]:
		stra = try_parse_guxing_1(type)

	elif name in [ 'shangy' ]:
		stra = try_parse_shangy_1(type)
	
	elif name == 'trends_good':
		stra = try_parse_trends_good_1(type)

	elif name in [ 'xiangshang' ]:
		stra = try_parse_xiangshang_1(type)
	elif name in [ 'xiangshang2' ]:
		stra = try_parse_xiangshang2_1(type)

	# 暴跌图形
	elif name in [ 'baodie','baodi','baode' ]:
		stra = try_parse_baodie_1(type)

	# 顶部缩量
	elif name in [ 'dbsl','dbsv','dbsuov','dbsuol','dingbu_suov','dingbu_suol' ]:
		stra = try_parse_dingbu_suov_1(type)

	# 底部缩量
	elif name in [ 'dibusv','dibusl','dibusuov','dibu_suov','dibu_suol' ]:
		stra = try_parse_dibu_suov_1(type)
	
	# 箱体内部爆量
	if name in [ 'xt_baov','xtbaov' ]:
		stra = try_parse_xt_baov_1(type)

	# 箱体底部
	if name in [ 'xt_dibu','xtdibu' ]:
		stra = try_parse_xt_dibu_1(type)

	# 向下破黏合的均线
	if name in [ 'break_tie','breaktie' ]:
		stra = try_parse_break_tie_1(type)

	if name in [ 'yz_nianhe','yznianhe' ]:
		stra = try_parse_youzi_nianhe_1(type)

	# 股价处于低位 这里的低位就是股价没有飞升
	if name in [ 'diwei','diw','dw' ]:
		stra = try_parse_diwei_1(type)

	if name in [ 'zhongwei','zhonwei','zhongw','zhonw','zw' ]:
		stra = try_parse_zhongwei_1(type)
	elif name in [ 'gaowei','gawei','gwei' ]:
		stra = try_parse_gaowei_1(type)

	if name in [ 'diwei_qidong','diwei_qd','dwqidong','dw_qidong' ]:
		stra = try_parse_diwei_qidong_1(type)

	if name in [ 'qidong','qd','qid','qido','qidon' ]:
		stra = try_parse_qidong_1(type)

	if name == 'bad':
		stra = try_parse_bad_1(type)

	if name in [ 'huoyue','huoy','hy' ]:
		stra = try_parse_huoyue_1(type)

	if name in [ 'bsd' ]:
		stra = try_parse_bsd_1(type)

	if name == 'jiasu':
		stra = try_parse_jiasu_1(type)

	if name in [ 'zhendang','zhendan','zhend','zhengdang','zhengd','zd' ]:
		stra = try_parse_zhendang_1(type)
	elif name in [ 'zhendang2','zhendan2','zhend2','zhengdang2','zhengd2','zd2' ]:
		stra = try_parse_zhendang_2(type)

	if name in [ 'redu_pos','redu_pos1' ]:
		stra = try_parse_redu_pos_1(type)
	elif name == 'redu_pos2':
		stra = try_parse_redu_pos_2(type)

	# update 2026-01-16: 添加try_single逻辑
	if not stra and may_try_single_type(origin):	
		from strategy.stra.builder.single_builder import build_single_one
		return build_single_one(origin)

	if not stra:
		return stra

	if bf_len > 0:
		#print u'call stra:%s set_bf_len:%s'%(stra,bf_len)
		stra.set_bf_len(bf_len)		
	return stra

# 当前不做任何逻辑判断 直接返回true
def may_try_single_type(type):
	return False

# example: tx:huoli:len=
def try_parse_huoli_1(type):
	from strategy.tuxing.huolis_1 import Huoli_1Strategy
	stra = Huoli_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
	return stra

# example: tx:huoli_alot
def try_parse_huoli_alot_1(type):
	from strategy.tuxing.huolis_1 import HuoliAlot_1Strategy
	stra = HuoliAlot_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
	return stra


# example: tx:baodie
def try_parse_baodie_1(type):
	from strategy.tuxing.baodies_1 import Baodie_1Strategy
	return Baodie_1Strategy()

# example: tx:zd
def try_parse_zhendang_1(type):
	from strategy.tuxing.zhendangs_1 import Zhendang_1Strategy
	return Zhendang_1Strategy()

# example: tx:zd2
def try_parse_zhendang_2(type):
	from strategy.tuxing.zhendangs_1 import Zhendang_2Strategy
	return Zhendang_2Strategy()

# example: tx:bad
def try_parse_bad_1(type):
	from strategy.tuxing.bads_1 import Bad_1Strategy
	return Bad_1Strategy()

# example: tx:huoyue
def try_parse_huoyue_1(type):
	from strategy.tuxing.huoyues_1 import Huoyue_1Strategy
	return Huoyue_1Strategy()

# example: tx:bsd
def try_parse_bsd_1(type):
	from strategy.tuxing.bianshidus_1 import Bsd_1Strategy
	return Bsd_1Strategy()

# example: tx:quanzhong
def try_parse_quanzhong_1(type):
	from strategy.tuxing.quanzhongs_1 import Quanzhong_1Strategy
	return Quanzhong_1Strategy()

# example: tx:jiasu
def try_parse_jiasu_1(type):
	from strategy.tuxing.jiasus_1 import Jiasu_1Strategy
	return Jiasu_1Strategy()

# example: tx:qushi
def try_parse_qushi_1(type):
	from strategy.tuxing.qushis_1 import Qushi_1Strategy
	return Qushi_1Strategy()

# example: tx:qushi2
def try_parse_qushi_2(type):
	from strategy.tuxing.qushis_1 import Qushi_2Strategy
	return Qushi_2Strategy()

# example: tx:yz_nianhe
def try_parse_youzi_nianhe_1(type):
	from strategy.tuxing.nianhes_1 import YouziNianhe_1Strategy
	stra = YouziNianhe_1Strategy()
	return stra

# example: tx:qidong
def try_parse_qidong_1(type):
	from strategy.tuxing.qidongs_1 import Qidong_1Strategy
	return Qidong_1Strategy()

# example: tx:diwei_qidong
def try_parse_diwei_qidong_1(type):
	from strategy.tuxing.diwei_qidongs_1 import DiweiQidong_1Strategy
	return DiweiQidong_1Strategy()

# example: tx:diwei
def try_parse_diwei_1(type):
	from strategy.tuxing.diweis_1 import Diwei_1Strategy
	return Diwei_1Strategy()

# example: tx:zhongwei
def try_parse_zhongwei_1(type):
	from strategy.tuxing.zhongweis_1 import Zhongwei_1Strategy
	return Zhongwei_1Strategy()

# example: tx:gaowei
def try_parse_gaowei_1(type):
	from strategy.tuxing.gaoweis_1 import Gaowei_1Strategy
	return Gaowei_1Strategy()

# example: tx:break_tie
def try_parse_break_tie_1(type):
	from strategy.tuxing.break_ties_1 import BreakTie_1Strategy
	stra = BreakTie_1Strategy()
	return stra

# example: tx:xt_dibu
def try_parse_xt_dibu_1(type):
	from strategy.tuxing.xt_dibus_1 import XtDibu_1Strategy
	stra = XtDibu_1Strategy()
	return stra

# example: tx:xtbaov
def try_parse_xt_baov_1(type):
	from strategy.tuxing.xt_baovs_1 import XtBaov_1Strategy
	stra = XtBaov_1Strategy()
	return stra

# example: tx:dibu_suov
def try_parse_dibu_suov_1(type):
	from strategy.tuxing.suovs_1 import DibuSuov_1Strategy
	stra = DibuSuov_1Strategy()
	return stra

# example: tx:dbsl
def try_parse_dingbu_suov_1(type):
	from strategy.tuxing.suovs_1 import DingbuSuov_1Strategy
	stra = DingbuSuov_1Strategy()
	return stra

# example: tx:guxing2
def try_parse_guxing_2(type):
	from strategy.tuxing.guxings_1 import Guxing_2Strategy
	stra = Guxing_2Strategy()
	return stra

# example: tx:guxing
def try_parse_guxing_1(type):
	from strategy.tuxing.guxings_1 import Guxing_1Strategy
	stra = Guxing_1Strategy()
	return stra

# example: tx:zouqiang
def try_parse_zouqiang_1(type):
	from strategy.tuxing.zouqiangs_1 import Zouqiang_1Strategy
	stra = Zouqiang_1Strategy()
	return stra

# example: tx:buqiang
def try_parse_buqiang_1(type):
	from strategy.tuxing.buqiangs_1 import Buqiang_1Strategy
	stra = Buqiang_1Strategy()
	return stra

# example: tx:good
def try_parse_good_1(type):
	from strategy.tuxing.goods_1 import Good_1Strategy
	stra = Good_1Strategy()
	return stra

# example: tx:good2
def try_parse_good_2(type):
	from strategy.tuxing.goods_1 import Good_2Strategy
	stra = Good_2Strategy()
	return stra


# example: tx:qiangshi
def try_parse_qiangshi_1(type):
	from strategy.tuxing.qiangshis_1 import Qiangshi_1Strategy
	stra = Qiangshi_1Strategy()
	return stra

# example: tx:qiangshi2
def try_parse_qiangshi_2(type):
	from strategy.tuxing.qiangshis_1 import Qiangshi_2Strategy
	stra = Qiangshi_2Strategy()
	return stra

# example: tx:xiangshang
def try_parse_xiangshang_1(type):
	from strategy.tuxing.xiangshangs_1 import Xiangshang_1Strategy
	stra = Xiangshang_1Strategy()
	return stra

# example: tx:xiangshang2
def try_parse_xiangshang2_1(type):
	from strategy.tuxing.xiangshangs_1 import Xiangshang2_1Strategy
	stra = Xiangshang2_1Strategy()
	return stra

# example: tx:shangy
def try_parse_shangy_1(type):
	from strategy.tuxing.shangys_1 import Shangy_1Strategy
	stra = Shangy_1Strategy()
	return stra

# example: tx:trends_good
def try_parse_trends_good_1(type):
	from strategy.tuxing.trends_goods_1 import TrendsGood_1Strategy
	stra = TrendsGood_1Strategy()

	return stra

# example: tx:xt
def try_parse_xt_1(type):
	from strategy.tuxing.xts_1 import Xt_1Strategy
	stra = Xt_1Strategy()
	return stra

# example: tx:kuan_xt
def try_parse_kuan_xt_1(type):
	from strategy.tuxing.xts_1 import KuanXt_1Strategy	
	stra = KuanXt_1Strategy()
	return stra

# example: tx:dibu
def try_parse_dibu_1(type):
	from strategy.tuxing.dibus_1 import Dibu_1Strategy
	stra = Dibu_1Strategy()
	return stra

# example: tx:tie
def try_parse_tie_1(type):
	from strategy.tuxing.ties_1 import Tie_1Strategy
	stra = Tie_1Strategy()
	return stra

# example: tx:tie2
def try_parse_tie2_1(type):
	from strategy.tuxing.ties_1 import Tie2_1Strategy
	stra = Tie2_1Strategy()
	return stra

# example: tx:break5
def try_parse_break5_1(type):
	from strategy.tuxing.break5s_1 import Break5_1Strategy
	stra = Break5_1Strategy()
	return stra

# example: tx:duoyang
def try_parse_duoyang_1(type):
	from strategy.tuxing.duo_yangs_1 import Duoyang_1Strategy
	stra = Duoyang_1Strategy()

	return stra

# example: tx:duoyang_2
def try_parse_duoyang_2(type):
	from strategy.tuxing.duo_yangs_1 import Duoyang_2Strategy
	stra = Duoyang_2Strategy()

	return stra

# example: tx:duotrd
def try_parse_duotrd_1(type):
	from strategy.tuxing.duo_trds_1 import Duotrd_1Strategy
	stra = Duotrd_1Strategy()

	return stra

# example: tx:redu_pos
def try_parse_redu_pos_1(type):
	from strategy.tuxing.redu_poss_1 import ReduPos_1Strategy
	stra = ReduPos_1Strategy()

	return stra

# example: tx:redu_pos2
def try_parse_redu_pos_2(type):
	from strategy.tuxing.redu_poss_1 import ReduPos_2Strategy
	stra = ReduPos_2Strategy()

	return stra

if __name__ == "__main__":
	pass
