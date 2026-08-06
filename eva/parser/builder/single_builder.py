# !/usr/bin/python
# coding=utf-8

def is_single_type(type,debug=False):
	eva = build_single_one(type,debug)
	if eva:
		return True
	return False

# return eva
def build_single_one(type,debug=False):
	if debug:
		print u'single_builder.build_single_one,eva-type: %s'%(type)

	# update 2025-01-16: 添加spec codetype的逻辑
	from eva.parser.builder.wrap_stra_builder import is_spec_code_type
	if is_spec_code_type(type,debug):
		return None

	# update 2025-04-01: 处理一下误输入的;
	type = type.replace(';',':')

	# update 2023-08-15: 记录一下输入的type
	origin = type

	from eva.parser.at_util import get_at_and_return_type
	at_timestr,type = get_at_and_return_type(type,debug)

	commons,params = get_seprate_params(type)
	if debug:
		print 'build_single_one,type:%s,commons:%s'%(type,commons)
		print 'at_timestr:%s'%(at_timestr)

	from helper import to_str
	type = to_str(params,sep=':')
	name = type.split(':')[0].split('.bf')[0]

	eva = None

	is_bound = ( name.startswith('upbound') or name.startswith('bound') ) and not name.endswith('fenbu')
	
	if type.startswith( 'trd' ):
		eva = try_parse_trd(type)
	elif type.startswith( 'ggzj2' ):
                eva = try_parse_ggzj2(type)
	elif type.startswith( 'ggzj' ):
		eva = try_parse_ggzj(type)
	elif is_bound:
		eva = try_parse_upbound_eva(type)
	elif type.startswith( 'dban_size' ): 
		eva = try_parse_dban_size(type)
	elif type.startswith( 'ban_size' ) or type.startswith('ban:') or type.startswith('ban.at'):
		eva = try_parse_ban_size(type) 
	elif type.startswith( 'jinji' ) or type.startswith( 'jingji' ):
		eva = try_parse_jinji_eva(type)
	#elif type.startswith( 'zhusheng' ) or type.startswith( 'zhushen' ):
	#	eva = try_parse_zhusheng_eva(type)
	elif type.startswith( 'qiehuan' ) or type.startswith( 'qieh' ) or type.startswith( 'qh' ):
		eva = try_parse_qiehuan_eva(type)
	elif type.startswith( 'bodong' ):
		eva = try_parse_bodong_eva(type)
	elif type.startswith( 'hopp' ):
		eva = try_parse_hopp_eva(type)
	elif type.startswith( 'youkong' ):
		eva = try_parse_youkong_eva(type)
	#elif name == 'qushi' or name == 'iqushi':
	#	eva = try_parse_qushi_eva(type)
	#elif type.startswith( 'rzq' ) or type.startswith('ruozq'):
	#	eva = try_parse_rzq(type)
	elif type.startswith( 'huiluo' ):
		eva = try_parse_huiluo(type)
	elif type.startswith('risk'):
		eva = try_parse_risk(type)
	elif type.startswith('advanced'):
		eva = try_parse_advanced(type)
	elif type.startswith('dstp'):
		eva = try_parse_dstp(type)
	elif type.startswith( 'upstp' ):
		eva = try_parse_upstp(type)
	elif name == 'zhusheng':
		eva = try_parse_zhusheng(type)
	elif name == 'qiangshi2':
		eva = try_parse_qiangshi2(type)
	elif name in [ 'qiangshi' ]:
		eva = try_parse_qiangshi(type)
	elif name in [ 'qushi' ]:
		eva = try_parse_qushi(type)
	elif name == 'baofa':
                eva = try_parse_baofa(type)
	elif name == 'jiasu':
		eva = try_parse_jiasu(type)
	elif name == 'zhongwei':
		eva = try_parse_zhongwei(type)
	elif name == 'gaowei':
		eva = try_parse_gaowei(type)
	elif name in [ 'irzq','irzz','irqq' ]:
                eva = try_parse_irzq(type)
	elif name in [ 'rzq','rzz','rqq' ]:
		eva = try_parse_rzq(type)
	elif name in [ 'dibu_rzq','diburzq','db_rzq' ]:
		eva = try_parse_dibu_rzq(type)
	elif name in [ 'izouqiang','izouq','izq' ]:
		eva = try_parse_izouqiang(type)

	elif name in [ 'xt_pull','xtpull','xt_npull','xtnpull' ]:
		eva = try_parse_xt_pull_eva(type)
	elif name in [ 'fast_pull','fastpull' ]:
		eva = try_parse_fast_pull_eva(type)
	elif name in [ 'deep_pull','deeppull' ]:
		eva = try_parse_deep_pull_eva(type)
	elif name in [ 'zhou2_pull','zhou2pull','zhou2_npull','zhou2npull' ]:
		eva = try_parse_zhou2_pull_eva(type)
	elif name in [ 'zhou3_pull','zhou3pull','zhou3_npull','zhou3npull' ]:
                eva = try_parse_zhou3_pull_eva(type)
	elif name in [ 'zero_pull','zeropull','0zhou_pull','0zhoupull' ]:
                eva = try_parse_zero_pull_eva(type)
	elif name in [ 'irzq_pull','irzqpull','irzq_npull','irzqnpull' ]:
		eva = try_parse_irzq_pull_eva(type)
	elif name in [ 'izouq_pull','izouqpull','izouqiang_pull','izouqiang_npull','izouqiangnpull' ]:
                eva = try_parse_izouqiang_pull_eva(type)
	elif name in [ 'chonggao_pull','chongao_pull','chonggaopull','chonggao_npull','chonggaonpull' ]:
                eva = try_parse_chonggao_pull_eva(type)

	elif name in [ 'chonggao2','chongao2','chongga2' ]:

		eva = try_parse_chonggao2(type)
	elif name in [ 'chonggao','chongao','chongga' ] or name.startswith('chong'):
		eva = try_parse_chonggao(type)
	elif name in [ 'zero_chonggao','zerochonggao' ]:
		eva = try_parse_zero_chonggao(type)

	elif name in [ 'baov_chonggao','baovchonggao' ]:
		eva = try_parse_baov_chonggao(type)
	elif name in [ 'xt_chonggao','xtchonggao' ]:
                eva = try_parse_xt_chonggao(type)
	elif name in [ 'xg_chonggao','xingao_chonggao','newhigh_chonggao','newh_chonggao' ]:
		eva = try_parse_xingao_chonggao(type)

	elif name in [ 'new_chonggao','newchonggao' ]:
		eva = try_parse_new_chonggao(type)
	elif name in [ 'new_chonggao2','newchonggao2' ]:
		eva = try_parse_new_chonggao2(type)

	elif name in [ 'zero','0zhou' ]:
		eva = try_parse_zero(type)
	elif name in [ '1zhou','zhou1' ]:
                eva = try_parse_zhou1(type)
	elif name in [ '2zhou','zhou2' ]:
		eva = try_parse_zhou2(type)
	elif name in [ '3zhou','zhou3' ]:
		eva = try_parse_zhou3(type)
	elif name in [ '5zhou','zhou5' ]:
		eva = try_parse_zhou5(type)

	elif type.startswith( 'ever_upstp' ):
		eva = try_parse_ever_upstp(type)
	#elif type.startswith('not_upstp'):
	#	eva = try_parse_not_upstp(type)
	elif type.startswith( 'zaopan_good2' ) or type.startswith( 'topq2' ):
		eva = try_parse_zaopan_good2_eva(type)
	elif type.startswith( 'zaopan_good' ) or type.startswith( 'zaopang' ) or type.startswith( 'zaopan_g' ) or type.startswith( 'topq' ):
		eva = try_parse_zaopan_good_eva(type)
	elif name == 'ctop' or name == 'dtop':
		eva = try_parse_ctop_eva(type)
	elif type.startswith( 'dopp' ):
		eva = try_parse_dopp_eva(type)
	elif type.startswith( 'dgood' ) or type.startswith( 'd_good' ):
		eva = try_parse_dgood_eva(type)
	elif type.startswith( 'dbad' ) or type.startswith( 'd_bad' ):
		eva = try_parse_dbad_eva(type)
	elif name == 'cut2':
		eva = try_parse_cut2_eva(type)
	elif name == 'cut':
		eva = try_parse_cut_eva(type)
	elif type == 'hot':
		eva = try_parse_hot_eva(type)
	elif type.startswith( 'wenhe2' ) or type in [ 'wram','warm' ]:
		eva = try_parse_wenhe2_eva(type)
	elif type.startswith( 'wenhe' ):
		eva = try_parse_wenhe_eva(type)
	elif type.startswith( 'maichong2' ) or type.startswith( 'jidie' ):
                eva = try_parse_jidie(type)
	elif type.startswith( 'maichong' ):
		eva = try_parse_maichong(type)
	elif type.startswith( 'fanhe' ):
		eva = try_parse_fanhe(type)
	elif type.startswith( 'hean' ) or type.startswith( 'heen' ):
		eva = try_parse_hean(type)
	elif type.startswith( 'up_to' ) or type.startswith( 'upto' ):
		eva = try_parse_up_to(type)
	#elif type.startswith('fenqi2'):
	#	eva = try_parse_fenqi2(type)
	elif type.startswith('fenqi'):
		eva = try_parse_fenqi(type)
	elif type.startswith('gaowei_fenqi') or type.startswith('gfenqi') or type.startswith('gwfenqi'):
		eva = try_parse_gaowei_fenqi(type)
	elif type.startswith( 'append_state' ) or type.startswith( 'appendstate' ):
		eva = try_parse_append_state(type)
	elif type.startswith('opp'):
		eva = try_parse_opp(type)
	#elif type.startswith('upma'):
	#	eva = try_parse_upma(type)
	elif type.startswith('name'):
		eva = try_parse_name(type)
	elif type.startswith('amount'):
		eva = try_parse_amount(type)
	elif type.startswith('shizhi'):
		eva = try_parse_shizhi(type)
	elif type.startswith('yidong'):
		eva = try_parse_yidong_eva(type)
	elif type.startswith('change2') or type.startswith('change'):
		eva = try_parse_change2_eva(type)
	elif type.startswith('nothing') or type.startswith('nothi'):
		eva = try_parse_nothing_eva(type)
	elif type.startswith('shake'):
		eva = try_parse_shake_eva(type)
	elif name in [ 'open_high','openhigh' ]: 
		eva = try_parse_open_high_eva(type)

	elif type.startswith('open'):
		eva = try_parse_open_eva(type)
	elif name in [ 'co_zhanbi','co_zb','cozb' ]:
		eva = try_parse_co_zhanbi_eva(type)
	elif type.startswith('co:') or type == 'co':
		eva = try_parse_co_eva(type)
	elif type.startswith('ol'):
		eva = try_parse_ol_eva(type)
	elif type.startswith('cl'):
		eva = try_parse_cl_eva(type)
	elif type.startswith('hc'):
		eva = try_parse_hc_eva(type)
	elif type.startswith('ho:') or type == 'ho':
		eva = try_parse_ho_eva(type)
	elif type.startswith('btws'):
		eva = try_parse_btws_eva(type)
	#elif type.startswith('btw') or type == 'fast':
	elif name == 'btw' or type == 'fast':
		eva = try_parse_btw_eva(type)
	elif type.startswith( 'fengdan' ) or type == 'fd':
		eva = try_parse_fengdan_eva(type)
	elif type.startswith('tover'):
		eva = try_parse_tover_eva(type)
	elif type.startswith('pb'):
		eva = try_parse_pb_eva(type)
	elif type.startswith('shizhi'):
		eva = try_parse_shizhi_eva(type)
	elif type.startswith( 'low_pull' ) or type.startswith( 'lowpull' ) or type.startswith( 'lpull' ):
		eva = try_parse_low_pull_eva(type)
	elif name == 'tpull' or name.startswith('tpull'):
		eva = try_parse_tpull_eva(type)
	elif type.startswith('low') or type.startswith('lpchg'):
		eva = try_parse_low_eva(type)
	elif type.startswith('hpchg') or type.startswith('high'):
		eva = try_parse_hpchg_eva(type)
	elif name in [ 'xt_higher','xthigher' ]:
		eva = try_parse_xt_higher_eva(type)

	elif type.startswith('xt'):
		eva = try_pase_xt_eva(type)
	elif type.startswith('pulluped'):
		eva = try_parse_pulluped_eva(type)
	elif type.startswith('pullup'):
		eva = try_parse_pullup_eva(type)
	elif type.startswith('pulled'):
		eva = try_parse_pulled_eva(type)
	elif type.startswith('pull'):
		eva = try_parse_pull_eva(type)
	elif type.startswith('bottom_pull') or type.startswith('pull_bottom'):
		eva = try_parse_bottom_pull_eva(type)
	elif type.startswith( 'inh_pull' ) or type.startswith( 'nh_pull' ):
		eva = try_parse_inewhigh_pull_eva(type)
	elif type.startswith('bottom') or type.startswith('bot'):
		eva = try_parse_bottom_eva(type)
	elif type.startswith('near_top') or type.startswith('neartop') or type.startswith('ntop'):
		eva = try_parse_near_top_eva(type)
	elif type.startswith('big_shake') or type.startswith('bigshake'):
		eva = try_parse_big_shake_eva(type)
	elif type.startswith('fast2') or type == 'simple':
		#print u'eva.parser.single_builder.try_parse_fast2_eva'

                eva = try_parse_fast2_eva(type)
	#elif type.startswith('fast_pull'):
	#	eva = try_parse_fast_pull_eva(type)
	elif type.startswith('drop'):
		eva = try_parse_drop_eva(type)
	elif type.startswith('rup2'):
		eva = try_parse_rup2_eva(type)
	elif type.startswith('rup'):
		eva = try_parse_rup_eva(type)
	elif type.startswith('rdown'):
		eva = try_parse_rdown_eva(type)
	elif name.startswith('upbound') and not name.endswith('fenbu'):
		eva = try_parse_upbound_eva(type)
	elif type.startswith('section'):
		eva = try_parse_section_eva(type)
	elif type.startswith('inewhigh2') or type.startswith('inewhigh'):
		eva = try_parse_inewhigh2_eva(type)
	elif type.startswith('inewhigh'):
		eva = try_parse_inewhigh_eva(type)
	elif type.startswith('inewlow'):
		eva = try_parse_inewlow_eva(type)
	elif type == 'baola':
		eva = try_parse_baola_eva(type)
	elif name in [ 'baod','baodie','baodi' ]:
		eva = try_parse_baodie_eva(type)
	elif type.startswith( 'lopp' ):
		eva = try_parse_lopp_eva(type)
	elif name == 'baov':
		eva = try_parse_baov_eva(type)
	elif type.startswith( 'hopp' ):
		eva = try_parse_hopp_eva(type)
	elif type.startswith( 'dopp' ):
		eva = try_parse_dopp_eva(type)
	elif type.startswith( 'low_pull' ) or type.startswith( 'lowpull' ):
		eva = try_parse_low_pull_eva(type)
	elif type.startswith( 'breaks' ):
		eva = try_parse_breaks_eva(type)

	if not eva:
		return eva

	# 解析bf字段
	bf_len = get_bf_len_from(type)
	if bf_len > 0:
		eva.set_bf_len(bf_len)

	# 处理at timestr
	if at_timestr:
		eva.set_at_timestr(at_timestr)	

	# 处理公共参数
	deal_common_params(eva,commons)
	return eva

# example: ggzj2
def try_parse_ggzj2(type):
	from eva.evas.ggzj_eva import Ggzj2Eva
	eva = Ggzj2Eva()

	return eva

# example: ggzj:bk=
def try_parse_ggzj(type):
	from eva.evas.ggzj_eva import GgzjEva
	eva = GgzjEva()

        params = type.split(':')
        for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_zhanbi':
			eva.set_min_zhanbi(float(k[1]))
		elif k[0] == 'max_zhanbi': 
			eva.set_max_zhanbi(float(k[1]))
		elif k[0] == 'min_zhuli':
			eva.set_min_zhuli(float(k[1]))
		elif k[0] == 'max_zhuli':
                        eva.set_max_zhuli(float(k[1]))
		elif k[0] == 'sort':
			eva.set_sort(k[1])
		elif k[0] == 'bk':
			eva.set_bk(k[1])
	return eva

# example: pull:fix_interval=600:min_pchg=0.5:max_pchg=:len=:t2=:mode=
def try_parse_pull_eva(type):
	#print u'eva_builder.try_parse_pull_eva,type: %s'%(type)

	from util.param_util import get_eva_type_from_param
	type = get_eva_type_from_param(type)

	from eva.evas.pull.pull_eva import PullEva
        name = 'pull:'
        params = type.split(':')
        eva = PullEva()

        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'fix_interval':
			eva.set_fix_interval(int(k[1]))
                elif k[0] in [ 'min','min_pchg' ]:
			eva.set_min_up_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_up_pchg(float(k[1]))
		elif k[0] == 'min_cpchg':
                        eva.set_min_cpchg(float(k[1]))
                elif k[0] == 'max_cpchg':
                        eva.set_max_cpchg(float(k[1]))
		elif k[0] == 'min_lpchg':
			eva.set_min_lpchg(float(k[1]))
		elif k[0] == 'max_lpchg':
			eva.set_max_lpchg(float(k[1]))
		elif k[0] == 'min_hpchg':
                        eva.set_min_hpchg(float(k[1]))
                elif k[0] == 'max_hpchg':
                        eva.set_max_hpchg(float(k[1]))
		elif k[0] == 'len':
			eva.set_len(float(k[1]))
		elif k[0] == 'limit':
			eva.set_limit(int(k[1]))
		elif k[0] == 't2':
			from util.param_util import fix_time_str
			eva.set_t2(fix_time_str(k[1]))
		elif k[0] == 'fix_zaopan':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_fix_zaopan(b)
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: nh_pull
def try_parse_inewhigh_pull_eva(type):
	from eva.evas.pull.inewhigh_pull import INewhighPullEva
	eva = INewhighPullEva()
	params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'fix_interval':
                        eva.set_fix_interval(int(k[1]))
                elif k[0] == 'min_pchg':
                        eva.set_min_up_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_up_pchg(float(k[1]))
		elif k[0] == 'min_cpchg':
                        eva.set_min_cpchg(float(k[1]))
                elif k[0] == 'max_cpchg':
                        eva.set_max_cpchg(float(k[1]))
		elif k[0] == 'min_lpchg':
			eva.set_min_lpchg(float(k[1]))
		elif k[0] == 'max_lpchg':
			eva.set_max_lpchg(float(k[1]))
		elif k[0] == 'min_hpchg':
                        eva.set_min_hpchg(float(k[1]))
                elif k[0] == 'max_hpchg':
                        eva.set_max_hpchg(float(k[1]))
		elif k[0] == 't2':
			from util.param_util import fix_time_str
			eva.set_t2(fix_time_str(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: bottom_pull:fix_interval=600:min_pchg=0.5:max_pchg=:max_rate=
def try_parse_bottom_pull_eva(type):
	from eva.evas.pull.bottom_pull import BottomPullEva
	eva = BottomPullEva()
	params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'fix_interval':
                        eva.set_fix_interval(int(k[1]))
                elif k[0] == 'min_pchg':
                        eva.set_min_up_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_up_pchg(float(k[1]))
		elif k[0] == 'min_cpchg':
                        eva.set_min_cpchg(float(k[1]))
                elif k[0] == 'max_cpchg':
			eva.set_max_cpchg(float(k[1]))
		elif k[0] == 'min_lpchg':
			eva.set_min_lpchg(float(k[1]))
		elif k[0] == 'max_lpchg':
			eva.set_max_lpchg(float(k[1]))
		elif k[0] == 'min_hpchg':
                        eva.set_min_hpchg(float(k[1]))
                elif k[0] == 'max_hpchg':
			eva.set_max_hpchg(float(k[1]))
		elif k[0] == 'max_rate':
			eva.set_max_rate(float(k[1]))
		elif k[0] == 't2':
			from util.param_util import fix_time_str
			eva.set_t2(fix_time_str(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: append_state
def try_parse_append_state(type):
	from eva.evas.append_state_eva import AppendStateEva
	eva = AppendStateEva()
	return eva

# example: cut2
def try_parse_cut2_eva(type):
	from eva.list.cut.cut2_eva import Cut2Eva
	eva = Cut2Eva()
	return eva

# example: cut
def try_parse_cut_eva(type):
	from eva.list.cut.cut_eva import CutEva
	eva = CutEva()
	return eva

# example: wenhe
def try_parse_wenhe_eva(type):
	from eva.list.wenhe_eva import WenheEva
	eva = WenheEva()
	return eva

# example: wenhe2
def try_parse_wenhe2_eva(type):
	from eva.list.wenhe2_eva import Wenhe2Eva
	eva = Wenhe2Eva()
	return eva

# example: hot
def try_parse_hot_eva(type):
	from eva.list.hot_eva import HotEva
	eva = HotEva()
	return eva

# example: dopp
def try_parse_dopp_eva(type):
	from eva.list.dopp_eva import DOppEva
	eva = DOppEva()
	return eva

# example: dgood
def try_parse_dgood_eva(type):
	from eva.list.dgood_eva import DGoodEva
	eva = DGoodEva()
	return eva

# example: dbad
def try_parse_dbad_eva(type):
	from eva.list.dbad_eva import DBadEva
	eva = DBadEva()
	return eva

# example: ctop
def try_parse_ctop_eva(type):
	from eva.list.ctop_eva import CTopEva
	eva = CTopEva()
	return eva

# example: zaopan_good2
def try_parse_zaopan_good2_eva(type):
	from eva.list.zaopan_good2_eva import ZaopanGood2Eva
	eva = ZaopanGood2Eva()
	return eva

# example: zaopan_good
def try_parse_zaopan_good_eva(type):
	from eva.list.zaopan_good_eva import ZaopanGoodEva
	eva = ZaopanGoodEva()
	return eva

# example: chaoyqs
def try_parse_chaoyqs_eva( type ):
	from eva.list.chaoyqs_eva import ChaoyqsEva
	eva = ChaoyqsEva()

	return eva

# exmaple: maodings
def try_parse_maodings_eva( type ):
	from eva.list.maodings_eva import MaodingsEva
	eva = MaodingsEva()

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,type.split(':'))
	return eva

# exmaple: maoding2
def try_parse_maoding2_eva( type ):
	from eva.list.maoding2_eva import Maoding2Eva
	eva = Maoding2Eva()

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,type.split(':'))
	return eva

# exmaple: maoding3
def try_parse_maoding3_eva( type ):
	from eva.list.maoding_and_risk_eva import MaodingAndRiskEva
	eva = MaodingAndRiskEva()

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,type.split(':'))
	return eva

# exmaple: maoding
def try_parse_maoding_eva( type ):
	from eva.list.maoding_eva import MaodingEva
	eva = MaodingEva()

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,type.split(':'))
	return eva

# example: lopp
def try_parse_lopp_eva(type):
	from eva.list.lopp_eva import LOppEva
	eva = LOppEva()

	return eva

# example: hopp
def try_parse_hopp_eva(type):
	from eva.list.hopp_eva import HOppEva
	eva = HOppEva()
	return eva

# example: dopp
def try_parse_dopp_eva(type):
	from eva.list.dopp_eva import DOppEva
	eva = DOppEva()
	return eva

# example: youkong
def try_parse_youkong_eva(type):
	from eva.list.youkong_eva import YoukongEva
	eva = YoukongEva()

	return eva

# example: tpull:min_pchg=:mode=:t2=
def try_parse_tpull_eva(type):
	from eva.list.tpull_eva import TPullEva
	eva = TPullEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg( float(k[1]) )

	name = params[0]
	if len(name) > len('tpull'):
		pchg = float(name[len('tpull'):])
		eva.set_min_pchg(pchg)

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,params)
	return eva

# example: low_pull:min_pchg=
def try_parse_low_pull_eva(type):
	from eva.list.low_pull_eva import LowPullEva
	eva = LowPullEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg( float(k[1]) )
	return eva

# example: baola
def try_parse_baola_eva(type):
	from eva.list.baola_eva import BaolaEva
	eva = BaolaEva()

	return eva

# example: baodie
def try_parse_baodie_eva(type):
	from eva.list.baodie_eva import BaodieEva
	eva = BaodieEva()

	return eva

# example: breaks
def try_parse_breaks_eva(type):
	from eva.list.breaks_eva import BreaksEva
	eva = BreaksEva()

	return eva

# example: opp:min_pchg=:max=
def try_parse_opp(type):
	from eva.evas.open_pull_eva import OpenPullEva	
	eva = OpenPullEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_pchg(float(k[1]))
	return eva

# example: baov:min_pchg=:max=
def try_parse_baov_eva(type):
	from eva.evas.baov_eva import BaovEva	
	eva = BaovEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_rate' ]:
			eva.set_min_rate(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_pchg(float(k[1]))
	return eva

# @Deprecated:
# example: qushi:
def try_parse_qushi_eva2(type):
	from eva.evas.qushi_eva import QushiEva
	eva = QushiEva()

	if type.startswith('iqushi'):
		eva.set_is_inner(True)

	name = type.split(':')[0]
	if len(type) > len(name)+1:
		eva.set_status( type[len(name)+1:] )
	return eva

# example: shizhi:sort_by_shizhi=
def try_parse_shizhi_eva(type):
	from eva.evas.shizhi_eva import ShizhiEva
	eva = ShizhiEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'type':
			eva.set_type(k[1])
		elif k[0] == 'sort_by_shizhi':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_sort_by_shizhi(b)
	return eva

# example: pb:
def try_parse_pb_eva(type):
	from eva.evas.pb_eva import PbEva
	eva = PbEva()
	return eva

# example: fengdan
def try_parse_fengdan_eva(type):
	from eva.evas.fengdan_eva import FengdanEva
	eva = FengdanEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_fengdan':
			eva.set_min_fengdan(float(k[1]))
		elif k[0] == 'max_fengdan':
			eva.set_max_fengdan(float(k[1]))

	name = params[0]
	if name in [ 'fengdaned','fengdand' ]:
		eva.set_filter(True)
	return eva

# example: tover:min_tover=:max_tover=:sort_by_tover=
def try_parse_tover_eva(type):
	from eva.evas.tover_eva import ToverEva
	eva = ToverEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'type':
			eva.set_type(k[1])
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 'min_tover' or k[0] == 'min':
			eva.set_min_tover(float(k[1]))
		elif k[0] in [ 'max','max_tover' ]:
			eva.set_max_tover(float(k[1]))
		elif k[0] == 'sort_by_tover':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_sort_by_tover(b)
	return eva

# example: name:sort=
def try_parse_name(type):
	from eva.evas.name_eva import NameEva
	eva = NameEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'type':
			eva.set_type(k[1])
		elif k[0] == 'sort':
			b = True if k[1] in [ 'true','TRUE','True','1' ] else False
			eva.set_sort(b)
	return eva

# example: not_upstp
def try_parse_not_upstp(type):
	from eva.wrap.not_upstp_eva import NotUpstpEva
	eva = NotUpstpEva()
	return eva

# example: upstp:has_up10=
def try_parse_upstp(type):
	from eva.list.upstp_eva import UpstpEva
	eva = UpstpEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'has_up10':
			b = True if k[1] in ['true','TRUE','True'] else False
			#eva.set_has_up10(b)
	return eva

# example: ever_upstp
def try_parse_ever_upstp(type):
	from eva.list.ever_upstp_eva import EverUpstpEva
	eva = EverUpstpEva()
	return eva

# example: zhusheng
def try_parse_zhusheng(type):
	from eva.list.zhusheng_eva import ZhushengEva
	eva = ZhushengEva()
	return eva

# example: qiangshi2
def try_parse_qiangshi2(type):
	from eva.list.qiangshi_eva import Qiangshi2Eva
	eva = Qiangshi2Eva()
	return eva

# example: qiangshi
def try_parse_qiangshi(type):
	from eva.list.qiangshi_eva import QiangshiEva
	eva = QiangshiEva()
	return eva

# example: qushi
def try_parse_qushi(type):
	from eva.list.qushi_eva import QushiEva
	eva = QushiEva()
	
	return eva

# example: baofa
def try_parse_baofa(type):
	from eva.list.baofa_eva import BaofaEva
	eva = BaofaEva()
	return eva

# example: jiasu
def try_parse_jiasu(type):
	from eva.list.jiasu_eva import JiasuEva
	eva = JiasuEva()
	return eva

# example: zhongwei
def try_parse_zhongwei(type):
	from eva.list.zhongwei_eva import ZhongweiEva
	eva = ZhongweiEva()
	return eva

# example: gaowei
def try_parse_gaowei(type):
	from eva.list.gaowei_eva import GaoweiEva
	eva = GaoweiEva()
	return eva

# example: jidie
def try_parse_jidie(type):
	from eva.list.jidie_eva import JidieEva
	eva = JidieEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 't2':
			eva.set_t2(k[1].replace(':',''))
	return eva

# example: maichong
def try_parse_maichong(type):
	from eva.list.maichong_eva import MaichongEva
	eva = MaichongEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 't2':
			eva.set_t2(k[1].replace(':',''))
	return eva

# example: fanhe
def try_parse_fanhe(type):
	from eva.list.fanhe_eva import FanheEva
	eva = FanheEva()
	return eva

# example: hean
def try_parse_hean(type):
	from eva.list.hean_eva import HeanEva
	eva = HeanEva()
	return eva

# example: up_to:pchg=
def try_parse_up_to(type):
	from eva.list.up_to_eva import UpToEva
	eva = UpToEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'pchg' or k[0] == 'min':
			eva.set_pchg(float(k[1]))

	from eva.parser.builder.new_builder import deal_new_builder_common_params
	eva = deal_new_builder_common_params(eva,params)	
	return eva

# example: dstp
def try_parse_dstp(type):
	from eva.list.dstp_eva import DstpEva
	eva = DstpEva()
	return eva

# example: advanced:min_pchg=
def try_parse_advanced(type):
	from eva.evas.advanced_eva import AdvancedEva
	eva = AdvancedEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
	return eva

# example: risk:min_pchg=
def try_parse_risk(type):
	from eva.evas.risk_eva import RiskEva
	eva = RiskEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
                        eva.set_max_pchg(float(k[1]))
	return eva

# example: huiluo:min_pchg=
def try_parse_huiluo(type):
	from eva.list.huiluo_eva import HuiluoEva
	eva = HuiluoEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_pchg(float(k[1]))

	return eva

# example: shizhi
def try_parse_shizhi(type):
	from eva.wrap.shizhi_eva import ShizhiEva
	return ShizhiEva()

# example: xt_higher
def try_parse_xt_higher_eva(type):
	from eva.list.higher.xt_higher_eva import XtHigherEva
	return XtHigherEva()

# example: xt_pull
def try_parse_xt_pull_eva(type):
	from eva.list.pull.xt_pull_eva import XtPullEva
	return XtPullEva()

# example: fast_pull
def try_parse_fast_pull_eva(type):
	from eva.list.pull.fast_pull_eva import FastPullEva
	return FastPullEva()

# example: deep_pull
def try_parse_deep_pull_eva(type):
	from eva.list.pull.deep_pull_eva import DeepPullEva
	return DeepPullEva()

# example: irzq_pull
def try_parse_irzq_pull_eva(type):
	from eva.list.pull.irzq_pull_eva import IrzqPullEva
	return IrzqPullEva()

# example: izouq_pull
def try_parse_izouqiang_pull_eva(type):
	from eva.list.pull.izouqiang_pull_eva import IZouqiangPullEva
	return IZouqiangPullEva()
	
# example: chonggao_pull
def try_parse_chonggao_pull_eva(type):
	from eva.list.pull.chonggao_pull_eva import ChonggaoPullEva
	return ChonggaoPullEva()

# example: zero_pull
def try_parse_zero_pull_eva(type):
	from eva.list.pull.zero_pull_eva import ZeroPullEva
	return ZeroPullEva()

# example: zhou2_pull
def try_parse_zhou2_pull_eva(type):
	from eva.list.pull.zhou2_pull_eva import Zhou2PullEva
	return Zhou2PullEva()

# example: zhou3_pull
def try_parse_zhou3_pull_eva(type):
	from eva.list.pull.zhou3_pull_eva import Zhou3PullEva
	return Zhou3PullEva()

# example: upshake:t2=
def try_parse_upshake_eva(type):
	from eva.wrap.upshake_eva import UpShakeEva
	eva = UpShakeEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 't2':
			eva.set_t2(k[1])
	return eva

# example: shake:fix_prec=:min_pchg=
def try_parse_shake_eva(type):
	from eva.evas.shake_eva import ShakeEva
	eva = ShakeEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'fix_prec':
			b = True if k[1] in [ 'true','TRUE','True' ] else False
			eva.set_fix_prec(b)
		elif k[0] in [ 'min_pchg','min' ]:
			eva.set_min_shake(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			eva.set_max_shake(float(k[1]))
	return eva

# example: outc
#def try_parse_outc_eva(type):
#	from eva.wrap.outc_eva import OutcEva
#	return OutcEva()

# @Deprecated:
# example: stage
def try_parse_stage_eva(type):
	from eva.evas.stage_eva import StageEva
	eva = StageEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'stage':
			eva.set_stage(k[1])
		elif k[0] == 'min_stage':
			eva.set_min_stage(k[1])
		elif k[0] == 'max_stage':
			eva.set_max_stage(k[1])
	return eva

# example: pchg_areas:
def try_parse_pchg_areas_eva(type):
	from eva.evas.pchg_areas_eva import PchgAreasEva
	return PchgAreasEva()

# example: chonggao
def try_parse_chonggao(type):
	from eva.list.chonggao.chonggao_eva import ChonggaoEva
	eva = ChonggaoEva()
	return eva

# example: chonggao2
def try_parse_chonggao2(type):
	from eva.list.chonggao.chonggao_eva import Chonggao2Eva
	eva = Chonggao2Eva()
	return eva

# example: zero_chonggao
def try_parse_zero_chonggao(type):
	from eva.list.chonggao.zero_chonggao_eva import ZeroChonggaoEva
	eva = ZeroChonggaoEva()
	return eva

# example: baov_chonggao
def try_parse_baov_chonggao(type):
	from eva.list.chonggao.baov_chonggao_eva import BaovChonggaoEva
	eva = BaovChonggaoEva()
	return eva

# example: xt_chonggao
def try_parse_xt_chonggao(type):
	from eva.list.chonggao.xt_chonggao_eva import XtChonggaoEva
	eva = XtChonggaoEva()
	return eva

# example: xingao_chonggao
def try_parse_xingao_chonggao(type):
	from eva.list.chonggao.xingao_chonggao_eva import XingaoChonggaoEva
	eva = XingaoChonggaoEva()
	return eva

# example: new_chonggao
def try_parse_new_chonggao(type):
	from eva.list.chonggao.new_chonggao_eva import NewChonggaoEva
	eva = NewChonggaoEva()
	return eva

# example: new_chonggao2
def try_parse_new_chonggao2(type):
	from eva.list.chonggao.new_chonggao_eva import NewChonggao2Eva
	eva = NewChonggao2Eva()
	return eva

# example: zero
def try_parse_zero(type):
	from eva.list.zhou.zero_eva import ZeroEva
	eva = ZeroEva()
	return eva

# example: zhou1
def try_parse_zhou1(type):
	from eva.list.zhou.zhou1_eva import Zhou1Eva
	eva = Zhou1Eva()
	return eva

# example: zhou2
def try_parse_zhou2(type):
	from eva.list.zhou.zhou2_eva import Zhou2Eva
	eva = Zhou2Eva()
	return eva

# example: zhou3
def try_parse_zhou3(type):
	from eva.list.zhou.zhou3_eva import Zhou3Eva
	eva = Zhou3Eva()
	return eva

# example: zhou5
def try_parse_zhou5(type):
	from eva.list.zhou.zhou5_eva import Zhou5Eva
	eva = Zhou5Eva()
	return eva

# 语义: 日间图形弱转强
# example: dibu_rzq
def try_parse_dibu_rzq(type):
	from eva.list.dibu_rzq_eva import DibuRzqEva
	eva = DibuRzqEva()
	return eva

# 语义: 日间图形弱转强
# example: rzq
def try_parse_rzq(type):
	from eva.list.rzq_eva import RzqEva
	eva = RzqEva()
	return eva

# 语义: 日内图形弱转强
# example: irzq
def try_parse_irzq(type):
	from eva.good.irzq_eva import IRzqEva
	eva = IRzqEva()
	return eva

# 语义: 个股股价在持续走强
# example: izouqiang
def try_parse_izouqiang(type):
	from eva.good.izouqiang_eva import IZouqiangEva
	eva = IZouqiangEva()
	return eva

# @Deprecated: 这个是旧版的日内弱转强实现
# example: rzq:min_pchg=:mode=
def try_parse_rzq2(type):
	from eva.evas.ruozq_eva import RuozhuanqiangEva
	eva = RuozhuanqiangEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
	return eva

# example: jinji
def try_parse_jinji_eva(type):
	from eva.evas.jinji_eva import JinjiEva
	eva = JinjiEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'sort':
			b = True if k[1] in [ 'true','TRUE','True','1' ] else False
			eva.set_sort(b)
		elif k[0] == 'filter':
			b = True if k[1] in [ 'true','TRUE','True','1' ] else False
			eva.set_filter(b)
		elif k[0] in [ 'stop','stop_sort' ]:
			b = True if k[1] in [ '1','true','TRUE','True' ] else False
			eva.set_stop_sort(b)

	name = params[0]
	if name in [ 'jinjied','jinjid' ]:
		eva.set_filter(True)
	return eva

# example: bodong 
def try_parse_bodong_eva(type):
	from eva.evas.bodong_eva import BodongEva
	eva = BodongEva()

	params = type.split(':')
	name = params[0]
	if name.endswith( 'ed' ):
		eva.set_filter(True)

	return eva

# example: qiehuan
def try_parse_qiehuan_eva(type):
	from eva.evas.qiehuan_eva import QiehuanEva
	eva = QiehuanEva()

	params = type.split(':')
	name = params[0]
	if name.endswith( 'ed' ):
		eva.set_filter(True)

	return eva

# @Deprected:
# example: zhusheng:len=:min_pchg=:min_ht=
def try_parse_zhusheng_eva(type):
	from eva.evas.zhusheng_eva import ZhushengEva
	eva = ZhushengEva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			eva.set_day_len(int(k[1]))
		elif k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'min_height','min_ht' ]:
			eva.set_min_height(float(k[1]))			
		elif k[0] == 'limit':
			eva.set_limit(int(k[1]))
	name = params[0]
	if name.endswith( 'ed' ):
		eva.set_filter(True)
	return eva

# example: ban_size:min_ban=:max_ban=:len=
def try_parse_ban_size(type):
	from eva.stra.ban_size_eva import BanSizeEva
	eva = BanSizeEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_ban','min' ]:
			eva.set_min_ban(int(k[1]))
		elif k[0] in [ 'max_ban','max' ]:
			eva.set_max_ban(int(k[1]))
		elif k[0] == 'len':
			eva.set_day_len(int(k[1]))
		elif k[0] == 'limit':
			eva.set_limit(int(k[1]))
	return eva

# example: dban_size:min_ban=:max_ban=:len=
def try_parse_dban_size(type):
	from eva.stra.dban_size_eva import DBanSizeEva
	eva = DBanSizeEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_ban','min' ]:
			eva.set_min_ban(int(k[1]))
		elif k[0] in [ 'max_ban','max' ]:
			eva.set_max_ban(int(k[1]))
		elif k[0] == 'len':
			eva.set_day_len(int(k[1]))
	return eva

# example: trd:min_pchg=:max_pchg=
def try_parse_trd(type):
	from eva.evas.trd_eva import TrdEva
	eva = TrdEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_pchg(float(k[1]))
	return eva

# example: trd_sum:day_len=:min_pchg=:max_pchg=
def try_parse_trd_sum(type):
	from eva.wrap.trd_sum_eva import TrdSumEva
	eva = TrdSumEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_pchg(float(k[1]))
		elif k[0] == 'day_len':
			eva.set_day_len(int(k[1]))
	return eva

# example: strength
def try_parse_strength_eva(type):
	from eva.evas.strength.strength_eva import StrengthEva
	return StrengthEva()

# example: section:mode=simple:stage=
def try_parse_section_eva(type):
	from eva.evas.section_eva import SectionEva
	eva = SectionEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 'stage':
			eva.set_stage(k[1])
	return eva

# example: upbound:min_hl_pchg=1.0:rate=0.5:max_rate=1.0
def try_parse_upbound_eva(type):
	from eva.evas.upbound_eva import UpboundEva
	params = type.split(':')
	eva = UpboundEva()
	for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min_hl_pchg','min_sk_pchg' ]:
                        eva.set_min_hl_pchg(float(k[1]))
		elif k[0] in [ 'min','rate','min_rate' ]:
			eva.set_rate(float(k[1]))
		elif k[0] in [ 'max','max_rate' ]:
			eva.set_max_rate(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: cl:min_pchg=:max_pchg=
def try_parse_cl_eva(type):
	from eva.evas.cl_eva import ClEva
	params = type.split(':')
	eva = ClEva()
	for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min','min_pchg' ]:
                        eva.set_min_cl_pchg(float(k[1]))
                elif k[0] in [ 'max_pchg','max' ]:
                        eva.set_max_cl_pchg(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: ol:min_pchg=:max_pchg=
def try_parse_ol_eva(type):
	from eva.evas.ol_eva import OLEva
	params = type.split(':')
	eva = OLEva()
	for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min','min_pchg' ]:
                        eva.set_min_pchg(float(k[1]))
                elif k[0] in [ 'max','max_pchg' ]:
                        eva.set_max_pchg(float(k[1]))
		#elif k[0] == 'min_abs':
		#	eva.set_min_abs(float(k[1]))
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: co_zhanbi:min=:max=
def try_parse_co_zhanbi_eva(type):
	from eva.evas.co_zhanbi_eva import CoZhanbiEva
	params = type.split(':')
	eva = CoZhanbiEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_zb' ]:
			eva.set_min_zb(float(k[1]))
		elif k[0] in [ 'max','max_zb' ]:
			eva.set_max_zb(float(k[1]))
		elif k[0] == 'asc' or k[0] == 'ascending':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_ascending(b)
	return eva

# example: co:min_pchg=:max_pchg=:min_abs
def try_parse_co_eva(type):
	#print u'eva.single-builder.try_parse_co_eva,type:%s'%(type)
	from eva.evas.co_eva import CoEva
	params = type.split(':')
	eva = CoEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_co_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_co_pchg(float(k[1]))
		elif k[0] == 'min_abs':
			eva.set_min_abs(float(k[1]))
		elif k[0] == 'asc' or k[0] == 'ascending':
			b = True if k[1] in [ '1','true','TRUE','True'] else False
			eva.set_ascending(b)
		elif k[0] == 'sort':
			eva.set_sort(k[1])
	return eva

# example: low:min_pchg=1.0:max_pchg=2.0:asc=true
def try_parse_low_eva(type):
	from eva.evas.low_eva import LowEva
	params = type.split(':')
	eva = LowEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_lpchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			eva.set_max_lpchg(float(k[1]))
		elif k[0] == 'asc' or k[0] == 'ascending':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_ascending(b)
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: open_high
def try_parse_open_high_eva(type):
	from eva.list.open_high_eva import OpenHighEva
	eva = OpenHighEva()
	return eva

# example: open:min_pchg=1.0:max_pchg=2.0
def try_parse_open_eva(type):
	from eva.evas.open_eva import OpenEvaluater
	params = type.split(':')
	eva = OpenEvaluater()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			eva.set_max_pchg(float(k[1]))
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: gaowei_fenqi|gfenqi|gwfenqi
def try_parse_gaowei_fenqi(type):
	from eva.list.gaowei_fenqi_eva import GaoweiFenqiEva
	eva = GaoweiFenqiEva()

	return eva

# example: fenqi2
def try_parse_fenqi2(type):
	from eva.wrap.fenqi2_eva import Fenqi2Eva
	eva = Fenqi2Eva()
	return eva

# example: fenqi:min_up=:min_down=
def try_parse_fenqi(type):
	from eva.list.fenqi_eva import FenqiEva
	eva = FenqiEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_up':
			eva.set_min_up(float(k[1]))
		elif k[0] in [ 'min','min_down' ]:
			eva.set_min_down(float(k[1]))
	return eva

# example: fast2
def try_parse_fast2_eva(type):
	from eva.wrap.fast2_eva import Fast2Eva
	eva = Fast2Eva()
	return eva

# example: rup2:min_pchg=
def try_parse_rup2_eva(type):
	from eva.wrap.rup2_eva import Rup2Eva
	eva = Rup2Eva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
	return eva

# example: rup:min_pchg=0.0:max_pchg=10.0:type=close
def try_parse_rup_eva(type):
	from eva.evas.real_up_eva import RealUpEva
	params = type.split(':')
	eva = RealUpEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_up_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_up_pchg(float(k[1]))
		elif k[0] == 'type':
			eva.set_type(k[1])
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: rdown:min_pchg=0.0:type=close
def try_parse_rdown_eva(type):
	from eva.evas.real_down_eva import RealDownEva
	params = type.split(':')
        eva = RealDownEva()
        for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min','min_pchg' ]:
                        eva.set_min_down_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			eva.set_max_down_pchg(float(k[1]))
                elif k[0] == 'type':
                        eva.set_type(k[1])
                else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: lpchg:min_pchg=0.0:max_pchg=20.0:asc=true:fix_interval=600
def try_parse_lpchg_eva(type):
	from eva.evas.low_eva import LowEva
	params = type.split(':')
	eva = LowEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_lpchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_lpchg(float(k[1]))
		elif k[0] == 'asc' or k[0] == 'ascending':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_ascending(b)
		elif k[0] == 'fix_interval':
			eva.set_fix_interval(int(k[1]))
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: hpchg:min_pchg=0.0:max_pchg=20.0
def try_parse_hpchg_eva(type):
	from eva.evas.high_eva import HighEva
	params = type.split(':')
	eva = HighEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max_pchg','max' ]:
			eva.set_max_pchg(float(k[1]))
		elif k[0] in [ 'stop','stop_sort' ]:
			b = True if k[1] in [ '1','true','TRUE','True' ] else False
			eva.set_stop_sort(b)
	return eva

# example: inewlow:mode=:len=
def try_parse_inewlow_eva(type):
	from eva.evas.inewlow_eva import INewlowEva
	params = type.split(':')
	eva = INewlowEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] == 'len':
			eva.set_len(int(k[1]))
	return eva

# example: inewhigh2:mode=:len=
def try_parse_inewhigh2_eva(type):
	from eva.evas.inewhigh2_eva import INewhigh2Eva
	params = type.split(':')
	eva = INewhigh2Eva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] == 'len':
			eva.set_len(int(k[1]))
	return eva

# example: inewhigh:fix_interval=1800:fix_start=300:fix_pchg=0.3:min_pchg=0.1:max_pchg=
def try_parse_inewhigh_eva(type):
	from eva.evas.inewhigh_eva import INewhighEva
	params = type.split(':')
	eva = INewhighEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'fix_interval':
			eva.set_fix_interval(int(k[1]))
		elif k[0] == 'fix_pchg':
			eva.set_fix_pchg(float(k[1]))
		elif k[0] == 'fix_start':
                        eva.set_fix_start(int(k[1]))
		elif k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_pchg(float(k[1]))
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: pulluped
def try_parse_pulluped_eva(type):
	from eva.wrap.pulluped_eva import PullupedEva
	eva = PullupedEva()
	return eva

# example: pullup:min_pchg=:max_pchg=:min_up
def try_parse_pullup_eva(type):
	from eva.wrap.pullup_eva import PullupEva
	eva = PullupEva()	
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        eva.set_min_cpchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_cpchg(float(k[1]))
		elif k[0] == 'min_up':
			eva.set_min_up_pchg(float(k[1]))
	return eva

# @Deprecated:
# example: fast_pull
def try_parse_fast_pull_eva2(type):
	from eva.wrap.fast_pull_eva import FastPullEva
	eva = FastPullEva()
	return eva

# example: big_shake:down=:up=:fix_prec=
def try_parse_big_shake_eva(type):
	from eva.evas.big_shake_eva import BigShakeEva
	eva = BigShakeEva()
        params = type.split(':')
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'down':
                        eva.set_down(int(k[1]))
		elif k[0] == 'up':
			eva.set_up(int(k[1]))
		elif k[0] == 'fix_prec':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_fix_prec(b)
	return eva

# example: near_top
def try_parse_near_top_eva(type):
	from eva.evas.near_top_eva import NearTopEva
	return NearTopEva()

# example: bottom
def try_parse_bottom_eva(type):
	from eva.evas.bottom_eva import BottomEva
	return BottomEva()

# example: pulled:min_pchg=:min_rate=
def try_parse_pulled_eva(type):
	from eva.wrap.pulled_eva import PulledEva
	eva = PulledEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_up(float(k[1]))
		elif k[0] == 'min_rate':
			eva.set_min_rate(float(k[1]))
	return eva

# example: drop:fix_interval=600:min_pchg=0.5
def try_parse_drop_eva(type):
        from eva.evas.pull.drop_eva import DropEva
        params = type.split(':')
        eva = DropEva()
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'fix_interval':
                        eva.set_fix_interval(int(k[1]))
                elif k[0] in [ 'min_pchg','min' ]:
                        eva.set_min_down_pchg(float(k[1]))
		elif k[0] == 'max_pchg':
			eva.set_max_down_pchg(float(k[1]))
		elif k[0] == 'limit':
			eva.set_limit(int(k[1]))
		elif k[0] == 't2':
			from util.param_util import fix_time_str
			eva.set_t2(fix_time_str(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
                #else:
		#	raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: amount:mode=:min_amount=
def try_parse_amount(type):
	from eva.evas.amount_eva import AmountEva
	eva = AmountEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] in [ 'min_amount','min_pchg','min','min_amt' ]:
			eva.set_min_amount(float(k[1]))
		elif k[0] in [ 'max_amount','max_pchg','max_amt','max' ]:
                        eva.set_max_amount(float(k[1]))
	return eva

# example: nothing:append_dealed=true
def try_parse_nothing_eva(type):
	from eva.evas.nothing_eva import NothingEva
	eva = NothingEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'append_dealed':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_append_dealed(b)
	return eva

# example: 2day_good
def try_parse_2day_good(type):
	from eva.evas.two_day_good_eva import TwoDayGoodEva
	eva = TwoDayGoodEva()

	return eva

# example: btws
def try_parse_btws_eva(type):
	from eva.wrap.btws_eva import BtwsEva
	return BtwsEva()

# example: btw:min_pchg=1.0:max_pchg=4.0:asc=
def try_parse_btw_eva(type):
	from eva.evas.btw_eva import BetweenEvaluater
	name = 'btw:'
	params = type.split(':')
	eva = BetweenEvaluater()
	for p in params[1:]:
                k = p.split('=')
                if k[0] in [ 'min_pchg','min' ]:
                        eva.set_min_cpchg(float(k[1]))
                elif k[0] in [ 'max_pchg','max' ]:
                        eva.set_max_cpchg(float(k[1]))
		elif k[0] in [ 'asc','ascending' ]:
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_ascending(b)
		elif k[0] in [ 'stop','stop_sort' ]:
			b = True if k[1] in [ '1','true','TRUE','True' ] else False
                        eva.set_stop_sort(b)

		#else:
		#	raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: ho:min_pchg=:max_pchg=
def try_parse_ho_eva(type):
	from eva.evas.ho_eva import HOEva
	eva = HOEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min','min_pchg' ]:
			eva.set_min_pchg(float(k[1]))
		elif k[0] in [ 'max','max_pchg' ]:
			eva.set_max_pchg(float(k[1]))
		elif k[0] in [ 'mode','t2' ]:
			pass
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: hc:min_pchg=:max_pchg=
def try_parse_hc_eva(type):
	from eva.evas.hc_eva import HCEva
	eva = HCEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min' ]:
			eva.set_min_pchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        eva.set_max_pchg(float(k[1]))
		elif k[0] in [ 'stop','stop_sort' ]:
                        b = True if k[1] in [ '1','true','TRUE','True' ] else False
                        eva.set_stop_sort(b)
		else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: pchg:min_pchg=1.0:max_pchg=4.0:time_str=
def try_parse_pchg_eva(type):
	from eva.evas.pchg_eva import PchgEva
	name = 'pchg:'
	params = type.split(':')
	eva = PchgEva()
	for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        eva.set_min_pchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        eva.set_max_pchg(float(k[1]))
		elif k[0] in ['time_str','timestr']:
			s = k[1]
			time_str = '%s:%s:%s'%(s[0:2],s[2:4],s[4:6])
			eva.set_time_str(time_str)
		else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva

# example: xt:min_hl_pchg=:max_hl_pchg=:min_pchg=:max_pchg=
def try_pase_xt_eva(type):
	from eva.evas.xt_eva import XtEva
	name = 'xt:'
	params = type.split(':')
	eva = XtEva()
	for p in params[1:]:
		k = p.split('=')
		if k[0] in ['max_hl_pchg','max_pchg']:
			eva.set_max_hl_pchg(float(k[1]))
		elif k[0] in ['min_hl_pchg','min_pchg']:
			eva.set_min_hl_pchg(float(k[1]))
		elif k[0] == 'sort_by_sk':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_sort_by_sk(b)
		else:
			raise Exception("fail to parse %s,param:%s"%(type,k))
	return eva


# example: hist_btw:fix_interval=1800:fix_start=300:max_hl_pchg=1.5:min_pchg=1.0:max_pchg=4.0:min_max_pchg=4.0:min_hl_pchg=0.0:sort_by_sk=true
def try_parse_hist_btw_eva(type,eva=None):
	from eva.evas.hist_btw_eva import HistBtwEva
	name = 'hist_btw:'
	params = type.split(':')
        eva = HistBtwEva() if not eva else eva
        for p in params[1:]:
                k = p.split('=')
                if k[0] == 'min_pchg':
                        eva.set_min_cpchg(float(k[1]))
                elif k[0] == 'max_pchg':
                        eva.set_max_cpchg(float(k[1]))
		elif k[0] == 'min_max_pchg':
			eva.set_min_max_pchg(float(k[1]))
		elif k[0] == 'fix_interval':
			eva.set_fix_interval(int(k[1]))
		elif k[0] == 'fix_start':
			eva.set_fix_start(int(k[1]))
		elif k[0] == 'max_hl_pchg':
			eva.set_max_hl_pchg(float(k[1]))
		elif k[0] == 'min_hl_pchg':
			eva.set_min_hl_pchg(float(k[1]))
		elif k[0] == 'sort_by_sk':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_sort_by_sk(b)
		else:
                        raise Exception("fail to parse %s,param:%s"%(type,k))
        return eva

# example: diagram:type=
def try_pase_diagram_eva(type):
	from eva.evas.diagram_eva import DiagramEva
	eva = DiagramEva()
	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'type':
			eva.set_type(k[1])
		elif k[0] == 'max_in_size':
			eva.set_max_in_size(int(k[1]))
		elif k[0] == 'max_out_size':
			eva.set_max_out_size(int(k[1]))
	return eva

def get_seprate_params(type):
	do_sepreate = True
	if 'query_candi' in type or 'qrc' in type:
		do_sepreate = False
	if 'add:' in type:
		do_sepreate = False
	# 复合类型,此时应该不做处理
	if '*' in type:
		do_sepreate = False
	if 'newhigh' in type:
		do_sepreate = False
	if 'ban_size' in type:
		do_sepreate = False

	# update 2023-09-09: 特殊处理height eva
	if 'height' in type:
		do_sepreate = False

	if 'zhusheng' in type:
		do_sepreate = False
	
	# 特殊处理subs comp eva
	if 'subs:' in type or 'comp:' in type:
		do_sepreate = False
	if type.startswith('pull'):
		do_sepreate = False

	if not do_sepreate:
		return [],type.split(':')	

	params = type.split(':')
	commons,uniques = [],[params[0]]
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'stop','fix_20cm','fix_interval','min_point','len','max_in_size','max_out_size','limit','ascending','asc','fix_chuangye','merge_left','hack' ]:
			commons.append(p)
		else:
			uniques.append(p)
	return commons,uniques

def deal_common_params(eva,commons):
	if not eva:
		return eva
	# 解析common字段
	for p in commons:
		k = p.split('=')
		if k[0] == 'fix_interval':
			eva.set_fix_interval(int(k[1]))
		elif k[0] == 'min_point':
			eva.set_min_point_num(int(k[1]))
		elif k[0] in [ 'stop','stop_sort' ]:
			b = True if k[1] in [ '1','true','TRUE','True' ] else False
			eva.set_stop_sort(b)
		elif k[0] == 'len':
			eva.set_fix_interval(60*float(k[1]))
		elif k[0] == 'limit':
			eva.set_limit(int(k[1]))
		elif k[0] in ['ascending','asc']:
			b = True if k[1] in [ '1','true','TRUE','True' ] else False
			eva.set_ascending(b)	
		elif k[0] == 'fix_chuangye':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_fix_chuangye(b)
		elif k[0] == 'fix_20cm':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_fix_20cm(b)
		elif k[0] == 'merge_left':
			b = True if k[1] in ['true','TRUE','True'] else False
			eva.set_merge_left(b)
		elif k[0] == 'hack':
			eva.set_hack(k[1])
	return eva

# 默认为1
def get_bf_len_from(type):
	type = type.split(':')[0]
	if not '.bf' in type:
		return 0
        l = 1
        if type.index('.bf')+len('.bf') < len(type):
                l = float(type[type.index('.bf')+len('.bf'):])
        return l 

def fix_xls_param(xls):
	return xls.replace('.',':').replace('__','*')

def fix_time_str(t):
	if len(t) == 6:
		return '%s:%s:%s'%(t[0:2],t[2:4],t[4:6])
	return t

if __name__ == "__main__":
	pass
