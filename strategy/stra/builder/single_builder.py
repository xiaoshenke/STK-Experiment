#!/usr/bin/python
# coding=utf-8

# 单个形态类型: strategy.single包下的node,也是最基本的计算算子

import re
from util.df_util import empty
from util.param_util import fix_time_str

def is_single_type(type,debug=False):
        node = build_single_one(type,debug)
        if node:
                return True
        return False

def build_single_one(type,debug=False):
	if debug:
		print 'single_builder.build_single_one,type: %s'%type

	stra = None
	commons,params = get_seprate_params(type)
	from helper import to_str
	type = to_str(params,sep=':')

	name = params[0].split('.')[0]
	#print u'single_builder.build_single_one,name:%s'%(name)

	#if type.startswith('xt'):
	#	stra = try_parse_xt(type)
	if type.startswith('tiao'):
		stra = try_parse_tiao(type)
	elif type.startswith( 'append_name' ) or type == 'name':
		stra = try_parse_append_name(type)
	elif type.startswith('baov') or type.startswith('baol') or type.startswith('bao_v'):
		stra = try_parse_baov(type)
	elif type.startswith('suov') or type.startswith('suo_v'):
		stra = try_parse_suov(type)
	elif type.startswith( 'height' ):
		stra = try_parse_height(type)
	elif type.startswith( 'ma_dis' ) or type.startswith( 'dis:' ) or type == 'dis' or type.startswith('dist'):
		stra = try_parse_ma_dis(type)
	elif type.startswith( 'ma_yuanli' ) or type.startswith( 'yuanli:' ) or type == 'yuanli':
		stra = try_parse_ma_yuanli(type)
	elif type.startswith('ma_xt'):
		stra = try_parse_ma_xt(type)
	elif type.startswith( 'nianhe' ):
		stra = try_parse_nianhe(type)
	elif type.startswith( 'fasan' ):
		stra = try_parse_fasan(type)
	elif type.startswith( 'zouq' ):
		stra = try_parse_zouqiang(type)
	elif type.startswith( 'tie' ):
		stra = try_parse_tie(type)
	elif type.startswith('price'):
		stra = try_parse_price(type)
	elif type.startswith('breakup_ma') or type.startswith('break_up_ma') or type.startswith('breakup'):
		stra = try_parse_breakup_ma(type)
	elif type.startswith('break_ma') or type.startswith('break'):
		stra = try_parse_break_ma(type)
	elif type.startswith('up_ma') or type.startswith('upma'):
		stra = try_parse_up_ma(type)
	elif type.startswith('down_ma') or type.startswith( 'downma' ) or type.startswith( 'dma' ):
		stra = try_parse_down_ma(type)
	elif type.startswith('away_close'):
		stra = try_parse_away_close(type)
	elif type.startswith('away_trd') or type.startswith('trd_away'):
		stra = try_parse_away_trd(type)
	elif type.startswith('trd_sum') or type.startswith('trdsum'):
		stra = try_parse_trd_sum(type)
	elif type.startswith('shangy'):
		stra = try_parse_shangy(type)
	elif type.startswith('xiay'):
		stra = try_parse_xiay(type)
	elif type.startswith('rup'):
		stra = try_parse_rup(type)
	elif type.startswith('minus_ma'):
		stra = try_parse_minus_ma(type)
	elif type.startswith('pos_pchg'):
		stra = try_parse_pos_pchg(type)
	elif type.startswith('close_minus'):
		stra = try_parse_close_minus(type)
	elif type.startswith('trd_minus'):
                stra = try_parse_trd_minus(type)
	elif type.startswith('trds'):
		stra = try_parse_trds(type)
	elif type.startswith('trd'):
		stra = try_parse_trd(type)
	elif type.startswith( 'shiti' ):
		stra = try_parse_shiti(type)
	elif type.startswith('upbound'):
		stra = try_parse_upbound(type)
	elif type.startswith('ma_upbound'):
		stra = try_parse_ma_upbound(type)
	elif type.startswith('dbound'):
		stra = try_parse_dbound(type)
	elif type.startswith('ts'):
		stra = try_parse_ts(type)
	elif type.startswith('cos'):
		stra = try_parse_cos(type)
	# lsk: little shake
	elif type.startswith('co') or type.startswith( 'lsk' ):
		stra = try_parse_co(type)
	elif type.startswith('shake') or type.startswith('sk'):
		stra = try_parse_shake(type)
	elif type.startswith('msk'):
		stra = try_parse_msk(type)
	elif type.startswith('shakes'):
		stra = try_parse_shakes(type)
	elif type.startswith('closes'):
		stra = try_parse_closes(type)
	elif type.startswith('highs'):
		stra = try_parse_highs(type)
	elif type.startswith('days_pchg'):
		stra = try_parse_days_pchg(type)
	elif type.startswith('ma_pchgs') or type.startswith('ma_pchg'):
		stra = try_parse_ma_pchgs(type)
	elif type.startswith('max_pchg'):
		stra = try_parse_max_pchg(type)
	elif type.startswith('max_drop'):
		stra = try_parse_max_drop(type)
	elif type.startswith( 'higher' ):
                stra = try_parse_higher(type)
	elif type.startswith( 'lower' ):
		stra = try_parse_lower(type)
	elif type.startswith('newlow'):
		stra = try_parse_newlow(type)
	elif type.startswith('v_newlow'):
		stra = try_parse_v_newlow(type)
	elif type.startswith('v_newhigh'):
		stra = try_parse_v_newhigh(type)
	elif type.startswith('pchg_newhigh') or type.startswith('newh_pchg') or type.startswith('nh_pchg'):
		stra = try_parse_pchg_newhigh(type)
	elif type.startswith('nh_trd'):
		stra = try_parse_trd_newhigh(type)
	elif type.startswith('newhigh'):
		stra = try_parse_newhigh(type)
	elif type.startswith('hit_press'):
		stra = try_parse_hit_press(type)
	elif type.startswith('hcl') or name == 'btw':
		stra = try_parse_hcl(type)
	elif type.startswith('hh'):
		stra = try_parse_hh(type)
	elif type.startswith('tover'):
		stra = try_parse_tover(type)
	elif type.startswith('pb'):
		stra = try_parse_pb(type)
	elif type.startswith('pe'):
		stra = try_parse_pe(type)
	elif type.startswith('ma_tover'):
		stra = try_parse_ma_tover(type)
	elif type.startswith('amt') or type.startswith('amount'):
                stra = try_parse_amt(type)
        elif type.startswith('ma_amt') or type.startswith('ma_amount'):
                stra = try_parse_ma_amt(type)
	elif type.startswith('days_v'):
		stra = try_parse_days_v(type)
	elif type.startswith('ma_v'):
		stra = try_parse_ma_days_v(type)
	elif type.startswith('guxing'):
		stra = try_parse_guxing(type)
	elif type.startswith('shizhi'):
		stra = try_parse_shizhi(type)
	elif type.startswith('info'):
		stra = try_parse_info(type)
	elif type == 'random_eva':
		stra = try_parse_random_eva(type)
	elif type.startswith( 'rand' ) or type.startswith('rank'):
		stra = try_parse_random(type)
	elif type.startswith('pos'):
		stra = try_parse_pos(type)
	elif type.startswith('in_xt') or type.startswith('inxt'):
		stra = try_parse_in_xt(type)
	elif type.startswith('out_xt') or type.startswith('outxt'):
		stra = try_parse_out_xt(type)
	elif type.startswith( 'bound' ) or name == 'xt':
		stra = try_parse_bound(type)
	elif name in [ 'duanxt','duan_xt' ]:
		stra = try_parse_duan_xt(type)		
	elif name in [ 'xiaoxt','xiao_xt','xxt' ]:
		stra = try_parse_xiao_xt(type)

	elif type.startswith('qushi:') or type == 'qushi':
		stra = try_parse_qushi(type)

	if not stra:
		return stra

	for p in commons:
		k = p.split('=')
		if k[0] in ['ma','ma_len']:
			stra.set_ma_len(int(k[1]))
		elif k[0] == 'fix_chuangye':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_fix_chuangye(b)
		elif k[0] == 'limit':
			stra.set_limit(int(k[1]))
		elif k[0] == 'len':
			stra.set_day_len(int(k[1]))

	return stra

# core LOGIC:
def deal_bf_and_inn_logic(type,stra):
	if not stra:
		return stra

	_type = type.split(':')[0]
	inn_mode = True if '.inn' in _type else False
	_type = _type.replace('.inn','') if inn_mode else _type
	bf_len = 0
	bf_len = _get_bf_len_from(_type,bf_len)	
	if inn_mode and bf_len > 0:
		bf_len = bf_len-1
		stra.set_bf_mode(True).set_bf_len(bf_len)
	else:
		# 设置bf模式
		if bf_len > 0:
			stra.set_bf_mode(True).set_bf_len(bf_len)
		# 设置日内模式
		if inn_mode:
			stra.set_inn_mode(True)
	return stra

# 若type内部也有bf,比如newhigh.bf,那么将这个bf的数值加上外部传入的bf_len然后返回
# bf_len:外部传入的bf_len
def _get_bf_len_from(type,bf_len):
	if not '.bf' in type:
		return bf_len
	l = 1
        if type.index('.bf')+len('.bf') < len(type):
		l = int(type[type.index('.bf')+len('.bf'):])
	# 根据外部的bf_len是否有效进行计算
	return l if bf_len<=0 else l+bf_len

# example: ma_yuanli:min=:max=
def try_parse_ma_yuanli(type):
	from strategy.single.ma_yuanli import MaYuanliStrategy
	stra = MaYuanliStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'ma','ma_len','len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min_yuanli','min_pchg','min' ]:
			stra.set_min_yuanli(float(k[1]))
		elif k[0] in [ 'max_yuanli','max_pchg','max' ]:
			stra.set_max_yuanli(float(k[1]))
		elif k[0] == 'type':
			stra.set_type(k[1])
	return stra


# example: ma_dis:min_pchg=:max_pchg
def  try_parse_ma_dis(type):
	from strategy.single.ma_distance import MaDistanceStrategy
	stra = MaDistanceStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'ma','ma_len','len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min_dis','min_pchg','min' ]:
			stra.set_min_dis(float(k[1]))
		elif k[0] in [ 'max_dis','max_pchg','max' ]:
			stra.set_max_dis(float(k[1]))
	return stra

# example: down_ma:len=:ma_len=:min_up=:max_up=:min_num=
def try_parse_down_ma(type):
	from strategy.single.down_ma import DownMaStrategy
	stra = DownMaStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'ma','ma_len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min_down','min_pchg' ]:
			stra.set_min_down(float(k[1]))
		elif k[0] in [ 'max_down','max_pchg' ]:
			stra.set_max_down(float(k[1]))
		elif k[0] == 'min_num':
			stra.set_min_num(int(k[1]))
	return stra

# example: up_ma:len=:ma_len=:min_up=:max_up=:min_num=
def try_parse_up_ma(type):
	from strategy.single.up_ma import UpMaStrategy
	stra = UpMaStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'ma','ma_len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min','min_up','min_pchg' ]:
			stra.set_min_up(float(k[1]))
		elif k[0] in [ 'max','max_up','max_pchg' ]:
			stra.set_max_up(float(k[1]))
		elif k[0] == 'min_num':
			stra.set_min_num(int(k[1]))
	return stra

# example: breakup_ma:len=:ma_len=:fix=:use_high=
def try_parse_breakup_ma(type):
	from strategy.single.break_up_ma import BreakupMaStrategy
	stra = BreakupMaStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'ma','ma_len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] == 'fix':
			stra.set_fix(float(k[1]))
		elif k[0] == 'use_high':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_high(b)
	return stra

# example: break_ma:len=:ma_len=
def try_parse_break_ma(type):
	from strategy.single.break_ma import BreakMaStrategy
	stra = BreakMaStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'ma','ma_len' ]:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: minus_ma:ma1=:ma2=
def try_parse_minus_ma(type):
	from strategy.ma.minus_ma import MinusMaStrategy
	stra = MinusMaStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma1':
			stra.set_ma1(int(k[1]))
		elif k[0] == 'ma2':
			stra.set_ma2(int(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
	return stra

# example: pos_pchg:ma=:len=
def try_parse_pos_pchg(type):
	from strategy.single.pos_pchg import PosPchgStrategy
	stra = PosPchgStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min_pchg','min' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			stra.set_max_pchg(float(k[1]))
		elif k[0] == 'asc':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_asc(b)    
	return stra

# example: suov:len=:min_num=:max_num=
def try_parse_suov(type):
	from strategy.single.suo_v import SuoVStrategy
	stra = SuoVStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_num':
			stra.set_min_num(int(k[1]))
		elif k[0] == 'max_num':
			stra.set_max_num(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
	return stra

# example: baov:len=:min_num=:max_num=:min_rate
def try_parse_baov(type):
	from strategy.single.bao_v import BaoVStrategy
	stra = BaoVStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_num':
			stra.set_min_num(int(k[1]))
		elif k[0] == 'max_num':
			stra.set_max_num(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_rate' ]:
			stra.set_min_rate(float(k[1]))
	return stra

# example: qushi:len=:min=:max=:limit=
def try_parse_qushi(type):
	from strategy.wrap.qushi_strategy import QushiStrategy
	stra = QushiStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
		elif k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: name
def try_parse_append_name(type):
	from strategy.wrap.append_name_strategy import AppendNameStrategy
	return AppendNameStrategy()

# example: random_eva
def try_parse_random_eva(type):
	from strategy.wrap.random_eva_strategy import RandomEvaStrategy
	return RandomEvaStrategy()

# example: random:limit=
def try_parse_random(type):
	from strategy.wrap.random_strategy import RandomStrategy
	return RandomStrategy()

# example: tiao:min_pchg=:max_pchg
def try_parse_tiao(type):
	from strategy.single.tiao_strategy import TiaoStrategy
	stra = TiaoStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
	return stra

# example: height:len=:min_ban=
def try_parse_height(type):
	from strategy.single.height import HeightStrategy
	stra = HeightStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'min_ban':
			stra.set_min_ban(int(k[1]))
		elif k[0] == 'limit':
			stra.set_limit(int(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
	return stra

# example: shizhi:min_shizhi=:max_shizhi=
def try_parse_shizhi(type):
	from strategy.single.shizhi import ShizhiStrategy
	stra = ShizhiStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_shizhi','min_pchg','min' ]:
			stra.set_min_shizhi(float(k[1]))
		elif k[0] in [ 'max_shizhi','max' ]:
			stra.set_max_shizhi(float(k[1]))
	return stra

# example: price:min_price=:max_price=
def try_parse_price(type):
	from strategy.single.price import PriceStrategy
	stra = PriceStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_price':
                        stra.set_min_price(float(k[1]))
                elif k[0] == 'max_price':
                        stra.set_max_price(float(k[1]))
	return stra

# example: xiay:min_pchg=
def try_parse_xiay(type):
	from strategy.single.xiay import XiayStrategy
	stra = XiayStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        stra.set_min_pchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        stra.set_max_pchg(float(k[1]))
	return stra

# example: shangy:min_pchg=:max_pchg=
def try_parse_shangy(type):
	from strategy.single.shangy import ShangyStrategy
	stra = ShangyStrategy()
        params = type.split(':')
        for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
                        stra.set_min_pchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        stra.set_max_pchg(float(k[1]))
	return stra

# example: away_close:away_len=2:min_pchg=:max_pchg=:min_away=:max_away=
def try_parse_away_close(type):
	from strategy.away.close import AwayCloseStrategy
	stra = AwayCloseStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] == 'min_away':
			stra.set_min_away(float(k[1]))
		elif k[0] == 'max_away':
			stra.set_max_away(float(k[1]))
		elif k[0] == 'away_len':
			stra.set_away_len(int(k[1]))
	return stra

# example: away_trd:len=2:min_pchg=:max_pchg=
def try_parse_away_trd(type):
	from strategy.away.trd import AwayTrdStrategy
	stra = AwayTrdStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] in ['len','day_len']:
			star.set_day_len(int(k[1]))
	return stra

# example: shiti:min_pchg=:max_pchg=
def try_parse_shiti(type):
	from strategy.single.shiti import ShitiStrategy
	stra = ShitiStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_shiti(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_shiti(float(k[1]))
	return stra

# example: trd:min_pchg=:max_pchg
def try_parse_trd(type):
	from strategy.single.trd import TrendStrategy
	stra = TrendStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			stra.set_min_trend(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			stra.set_max_trend(float(k[1]))
	return stra

# example: rup:min_pchg=:max_pchg
def try_parse_rup(type):
	from strategy.single.rup import RupStrategy
	stra = RupStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: close_minus:min_pchg=:max_pchg=
def try_parse_close_minus(type):
	from strategy.minus.close import MinusCloseStrategy
	stra = MinusCloseStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_minus(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_minus(float(k[1]))
	return stra

# example: trd_minus:min_pchg=:max_pchg=:len=
def try_parse_trd_minus(type):
	from strategy.minus.trd import MinusTrdStrategy
	stra = MinusTrdStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			stra.set_min_minus(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_minus(float(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
	return stra

# example: trd_sum:min_pchg=:max_pchg=:len=
def try_parse_trd_sum(type):
	from strategy.sum.trd import SumTrdStrategy
	stra = SumTrdStrategy()
        
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			stra.set_min_sum(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_sum(float(k[1]))
		elif k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'only_up0' ]:
			b = True if k[1] in [ 'true','TRUE','True','1' ] else False
			stra.set_only_up0(b)	
	return stra

# example: duanxt:len=:min_xt=:min=:max=:use_hl=
def try_parse_duan_xt(type):
	from strategy.single.duan_xt import DuanXtStrategy
	stra = DuanXtStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] in [ 'max_rate' ]:
			stra.set_max_rate(float(k[1]))
		elif k[0] in [ 'min','min_xt','min_pchg' ]:
			stra.set_min_xt(float(k[1]))
		elif k[0] in [ 'max','max_xt','max_pchg' ]:
			stra.set_max_xt(float(k[1]))
		elif k[0] in [ 'use','use_hl','use_highlow','usehl' ]:
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_highlow(b)
	return stra

# example: xiaoxt:len=:min_xt=:min=:max=:use_hl=
def try_parse_xiao_xt(type):
	from strategy.single.xiao_xt import XiaoXtStrategy
	stra = XiaoXtStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] in [ 'max_rate' ]:
			stra.set_max_rate(float(k[1]))
		elif k[0] in [ 'min','min_xt','min_pchg' ]:
			stra.set_min_xt(float(k[1]))
		elif k[0] in [ 'max','max_xt','max_pchg' ]:
			stra.set_max_xt(float(k[1]))
		elif k[0] in [ 'use','use_hl','use_highlow','usehl' ]:
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_highlow(b)
	return stra

# example: bound|xt:len=:min_xt=:min=:max=:use_hl=
def try_parse_bound(type):
	from strategy.single.bound import BoundStrategy
	stra = BoundStrategy()

	is_xt = type.startswith('xt')

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] in [ 'max_rate' ]:
			stra.set_max_rate(float(k[1]))
		elif k[0] in [ 'min_xt','min_pchg' ]:
			stra.set_min_xt(float(k[1]))
		elif k[0] in [ 'max_xt','max_pchg' ]:
			stra.set_max_xt(float(k[1]))
		# 对不同的前缀(xt,bound)来说 'min'的解析方式不同
		elif is_xt and k[0] == 'min':
			stra.set_min_xt(float(k[1]))
		elif not is_xt and k[0] == 'min': 
			stra.set_min_rate(float(k[1]))
		elif is_xt and k[0] == 'max': 
			stra.set_max_xt(float(k[1]))	
		elif not is_xt and k[0] == 'max': 
			stra.set_max_rate(float(k[1]))
		elif k[0] in [ 'use','use_hl','use_highlow','usehl' ]:
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_highlow(b)
	return stra

# example: in_xt:len=:min_xt=:min=:max=
def try_parse_in_xt(type):
	from strategy.single.in_xt import InXtStrategy
	stra = InXtStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] in [ 'max','max_rate' ]:
			stra.set_max_rate(float(k[1]))
		elif k[0] == 'min_xt':
			stra.set_min_xt(float(k[1]))
		elif k[0] == 'max_xt':
			stra.set_max_xt(float(k[1]))
	return stra

# example: out_xt:len=:out=:min_xt=
def try_parse_out_xt(type):
	from strategy.single.out_xt import OutXtStrategy
	stra = OutXtStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] == 'min_xt':
			stra.set_min_xt(float(k[1]))
		elif k[0] in [ 'out','type' ]:
			stra.set_out(k[1])
	return stra

# example: guxing:len=5:min_pchg=5.0:max_pchg=10.0
def try_parse_guxing(type):
	from strategy.single.guxing import GuxingStrategy
	stra = GuxingStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_gx_len(int(k[1]))
		elif k[0] in [ 'min_pchg','min_gx','min' ]:
			stra.set_min_gx(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_gx(float(k[1]))
	return stra

# example: days_pchg:len|day_len=20:min_pchg=:max_pchg=
def try_parse_days_pchg(type):
	from strategy.single.days_pchg import DaysPchgStrategy
	stra = DaysPchgStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['len','day_len']:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
                        stra.set_min_pchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        stra.set_max_pchg(float(k[1]))
	return stra

# example: ma_pchgs:len=5:ma=5:min_pchg=5.0:max_pchg=20.0
def try_parse_ma_pchgs(type):
	from strategy.ma.days_pchg import MaPchgsStrategy
	stra = MaPchgsStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))	
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: ma_upbound:len=10:min_rate=0.5:min_pchg=8.0
def try_parse_ma_upbound(type):
	from strategy.ma.upbound import MaUpboundStrategy
	stra = MaUpboundStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'rate','min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] == 'max_rate':
			stra.set_max_rate(float(k[1])) 
		elif k[0] == 'min_pchg':
			stra.set_min_bound_pchg(float(k[1]))
	return stra

# example: upbound:len=10:rate=0.5:use_low=true:max_rate=1.0:use_high=
def try_parse_upbound(type):
	from strategy.single.upbound import UpboundStrategy
	stra = UpboundStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'rate','min_rate' ]:
			stra.set_min_rate(float(k[1]))
		elif k[0] == 'max_rate':
			stra.set_max_rate(float(k[1]))
		elif k[0] == 'use_low':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_low(b)	
		elif k[0] == 'use_high':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_high(b)
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
		
	return stra	

# example: dbound:len=10:rate=0.5:min_pchg=4.0
def try_parse_dbound(type):
	from strategy.single.downbound import DownboundStrategy
	stra = DownboundStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] == 'rate':
			stra.set_rate(float(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_bound_pchg(float(k[1]))
	return stra

# 使用该算子能够精确找到高度数据,是一个板还是1.5个板
# example: max_pchg:len=3:min_pchg=12.0:max_pchg=18.5:type=close:use_low=
def try_parse_max_pchg(type):
	from strategy.single.max_pchg import MaxPchgStrategy
	stra = MaxPchgStrategy()
        params = type.split(':')
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] in [ 'max','max_pchg' ]:
                        stra.set_max_max_pchg(float(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_max_pchg(float(k[1]))
		elif k[0] == 'type':
			stra.set_type(k[1])
		elif k[0] == 'use_low':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_low(b)
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: max_drop:len=3:min_pchg=12.0:max_pchg=18.5:type=close::min_dis=10
def try_parse_max_drop(type):
	from strategy.single.max_drop import MaxDropStrategy
	stra = MaxDropStrategy()
        params = type.split(':')
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] in [ 'max','max_pchg' ]:
                        stra.set_max_max_drop(float(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_max_drop(float(k[1]))
		elif k[0] == 'type':
                        stra.set_type(k[1])
		elif k[0] in ['min_dis','min_distance']:
			stra.set_min_distance(int(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: hh:min_pchg=9.0
def try_parse_hh(type):
	from strategy.single.high import HighHigh
	stra = HighHigh()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
	return stra

# example: super_buy
def try_parse_super_buy(type):
	from strategy.wrap.super_buy import SuperBuyStrategy
	return SuperBuyStrategy()

# example: days_v:min_rate=:max_rate=
def try_parse_days_v(type):
	from strategy.single.days_v import DaysVStrategy
	stra = DaysVStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] in ['min_rate']:
                        stra.set_min_rate(float(k[1]))
                elif k[0] in ['max_rate']:
                        stra.set_max_rate(float(k[1]))
	return stra

# example: ma_v:min_rate=:max_rate=:ma=
def try_parse_ma_days_v(type):
	from strategy.ma.days_v import MaDaysVStrategy
	stra = MaDaysVStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min_rate' ]:
                        stra.set_min_rate(float(k[1]))
                elif k[0] in [ 'max_rate' ]:
                        stra.set_max_rate(float(k[1]))
	return stra

# exmaple: amt:min_amt=:max_amt=
def try_parse_amt(type):
	from strategy.single.amount import AmountStrategy
	stra = AmountStrategy()
        params = type.split(':')
        for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_amt','min_amount','min' ]:
			stra.set_min_amount(float(k[1]))
		elif k[0] in [ 'max','max_amt','max_amount' ]:
			stra.set_max_amount(float(k[1]))
	return stra

# example: ma_amt:ma=:min_amt=:max_amt=
def try_parse_ma_amt(type):
        from strategy.ma.amount import MaAmountStrategy
        stra = MaAmountStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min_amt','min_amount' ]:
                        stra.set_min_amount(float(k[1]))
                elif k[0] in [ 'max_amt','max_amount' ]:
                        stra.set_max_amount(float(k[1]))
	return stra

# example: pe:min_pe=:max_pe=
def try_parse_pe(type):
	from strategy.single.pe import PeStrategy
	stra = PeStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pe':
			stra.set_min_pe(float(k[1]))
		elif k[0] == 'max_pe':
			stra.set_max_pb(float(k[1]))
	return stra

# example: pb:min_pb=:max_pb=
def try_parse_pb(type):
	from strategy.single.pb import PbStrategy
	stra = PbStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pb':
			stra.set_min_pb(float(k[1]))
		elif k[0] == 'max_pb':
			stra.set_max_pb(float(k[1]))
	return stra

# example: tover:min_tover=:max_tover=
def try_parse_tover(type):
	from strategy.single.tover import TOverStrategy
	stra = TOverStrategy()
        params = type.split(':')
        for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_tover','min_pchg' ]:
			stra.set_min_tover(float(k[1]))
		elif k[0] == [ 'max','max_tover' ]:
                        stra.set_max_tover(float(k[1]))
	return stra

# example: ma_tover:ma=:min_tover=:max_tover=
def try_parse_ma_tover(type):
	from strategy.ma.tover import MaTOverStrategy
	stra = MaTOverStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_tover':
                        stra.set_min_tover(float(k[1]))
		elif k[0] == 'max_tover':
                        stra.set_max_tover(float(k[1]))
	return stra

# example: hcl:min_pchg=9.0:max_pchg=9.0
def try_parse_hcl(type):
	from strategy.single.close import CloseHigh
	stra = CloseHigh()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
                        stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			stra.set_max_pchg(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example cos:len=:min_pchg=:max_pchg=
def try_parse_cos(type):
	from strategy.single.abs_cos import AbsCosStrategy
	stra = AbsCosStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
                elif k[0] == 'min_pchg':
                        stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
	return stra

# example co:min_pchg=:max_pchg=
def try_parse_co(type):
	from strategy.single.abs_co import AbsCoStrategy
	stra = AbsCoStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
	return stra

# example: sk:len=3:min_pchg=2.0:max_pchg=
def try_parse_shake(type):
	from strategy.single.shake import AbsShakeStrategy
	stra = AbsShakeStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] in ['len','day_len']:
			stra.set_day_len(int(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: msk:len=3:min_pchg=2.0:min_rate=1.5
def try_parse_msk(type):
	from strategy.single.multi_shake import MultiShakeStrategy
	stra = MultiShakeStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'min_rate':
			stra.set_min_rate(float(k[1]))
		elif k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: ts:min_pchg=1.5
def try_parse_ts(type):
	from strategy.single.ts import TsStrategy
	stra  = TsStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
	return stra

# example: tie:len=:ma=
def try_parse_tie(type):
	from strategy.single.tie import TieStrategy
	stra = TieStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['ma','ma_len']:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: zouqiang:len=:ma=
def try_parse_zouqiang(type):
	from strategy.single.zouqiang import ZouqiangStrategy
	stra = ZouqiangStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['ma','ma_len']:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
		elif k[0] in [ 'min2','min_minus' ]:
			stra.set_min_minus(float(k[1]))

	return stra

# example: fasan:len=:ma=
def try_parse_fasan(type):
	from strategy.single.fasan import FasanStrategy
	stra = FasanStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['ma','ma_len']:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: nianhe:len=:ma=
def try_parse_nianhe(type):
	from strategy.single.nianhe import NianheStrategy
	stra = NianheStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['ma','ma_len']:
			stra.set_ma_len(int(k[1]))
		elif k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
	return stra

# example: ma_xt:len=10:ma=10:max_pchg=5.0
def try_parse_ma_xt(type):
	from strategy.ma.xt import MaXTStrategy
	stra = MaXTStrategy()
	params = type.split(':')
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
			stra.set_day_len(int(k[1]))
                elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))	
	return stra

# example: xt:len=10:max_pchg=6.0:min_pchg=0.0:asc=true:use_high=False:use_low=False
def try_parse_xt(type):
	from strategy.single.xt import XTStrategy
	stra = XTStrategy()
	params = type.split(':')
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
			stra.set_day_len(int(k[1]))
                elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'asc' or k[0] == 'ascending':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_ascending(b)
		elif k[0] == 'use_high':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_high(b)
		elif k[0] == 'use_low':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_low(b)
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))	
	return stra

# trds:len=5:min_max_pchg=:max_max_pchg=
def try_parse_trds(type):
	from strategy.single.trds import TrendsStrategy
	stra = TrendsStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] == 'max_max_pchg':
                        stra.set_max_max_trd(float(k[1]))
		elif k[0] == 'min_max_pchg':
			stra.set_min_max_trd(float(k[1]))
		elif k[0] == 'min_max_abs':
			stra.set_max_max_abs(float(k[1]))
		elif k[0] == 'max_max_abs':
			stra.set_max_max_abs(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: highs:len=5:min_max_pchg=:max_max_pchg=
def try_parse_highs(type):
	from strategy.single.highs import HighsStrategy
	stra = HighsStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] == 'max_max_pchg':
                        stra.set_max_max_high(float(k[1]))
		elif k[0] == 'min_max_pchg':
			stra.set_min_max_high(float(k[1]))
		elif k[0] == 'min_max_abs':
			stra.set_max_max_abs(float(k[1]))
		elif k[0] == 'max_max_abs':
			stra.set_max_max_abs(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: closes:len=5:min_max_pchg=8.8:max_max_pchg=:min_max_abs=:max_max_abs=:min_min_pchg=:max_min_pchg=
def try_parse_closes(type):
	from strategy.single.closes import ClosesStrategy
	stra = ClosesStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] == 'max_max_pchg':
                        stra.set_max_max_close(float(k[1]))
		elif k[0] == 'min_max_pchg':
			stra.set_min_max_close(float(k[1]))
		elif k[0] == 'max_min_pchg':
                        stra.set_max_min_close(float(k[1]))
                elif k[0] == 'min_min_pchg':
                        stra.set_min_min_close(float(k[1]))
		elif k[0] == 'min_max_abs':
			stra.set_max_max_abs(float(k[1]))
		elif k[0] == 'max_max_abs':
			stra.set_max_max_abs(float(k[1]))
                else:
                   
		     raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: shakes:len=5:max_pchg=4.0
def try_parse_shakes(type):
	from strategy.single.shakes import ShakesStrategy
	stra = ShakesStrategy()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'len':
                        stra.set_day_len(int(k[1]))
                elif k[0] == 'max_pchg':
                        stra.set_max_pchg(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: info:min_shizhi=:max_shizhi=:min_tover=:max_tover=:min_amount=:max_amount=
def try_parse_info(type):
	from strategy.single.info import InfoStrategy
	stra = InfoStrategy()
	params = type.split(':')
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_shizhi':
                        stra.set_min_shizhi(float(k[1]))
		elif k[0] == 'max_shizhi':
			stra.set_max_shizhi(float(k[1]))
		elif k[0] == 'min_tover':
			stra.set_min_tover(float(k[1]))
		elif k[0] == 'max_tover':
			stra.set_max_tover(float(k[1]))
		elif k[0] == 'min_amount':
			stra.set_min_amount(float(k[1]))
		elif k[0] == 'max_amount':
			stra.set_max_amount(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	
	return stra

# example: hit_press:len=:min_pchg=0.0:max_pchg=10.0:type=high:min_dis=10:fix|fix_pchg=
def try_parse_hit_press(type):
	from strategy.single.hit_press import HitPressStrategy
	stra = HitPressStrategy()
	params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] in ['len','day_len']:
                        stra.set_day_len(int(k[1]))
                elif k[0] == 'min_pchg':
                        stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] in ['min_dis','min_distance']:
			stra.set_min_distance(int(k[1]))
		elif k[0] in ['fix','fix_pchg']:
			stra.set_fix_pchg(float(k[1]))
		elif k[0] == 'type':
			stra.set_type(k[1])
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: newhigh:len=10:min_pchg=0.0:max_pchg=10.0:type=high:min_dis=10:fix|fix_pchg=:start_len=
def try_parse_newhigh(type):
	from strategy.newhigh.newhigh import NewhighStrategy
	stra = NewhighStrategy()
	params = type.split(':')
	
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'len','day_len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'start','start_len' ]:
			stra.set_start_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
		elif k[0] in ['min_dis','min_distance']:
			stra.set_min_distance(int(k[1]))
		elif k[0] in [ 'fix','fix_pchg' ]:
			stra.set_fix_pchg(float(k[1]))
		elif k[0] == 'type':
			stra.set_type(k[1])
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: pchg_newhigh:len=:min_pchg=
def try_parse_pchg_newhigh(type):
	from strategy.newhigh.pchg_newhigh import PchgNewHighStrategy
	stra = PchgNewHighStrategy()
	params = type.split(':')
        
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
	return stra

# example: nh_trd
def try_parse_trd_newhigh(type):
	from strategy.newhigh.trd_newhigh import TrdNewHighStrategy
	stra = TrdNewHighStrategy()
	params = type.split(':')
        
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
	return stra


# example: v_newhigh:len=:rate=
def try_parse_v_newhigh(type):
	from strategy.newhigh.v_newhigh import VNewHighStrategy
	stra = VNewHighStrategy()
	params = type.split(':')
        
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'rate':
			stra.set_rate(float(k[1]))
	return stra

# example: v_newlow:len=:rate=
def try_parse_v_newlow(type):
	from strategy.single.v_newlow import VNewLowStrategy
	stra = VNewLowStrategy()
	params = type.split(':')
        
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'rate':
			stra.set_rate(float(k[1]))
	return stra

# example: newlow:len=:min_pchg=:max_pchg=:type=:min_dis=:use_low=:fix=
def try_parse_newlow(type):
	#print 'single_builder.try_parse_newlow,type: %s'%(type)

	from strategy.single.newlow import NewLowStrategy
	stra = NewLowStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] == 'min_pchg':
			stra.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			stra.set_max_pchg(float(k[1]))
		elif k[0] == 'min_dis':
			stra.set_min_distance(int(k[1]))
		elif k[0] == 'fix':
			stra.set_fix_pchg(float(k[1]))
		elif k[0] == 'type':
			stra.set_type(k[1])
		elif k[0] == 'use_low':
			b = True if k[1] in ['true','TRUE','True'] else False
			stra.set_use_low(b)
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return stra

# example: lower:max=
def try_parse_lower(type):
	from strategy.single.lower import LowerStrategy
	stra = LowerStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
		
	return stra

# example: higher:min=
def try_parse_higher(type):
	from strategy.single.higher import HigherStrategy
	stra = HigherStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'day_len','len' ]:
			stra.set_day_len(int(k[1]))
		elif k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			stra.set_max_pchg(float(k[1]))
		
	return stra

def get_seprate_params(type):
	if 'to_size' in type:
		return [],type.split(':')

        params = type.split(':')
        commons,uniques = [],[params[0]]
        for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'ma','ma_len','fix_chuangye','limit' ]:
#,'len']:
                        commons.append(p)
                else:
                        uniques.append(p)
        return commons,uniques

def demo():
	pass

if __name__ == "__main__":
	print demo()
