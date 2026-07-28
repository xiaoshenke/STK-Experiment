#!/usr/bin/python
# coding=utf-8

# 判断是否是@strategy.alias包下的类

import re
from util.df_util import empty
from util.param_util import fix_time_str

def is_wrap_alias_type(type,debug=False):
	if type.startswith('not'):
		return False

	if not type.startswith('not') and not type.startswith('not:') and not type.startswith( 'xls:' ) and not type.startswith('stocks:'):
		type = type.split(':')[0] 

	node = build_wrap_alias_one(type,debug)
	if debug:
		print u'wrap_alias_builder.is_wrap_alias_type node: %s'%(node)
	if not node:
		return False

	from strategy.alias.wrap_alias_strategy import WrapAliasStrategy
	if isinstance( node,WrapAliasStrategy ):
		if debug:
			print 'wrap_alias_builder.is_wrap_alias_type return True.'
		return True
	return False	

def build_wrap_alias_one(type,debug=False):
	stra = None

	if debug:
		print u'build_wrap_alias_one,before get_param_removed_type_by,type: %s'%(type)

	from util.param_util import get_param_from	
	from util.param_util import fix_day
	day = str(get_param_from(type.split(':'),'day',''))
	day = fix_day(day)        

	t2 = str(get_param_from(type.split(':'),'t2',''))

	limit = int(get_param_from(type.split(':'),'limit',-1))

	from util.param_util import get_param_removed_type_by
	type = get_param_removed_type_by(type,[ 't2','day','limit' ])

	# 处理一下.bf参数
	from strategy.stra.builder.param_util import get_bf_len_from
	bf_len = get_bf_len_from(type)
	if '.bf' in type:
		type = type.split('.bf')[0]

	name = ''
	if not type.startswith('xls:'):
		name = type.split(':')[0]
		name = name.replace('ppchg','pos_pchg')
	else:
		name = type

	from helper import to_str
	if debug:
		print u'build_wrap_alias_one,after get_param_removed_type_by,type: %s'%(type)
		print 'name:%s'%(name)

	#if type == 'diwei':
	#	stra = try_parse_diwei(type)
	if type == 'tidui12':
		stra = try_parse_tidui12(type)
	#elif type == 'qxb':
	#	stra = try_parse_qxb(type)
	elif type in [ 'qingxu2','Qingxu2' ]:
		stra = try_parse_qingxu_2(type)
	# update 2024-03-11: 不知道之前为什么会新增hw_qiche2
	#elif type in [ 'hw_qiche2' ]:
	#	stra = try_parse_hw_qiche_2(type)
	elif type in [ 'guancha_candidates' ]:
		stra = try_parse_guancha_candidates(type)
	elif type in [ 'rlbt','rongliang_baotuan' ]:
		stra = try_parse_rongliang_baotuan_1(type)
	elif type in [ 'rongliang','rl' ]:
		stra = try_parse_rongliang_1(type)
	elif type == 'db102s':
		stra = try_parse_db102s(type)
	elif type == 'db102s_2':
		stra = try_parse_db102s_2(type)
	elif type == 'db102s_3':
		stra = try_parse_db102s_3(type)
	elif type == 'xls:baotuan':
		stra = try_parse_baotuan_1(type)
	elif type == 'xls:zhuli':
		stra = try_parse_zhuli_1(type)
	# 高位趋势票
	elif type == 'xls:gqushi' or type == 'xls:qushi':
		stra = try_parse_xls_gqushi_1(type)
	elif type == 'xls:dqushi':
		stra = try_parse_xls_dqushi_1(type)
	elif type == 'xls:dqushi2':
		stra = try_parse_xls_dqushi_2(type)
	elif type == 'auto':
		stra = try_parse_auto_1(type)
	elif type == 'niu':
		stra = try_parse_niu_1(type)
	#elif type in [ 'xt','xt3' ]:
	#	stra = try_parse_xt3_1(type)
	#elif type == 'xt3_2' or type == 'xt_2' or type == 'Xt2':
	#	stra = try_parse_xt3_2(type)

	elif name in [ 'bd1','bound1' ]:
		stra = try_parse_bound_1(type)
	elif name in [ 'bd2','bound2' ]:
		stra = try_parse_bound_2(type)
	elif name in [ 'bd3','bound3' ]:
                stra = try_parse_bound_3(type)
	elif name in [ 'duanxt0','duan_xt0' ]:
		stra = try_parse_duan_xt_0(type)
	elif name in [ 'duanxt1','duan_xt1' ]:
		stra = try_parse_duan_xt_1(type)
	elif name in [ 'duanxt2','duan_xt2' ]:
		stra = try_parse_duan_xt_2(type)
	elif name in [ 'duanxt22','duan_xt22' ]:
                stra = try_parse_duan_xt_2_2(type)
	elif name in [ 'duanxt3','duan_xt3' ]:
		stra = try_parse_duan_xt_3(type)
	elif name in [ 'duanxt32','duan_xt32' ]:
		stra = try_parse_duan_xt_3_2(type)	
	elif name in [ 'duanxt4','duan_xt4' ]:
		stra = try_parse_duan_xt_4(type)
	elif name == 'xt1':
		stra = try_parse_xt_1(type)
	elif name == 'xt2':
		stra = try_parse_xt_2(type)
	elif name in [ 'xls:mapchg50','xls:ma_pchg50' ]:
		stra = try_parse_xls_ma_pchg50_1(type)
	elif name in [ 'xls:ppchg','xls:ppchg_1','xls:ppchg100','xls:ppchg100_1' ]:
		stra = try_parse_xls_ppchg_1(type)
	elif name in [ 'xls:ppchg_2','xls:ppchg100_2' ]:
		stra = try_parse_xls_ppchg_2(type)
	
	elif name in [ 'pos_pchg15','pos_pchg15_1' ]:
		stra = try_parse_pos_pchg15_1(type)
	elif name == 'pos_pchg15_2':
		stra = try_parse_pos_pchg15_2(type)
	elif name in [ 'pos_pchg25','pos_pchg25_1' ]:
		stra = try_parse_pos_pchg25_1(type)
	elif name in [ 'pos_pchg35','pos_pchg35_1' ]:
		stra = try_parse_pos_pchg35_1(type)
	elif name in [ 'pos_pchg45','pos_pchg45_1' ]:
                stra = try_parse_pos_pchg45_1(type)
	elif name in [ 'pos_pchg55','pos_pchg55_1' ]:
		stra = try_parse_pos_pchg55_1(type)
	elif type in [ 'baseshape','base_shape' ]:
		stra = try_parse_baseshape_1(type)
	elif type in [ 'baseshape2','base_shape2' ]:
		stra = try_parse_baseshape_2(type)
	elif type in [ 'baseshape3','base_shape3' ]:
		stra = try_parse_baseshape_3(type)
	elif type == 'weipiao' or name.startswith('weip'):
		stra = try_parse_weipiao_1(type)
	elif type == 'xls:xiaopiao' or type == 'xls:xp':
		stra = try_parse_xls_xiaopiao_1(type)
	elif type == 'xiaopiao' or name.startswith('xiaop'):
		stra = try_parse_xiaopiao_1(type)
	elif type == 'xls:dapiao':
		stra = try_parse_xls_dapiao_1(type)
	elif type == 'dapiao' or name.startswith('dap'):
		stra = try_parse_dapiao_1(type)
	elif type in [ 'zhongshizhi','zshizhi','zhongpiao' ]:
		stra = try_parse_zhongshizhi_1(type)
	elif type in [ 'xiaoshizhi','xshizhi','xiaopiao' ]:
		stra = try_parse_xiaoshizhi_1(type)
	elif type == 'shizhi10':	
		stra = try_parse_shizhi10_1(type)
	elif type == 'shizhi100':
		stra = try_parse_shizhi100_1(type)
	elif type == 'shizhi100_2':
		stra = try_parse_shizhi100_2(type)
	elif type == 'shizhi200_2':
		stra = try_parse_shizhi200_2(type)
	elif type == 'shizhi200':
		stra = try_parse_shizhi200_1(type)
	elif type == 'shizhi300':
		stra = try_parse_shizhi300_1(type)
	elif type == 'shizhi500':
		stra = try_parse_shizhi500_1(type)
	elif type == 'shizhi800':
		stra = try_parse_shizhi800_1(type)
	elif type == 'shizhi1000':
		stra = try_parse_shizhi1000_1(type)
	elif type == 'shizhi50' or type == 'shizhi40':
		stra = try_parse_shizhi50_1(type)
	elif type == 'shizhi20':
		stra = try_parse_shizhi20_1(type)
	elif type == 'shizhi30':
		stra = try_parse_shizhi30_1(type)
	elif type == 'tover20':
                stra = try_parse_tover20_1(type)
	elif type == 'tover25':
		stra = try_parse_tover25_1(type)
	elif type == 'lianghua' or type == 'liangh' or type == 'lh':
		stra = try_parse_lianghua_1(type)
	elif type in [ 'lsk1','lsk0' ]:
		stra = try_parse_lsk_1(type)
	elif type == 'codes_12ban':
		stra = try_parse_codes_12ban_1(type)
	elif type in [ '1p1','xls:1p1' ]:
		stra = try_parse_one_plus_one(type)
	#elif type in [ 'jinji','jinjisai' ]:
	#	stra = try_parse_jinjisai_1(type)
	#elif type.startswith( 'sjz' ) or type.startswith( 'shijianzhou' ) or type.startswith( 'shijianz' ) or type.startswith( 'shijian' ):
	#	stra = try_parse_shijianzhou(type)
	elif type in [ 'db100','db10_0' ]:
		stra = try_parse_db100_1(type)
	elif type == 'db103_2':
		stra = try_parse_db103_2(type)
	elif type in [ 'db103','db103_1' ]:
		stra = try_parse_db103_1(type)
	elif type in [ 'db104','db104_1' ]:
		stra = try_parse_db104_1(type)
	elif type == 'xls:db104':
		stra = try_parse_xls_db104_0(type)
	elif type == 'xls:db104_2':
		stra = try_parse_xls_db104_2(type)
	elif type == 'xls:db104_3':
		stra = try_parse_xls_db104_3(type)
	elif type in [ 'db105','db105_1' ]:
                stra = try_parse_db105_1(type)
	elif type in [ 'dlb4','dlb4_1' ]:
		stra = try_parse_dlb4_1(type)
	elif type == 'dlb4_2':
		stra = try_parse_dlb4_2(type)
	elif type == 'dlb62':
		stra = try_parse_dlb62_1(type)
	elif type == 'dlb82':
		stra = try_parse_dlb82_1(type)
	elif type == 'dlb83':
                stra = try_parse_dlb83_1(type)
	elif type == 'dlb103':
		stra = try_parse_dlb103_1(type)
	elif type == 'dlb153':
		stra = try_parse_dlb153_1(type)
	elif type in [ 'dlb3','dlb3_1' ]:
		stra = try_parse_dlb3_1(type)
	elif type == 'dlb3_2':
		stra = try_parse_dlb3_2(type)
	elif type == 'dlb3_3':
		stra = try_parse_dlb3_3(type)
	elif type == 'dlb3_4':
		stra = try_parse_dlb3_4(type)
	elif type == 'dlb42':
		stra = try_parse_dlb42_1(type)
	elif type == 'dlb52':
		stra = try_parse_dlb52_1(type)
	elif type in [ 'dlb2','dlb2_1' ]:
		stra = try_parse_dlb2_1(type)
	elif type == 'dlb2_2':
		stra = try_parse_dlb2_2(type)
	elif type == 'dlb2_3':
		stra = try_parse_dlb2_3(type)
	elif type == 'dlb2_4':
		stra = try_parse_dlb2_4(type)
	elif type == 'xls:db102':
		stra = try_parse_xls_db102_0(type)
	elif type == 'xls:db102_2':
		stra = try_parse_xls_db102_2(type)
	elif type == 'xls:db102_3':
                stra = try_parse_xls_db102_3(type)
	elif type.startswith('Db102_0') or type in [ 'Db102','db102','db102_0' ]:
		stra = try_parse_db102_0(type)
	elif type.startswith('Db102_1') or type == 'db102_1':
		stra = try_parse_db102_1(type)
	elif type.startswith('Db102_2') or type == 'db102_2':
		stra = try_parse_db102_2(type)
	elif type in [ 'db151','db151_0' ]:
		stra = try_parse_db151_0(type)
	elif type in [ 'db152','db152_0' ]:
                stra = try_parse_db152_0(type)
	elif type in [ 'db101','db101_0' ]:
		stra = try_parse_db101_0(type)
	elif type == 'db101_1':
		stra = try_parse_db101_1(type)
	elif type in [ 'db81','db81_0' ]:
		stra = try_parse_db81_0(type)
	elif type == 'db81_1':
		stra = try_parse_db81_1(type)
	elif type == 'db81_2':
		stra = try_parse_db81_2(type)
	elif type == 'xls:db82':
		stra = try_parse_xls_db82_0(type)
	elif type == 'xls:db82_2':
                stra = try_parse_xls_db82_2(type)
	elif type in [ 'db82','db82_0' ]:
                stra = try_parse_db82_0(type)
	elif type == 'db83':
		stra = try_parse_db83_0(type)
	elif type == 'db80':
		stra = try_parse_db80_1(type)
	elif type == 'db60':
		stra = try_parse_db60_1(type)
	elif type in [ 'db61','db61_0' ]:
		stra = try_parse_db61_0(type)
	elif type == 'db61_2' or type == 'db61_1':
		stra = try_parse_db61_2(type)
	elif type in [ 'db62','db62_0' ]:
		stra = try_parse_db62_0(type)
	elif type == 'db62_2' or type == 'db62_1':
		stra = try_parse_db62_2(type)
	elif type in [ 'xls:db62','xls:db62_1' ]:
		stra = try_parse_xls_db62_1(type)
	elif type == 'xls:db62_2':
		stra = try_parse_xls_db62_2(type)
	elif type == 'db63':
		stra = try_parse_db63_0(type)
	elif type == 'db64':	
		stra = try_parse_db64_0(type)
	elif type == 'db65':
		stra = try_parse_db65_0(type)
	elif type == 'longhu81':
		stra = try_parse_longhu81_1(type)
	#elif type == 'chaoduan3':
	#	stra = try_parse_chaoduan_3(type)
	#elif type == 'chaoduan2':
	#	stra = try_parse_chaoduan_2(type)
	#elif type in [ 'chaoduan','chaod','chaoduan1' ]:
	#	stra = try_parse_chaoduan_1(type)
	elif type in [ 'chaoduan0','chaoduan' ]:
		stra = try_parse_chaoduan_0(type)
	elif type == 'chaoduan2':
		stra = try_parse_chaoduan_2(type)
	elif name in [ 'fav','fav1' ]:
		stra = try_parse_fav1_1(type)
	elif type.startswith( 'fav' ) or type.startswith( 'ff' ):
		stra = try_parse_auto_fav_1(type)
	elif type in [ 'suov2','suov21' ]:
		stra = try_parse_suov21_1(type)
	elif type in [ 'suov3','suov31' ]:
		stra = try_parse_suov31_1(type)
	elif type in [ 'suov5','suov51' ]:
		stra = try_parse_suov51_1(type)
	elif name in [ 'baov2','baov21' ]:
		stra = try_parse_baov21_1(type)
	elif type in [ 'baov2_2' ]:
		stra = try_parse_baov21_2(type)
	elif name in [ 'baov3','baov31' ]:
		stra = try_parse_baov31_1(type)
	elif type in [ 'baov3_2','baov31_2' ]:
		stra = try_parse_baov31_2(type)
	elif type == 'baov42':
		stra = try_parse_baov42_1(type)
	elif type in [ 'baov5','baov51','baov51_0' ]:
		stra = try_parse_baov51_0(type)
	elif type == 'baov51_1':
		stra = try_parse_baov51_1(type)
	elif type == 'baov5_2':
		stra = try_parse_baov51_2(type)
	elif type == 'baov52':
		stra = try_parse_baov52_1(type)
	elif type in [ 'baov6','baov61' ]:
		stra = try_parse_baov61_1(type)
	elif type in [ 'baov7','baov71' ]:
		stra = try_parse_baov71_1(type)
	elif type in [ 'dov31','dov31_0' ]:
		stra = try_parse_dov31_1(type)
	elif type in [ 'dov51','dov51_0' ]:
		stra = try_parse_dov51_0(type)
	elif type == 'dov51_1':
		stra = try_parse_dov51_1(type)
	elif type == 'db95':
		stra = try_parse_db95_0(type)
	elif type == 'db75':
		stra = try_parse_db75_0(type)
	elif type == 'db76':
		stra = try_parse_db76_0(type)
	elif type == 'db86':
		stra = try_parse_db86_0(type)
	elif type == 'db87':
		stra = try_parse_db87_0(type)
	elif type == 'db108':
		stra = try_parse_db108_0(type)
	elif type == 'db50':
		stra = try_parse_db50_0(type)
	elif type in [ 'db55','db55_0' ]:
		stra = try_parse_db55_0(type)
	elif type in [ 'db53','db53_0' ]:
		stra = try_parse_db53_0(type)
	elif type == 'db53_2':
		stra = try_parse_db53_2(type)
	elif type in [ 'db54','db54_0' ]:
		stra = try_parse_db54_0(type)
	elif type.startswith('Db52_0') or type in [ 'Db52','db52' ]:
		stra = try_parse_db52_0(type)
	elif type.startswith('Db52_1') or type == 'db52_1':
		stra = try_parse_db52_1(type)
	elif type.startswith('Db52_2') or type == 'db52_2':
		stra = try_parse_db52_2(type)
	elif type.startswith('Db52_3'):
		stra = try_parse_db52_3(type)
	elif type.startswith( 'db51_amount' ):
		stra = try_parse_db51_amount_1(type)
	elif type == 'db51s_2':
		stra = try_parse_db51s_2(type)
	elif type == 'db51s':
		stra = try_parse_db51s(type)
	elif type in [ 'jin_db51','jindb51','db51_jin' ]:
		stra = try_parse_jin_db51_1(type)
	elif type in [ 'zhong_db51','db51_zhong' ]:
		stra = try_parse_zhong_db51_1(type)
	elif type in [ 'far_db51','yuan_db51','db51_far','db51_yuan' ]:
		stra = try_parse_far_db51_1(type)
	elif type == 'db51_0_2':
		stra = try_parse_db51_0_2(type)
	elif type.startswith('Db51_0') or type in [ 'db51_0','db51' ]:
		stra = try_parse_db51_0(type)
	elif type.startswith('Db51_1') or type in [ 'db51_1' ]:
		stra = try_parse_db51_1(type)
	elif type.startswith('Db51_2') or type == 'db51_2':
		stra = try_parse_db51_2(type)
	elif type == 'db51_3':
		stra = try_parse_db51_3(type)
	elif type == 'db10':
                stra = try_parse_db10_1(type)
	elif type == 'db20':
		stra = try_parse_db20_0(type)
	elif type == 'db21_2':
		stra = try_parse_db21_2(type)
	elif type == 'db21_1':
		stra = try_parse_db21_1(type)
	elif type in [ 'db21','db21_0' ]:
		stra = try_parse_db21_0(type)
	elif type == 'db22_2':
		stra = try_parse_db22_2(type)
	elif type == 'db22_1':
		stra = try_parse_db22_1(type)
	elif type == 'db22':
		stra = try_parse_db22_0(type)
	elif type == 'db40':
		stra = try_parse_db40_0(type)
	elif type in [ 'db43','db43_0' ]:
		stra = try_parse_db43_0(type)
	elif type == 'db43_1':
		stra = try_parse_db43_1(type)
	elif type == 'db43_2':
                stra = try_parse_db43_2(type)
	elif type in [ 'db41','db41_0' ]:
		stra = try_parse_db41_0(type)
	elif type in [ 'db42','db42_0' ]:
		stra = try_parse_db42_0(type)
	elif type == 'db42_1':
                stra = try_parse_db42_1(type)
	elif type == 'db42_2':
		stra = try_parse_db42_2(type)
	elif type in [ 'db44','db44_0' ]:
		stra = try_parse_db44_0(type)
	elif type == 'db44_1':
		stra = try_parse_db44_1(type)
	elif type in [ 'db33','db33_0' ]:
		stra = try_parse_db33_0(type)
	elif type == 'db33_1':
		stra = try_parse_db33_1(type)
	elif type in [ 'db32','db32_0' ]:
		stra = try_parse_db32_0(type)
	elif type == 'db32_1':
		stra = try_parse_db32_1(type)
	elif type == 'db32_2':
		stra = try_parse_db32_2(type)
	elif type == 'db30':
		stra = try_parse_db30_0(type)
	elif type in [ 'db31','db31_0' ]:
		stra = try_parse_db31_0(type)
	elif type == 'db31_1':
		stra = try_parse_db31_1(type)
	elif type in [ 'db31_2' ]:
		stra = try_parse_db31_2(type)
	elif type in [ 'db31_height','db31_height_1' ]:
		stra = try_parse_db31_height_1(type)
	elif type in [ 'height5' ]:
		stra = try_parse_height5_1(type)
	elif type in [ 'qidongs','qidong' ]:
		stra = try_parse_qidongs_1(type)
	elif type == 'qidong1':
		stra = try_parse_qidong_1(type)
	elif type == 'dis01':
		stra = try_parse_dis01_0(type)
	elif type == 'dis01_2':
		stra = try_parse_dis01_2(type)
	elif type == 'dis02':
		stra = try_parse_dis02_0(type)
	elif type == 'dis02_2':
		stra = try_parse_dis02_2(type)
	elif type == 'dis03':
		stra = try_parse_dis03_0(type)
	elif type == 'dis14':
                stra = try_parse_dis14_0(type)
	elif type == 'dis2':
		stra = try_parse_dis2_0(type)
	elif type == 'dis24':
		stra = try_parse_dis24_0(type)
	elif type == 'dis25':
		stra = try_parse_dis25_0(type)
	elif type == 'dis26':
		stra = try_parse_dis26_0(type)
	elif type == 'dis27':
		stra = try_parse_dis27_0(type)
	elif type == 'dis3':
		stra = try_parse_dis3_0(type)
	elif type == 'dis36':
		stra = try_parse_dis36_0(type)
	elif type == 'dis37':
		stra = try_parse_dis37_0(type)
	elif type == 'dis4':
		stra = try_parse_dis4_0(type)
	elif name == 'dis5':
		stra = try_parse_dis5_0(type)
	elif type == 'dis59':
		stra = try_parse_dis59_0(type)
	elif name == 'dis6':
		stra = try_parse_dis6_0(type)
	elif type == 'dis8':
		stra = try_parse_dis8_0(type)
	elif type == 'dis9':
		stra = try_parse_dis9_0(type)
	elif name in [ '1lyin','lyin1','1lianyin','lianyin1' ]:
		stra = try_parse_lianyin1_1(type)
	elif name in [ '1lyin_2','lyin1_2','1lianyin_2','lianyin1_2' ]:
		stra = try_parse_lianyin1_2(type)
	elif name in [ '2lyin','lyin2','2lianyin','lianyin2' ]:
		stra = try_parse_lianyin2_1(type)
	elif name in [ '3lyin','lyin3','3lianyin','lianyin3' ]:
		stra = try_parse_lianyin3_1(type)
	elif name in [ '4lyin','lyin4','4lianyin','lianyin4' ]:
		stra = try_parse_lianyin4_1(type)
	elif name in [ '1lyang','lyang1','1lianyang','lianyang1' ]:
		stra = try_parse_lianyang1_1(type)
	elif name in [ '1lyang_2','lyang1_2','1lianyang_2','lianyang1_2' ]:
		stra = try_parse_lianyang1_2(type)
	elif name in [ '2lyang','lyang2','2lianyang','lianyang2' ]:
		stra = try_parse_lianyang2_1(type)
	elif name in [ '3lyang','lyang3','3lianyang','lianyang3' ]:
		stra = try_parse_lianyang3_1(type)
	elif name == 'upma03':
		stra = try_parse_upma03_1(type)
	elif name == 'upma36':
		stra = try_parse_upma36_1(type)
	elif name == 'upma6':
		stra = try_parse_upma6_1(type)
	elif type == 'dtrd3_1':
		stra = try_parse_dtrd3_1(type)
	elif type == 'dtrd3_2':
		stra = try_parse_dtrd3_2(type)
	elif type == 'dtrd32_1' or type == 'dtrd32':
		stra = try_parse_dtrd32_1(type)
	elif type == 'dtrd32_4':
		stra = try_parse_dtrd32_4(type)
	elif type == 'dtrd32_7':
		stra = try_parse_dtrd32_7(type)
	elif type == 'dtrd53' or type == 'dtrd53_1':
		stra = try_parse_dtrd53_1(type)
	elif type == 'dtrd52' or type == 'dtrd52_1':
		stra = try_parse_dtrd52_1(type)
	elif type in [ 'outv1','outv_1' ]:
		stra = try_parse_outv_1(type)
	elif type in [ 'outv2','outv_2' ]:
		stra = try_parse_outv_2(type)
	elif type == 'outvs':
		stra = try_parse_outvs(type)
	#elif name == 'qushi' or type.startswith( 'qushi:' ):
	#	stra = try_parse_qushi(type) 
	elif type in [ 'qushi1' ]:
		stra = try_parse_qushi_1(type)
	elif type == 'qushi2':
		stra = try_parse_qushi_2(type)
	elif type in [ 'qstop','qushitop','qushi_top' ]:
		stra = try_parse_qushi_top_1(type)
	elif type in [ 'qsup2','qushiup2','qushi_up2' ]:
		stra = try_parse_qushi_up_2(type)
	elif name in [ 'qsup','qushiup','qushi_up' ]:
		stra = try_parse_qushi_up_1(type)
	elif type in [ 'qsgood2','qushigood2','qushi_good2' ]:
		stra = try_parse_qushi_good_2(type)
	elif type in [ 'qsgood','qushigood','qushi_good' ]:
		stra = try_parse_qushi_good_1(type)
	elif type in [ 'qsbad','qushibad','qushi_bad' ]:
                stra = try_parse_qushi_bad_1(type)
	# 趋势龙
	elif type in [ 'qslong','qsl','qushilong' ]:
		stra = try_parse_qushilong_1(type)
	elif type in [ 'tph','tph1','tph2' ] or type.startswith( 'tph:' ) or type.startswith( 'thp1:' ) or type.startswith( 'tph2:' ):
		stra = try_parse_top_height_1(type)
	elif type in [ 'sanhu1' ]:
		stra = try_parse_sanhu_1(type)
	elif type in [ 'sanhu2' ]:
		stra = try_parse_sanhu_2(type)
	elif type in [ 'youzi1' ]:
		stra = try_parse_youzi_1(type)
	elif type in [ 'youzi2' ]:
		stra = try_parse_youzi_2(type)
	elif type in [ 'youzi3' ]:
		stra = try_parse_youzi_3(type)
	elif type in [ 'youzi4' ]:
		stra = try_parse_youzi_4(type)
	elif type == 'qsrls':
		stra = try_parse_qsrls(type)
	elif type in [ 'qsrl','qsrl1' ]:
		stra = try_parse_qsrl_1(type)
	elif type == 'qsrl2':
		stra = try_parse_qsrl_2(type)
	elif type == 'breaks':
		stra = try_parse_breaks(type)
	elif type == 'breakups':
		stra = try_parse_breakups(type)
	elif type == 'stocks:zhongjun':
		stra = try_parse_stocks_zhongjun_1(type)
	elif type == 'zhongpiaos':
		stra = try_parse_zhongpiaos(type)
	elif type in [ 'zhongpiao','zhongpiao_1','zp','zp1' ]:
		stra = try_parse_zhongpiao_1(type)
	elif type in [ 'zhongpiao2' ]:
		stra = try_parse_zhongpiao_2(type)
	elif type == 'zhongpiao3':
		stra = try_parse_zhongpiao_3(type)
	elif type in [ 'huoyue','huoyue1' ]:
		stra = try_parse_huoyue_1(type)
	elif type in [ 'ignore','ignores' ]:
		stra = try_parse_ignores_1(type)
	elif type in [ 'not:ignores','not_ignores','not:ignore','nignores' ]:
		stra = try_parse_not_ignores(type)
	elif type in [ 'new_dgx','new_dgx_1' ]:
		stra = try_parse_new_dgx_1(type)
	elif type in [ 'nnh','nnh1' ]:
		stra = try_parse_near_newhigh_1(type)
	elif type == 'nnh2':
		stra = try_parse_near_newhigh_2(type)
	elif type == 'shangy3':
		stra = try_parse_shangy3_1(type)
	elif type == 'shangy5':
		stra = try_parse_shangy5_1(type)
	#elif type == 'shangy2' or type == 'Shangy2':
	#	stra = try_parse_shangy_2(type)
	elif type == 'upbound1':
		stra = try_parse_upbound_1(type)
	elif type == 'upbound2':
		stra = try_parse_upbound_2(type)
	elif type in [ 'cores2','cores_2' ]:
		stra = try_parse_cores_2(type)
	elif type == 'cores':
		stra = try_parse_cores(type)
	elif type == 'core':
		stra = try_parse_auto_core_1(type)
	elif type == 'core1' or type == 'core':
		stra = try_parse_core_1(type)
	elif type == 'core2':
		stra = try_parse_core_2(type)
	elif type == 'core3':
		stra = try_parse_core_3(type)
	elif type in [ 'level1','levle1','lv1' ]: 
		stra = try_parse_level_1(type)
	elif type in [ 'level2','levle2','lv2' ]: 
		stra = try_parse_level_2(type)
	elif type in [ 'level3','levle3','lv3' ]: 
		stra = try_parse_level_3(type)
	elif type == 'base':
		stra = try_parse_base_0(type)
	elif type == 'base1':
		stra = try_parse_base_1(type)
	elif type == 'base2':
		stra = try_parse_base_2(type)
	elif type == 'base3':
		stra = try_parse_base_3(type)
	#elif type == 'base4':
	#	stra = try_parse_base_4(type)
	elif type in [ 'pos15','pos15_1' ]:
		stra = try_parse_pos15_1(type)
	elif type in [ 'shape','shape0' ]:
		stra = try_parse_shape_0(type)
	elif type == 'shape1':
		stra = try_parse_shape_1(type)
	elif type == 'shape2':
		stra = try_parse_shape_2(type)
	elif type == 'shape3':
		stra = try_parse_shape_3(type)
	elif type == 'shape4':
		stra = try_parse_shape_4(type)
	elif type == 'pool1':
		stra = try_parse_pool_1(type)
	elif type == 'pool2':
		stra = try_parse_pool_2(type)
	elif type == 'duan':
		stra = try_parse_duan(type)
	elif type in [ 'hexin1' ]:
		stra = try_parse_hexin_1(type)
	elif type == 'hexin2':
		stra = try_parse_hexin_2(type)
	elif type == 'hexin3':
		stra = try_parse_hexin_3(type)
	elif type == 'hexins':
		stra = try_parse_hexins(type)	
	elif type in [ 'top_amount300','tamount300' ]:
                stra = try_parse_top_amount300_1(type)
	elif type in [ 'top_amount200','tamount200' ]:
		stra = try_parse_top_amount200_1(type)
	elif type in [ 'top_amount100','tamount100' ]:
                stra = try_parse_top_amount100_1(type)
	elif type in [ 'top_amount50','tamount50' ]:
		stra = try_parse_top_amount50_1(type)
	elif type in [ 'top_amount60','tamount60' ]:
                stra = try_parse_top_amount60_1(type)
	elif type in [ 'top_amount10','tamount10' ]:
		stra = try_parse_top_amount10_1(type)
	elif type in [ 'top_amount15','tamount15' ]:
		stra = try_parse_top_amount15_1(type)
	elif type in [ 'top_amount20','tamount20' ]:
		stra = try_parse_top_amount20_1(type)
	elif type in [ 'top_amount30','tamount30' ]:
		stra = try_parse_top_amount30_1(type)
	elif type.startswith( 'auto_amount' ) or type.startswith( 'aamount' ) or type.startswith( 'xamount' ):
		stra = try_parse_auto_amount_1(type)
	elif type == 'xls:amount':
		stra = try_parse_xls_amount_1(type)
	elif type == 'xls:amount2':
		stra = try_parse_xls_amount_2(type)
	elif type == 'amount3':
		stra = try_parse_amount3_1(type)
	elif type == 'amount5':
                stra = try_parse_amount5_1(type)
	elif type == 'amount10':
		stra = try_parse_amount10_1(type)
	elif type == 'amount15':
                stra = try_parse_amount15_1(type)
	elif type == 'amount20':
		stra = try_parse_amount20_1(type)
	elif type == 'amount30':
		stra = try_parse_amount30_1(type)
	elif type == 'amount50':
		stra = try_parse_amount50_1(type)
	elif type in [ 'xls:hexin','xls:hexin1' ]:
		stra = try_parse_xls_hexin_1(type)
	elif type == 'xls:hexin2':
		stra = try_parse_xls_hexin_2(type)
	elif type == 'xls:hexin3':
		stra = try_parse_xls_hexin_3(type)
	elif type in [ 'dst21' ]:
		stra = try_parse_dst21(type)
	elif type == 'dst22':
		stra = try_parse_dst22(type)
	elif type == 'dst32':
		stra = try_parse_dst32(type)
	elif type == 'dst42':
		stra = try_parse_dst42(type)
	elif type in [ 'autodgx','auto_dgx','adgx' ]:
		stra = try_parse_auto_dgx_1(type)
	elif type == 'dgx0':
		stra = try_parse_dgx0(type)
	elif type == 'dgx0_2':
		stra = try_parse_dgx0_2(type)
	elif type == 'dgx1' or type == 'dgx':
		stra = try_parse_dgx1(type)
	elif type == 'dgx1_2' or type == 'dgx_2':
		stra = try_parse_dgx1_2(type)
	elif type == 'dgx1_3':
		stra = try_parse_dgx1_3(type)
	elif type == 'dgx2':
		stra = try_parse_dgx2(type)
	elif type == 'dgx2_2':
		stra = try_parse_dgx2_2(type)
	elif type == 'dgx3':
		stra = try_parse_dgx3(type)
	elif type == 'dgx3_1':
                stra = try_parse_dgx3_1(type)
	elif type == 'dgx3_2':
		stra = try_parse_dgx3_2(type)
	elif type == 'dgx4':
		stra = try_parse_dgx4(type)
	elif type == 'dgx4_1':
		stra = try_parse_dgx4_1(type)
	elif type == 'dgx42' or type == 'dgx4_2':
		stra = try_parse_dgx42_1(type)
	elif type == 'dgx5_2':
		stra = try_parse_dgx5_2(type)
	elif type == 'dgx5':
		stra = try_parse_dgx5(type)
	elif type == 'dgx6':
		stra = try_parse_dgx6(type)
	elif type == 'guxing1':
		stra = try_parse_guxing1(type)
	elif name == 'maxtrd7' or name == 'max_trd7':
		stra = try_parse_max_trd7(type)
	elif name == 'maxtrd3' or name == 'max_trd3':
		stra = try_parse_max_trd3(type)
	elif name == 'maxtrd36' or name == 'max_trd36':
		stra = try_parse_max_trd36(type)
	elif name == 'maxtrd37' or name == 'max_trd37':
		stra = try_parse_max_trd37(type)
	elif name == 'maxtrd38' or name == 'max_trd38':
                stra = try_parse_max_trd38(type)
	elif name == 'maxtrd39' or name == 'max_trd39':
		stra = try_parse_max_trd39(type)
	elif name == 'maxtrd59' or name == 'max_trd59':
		stra = try_parse_max_trd59(type)
	elif name == 'maxtrd5' or name == 'max_trd5':
		stra = try_parse_max_trd5(type)
	elif name == 'maxtrd4' or name == 'max_trd4':
		stra = try_parse_max_trd4(type)
	elif type in [ 'lazhu2' ] or type.startswith( 'lazhu2' ):
		stra = try_parse_lazhu2(type)
	elif type in [ 'lazhu','lazhu1' ] or type.startswith('lazhu'):
		stra = try_parse_lazhu1(type)
	#elif type == 'pan11':
	#	stra = try_parse_pan11(type)
	#elif type == 'pan12':
	#	stra = try_parse_pan12(type)
	#elif type == 'pan1':
	#	stra = try_parse_pan1(type)
	#elif type == 'pan2':
	#	stra = try_parse_pan2(type)
	#elif type == 'pan3':
	#	stra = try_parse_pan3(type)
	#elif type == 'pan4':
	#	stra = try_parse_pan4(type)
	#elif type == 'pan':
	#	stra = try_parse_pan(type)
	elif type in [ 'xls:outv','xls:outv1' ]:
		stra = try_parse_xls_outv_1(type)
	elif type == 'xls:outv2':
		stra = try_parse_xls_outv_2(type)
	elif type in [ 'xls:mao1','xls:mao' ]:
		stra = try_parse_xls_mao_1(type)
	elif type == 'xls:mao2':
		stra = try_parse_xls_mao_2(type)
	#elif type in [ 'xls:zhongwei0' ]:
	#	stra = try_parse_xls_zhongwei_0(type)
	#elif type in [ 'xls:zhongwei','xls:zhongwei1' ]:
	#	stra = try_parse_xls_zhongwei_1(type)
	#elif type == 'xls:gaowei':
	#	stra = try_parse_xls_gaowei_1(type)
	#elif type == 'xls:gaowei2':
	#	stra = try_parse_xls_gaowei_2(type)
	#elif type == 'gaowei':
	#	stra = try_parse_gaowei_1(type)
	#elif type in [ 'xls:zgwei','xls:zhonggao','zhonggao','xls:zhongao','zhongao' ]:
	#	stra = try_parse_xls_zgwei_1(type)
	#elif name == 'diwei':
	#	stra = try_parse_diwei_1(type)
	#elif type == 'xls:diwei2':
	#	stra = try_parse_xls_diwei_2(type)
	#elif type == 'xls:diwei':
	#	stra = try_parse_xls_diwei_1(type)
	elif type == 'xls:ban5up':
		stra = try_parse_xls_ban5up_1(type)
	elif type == 'xls:ban4up':
		stra = try_parse_xls_ban4up_1(type)
	elif type == 'xls:chaoduan2':
		stra = try_parse_xls_chaoduan_2(type)
	elif type == 'xls:chaoduan':
		stra = try_parse_xls_chaoduan_1(type)
	elif type == 'stocks:main2' or type == 'main2':
		stra = try_parse_stocks_main_2(type)
	elif type in [ 'main','main1' ]:
		stra = try_parse_stocks_main_1(type)
	elif type == 'dijia':
		stra = try_parse_dijia_1(type)
	#elif type == 'maoding' or type == 'maodings':
	#	stra = try_parse_maoding_1(type)
	#elif type == 'maodians_2':
	#	stra = try_parse_maodians_2(type)
	#elif type == 'maodians':
	#	stra = try_parse_maodians_1(type)
	elif type == 'mao1':
		stra = try_parse_mao1(type)
	elif type == 'mao2':
		stra = try_parse_mao2(type)
	elif type == 'mao3':
		stra = try_parse_mao3(type)
	elif type == 'mao11':
		stra = try_parse_mao11(type)
	elif type == 'mao12':
		stra = try_parse_mao12(type)
	#elif type.startswith('sanhu1'):
	#	stra = try_parse_sanhu1(type)
	#elif type.startswith('sanhu2'):
	#	stra = try_parse_sanhu2(type)
	#elif type.startswith('Trd3_1') or type == 'Trd3' or type.startswith('Trd3:'):
	#	stra = try_parse_trd3_1(type)
	#elif type.startswith('Trd3_2') or type == 'trd3s_2':
	#	stra = try_parse_trd3s_2(type)
	#elif type.startswith('Trd3_3') or type == 'trd3s_3':
	#	stra = try_parse_trd3s_3(type)
	#elif type.startswith('Trd3_4') or type == 'trd3s_4':
	#	stra = try_parse_trd3s_4(type)

	elif name in [ 'trdsum05','trd_sum05' ]:
		stra = try_parse_trd_sum_05_1(type)
	elif type in [ 'trdsum3','trd_sum3' ]:
		stra = try_parse_trd_sum_3_1(type)
	elif type in [ 'trdsum38','trd_sum38' ]:
		stra = try_parse_trd_sum_38_1(type)
	elif type in [ 'trdsum5','trd_sum5','Trd5' ]:
		stra = try_parse_trd_sum_5_1(type)
	elif type in [ 'trdsum8','trd_sum8','Trd8' ]:
		stra = try_parse_trd_sum_8_1(type)
	elif type in [ 'trdsum14','trd_sum14','Trd14' ]:
		stra = try_parse_trd_sum_14_1(type)
	elif type in [ 'trdsum18','trd_sum18','Trd18' ]:
                stra = try_parse_trd_sum_18_1(type)
	elif type == 'trd3':
		stra = try_parse_trd3_1(type)
	elif type == 'trd4':
		stra = try_parse_trd4_1(type)
	elif type == 'trd9':
		stra = try_parse_trd9_1(type)
	elif type.startswith('trd1_1'):
		stra = try_parse_trd_1(type)
	elif type.startswith('trd1_2') or type.startswith('Trd1_2'):
		stra = try_parse_trd_2(type)
	elif type.startswith('Trd2_1') or type == 'Trd2' or type.startswith('Trd2:'):
		stra = try_parse_trd2_1(type)
	elif type.startswith('Trd2_2'):
		stra = try_parse_trd2_2(type)
	elif name in [ 'inxt1','in_xt1' ]:
		stra = try_parse_in_xt1_1(type)
	elif name in [ 'inxt2','in_xt2' ]:
		stra = try_parse_in_xt2_1(type)
	elif type == 'chaoda':
		stra = try_parse_chaoda(type)
	elif type == 'dapiao':
		stra = try_parse_dapiao(type)	
	
	elif type.startswith('Outv_1') or type == 'Outv' or type.startswith('Outv:'):
		stra = try_parse_Outv_1(type)
	elif type.startswith('Dsy_1') or type == 'Dsy' or type.startswith('Dsy:') or type in [ 'dsy','dsy_1' ]:
		stra = try_parse_dsy_1(type)
	elif type.startswith('Tiao_0') or type == 'Tiao' or type.startswith('Tiao:'):
		stra = try_parse_tiao_0(type)
	#elif type.startswith('Shangy_1') or type == 'Shangy' or type.startswith('Shangy:'):
	#	stra = try_parse_shangy_1(type)
	elif type == 'shiti4':
		stra = try_parse_trd4_1(type)

	if not stra:
		return None

	if day:
		stra.set_day(day)
	if t2:
		stra.set_t2(t2)
	if bf_len > 0:
		stra.set_bf_len(bf_len)
	if limit > 0:
		stra.set_limit(limit)
	return stra

def get_bf_len_from2(type):
	#print u'wrap_alias_builder.get_bf_len_from,type:%s'%(type)

	if not '.bf' in type:
		return 0
        l = 1
	if type.index('.bf')+len('.bf') < len(type):
		l = int(type[type.index('.bf')+len('.bf'):])
	return l 

# example: auto
def try_parse_auto_1(type):
	from strategy.alias.autos_1 import Auto_1Strategy
	stra = Auto_1Strategy()
	return stra

# example: niu
def try_parse_niu_1(type):
	from strategy.alias.nius_1 import Niu_1Strategy
	stra = Niu_1Strategy()
	return stra

# example: xls:mapchg50
def try_parse_xls_ma_pchg50_1(type):
	from strategy.alias.ma_pchgs_1 import XlsMaPchg50_1Strategy
	stra = XlsMaPchg50_1Strategy()
	return stra

# example: xls:ppchg
def try_parse_xls_ppchg_1(type):
	from strategy.alias.pos_pchgs_1 import XlsPosPchg100_1Strategy
	stra = XlsPosPchg100_1Strategy()
	return stra

# example: xls:ppchg_2
def try_parse_xls_ppchg_2(type):
	from strategy.alias.pos_pchgs_1 import XlsPosPchg100_2Strategy
	stra = XlsPosPchg100_2Strategy()
	return stra

# example: pos_pchg15
def try_parse_pos_pchg15_1(type):
	from strategy.alias.pos_pchgs_1 import PosPchg15_1Strategy
	stra = PosPchg15_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: pos_pchg15_2
def try_parse_pos_pchg15_2(type):
	from strategy.alias.pos_pchgs_1 import PosPchg15_2Strategy
	stra = PosPchg15_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: pos_pchg25
def try_parse_pos_pchg25_1(type):
	from strategy.alias.pos_pchgs_1 import PosPchg25_1Strategy
	stra = PosPchg25_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: pos_pchg35
def try_parse_pos_pchg35_1(type):
	from strategy.alias.pos_pchgs_1 import PosPchg35_1Strategy
	stra = PosPchg35_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: pos_pchg45
def try_parse_pos_pchg45_1(type):
	from strategy.alias.pos_pchgs_1 import PosPchg45_1Strategy
	stra = PosPchg45_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: pos_pchg55
def try_parse_pos_pchg55_1(type):
	from strategy.alias.pos_pchgs_1 import PosPchg55_1Strategy
	stra = PosPchg55_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: in_xt1:len=
def try_parse_in_xt1_1(type):
	from strategy.alias.in_xts_1 import InXt1_Strategy
	stra = InXt1_Strategy()
	
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra
	
# example: in_xt2:len=
def try_parse_in_xt2_1(type):
	from strategy.alias.in_xts_1 import InXt2_Strategy
	stra = InXt2_Strategy()
	
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra
	
# example: dijia
def try_parse_dijia_1(type):
	from strategy.alias.dijia_1 import Dijia_1Strategy
	stra = Dijia_1Strategy()
	return stra

# example: chaoda
def try_parse_chaoda(type):
	from strategy.alias.chaoda_1 import Chaoda_1Strategy
	stra = Chaoda_1Strategy()
	return stra

# example: dapiao
def try_parse_dapiao(type):
	from strategy.alias.dapiao import DapiaoStrategy
	stra = DapiaoStrategy()
	return stra

# example: Qingxu2
def try_parse_qingxu_2(type):
	from strategy.alias.qingxu_2 import Qingxu_2Strategy
	return Qingxu_2Strategy()

# example: hw_qiche2
def try_parse_hw_qiche_2(type):
	from strategy.alias.hw_qiche_2 import HwQiche_2Strategy
	return HwQiche_2Strategy()

# example: bound1:len=
def try_parse_bound_1(type):
	from strategy.alias.bounds_1 import Bound_1Strategy
	stra = Bound_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: bound2:len=
def try_parse_bound_2(type):
	from strategy.alias.bounds_1 import Bound_2Strategy
	stra = Bound_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: bound3:len=
def try_parse_bound_3(type):
	from strategy.alias.bounds_1 import Bound_3Strategy
	stra = Bound_3Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt0:len=
def try_parse_duan_xt_0(type):
	from strategy.alias.duan_xts_1 import Duanxt_0Strategy
	stra = Duanxt_0Strategy()
	
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt1:len=
def try_parse_duan_xt_1(type):
	from strategy.alias.duan_xts_1 import Duanxt_1Strategy
	stra = Duanxt_1Strategy()
	
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt2:len=
def try_parse_duan_xt_2(type):
	from strategy.alias.duan_xts_1 import Duanxt_2Strategy
	stra = Duanxt_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt22:len=
def try_parse_duan_xt_2_2(type):
	from strategy.alias.duan_xts_1 import Duanxt_2_2Strategy
	stra = Duanxt_2_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt3:len=
def try_parse_duan_xt_3(type):
	from strategy.alias.duan_xts_1 import Duanxt_3Strategy
	stra = Duanxt_3Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt32:len=
def try_parse_duan_xt_3_2(type):
	from strategy.alias.duan_xts_1 import Duanxt_3_2Strategy
	stra = Duanxt_3_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: duanxt4:len=
def try_parse_duan_xt_4(type):
	from strategy.alias.duan_xts_1 import Duanxt_4Strategy
	stra = Duanxt_4Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: xt1:len=
def try_parse_xt_1(type):
	from strategy.alias.xts_1 import Xt_1Strategy
	stra = Xt_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: xt2:len=
def try_parse_xt_2(type):
	from strategy.alias.xts_1 import Xt_2Strategy
	stra = Xt_2Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: xt|xt3
def try_parse_xt3_1(type):
	from strategy.alias.xts_1 import Xt3_1Strategy
	return Xt3_1Strategy()

# example: xt_2|xt3_2
def try_parse_xt3_2(type):
	from strategy.alias.xts_1 import Xt3_2Strategy
	return Xt3_2Strategy()

# example: guancha_candidates
def try_parse_guancha_candidates(type):
	from strategy.alias.guancha_candidates_1 import Guancha_Candidates_1Strategy
	stra = Guancha_Candidates_1Strategy()
	return stra

# example: rl
def try_parse_rongliang_1(type):
	from strategy.alias.rongliangs_1 import Rongliang_1Strategy
	stra = Rongliang_1Strategy()
	return stra

# example: rlbt 容量抱团
def try_parse_rongliang_baotuan_1(type):
	from strategy.alias.rongliangs_1 import RongliangBaotuan_1Strategy
	stra = RongliangBaotuan_1Strategy()
	return stra

# example: baseshape
def try_parse_baseshape_1(type):
	from strategy.alias.baseshapes_1 import BaseShapes_1Strategy
	stra = BaseShapes_1Strategy()
	return stra

# example: baseshape2
def try_parse_baseshape_2(type):
	from strategy.alias.baseshapes_1 import BaseShapes_2Strategy
	stra = BaseShapes_2Strategy()
	return stra

# example: baseshape3
def try_parse_baseshape_3(type):
	from strategy.alias.baseshapes_1 import BaseShapes_3Strategy
	stra = BaseShapes_3Strategy()
	return stra

# example: xls:ban5up
def try_parse_xls_ban5up_1(type):
	from strategy.alias.xls_ban5up_1 import XlsBan5up_1Strategy
	stra = XlsBan5up_1Strategy()
	return stra

# example: xls:ban4up
def try_parse_xls_ban4up_1(type):
	from strategy.alias.xls_ban4up_1 import XlsBan4up_1Strategy
	stra = XlsBan4up_1Strategy()
	return stra

# example: tidui12
def try_parse_tidui12(type):
	from strategy.alias.tidui12_1 import Tidui12_1Strategy
	stra = Tidui12_1Strategy()
	return stra

# example: qxb
def try_parse_qxb(type):
	from strategy.comp.comp_qxb import CompQxb
	stra = CompQxb()
	return stra

# example: shijianzhou:len=:day=
def try_parse_shijianzhou(type):
	from strategy.alias.shijianzhou_strategy import ShijianzhouStrategy
	stra = ShijianzhouStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
		elif k[0] == 'day':
			from util.param_util import fix_day
			day = fix_day(k[1])
			stra.set_day(day)
	return stra

# example: codes_12ban
def try_parse_codes_12ban_1(type):
	from strategy.alias.codes_12ban_1 import Codes12Ban_1Strategy
	stra = Codes12Ban_1Strategy()
	return stra

# example: weipiao
def try_parse_weipiao_1(type):
	from strategy.alias.shizhis_1 import Weipiao_1Strategy
	stra = Weipiao_1Strategy()
	return stra

# example: xiaoshizhi
def try_parse_xiaoshizhi_1(type):
	from strategy.alias.shizhis_1 import XiaoShizhi_1Strategy
	stra = XiaoShizhi_1Strategy()
	return stra

# example: xiaopiao
def try_parse_xiaopiao_1(type):
	from strategy.alias.shizhis_1 import Xiaopiao_1Strategy
	stra = Xiaopiao_1Strategy()
	return stra

# example: xls:xiaopiao|xls:xp
def try_parse_xls_xiaopiao_1(type):
	from strategy.alias.shizhis_1 import XlsXiaopiao_1Strategy
	stra = XlsXiaopiao_1Strategy()
	return stra

# example: xls:dapiao
def try_parse_xls_dapiao_1(type):
	from strategy.alias.shizhis_1 import XlsDapiao_1Strategy
	stra = XlsDapiao_1Strategy()
	return stra

# example: dapiao
def try_parse_dapiao_1(type):
	from strategy.alias.shizhis_1 import Dapiao_1Strategy
	stra = Dapiao_1Strategy()
	return stra

# example: zhongpiao|zhongshizhi
def try_parse_zhongshizhi_1(type):
	from strategy.alias.shizhis_1 import ZhongShizhi_1Strategy
	stra = ZhongShizhi_1Strategy()
	return stra

# example: shizhi10
def try_parse_shizhi10_1(type):
	from strategy.alias.shizhis_1 import Shizhi10_1Strategy
	stra = Shizhi10_1Strategy()
	return stra

# example: shizhi100
def try_parse_shizhi100_1(type):
	from strategy.alias.shizhis_1 import Shizhi100_1Strategy
	stra = Shizhi100_1Strategy()
	return stra

# example: shizhi100_2
def try_parse_shizhi100_2(type):
	from strategy.alias.shizhis_1 import Shizhi100_2Strategy
	stra = Shizhi100_2Strategy()
	return stra

# example: shizhi200
def try_parse_shizhi200_1(type):
	from strategy.alias.shizhis_1 import Shizhi200_1Strategy
	stra = Shizhi200_1Strategy()
	return stra

# example: shizhi200_2
def try_parse_shizhi200_2(type):
	from strategy.alias.shizhis_1 import Shizhi200_2Strategy
	stra = Shizhi200_2Strategy()
	return stra

# example: shizhi300
def try_parse_shizhi300_1(type):
	from strategy.alias.shizhis_1 import Shizhi300_1Strategy
	stra = Shizhi300_1Strategy()
	return stra

# example: shizhi500
def try_parse_shizhi500_1(type):
	from strategy.alias.shizhis_1 import Shizhi500_1Strategy
	stra = Shizhi500_1Strategy()
	return stra

# example: shizhi800
def try_parse_shizhi800_1(type):
	from strategy.alias.shizhis_1 import Shizhi800_1Strategy
	stra = Shizhi800_1Strategy()
	return stra

# example: shizhi1000
def try_parse_shizhi1000_1(type):
	from strategy.alias.shizhis_1 import Shizhi1000_1Strategy
	stra = Shizhi1000_1Strategy()
	return stra

# example: shizhi50
def try_parse_shizhi50_1(type):
	from strategy.alias.shizhis_1 import Shizhi50_1Strategy
	stra = Shizhi50_1Strategy()
	return stra

# example: shizhi20
def try_parse_shizhi20_1(type):
	from strategy.alias.shizhis_1 import Shizhi20_1Strategy
	stra = Shizhi20_1Strategy()
	return stra

# example: shizhi30
def try_parse_shizhi30_1(type):
	from strategy.alias.shizhis_1 import Shizhi30_1Strategy
	stra = Shizhi30_1Strategy()
	return stra

# example: tover20
def try_parse_tover20_1(type):
	from strategy.alias.tovers_1 import Tover20_1Strategy
	return Tover20_1Strategy()

# example: tover25
def try_parse_tover25_1(type):
	from strategy.alias.tovers_1 import Tover25_1Strategy
	return Tover25_1Strategy()

# example: lianghua
def try_parse_lianghua_1(type):
	from strategy.alias.lianghua_1 import Lianghua_1Strategy
	stra = Lianghua_1Strategy()
	return stra

# example: jinjisai
def try_parse_jinjisai_1(type):
	from strategy.alias.jinjisai_1 import Jinjisai_1Strategy
	stra = Jinjisai_1Strategy()
	return stra

# example: 1p1
def try_parse_one_plus_one(type):
	from strategy.alias.one_plus_one import OnePlusOneStrategy
	stra = OnePlusOneStrategy()
	return stra

# example: core
def try_parse_auto_core_1(type):
	from strategy.alias.cores_1 import AutoCore_1Strategy
	stra = AutoCore_1Strategy()
	return stra

# example: core1
def try_parse_core_1(type):
	from strategy.alias.cores_1 import Core_1Strategy
	stra = Core_1Strategy()
	return stra

# example: core2
def try_parse_core_2(type):
	from strategy.alias.cores_1 import Core_2Strategy
	stra = Core_2Strategy()
	return stra

# example: core3
def try_parse_core_3(type):
	from strategy.alias.cores_1 import Core_3Strategy
	stra = Core_3Strategy()
	return stra

# example: qidongs
def try_parse_qidongs_1(type):
	from strategy.alias.qidongs_1 import Qidongs_1Strategy
	stra = Qidongs_1Strategy()
	return stra

# example: qidong
def try_parse_qidong_1(type):
	from strategy.alias.qidongs_1 import Qidong1_1Strategy
	stra = Qidong1_1Strategy()
	return stra

# example: level1
def try_parse_level_1(type):
	from strategy.alias.levels_1 import Level_1Strategy
	stra = Level_1Strategy()
	return stra

# example: level2
def try_parse_level_2(type):
	from strategy.alias.levels_1 import Level_2Strategy
	stra = Level_2Strategy()
	return stra

# example: level3
def try_parse_level_3(type):
	from strategy.alias.levels_1 import Level_3Strategy
	stra = Level_3Strategy()
	return stra

# example: base_0|base
def try_parse_base_0(type):
	from strategy.alias.bases_1 import Base_0Strategy
	stra = Base_0Strategy()
	return stra

# example: base1
def try_parse_base_1(type):
	from strategy.alias.bases_1 import Base_1Strategy
	stra = Base_1Strategy()
	return stra

# example: base2
def try_parse_base_2(type):
	from strategy.alias.bases_1 import Base_2Strategy
	stra = Base_2Strategy()
	return stra

# example: base3
def try_parse_base_3(type):
	from strategy.alias.bases_1 import Base_3Strategy
	stra = Base_3Strategy()
	return stra

# @Deprecated:
# example: base4
def try_parse_base_4(type):
	from strategy.alias.bases_1 import Base_4Strategy
	stra = Base_4Strategy()
	return stra

# example: pos15_1
def try_parse_pos15_1(type):
	from strategy.alias.pos15_1 import Pos15_1Strategy
	stra = Pos15_1Strategy()
	return stra

# example: shape0
def try_parse_shape_0(type):
	from strategy.alias.shape_0 import Shape_0Strategy
	stra = Shape_0Strategy()
	return stra

# example: shape1
def try_parse_shape_1(type):
	from strategy.alias.shape_1 import Shape_1Strategy
	stra = Shape_1Strategy()
	return stra

# example: shape2
def try_parse_shape_2(type):
	from strategy.alias.shape_2 import Shape_2Strategy
	stra = Shape_2Strategy()
	return stra

# example: shape3
def try_parse_shape_3(type):
	from strategy.alias.shape_3 import Shape_3Strategy
	stra = Shape_3Strategy()
	return stra

# example: shape4
def try_parse_shape_4(type):
	from strategy.alias.shape_4 import Shape_4Strategy
	stra = Shape_4Strategy()
	return stra

# example: main_pool
def try_parse_main_pool(type):
	from strategy.alias.main_pool import MainPoolStrategy
	stra = MainPoolStrategy()
	return stra

# example: not_main_pool
def try_parse_not_main_pool(type):
	from strategy.alias.not_main_pool import NotMainPoolStrategy
	stra = NotMainPoolStrategy()
	return stra

# example: sanhu1
def try_parse_sanhu1(type):
	from strategy.alias.sanhu1_strategy import Sanhu1Strategy
	stra = Sanhu1Strategy()
	return stra

# example: sanhu2
def try_parse_sanhu2(type):
	from strategy.alias.sanhu2_strategy import Sanhu2Strategy
	stra = Sanhu2Strategy()
	return stra

# example: duan
def try_parse_duan(type):
	from strategy.alias.duan import DuanStrategy
	return DuanStrategy()

# example: pool1
def try_parse_pool_1(type):
	from strategy.alias.pool_1 import Pool_1Strategy
	return Pool_1Strategy()

# example: pool2
def try_parse_pool_2(type):
	from strategy.alias.pool_2 import Pool_2Strategy
	return Pool_2Strategy()

# example: hexin
def try_parse_hexin_1(type):
	from strategy.alias.hexins_1 import Hexin_1Strategy
	return Hexin_1Strategy()

# example: hexin2
def try_parse_hexin_2(type):
	from strategy.alias.hexins_1 import Hexin_2Strategy
	return Hexin_2Strategy()

# example: hexin3
def try_parse_hexin_3(type):
	from strategy.alias.hexins_1 import Hexin_3Strategy
	return Hexin_3Strategy()

# example: hexins
def try_parse_hexins(type):
	from strategy.alias.hexins_1 import HexinsStrategy
	return HexinsStrategy()

# example: amount3
def try_parse_amount3_1(type):
	from strategy.alias.amounts_1 import Amount3_1Strategy
	return Amount3_1Strategy()

# example: amount5
def try_parse_amount5_1(type):
	from strategy.alias.amounts_1 import Amount5_1Strategy
	return Amount5_1Strategy()

# example: amount10
def try_parse_amount10_1(type):
	from strategy.alias.amounts_1 import Amount10_1Strategy
	return Amount10_1Strategy()

# example: amount15
def try_parse_amount15_1(type):
	from strategy.alias.amounts_1 import Amount15_1Strategy
	return Amount15_1Strategy()

# example: amount20
def try_parse_amount20_1(type):
	from strategy.alias.amounts_1 import Amount20_1Strategy
	return Amount20_1Strategy()

# example: amount30
def try_parse_amount30_1(type):
	from strategy.alias.amounts_1 import Amount30_1Strategy
	return Amount30_1Strategy()

# example: amount50
def try_parse_amount50_1(type):
	from strategy.alias.amounts_1 import Amount50_1Strategy
	return Amount50_1Strategy()

# example: tamount10
def try_parse_top_amount10_1(type):
	from strategy.alias.top_amounts_1 import TopAmount10_1Strategy
	return TopAmount10_1Strategy()

# example: tamount15
def try_parse_top_amount15_1(type):
	from strategy.alias.top_amounts_1 import TopAmount15_1Strategy
	return TopAmount15_1Strategy()

# example: tamount20
def try_parse_top_amount20_1(type):
	from strategy.alias.top_amounts_1 import TopAmount20_1Strategy
	return TopAmount20_1Strategy()

# example: tamount30
def try_parse_top_amount30_1(type):
	from strategy.alias.top_amounts_1 import TopAmount30_1Strategy
	return TopAmount30_1Strategy()

# example: tamount50
def try_parse_top_amount50_1(type):
	from strategy.alias.top_amounts_1 import TopAmount50_1Strategy
	return TopAmount50_1Strategy()

# example: tamount60
def try_parse_top_amount60_1(type):
	from strategy.alias.top_amounts_1 import TopAmount60_1Strategy
	return TopAmount60_1Strategy()

# example: tamount100
def try_parse_top_amount100_1(type):
	from strategy.alias.top_amounts_1 import TopAmount100_1Strategy
	return TopAmount100_1Strategy()

# example: tamount300
def try_parse_top_amount300_1(type):
	from strategy.alias.top_amounts_1 import TopAmount300_1Strategy
	return TopAmount300_1Strategy()

# example: tamount200
def try_parse_top_amount200_1(type):
	from strategy.alias.top_amounts_1 import TopAmount200_1Strategy
	return TopAmount200_1Strategy()

# example: aamount
def try_parse_auto_amount_1(type):
	from strategy.alias.amounts_1 import AutoAmount_1Strategy
	return AutoAmount_1Strategy()

# example: xls:amount
def try_parse_xls_amount_1(type):
	from strategy.alias.amounts_1 import XlsAmount_1Strategy
	return XlsAmount_1Strategy()

# example: xls:amount2
def try_parse_xls_amount_2(type):
	from strategy.alias.amounts_1 import XlsAmount_2Strategy
	return XlsAmount_2Strategy()

# example: xls:hexin
def try_parse_xls_hexin_1(type):
	from strategy.alias.hexins_1 import XlsHexin_1Strategy
	return XlsHexin_1Strategy()

# example: xls:hexin2
def try_parse_xls_hexin_2(type):
	from strategy.alias.hexins_1 import XlsHexin_2Strategy
	return XlsHexin_2Strategy()

# example: xls:hexin3
def try_parse_xls_hexin_3(type):
	from strategy.alias.hexins_1 import XlsHexin_3Strategy
	return XlsHexin_3Strategy()

# example: guxing1
def try_parse_guxing1(type):
	from strategy.alias.guxing_1 import Guxing_1Strategy
	return Guxing_1Strategy()

# example: maxtrd3
def try_parse_max_trd3(type):
	from strategy.alias.max_trds_1 import MaxTrd3_1Strategy
	stra = MaxTrd3_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd4
def try_parse_max_trd4(type):
	from strategy.alias.max_trds_1 import MaxTrd4_1Strategy
	stra = MaxTrd4_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd5
def try_parse_max_trd5(type):
	from strategy.alias.max_trds_1 import MaxTrd5_1Strategy
	stra = MaxTrd5_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd7
def try_parse_max_trd7(type):
	from strategy.alias.max_trds_1 import MaxTrd7_1Strategy
	stra = MaxTrd7_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd36:len=
def try_parse_max_trd36(type):
	from strategy.alias.max_trds_1 import MaxTrd36_1Strategy
	stra = MaxTrd36_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd37:len=
def try_parse_max_trd37(type):
	from strategy.alias.max_trds_1 import MaxTrd37_1Strategy
	stra = MaxTrd37_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd38:len=
def try_parse_max_trd38(type):
	from strategy.alias.max_trds_1 import MaxTrd38_1Strategy
	stra = MaxTrd38_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd39:len=
def try_parse_max_trd39(type):
	from strategy.alias.max_trds_1 import MaxTrd39_1Strategy
	stra = MaxTrd39_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: maxtrd59:len=
def try_parse_max_trd59(type):
	from strategy.alias.max_trds_1 import MaxTrd59_1Strategy
	stra = MaxTrd59_1Strategy()

	from util.param_util import get_param_from    
	day_len = int(get_param_from(type.split(':'),'len',-1))
	if day_len > 0:
		stra.set_day_len(day_len)
	return stra

# example: lsk1
def try_parse_lsk_1(type):
	from strategy.alias.lsks_1 import Lsk_1Strategy
	return Lsk_1Strategy()

# example: dst21
def try_parse_dst21(type):
	from strategy.alias.dsts_1 import Dst21_1Strategy
	return Dst21_1Strategy()

# example: dst22
def try_parse_dst22(type):
	from strategy.alias.dsts_1 import Dst22_1Strategy
	return Dst22_1Strategy()

# example: dst32
def try_parse_dst32(type):
	from strategy.alias.dsts_1 import Dst32_1Strategy
	return Dst32_1Strategy()

# example: dst42
def try_parse_dst42(type):
	from strategy.alias.dsts_1 import Dst42_1Strategy
	return Dst42_1Strategy()

# example: adgx
def try_parse_auto_dgx_1(type):
	from strategy.alias.dgxs_1 import AutoDgx_1Strategy
	return AutoDgx_1Strategy()

# example: dgx42
def try_parse_dgx42_1(type):
	from strategy.alias.dgxs_1 import Dgx_4_2Strategy
	return Dgx_4_2Strategy()

# example: dgx0
def try_parse_dgx0(type):
	from strategy.alias.dgxs_1 import Dgx_0Strategy
	return Dgx_0Strategy()

# example: dgx0_2
def try_parse_dgx0_2(type):
	from strategy.alias.dgxs_1 import Dgx_0_2Strategy
	return Dgx_0_2Strategy()

# example: dgx1
def try_parse_dgx1(type):
	from strategy.alias.dgxs_1 import Dgx_1Strategy
	return Dgx_1Strategy()

# example: dgx1_2
def try_parse_dgx1_2(type):
	from strategy.alias.dgxs_1 import Dgx_1_2Strategy
	return Dgx_1_2Strategy()

# example: dgx1_3
def try_parse_dgx1_3(type):
	from strategy.alias.dgxs_1 import Dgx_1_3Strategy
	return Dgx_1_3Strategy()

# example: dgx2
def try_parse_dgx2(type):
	from strategy.alias.dgxs_1 import Dgx_2Strategy
	return Dgx_2Strategy()

# example: dgx2_2
def try_parse_dgx2_2(type):
	from strategy.alias.dgxs_1 import Dgx2_2Strategy
	return Dgx2_2Strategy()

# example: dgx3
def try_parse_dgx3(type):
	from strategy.alias.dgxs_1 import Dgx_3Strategy
	return Dgx_3Strategy()

# example: dgx3_1
def try_parse_dgx3_1(type):
	from strategy.alias.dgxs_1 import Dgx_3_1Strategy
	return Dgx_3_1Strategy()

# example: dgx3_2
def try_parse_dgx3_2(type):
	from strategy.alias.dgxs_1 import Dgx_3_2Strategy
	return Dgx_3_2Strategy()

# example: dgx4
def try_parse_dgx4(type):
	from strategy.alias.dgxs_1 import Dgx_4Strategy
	return Dgx_4Strategy()

# example: dgx4_1
def try_parse_dgx4_1(type):
	from strategy.alias.dgxs_1 import Dgx_4_1Strategy
	return Dgx_4_1Strategy()

# example: dgx5
def try_parse_dgx5(type):
	from strategy.alias.dgxs_1 import Dgx_5Strategy
	return Dgx_5Strategy()

def try_parse_dgx5_2(type):
	from strategy.alias.dgxs_1 import Dgx_5_2Strategy
        return Dgx_5_2Strategy()


# example: dgx6
def try_parse_dgx6(type):
	from strategy.alias.dgxs_1 import Dgx_6Strategy
	return Dgx_6Strategy()

# example: pan11
def try_parse_pan11(type):
	from strategy.alias.pans_1 import Pan_11Strategy
	return Pan_11Strategy()

# example: pan12
def try_parse_pan12(type):
	from strategy.alias.pans_1 import Pan_12Strategy
	return Pan_12Strategy()

# example: pan1
def try_parse_pan1(type):
	from strategy.alias.pans_1 import Pan_1Strategy
	return Pan_1Strategy()

# example: pan2
def try_parse_pan2(type):
	from strategy.alias.pans_1 import Pan_2Strategy
	return Pan_2Strategy()

# example: pan3
def try_parse_pan3(type):
	from strategy.alias.pans_1 import Pan_3Strategy
	return Pan_3Strategy()

# example: pan4
def try_parse_pan4(type):
	from strategy.alias.pans_1 import Pan_4Strategy
	return Pan_4Strategy()

# example: xls:outv1|xls_outv1
def try_parse_xls_outv_1(type):
	from strategy.alias.outvs_1 import XlsOutv_1Strategy
	return XlsOutv_1Strategy()

# example: xls:outv1
def try_parse_xls_outv_2(type):
	from strategy.alias.outvs_2 import XlsOutv_2Strategy
	return XlsOutv_2Strategy()

# example: maoding
def try_parse_maoding_1(type):
	from strategy.alias.maoding_1 import Maoding_1Strategy
	return Maoding_1Strategy()

# example: maodians_2
def try_parse_maodians_2(type):
	from strategy.alias.maodians_2 import Maodians_2Strategy
	return Maodians_2Strategy()

# example: maodians
def try_parse_maodians_1(type):
	from strategy.alias.maodians_1 import Maodians_1Strategy
	return Maodians_1Strategy()

# example: xls:mao1
def try_parse_xls_mao_1(type):
	from strategy.alias.xls_mao_1 import XlsMao_1Strategy
	return XlsMao_1Strategy()

# example: xls:mao2
def try_parse_xls_mao_2(type):
	from strategy.alias.xls_mao_2 import XlsMao_2Strategy
	return XlsMao_2Strategy()

# example: xls:zhongwei0
def try_parse_xls_zhongwei_0(type):
	from strategy.alias.xls_zhongwei_0 import XlsZhongwei_0Strategy
	return XlsZhongwei_0Strategy()

# example: xls:zhongwei
def try_parse_xls_zhongwei_1(type):
	from strategy.alias.xls_zhongwei_1 import XlsZhongwei_1Strategy
	return XlsZhongwei_1Strategy()

# example: zhonggao
def try_parse_xls_zgwei_1(type):
	from strategy.alias.xls_zgwei_1 import XlsZgwei_1Strategy
	return XlsZgwei_1Strategy()

# example: gaowei
def try_parse_gaowei_1(type):
	from strategy.alias.gaoweis_1 import Gaowei_1Strategy
	return Gaowei_1Strategy()

# example: xls:gaowei
def try_parse_xls_gaowei_1(type):
	from strategy.alias.gaoweis_1 import XlsGaowei_1Strategy
	return XlsGaowei_1Strategy()

# example: xls:gaowei2
def try_parse_xls_gaowei_2(type):
	from strategy.alias.gaoweis_1 import XlsGaowei_2Strategy
	return XlsGaowei_2Strategy()

# example: diwei:len=
def try_parse_diwei_1(type):
	from strategy.alias.diweis_1 import Diwei_1Strategy
	stra = Diwei_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: xls:diwei
def try_parse_xls_diwei_1(type):
	from strategy.alias.diweis_1 import XlsDiwei_1Strategy
	return XlsDiwei_1Strategy()

# example: xls:diwei2
def try_parse_xls_diwei_2(type):
	from strategy.alias.diweis_1 import XlsDiwei_2Strategy
	return XlsDiwei_2Strategy()

# example: xls:gqushi
def try_parse_xls_gqushi_1(type):
	from strategy.alias.xls_qushi_1 import XlsGQushi_1Strategy
	return XlsGQushi_1Strategy()

# example: xls:dqushi
def try_parse_xls_dqushi_1(type):
	from strategy.alias.xls_qushi_1 import XlsDQushi_1Strategy
	return XlsDQushi_1Strategy()

# example: xls:dqushi2
def try_parse_xls_dqushi_2(type):
	from strategy.alias.xls_qushi_1 import XlsDQushi_2Strategy
	return XlsDQushi_2Strategy()

# example: xls:chaoduan
def try_parse_xls_chaoduan_1(type):
	from strategy.alias.chaoduans_1 import XlsChaoduan_1Strategy
	return XlsChaoduan_1Strategy()

# example: xls:chaoduan2
def try_parse_xls_chaoduan_2(type):
	from strategy.alias.chaoduans_1 import XlsChaoduan_2Strategy
	return XlsChaoduan_2Strategy()

# example: stocks:main2
def try_parse_stocks_main_2(type):
	from strategy.alias.stocks_main_2 import StocksMain_2Strategy
	return StocksMain_2Strategy()

# example: stocks:main1
def try_parse_stocks_main_1(type):
	from strategy.alias.stocks_main_1 import StocksMain_1Strategy
	return StocksMain_1Strategy()

# example: mao1
def try_parse_mao1(type):
	from strategy.alias.maos_1 import Mao_1Strategy
	return Mao_1Strategy()

# example: mao2
def try_parse_mao2(type):
	from strategy.alias.maos_1 import Mao_2Strategy
	return Mao_2Strategy()

# example: mao3
def try_parse_mao3(type):
	from strategy.alias.maos_1 import Mao_3Strategy
	return Mao_3Strategy()

# example: mao11
def try_parse_mao11(type):
	from strategy.alias.maos_1 import Mao_11Strategy
	return Mao_11Strategy()

# example: mao12
def try_parse_mao12(type):
	from strategy.alias.maos_1 import Mao_12Strategy
	return Mao_12Strategy()

# example: nnh
def try_parse_near_newhigh_1(type):
	from strategy.alias.near_newhigh_1 import NearNewhigh_1Strategy
	return NearNewhigh_1Strategy()

# example: nnh2
def try_parse_near_newhigh_2(type):
	from strategy.alias.near_newhigh_2 import NearNewhigh_2Strategy
	return NearNewhigh_2Strategy()

# example: tph
def try_parse_top_height_1(type):
	from strategy.alias.top_height_1 import TopHeight_1Strategy
	return TopHeight_1Strategy()

# example: qushi:min=
def try_parse_qushi(type):
	from strategy.alias.qushis_1 import QushiStrategy
	stra = QushiStrategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
	return stra

# example: qushi1
def try_parse_qushi_1(type):
	from strategy.alias.qushis_1 import Qushi_1Strategy
	return Qushi_1Strategy()

# example: qushi2
def try_parse_qushi_2(type):
	from strategy.alias.qushis_1 import Qushi_2Strategy
	return Qushi_2Strategy()

# example: qushi_top
def try_parse_qushi_top_1(type):
	from strategy.alias.qushis_1 import QushiTop_1Strategy
	return QushiTop_1Strategy()

# example: qushi_up2
def try_parse_qushi_up_2(type):
	from strategy.alias.qushis_1 import QushiUp_2Strategy
	return QushiUp_2Strategy()

# example: qushi_up:min=
def try_parse_qushi_up_1(type):
	from strategy.alias.qushis_1 import QushiUp_1Strategy
	stra = QushiUp_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			stra.set_min_pchg(float(k[1]))
	return stra

# example: qushi_bad:len=
def try_parse_qushi_bad_1(type):
	from strategy.alias.qushis_1 import QushiBad_1Strategy
	stra = QushiBad_1Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			stra.set_day_len(int(k[1]))
	return stra

# example: qushi_good2
def try_parse_qushi_good_2(type):
	from strategy.alias.qushis_1 import QushiGood_2Strategy
	return QushiGood_2Strategy()

# example: qushi_good
def try_parse_qushi_good_1(type):
	from strategy.alias.qushis_1 import QushiGood_1Strategy
	return QushiGood_1Strategy()

# example: youzi1
def try_parse_youzi_1(type):
	from strategy.alias.youzis_1 import Youzi_1Strategy
	return Youzi_1Strategy()

# example: youzi2
def try_parse_youzi_2(type):
	from strategy.alias.youzis_1 import Youzi_2Strategy
	return Youzi_2Strategy()

# example: youzi3
def try_parse_youzi_3(type):
	from strategy.alias.youzis_1 import Youzi_3Strategy
	return Youzi_3Strategy()

# example: youzi4
def try_parse_youzi_4(type):
	from strategy.alias.youzis_1 import Youzi_4Strategy
	return Youzi_4Strategy()

# example: sanhu1
def try_parse_sanhu_1(type):
	from strategy.alias.sanhu_1 import Sanhu_1Strategy
	return Sanhu_1Strategy()

# example: sanhu2
def try_parse_sanhu_2(type):
	from strategy.alias.sanhu_2 import Sanhu_2Strategy
	return Sanhu_2Strategy()

# example: qslong
def try_parse_qushilong_1(type):
	from strategy.alias.qslong_1 import QsLong_1Strategy
	return QsLong_1Strategy()

# example: qsrls
def try_parse_qsrls(type):
	from strategy.alias.qsrls import QsrlsStrategy
	return QsrlsStrategy()

# example: qsrl
def try_parse_qsrl_1(type):
	from strategy.alias.qsrl_1 import Qsrl_1Strategy
	return Qsrl_1Strategy()

# example: qsrl2
def try_parse_qsrl_2(type):
	from strategy.alias.qsrl_2 import Qsrl_2Strategy
	return Qsrl_2Strategy()

# example: stocks:zhongjun
def try_parse_stocks_zhongjun_1(type):
	from strategy.alias.stocks_zhongjun_1 import StocksZhongjun_1Strategy
	return StocksZhongjun_1Strategy()

# example: breaks
def try_parse_breaks(type):
	from strategy.alias.breaks import BreaksStrategy
	return BreaksStrategy()

# example: breakups
def try_parse_breakups(type):
	from strategy.alias.breakups import BreakupsStrategy
	return BreakupsStrategy()

# example: zhongpiaos
def try_parse_zhongpiaos(type):
	from strategy.alias.zhongpiaos_1 import ZhongpiaosStrategy
	return ZhongpiaosStrategy()

# example: zhongpiao
def try_parse_zhongpiao_1(type):
	from strategy.alias.zhongpiaos_1 import Zhongpiao_1Strategy
	return Zhongpiao_1Strategy()

# example: zhongpiao2
def try_parse_zhongpiao_2(type):
	from strategy.alias.zhongpiaos_1 import Zhongpiao_2Strategy
	return Zhongpiao_2Strategy()

# example: zhongpiao3
def try_parse_zhongpiao_3(type):
	from strategy.alias.zhongpiaos_1 import Zhongpiao_3Strategy
	return Zhongpiao_3Strategy()

# example: huoyue
def try_parse_huoyue_1(type):
	from strategy.alias.huoyue_1 import Huoyue_1Strategy
	return Huoyue_1Strategy()

# example: ignores
def try_parse_ignores_1(type):
	from strategy.alias.ignores_1 import Ignores_1Strategy
	return Ignores_1Strategy()

# example: not_ignores
def try_parse_not_ignores(type):
	from strategy.alias.not_ignores import NotIgnoresStrategy
	return NotIgnoresStrategy()

# example: new_dgx
def try_parse_new_dgx_1(type):
	from strategy.alias.new_dgx_1 import NewDgx_1Strategy
	return NewDgx_1Strategy()

# example: db10
def try_parse_db10_1(type):
	from strategy.alias.duobans_1 import Db10_1Strategy
	return Db10_1Strategy()

# example: db22_2
def try_parse_db22_2(type):
	from strategy.alias.db2s_1 import Db22_2Strategy
	return Db22_2Strategy()

# example: db22
def try_parse_db22_0(type):
	from strategy.alias.db2s_1 import Db22_0Strategy
	return Db22_0Strategy()

# example: db22_1
def try_parse_db22_1(type):
	from strategy.alias.db2s_1 import Db22_1Strategy
	return Db22_1Strategy()

# example: db20
def try_parse_db20_0(type):
	from strategy.alias.db2s_1 import Db20_0Strategy
	return Db20_0Strategy()

# example: db21_0
def try_parse_db21_0(type):
	from strategy.alias.db2s_1 import Db21_0Strategy
	return Db21_0Strategy()

# example: db21
def try_parse_db21_1(type):
	from strategy.alias.db2s_1 import Db21_1Strategy
	return Db21_1Strategy()

# example: db21_2
def try_parse_db21_2(type):
	from strategy.alias.db2s_1 import Db21_2Strategy
	return Db21_2Strategy()

# example: db40
def try_parse_db40_0(type):
	from strategy.alias.db4s_1 import Db40_0Strategy
	return Db40_0Strategy()

# example: db43
def try_parse_db43_0(type):
	from strategy.alias.db4s_1 import Db43_0Strategy
	return Db43_0Strategy()

# example: db43_1
def try_parse_db43_1(type):
	from strategy.alias.db4s_1 import Db43_1Strategy
	return Db43_1Strategy()

# example: db43_2
def try_parse_db43_2(type):
	from strategy.alias.db4s_1 import Db43_2Strategy
	return Db43_2Strategy()

# example: db41
def try_parse_db41_0(type):
	from strategy.alias.db4s_1 import Db41_0Strategy
	return Db41_0Strategy()

# example: db42
def try_parse_db42_0(type):
	from strategy.alias.db4s_1 import Db42_0Strategy
	return Db42_0Strategy()

# example: db42_1
def try_parse_db42_1(type):
	from strategy.alias.db4s_1 import Db42_1Strategy
	return Db42_1Strategy()

# example: db42_2
def try_parse_db42_2(type):
	from strategy.alias.db4s_1 import Db42_2Strategy
	return Db42_2Strategy()

# example: db44
def try_parse_db44_0(type):
	from strategy.alias.db4s_1 import Db44_0Strategy
	return Db44_0Strategy()

# example: db44
def try_parse_db44_1(type):
	from strategy.alias.db4s_1 import Db44_1Strategy
	return Db44_1Strategy()


# example: db33
def try_parse_db33_0(type):
	from strategy.alias.db3s_1 import Db33_0Strategy
	return Db33_0Strategy()

# example: db33_1
def try_parse_db33_1(type):
	from strategy.alias.db3s_1 import Db33_1Strategy
	return Db33_1Strategy()

# example: db32
def try_parse_db32_0(type):
	from strategy.alias.db3s_1 import Db32_0Strategy
	return Db32_0Strategy()

# example: db32_1
def try_parse_db32_1(type):
	from strategy.alias.db3s_1 import Db32_1Strategy
	return Db32_1Strategy()

# example: db32_2
def try_parse_db32_2(type):
	from strategy.alias.db3s_1 import Db32_2Strategy
	return Db32_2Strategy()

# example: db30
def try_parse_db30_0(type):
	from strategy.alias.db3s_1 import Db30_0Strategy
	return Db30_0Strategy()

# example: db31
def try_parse_db31_0(type):
	from strategy.alias.db3s_1 import Db31_0Strategy
	return Db31_0Strategy()

# example: db31_1
def try_parse_db31_1(type):
	from strategy.alias.db3s_1 import Db31_1Strategy
	return Db31_1Strategy()

# example: db31_2
def try_parse_db31_2(type):
	from strategy.alias.db3s_1 import Db31_2Strategy
	return Db31_2Strategy()

# example: db31_height
def try_parse_db31_height_1(type):
	from strategy.alias.db3s_1 import Db31Height_1Strategy
	return Db31Height_1Strategy()

# example: height5
def try_parse_height5_1(type):
	from strategy.alias.heights_1 import Height5_1Strategy
	return Height5_1Strategy()

# example: dis01
def try_parse_dis01_0(type):
	from strategy.alias.diss_1 import Dis01_0Strategy
	return Dis01_0Strategy()

# example: dis01_2
def try_parse_dis01_2(type):
	from strategy.alias.diss_1 import Dis01_2Strategy
	return Dis01_2Strategy()

# example: dis02
def try_parse_dis02_0(type):
	from strategy.alias.diss_1 import Dis02_0Strategy
	stra = Dis02_0Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
	return stra

# example: dis02_2
def try_parse_dis02_2(type):
	from strategy.alias.diss_1 import Dis02_2Strategy
	stra = Dis02_2Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
	return stra

# example: dis03
def try_parse_dis03_0(type):
	from strategy.alias.diss_1 import Dis03_0Strategy
	return Dis03_0Strategy()

# example: dis14
def try_parse_dis14_0(type):
	from strategy.alias.diss_1 import Dis14_0Strategy
	return Dis14_0Strategy()

# example: dis2
def try_parse_dis2_0(type):
	from strategy.alias.diss_1 import Dis2_0Strategy
	stra = Dis2_0Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
	return stra

# example: dis24
def try_parse_dis24_0(type):
	from strategy.alias.diss_1 import Dis24_0Strategy
	return Dis24_0Strategy()

# example: dis25
def try_parse_dis25_0(type):
	from strategy.alias.diss_1 import Dis25_0Strategy
	return Dis25_0Strategy()

# example: dis26
def try_parse_dis26_0(type):
	from strategy.alias.diss_1 import Dis26_0Strategy
	return Dis26_0Strategy()

# example: dis27
def try_parse_dis27_0(type):
	from strategy.alias.diss_1 import Dis27_0Strategy
	return Dis27_0Strategy()

# example: dis3
def try_parse_dis3_0(type):
	from strategy.alias.diss_1 import Dis3_0Strategy
	return Dis3_0Strategy()

# example: dis36
def try_parse_dis36_0(type):
	from strategy.alias.diss_1 import Dis36_0Strategy
	return Dis36_0Strategy()

# example: dis37
def try_parse_dis37_0(type):
	from strategy.alias.diss_1 import Dis37_0Strategy
	return Dis37_0Strategy()

# example: dis4
def try_parse_dis4_0(type):
	from strategy.alias.diss_1 import Dis4_0Strategy
	return Dis4_0Strategy()

# example: dis5
def try_parse_dis5_0(type):
	from strategy.alias.diss_1 import Dis5_0Strategy
	stra = Dis5_0Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
	return stra

# example: dis59
def try_parse_dis59_0(type):
	from strategy.alias.diss_1 import Dis59_0Strategy
	return Dis59_0Strategy()

# example: dis6
def try_parse_dis6_0(type):
	from strategy.alias.diss_1 import Dis6_0Strategy
	return Dis6_0Strategy()

# example: dis8
def try_parse_dis8_0(type):
	from strategy.alias.diss_1 import Dis8_0Strategy
	return Dis8_0Strategy()

# example: dis9
def try_parse_dis9_0(type):
	from strategy.alias.diss_1 import Dis9_0Strategy
	stra = Dis9_0Strategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'ma':
			stra.set_ma_len(int(k[1]))
	return stra

# example: lyin1
def try_parse_lianyin1_1(type):
	from strategy.alias.lianyins_1 import Lianyin1_1Strategy
	return Lianyin1_1Strategy()

# example: lyin1_2
def try_parse_lianyin1_2(type):
	from strategy.alias.lianyins_1 import Lianyin1_2Strategy
	return Lianyin1_2Strategy()

# example: lyin2
def try_parse_lianyin2_1(type):
	from strategy.alias.lianyins_1 import Lianyin2_1Strategy
	return Lianyin2_1Strategy()

# example: lyin3
def try_parse_lianyin3_1(type):
	from strategy.alias.lianyins_1 import Lianyin3_1Strategy
	return Lianyin3_1Strategy()

# example: lyin4
def try_parse_lianyin4_1(type):
	from strategy.alias.lianyins_1 import Lianyin4_1Strategy
	return Lianyin4_1Strategy()

# example: lyang1
def try_parse_lianyang1_1(type):
	from strategy.alias.lianyangs_1 import Lianyang1_1Strategy
	return Lianyang1_1Strategy()

# example: lyang1_2
def try_parse_lianyang1_2(type):
	from strategy.alias.lianyangs_1 import Lianyang1_2Strategy
	return Lianyang1_2Strategy()

# example: lyang2
def try_parse_lianyang2_1(type):
	from strategy.alias.lianyangs_1 import Lianyang2_1Strategy
	return Lianyang2_1Strategy()

# example: lyang3
def try_parse_lianyang3_1(type):
	from strategy.alias.lianyangs_1 import Lianyang3_1Strategy
	return Lianyang3_1Strategy()

# example: upma03
def try_parse_upma03_1(type):
	from strategy.alias.upmas_1 import Upma03_1Strategy
	return Upma03_1Strategy()

# example: upma36
def try_parse_upma36_1(type):
	from strategy.alias.upmas_1 import Upma36_1Strategy
	return Upma36_1Strategy()

# example: upma6
def try_parse_upma6_1(type):
	from strategy.alias.upmas_1 import Upma6_1Strategy
	return Upma6_1Strategy()

# example: dtrd3_1
def try_parse_dtrd3_1(type):
	from strategy.alias.dtrds_1 import DTrd3_1Strategy
	return DTrd3_1Strategy()

# example: dtrd3_2
def try_parse_dtrd3_2(type):
	from strategy.alias.dtrds_1 import DTrd3_2Strategy
	return DTrd3_2Strategy()

# example: dtrd32_1
def try_parse_dtrd32_1(type):
	from strategy.alias.dtrds_1 import DTrd32_1Strategy
	return DTrd32_1Strategy()

# example: dtrd32_4
def try_parse_dtrd32_4(type):
	from strategy.alias.dtrds_1 import DTrd32_4Strategy
	return DTrd32_4Strategy()

# example: dtrd32_7
def try_parse_dtrd32_7(type):
	from strategy.alias.dtrds_1 import DTrd32_7Strategy
	return DTrd32_7Strategy()

# example: dtrd53 | dtrd53_1
def try_parse_dtrd53_1(type):
	from strategy.alias.dtrds_1 import DTrd53_1Strategy
	return DTrd53_1Strategy()

# example: dtrd52 | dtrd52_1
def try_parse_dtrd52_1(type):
	from strategy.alias.dtrds_1 import DTrd52_1Strategy
	return DTrd52_1Strategy()

# example: db51_amount:limit=
def try_parse_db51_amount_1(type):
	from strategy.alias.db5s_1 import Db51AmountStrategy
	stra = Db51AmountStrategy()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: jin_db51
def try_parse_jin_db51_1(type):
	from strategy.alias.db5s_1 import JinDb51_Strategy
	return JinDb51_Strategy()

# example: zhong_db51
def try_parse_zhong_db51_1(type):
	from strategy.alias.db5s_1 import ZhongDb51_Strategy
	return ZhongDb51_Strategy()

# example: far_db51|yuan_db51
def try_parse_far_db51_1(type):
	from strategy.alias.db5s_1 import FarDb51_Strategy
	return FarDb51_Strategy()

# example: db51s
def try_parse_db51s(type):
	from strategy.alias.db5s_1 import Db51sStrategy
	return Db51sStrategy()

# example: db51s_2
def try_parse_db51s_2(type):
	from strategy.alias.db5s_1 import Db51s_2Strategy
	return Db51s_2Strategy()

# example: db51_0_2
def try_parse_db51_0_2(type):
	from strategy.alias.db5s_1 import Db51_0_2Strategy
	return Db51_0_2Strategy()

# example: Db51_0
def try_parse_db51_0(type):
	from strategy.alias.db5s_1 import Db51_0Strategy
	return Db51_0Strategy()

# example: Db51_1
def try_parse_db51_1(type):
	from strategy.alias.db5s_1 import Db51_1Strategy
	return Db51_1Strategy()

# example: Db51_2
def try_parse_db51_2(type):
	from strategy.alias.db5s_1 import Db51_2Strategy
	return Db51_2Strategy()

# example: db51_3
def try_parse_db51_3(type):
	from strategy.alias.db5s_1 import Db51_3Strategy
	return Db51_3Strategy()

# example: Tiao_0:limit=
def try_parse_tiao_0(type):
	from strategy.alias.tiao_0_strategy import Tiao_0Strategy
	stra = Tiao_0Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: trd4
def try_parse_shiti4_1(type):
	from strategy.alias.shiti4_1 import Shiti4_1Strategy
	return Shiti4_1Strategy()

# example: Shangy_1
def try_parse_shangy_1(type):
	from strategy.alias.shangy_1_strategy import Shangy_1Strategy
	stra = Shangy_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: shangy2
def try_parse_shangy_2(type):
	from strategy.alias.shangy_2 import Shangy_2Strategy
	stra = Shangy_2Strategy()
	return stra

# example: shangy5
def try_parse_shangy5_1(type):
	from strategy.alias.shangys_1 import Shangy5_1Strategy
	stra = Shangy5_1Strategy()
	return stra

# example: shangy3
def try_parse_shangy3_1(type):
	from strategy.alias.shangys_1 import Shangy3_1Strategy
	stra = Shangy3_1Strategy()
	return stra


# example: upbound1
def try_parse_upbound_1(type):
	from strategy.alias.upbound_1 import Upbound_1Strategy
	stra = Upbound_1Strategy()
	return stra

# example: upbound2
def try_parse_upbound_2(type):
	from strategy.alias.upbound_2 import Upbound_2Strategy
	stra = Upbound_2Strategy()
	return stra

# example: Dsy_1
def try_parse_dsy_1(type):
	from strategy.alias.dsy_1_strategy import Dsy_1Strategy
	stra = Dsy_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Dsy_2
def try_parse_dsy_2(type):
	from strategy.alias.dsy_2_strategy import Dsy_2Strategy
	stra = Dsy_2Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Dsy_3
def try_parse_dsy_3(type):
	from strategy.alias.dsy_3_strategy import Dsy_3Strategy
	stra = Dsy_3Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: trd1
def try_parse_trd_1(type):
	from strategy.alias.trd_1 import Trd_1Strategy
	stra = Trd_1Strategy()
	return stra

# example: trd2
def try_parse_trd_2(type):
	from strategy.alias.trd_2 import Trd_2Strategy
	stra = Trd_2Strategy()
	return stra

# example: trdm1
def try_parse_trd_m1(type):
	from strategy.alias.trd_m1 import Trd_M1Strategy
	stra = Trd_M1Strategy()
	return stra

# example: trd_sum05:len=
def try_parse_trd_sum_05_1(type):
	from strategy.alias.trd_sums_1 import TrdSum05_1Strategy
	stra = TrdSum05_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum3:len=
def try_parse_trd_sum_3_1(type):
	from strategy.alias.trd_sums_1 import TrdSum3_1Strategy
	stra = TrdSum3_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum38:len=
def try_parse_trd_sum_38_1(type):
	from strategy.alias.trd_sums_1 import TrdSum38_1Strategy
	stra = TrdSum38_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum5:len=
def try_parse_trd_sum_5_1(type):
	from strategy.alias.trd_sums_1 import TrdSum5_1Strategy
	stra = TrdSum5_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum8:len=
def try_parse_trd_sum_8_1(type):
	from strategy.alias.trd_sums_1 import TrdSum8_1Strategy
	stra = TrdSum8_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum14:len=
def try_parse_trd_sum_14_1(type):
	from strategy.alias.trd_sums_1 import TrdSum14_1Strategy
	stra = TrdSum14_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: trd_sum18:len=
def try_parse_trd_sum_18_1(type):
	from strategy.alias.trd_sums_1 import TrdSum18_1Strategy
	stra = TrdSum18_1Strategy()

	from util.param_util import get_param_from
	len = int(get_param_from(type.split(':'),'len',-1))
	if len > 0:
		stra.set_day_len(len)
	return stra

# example: Trd3_3
def try_parse_trd3s_3(type):
	from strategy.alias.trd3s_1 import Trd3s_3Strategy
	stra = Trd3s_3Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Trd3_4
def try_parse_trd3s_4(type):
	from strategy.alias.trd3s_1 import Trd3s_4Strategy
	stra = Trd3s_4Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Trd3_2
def try_parse_trd3s_2(type):
	from strategy.alias.trd3s_1 import Trd3s_2Strategy
	stra = Trd3s_2Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: trd3
def try_parse_trd3_1(type):
	from strategy.alias.trd1s_1 import Trd3_1Strategy
	stra = Trd3_1Strategy()
	return stra

# example: trd4
def try_parse_trd4_1(type):
	from strategy.alias.trd1s_1 import Trd4_1Strategy
	stra = Trd4_1Strategy()
	return stra

# example: trd9
def try_parse_trd9_1(type):
	from strategy.alias.trd1s_1 import Trd9_1Strategy
	stra = Trd9_1Strategy()
	return stra

# example: Trd2_1
def try_parse_trd2_1(type):
	from strategy.alias.trd2_1_strategy import Trd2_1Strategy
	stra = Trd2_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Trd2_2
def try_parse_trd2_2(type):
	from strategy.alias.trd2_2_strategy import Trd2_2Strategy
	stra = Trd2_2Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: Outv_1
def try_parse_Outv_1(type):
	from strategy.alias.outvs_1 import OutvNewh_1Strategy
	stra = OutvNewh_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: outv_1
def try_parse_outv_1(type):
	from strategy.alias.outvs_1 import Outv_1Strategy
	stra = Outv_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'limit':
			stra.set_limit(int(k[1]))
	return stra

# example: outv_2
def try_parse_outv_2(type):
	from strategy.alias.outvs_1 import Outv_2Strategy
	stra = Outv_2Strategy()
	return stra

# example: outvs
def try_parse_outvs(type):
	from strategy.alias.outvs_1 import OutvsStrategy
	stra = OutvsStrategy()
	return stra

# example: cores2
def try_parse_cores_2(type):
	from strategy.alias.cores_1 import Cores_2Strategy
	return Cores_2Strategy()

# example: cores
def try_parse_cores(type):
	from strategy.alias.cores_1 import Cores_1Strategy
	return Cores_1Strategy()

# example: db80
def try_parse_db80_1(type):
	from strategy.alias.db8s_1 import Db80_1Strategy
	return Db80_1Strategy()

# example: db81
def try_parse_db81_0(type):
	from strategy.alias.db8s_1 import Db81_0Strategy
	return Db81_0Strategy()

# example: db81_1
def try_parse_db81_1(type):
	from strategy.alias.db8s_1 import Db81_1Strategy
	return Db81_1Strategy()

# example: db81_2
def try_parse_db81_2(type):
	from strategy.alias.db8s_1 import Db81_2Strategy
	return Db81_2Strategy()

# example: xls:db82
def try_parse_xls_db82_0(type):
	from strategy.alias.db8s_1 import XlsDb82_0Strategy
	return XlsDb82_0Strategy()

# example: xls:db82_2
def try_parse_xls_db82_2(type):
	from strategy.alias.db8s_1 import XlsDb82_2Strategy
	return XlsDb82_2Strategy()

# example: db82
def try_parse_db82_0(type):
	from strategy.alias.db8s_1 import Db82_0Strategy
	return Db82_0Strategy()

# example: db83
def try_parse_db83_0(type):
	from strategy.alias.db8s_1 import Db83_0Strategy
	return Db83_0Strategy()

# example: db60
def try_parse_db60_1(type):
	from strategy.alias.db6s_1 import Db60_1Strategy
	return Db60_1Strategy()

# example: db61
def try_parse_db61_0(type):
	from strategy.alias.db6s_1 import Db61_0Strategy
	return Db61_0Strategy()

# example: db61_2
def try_parse_db61_2(type):
	from strategy.alias.db6s_1 import Db61_2Strategy
	return Db61_2Strategy()

# example: db62
def try_parse_db62_0(type):
	from strategy.alias.db6s_1 import Db62_0Strategy
	return Db62_0Strategy()

# example: xls:db62
def try_parse_xls_db62_1(type):
	from strategy.alias.db6s_1 import XlsDb62_0Strategy
        return XlsDb62_0Strategy()

# example: xls:db62_2
def try_parse_xls_db62_2(type):
	from strategy.alias.db6s_1 import XlsDb62_2Strategy
        return XlsDb62_2Strategy()

# example: db62_2
def try_parse_db62_2(type):
	from strategy.alias.db6s_1 import Db62_2Strategy
	return Db62_2Strategy()

# example: db63
def try_parse_db63_0(type):
	from strategy.alias.db6s_1 import Db63_0Strategy
	return Db63_0Strategy()

# example: db64
def try_parse_db64_0(type):
	from strategy.alias.db6s_1 import Db64_0Strategy
	return Db64_0Strategy()

# example: db65
def try_parse_db65_0(type):
	from strategy.alias.db6s_1 import Db65_0Strategy
	return Db65_0Strategy()

# example: db151
def try_parse_db151_0(type):
	from strategy.alias.db15s_1 import Db151_0Strategy
	return Db151_0Strategy()

# example: db152
def try_parse_db152_0(type):
	from strategy.alias.db15s_1 import Db152_0Strategy
	return Db152_0Strategy()

# example: db101
def try_parse_db101_0(type):
	from strategy.alias.db10s_1 import Db101_0Strategy
	return Db101_0Strategy()

# example: db101_1
def try_parse_db101_1(type):
	from strategy.alias.db10s_1 import Db101_1Strategy
	return Db101_1Strategy()

# example: db102s
def try_parse_db102s(type):
	from strategy.alias.db10s_1 import Db102sStrategy
	return Db102sStrategy()

# example: db102s_2
def try_parse_db102s_2(type):
	from strategy.alias.db10s_1 import Db102s_2Strategy
	return Db102s_2Strategy()

# example: db102s_3
def try_parse_db102s_3(type):
	from strategy.alias.db10s_1 import Db102s_3Strategy
	return Db102s_3Strategy()

# example: xls:db102
def try_parse_xls_db102_0(type):
	from strategy.alias.db10s_1 import XlsDb102_0Strategy
	return XlsDb102_0Strategy()

# example: xls:db102_2
def try_parse_xls_db102_2(type):
	from strategy.alias.db10s_1 import XlsDb102_2Strategy
	return XlsDb102_2Strategy()

# example: xls:db102_3
def try_parse_xls_db102_3(type):
	from strategy.alias.db10s_1 import XlsDb102_3Strategy
	return XlsDb102_3Strategy()

# example: Db102_0
def try_parse_db102_0(type):
	from strategy.alias.db10s_1 import Db102_0Strategy
	return Db102_0Strategy()

# example: Db102_1
def try_parse_db102_1(type):
	from strategy.alias.db10s_1 import Db102_1Strategy
	return Db102_1Strategy()

# example: Db102_2
def try_parse_db102_2(type):
	from strategy.alias.db10s_1 import Db102_2Strategy
	return Db102_2Strategy()

# example: baotuan
def try_parse_baotuan_1(type):
	from strategy.alias.baotuans_1 import Baotuan_1Strategy
	return Baotuan_1Strategy()

# example: xls:zhuli
def try_parse_zhuli_1(type):
	from strategy.alias.zhulis_1 import Zhuli_1Strategy
	return Zhuli_1Strategy()

# example: db100
def try_parse_db100_1(type):
	from strategy.alias.db10s_1 import Db100_0Strategy
	return Db100_0Strategy()

# example: db103
def try_parse_db103_1(type):
	from strategy.alias.db10s_1 import Db103_1Strategy
	return Db103_1Strategy()

# example: db103_2
def try_parse_db103_2(type):
	from strategy.alias.db10s_1 import Db103_2Strategy
	return Db103_2Strategy()

# example: db104
def try_parse_db104_1(type):
	from strategy.alias.db10s_1 import Db104_1Strategy
	return Db104_1Strategy()

# example: xls:db104
def try_parse_xls_db104_0(type):
	from strategy.alias.db10s_1 import XlsDb104_0Strategy
	return XlsDb104_0Strategy()

# example: xls:db104_2
def try_parse_xls_db104_2(type):
	from strategy.alias.db10s_1 import XlsDb104_2Strategy
	return XlsDb104_2Strategy()

# example: xls:db104_3
def try_parse_xls_db104_3(type):
	from strategy.alias.db10s_1 import XlsDb104_3Strategy
	return XlsDb104_3Strategy()

# example: db105
def try_parse_db105_1(type):
	from strategy.alias.db10s_1 import Db105_1Strategy
	return Db105_1Strategy()

# example: longhu81
def try_parse_longhu81_1(type):
	from strategy.alias.longhus_1 import Longhu81_1Strategy
	return Longhu81_1Strategy()

# example: dlb4_1
def try_parse_dlb4_1(type):
	from strategy.alias.dlb4s_1 import Dlb4_1Strategy
	return Dlb4_1Strategy()

# example: dlb4_2
def try_parse_dlb4_2(type):
	from strategy.alias.dlb4s_1 import Dlb4_2Strategy
	return Dlb4_2Strategy()

# example: dlb62
def try_parse_dlb62_1(type):
	from strategy.alias.dlbs_1 import Dlb62_1Strategy
	return Dlb62_1Strategy()

# example: dlb82
def try_parse_dlb82_1(type):
	from strategy.alias.dlbs_1 import Dlb82_1Strategy
	return Dlb82_1Strategy()

# example: dlb83
def try_parse_dlb83_1(type):
	from strategy.alias.dlbs_1 import Dlb83_1Strategy
	return Dlb83_1Strategy()

# example: dlb103
def try_parse_dlb103_1(type):
	from strategy.alias.dlbs_1 import Dlb103_1Strategy
	return Dlb103_1Strategy()

# example: dlb153
def try_parse_dlb153_1(type):
	from strategy.alias.dlbs_1 import Dlb153_1Strategy
	return Dlb153_1Strategy()

# example: dlb3_1
def try_parse_dlb3_1(type):
	from strategy.alias.dlb3s_1 import Dlb3_1Strategy
	return Dlb3_1Strategy()

# example: dlb3_2
def try_parse_dlb3_2(type):
	from strategy.alias.dlb3s_1 import Dlb3_2Strategy
	return Dlb3_2Strategy()

# example: dlb3_3
def try_parse_dlb3_3(type):
	from strategy.alias.dlb3s_1 import Dlb3_3Strategy
	return Dlb3_3Strategy()

# example: dlb3_4
def try_parse_dlb3_4(type):
	from strategy.alias.dlb3s_1 import Dlb3_4Strategy
	return Dlb3_4Strategy()

# example: dlb42
def try_parse_dlb42_1(type):
	from strategy.alias.dlb2s_1 import Dlb42_1Strategy
	return Dlb42_1Strategy()

# example: dlb52
def try_parse_dlb52_1(type):
	from strategy.alias.dlb2s_1 import Dlb52_1Strategy
	return Dlb52_1Strategy()

# example: dlb2_1
def try_parse_dlb2_1(type):
	from strategy.alias.dlb2s_1 import Dlb2_1Strategy
	return Dlb2_1Strategy()

# example: dlb2_2
def try_parse_dlb2_2(type):
	from strategy.alias.dlb2s_1 import Dlb2_2Strategy
	return Dlb2_2Strategy()

# example: dlb2_3
def try_parse_dlb2_3(type):
	from strategy.alias.dlb2s_1 import Dlb2_3Strategy
	return Dlb2_3Strategy()

# example: dlb2_4
def try_parse_dlb2_4(type):
	from strategy.alias.dlb2s_1 import Dlb2_4Strategy
	return Dlb2_4Strategy()

# example: chaoduan3
def try_parse_chaoduan_3(type):
	from strategy.alias.chaoduans_1 import Chaoduan_3Strategy
	return Chaoduan_3Strategy()

# example: chaoduan2
def try_parse_chaoduan_2(type):
	from strategy.alias.chaoduans_1 import Chaoduan_2Strategy
	return Chaoduan_2Strategy()

# example: chaoduan
def try_parse_chaoduan_1(type):
	from strategy.alias.chaoduans_1 import Chaoduan_1Strategy
	return Chaoduan_1Strategy()

# example: chaoduan0
def try_parse_chaoduan_0(type):
	from strategy.alias.chaoduans_1 import Chaoduan_0Strategy
	return Chaoduan_0Strategy()

# example: fav1
def try_parse_fav1_1(type):
	from strategy.alias.favs_1 import Fav1_1Strategy
	return Fav1_1Strategy()

# example: fav
def try_parse_auto_fav_1(type):
	from strategy.alias.favs_1 import AutoFav_1Strategy
	return AutoFav_1Strategy()

# example: suov2|suov21
def try_parse_suov21_1(type):
	from strategy.alias.suovs_1 import Suov21_1Strategy
	return Suov21_1Strategy()

# example: suov3|suov31
def try_parse_suov31_1(type):
	from strategy.alias.suovs_1 import Suov31_1Strategy
	return Suov31_1Strategy()

# example: suov5|suov51
def try_parse_suov51_1(type):
	from strategy.alias.suovs_1 import Suov51_1Strategy
	return Suov51_1Strategy()

# example: baov2:min=
def try_parse_baov21_1(type):
	from strategy.alias.baovs_1 import Baov21_1Strategy
	stra = Baov21_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_rate' ]:
			stra.set_min_rate(float(k[1]))
	return stra

# example: baov2_2
def try_parse_baov21_2(type):
	from strategy.alias.baovs_1 import Baov21_2Strategy
	return Baov21_2Strategy()

# example: baov3:min=
def try_parse_baov31_1(type):
	from strategy.alias.baovs_1 import Baov3_1Strategy
	stra = Baov3_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_rate' ]:
			stra.set_min_rate(float(k[1]))
	return stra

# example: baov3_2
def try_parse_baov31_2(type):
	from strategy.alias.baovs_1 import Baov31_2Strategy
	return Baov31_2Strategy()

# example: baov51_0
def try_parse_baov51_0(type):
	from strategy.alias.baovs_1 import Baov51_0Strategy
	return Baov51_0Strategy()

# example: baov51_1
def try_parse_baov51_1(type):
	from strategy.alias.baovs_1 import Baov51_1Strategy
	return Baov51_1Strategy()

# example: baov5_2
def try_parse_baov51_2(type):
	from strategy.alias.baovs_1 import Baov5_2Strategy
	return Baov5_2Strategy()

# example: baov52
def try_parse_baov52_1(type):
	from strategy.alias.baovs_1 import Baov52_1Strategy
	return Baov52_1Strategy()

# example: baov42
def try_parse_baov42_1(type):
	from strategy.alias.baovs_1 import Baov42_1Strategy
	return Baov42_1Strategy()

# example: baov6
def try_parse_baov61_1(type):
	from strategy.alias.baovs_1 import Baov61_1Strategy
	return Baov61_1Strategy()

# example: baov7
def try_parse_baov71_1(type):
	from strategy.alias.baovs_1 import Baov71_1Strategy
	return Baov71_1Strategy()

# example: dov31
def try_parse_dov31_1(type):
	from strategy.alias.dov31_1 import Dov31_1Strategy
	return Dov31_1Strategy()

# example: dov51
def try_parse_dov51_0(type):
	from strategy.alias.dov51_0 import Dov51_0Strategy
	return Dov51_0Strategy()

# example: dov51_1
def try_parse_dov51_1(type):
	from strategy.alias.dov51_1 import Dov51_1Strategy
	return Dov51_1Strategy()

# example: db95
def try_parse_db95_0(type):
	from strategy.alias.duobans_1 import Db95_0Strategy
	return Db95_0Strategy()

# example: db108
def try_parse_db108_0(type):
	from strategy.alias.duobans_1 import Db108_0Strategy
	return Db108_0Strategy()

# example: db86
def try_parse_db86_0(type):
	from strategy.alias.duobans_1 import Db86_0Strategy
	return Db86_0Strategy()

# example: db87
def try_parse_db87_0(type):
	from strategy.alias.duobans_1 import Db87_0Strategy
	return Db87_0Strategy()

# example: db75
def try_parse_db75_0(type):
	from strategy.alias.duobans_1 import Db75_0Strategy
	return Db75_0Strategy()

# example: db76
def try_parse_db76_0(type):
	from strategy.alias.duobans_1 import Db76_0Strategy
	return Db76_0Strategy()

# example: db50
def try_parse_db50_0(type):
	from strategy.alias.db5s_1 import Db50_0Strategy
	return Db50_0Strategy()

# example: db55
def try_parse_db55_0(type):
	from strategy.alias.db5s_1 import Db55_0Strategy
	return Db55_0Strategy()

# example: db54
def try_parse_db54_0(type):
	from strategy.alias.db5s_1 import Db54_0Strategy
	return Db54_0Strategy()

# example: db53
def try_parse_db53_0(type):
	from strategy.alias.db5s_1 import Db53_0Strategy
	return Db53_0Strategy()

# example: db53_2
def try_parse_db53_2(type):
	from strategy.alias.db5s_1 import Db53_2Strategy
	return Db53_2Strategy()

# example: Db52_0
def try_parse_db52_0(type):
	from strategy.alias.db5s_1 import Db52_0Strategy
	return Db52_0Strategy()

# example: Db52_1
def try_parse_db52_1(type):
	from strategy.alias.db5s_1 import Db52_1Strategy
	return Db52_1Strategy()

# example: Db52_2
def try_parse_db52_2(type):
	from strategy.alias.db5s_1 import Db52_2Strategy
	return Db52_2Strategy()

# example: Db52_3
def try_parse_db52_3(type):
	from strategy.alias.db5s_1 import Db52_3Strategy
	return Db52_3Strategy()

# example: lazhu1
def try_parse_lazhu1(type):
	from strategy.alias.lazhu_1 import Lazhu_1Strategy
	stra = Lazhu_1Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'time_str':
			from util.param_util import fix_time_str
			stra.set_time_str(fix_time_str(k[1]))
	return stra

# example: lazhu2
def try_parse_lazhu2(type):
	from strategy.alias.lazhu_2 import Lazhu_2Strategy
	stra = Lazhu_2Strategy()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'time_str':
			from util.param_util import fix_time_str
			stra.set_time_str(fix_time_str(k[1]))
	return stra

if __name__ == "__main__":
	pass
