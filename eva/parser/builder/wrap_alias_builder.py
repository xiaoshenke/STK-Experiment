#!/usr/bin/python
# coding=utf-8

# 判断是否是 @eva.alias包下的类

def is_wrap_alias_type(type,debug=False):
	type = type.split(':')[0]

	node = build_wrap_alias_one(type)

	from eva.alias.wrap_alias_eva import WrapAliasEva
	if isinstance( node,WrapAliasEva ):
		if debug:
			print 'wrap_alias_builder.is_wrap_alias_type return True.'
		return True
        
	return False  

def build_wrap_alias_one(type,debug=False):
	eva = None

	from eva.parser.at_util import get_at_and_return_type
	at_timestr,type = get_at_and_return_type(type,debug)
	
	from util.param_util import get_param_from
	limit = int(get_param_from(type.split(':'),'limit',-1))

	day_len = int(get_param_from(type.split(':'),'len',-1))
	#print 'build_wrap_alias_one,day-len:%s'%(day_len)

	from util.param_util import get_param_removed_type_by
	type = get_param_removed_type_by(type,[ 'limit','len' ])

	name = type.split(':')[0]

	if name in [ 'pull0','pull1','pull2','pull3','pull4','pull5','pull7' ]:
		eva = try_parse_pulls(type)
	elif type == 'nh2' or type == 'nh2_1':
		eva = try_parse_nh2_1(type)
	elif type == 'maodian':
		eva = try_parse_maodian_1(type)
	elif type == 'fanbao':
		eva = try_parse_fanbao_1(type)
	elif name == 'nhigh':
		eva = try_parse_nhigh_1(type)
	elif type == 'jj_rzq1':
		eva = try_parse_jj_rzq1_1(type)
	elif type == 'jj_rzq3':
		eva = try_parse_jj_rzq3_1(type)
	elif type == 'jj_high2':
                eva = try_parse_jj_high2_1(type)
	elif type == 'jj_high3':
		eva = try_parse_jj_high3_1(type)
	elif type == 'jj_high5':
		eva = try_parse_jj_high5_1(type)
	elif type == 'jj_high7':
		eva = try_parse_jj_high7_1(type)
	elif type == 'jj_high10':
                eva = try_parse_jj_high10_1(type)
	elif type == 'jj_high15':
		eva = try_parse_jj_high15_1(type)
	elif type == 'jj_low0':
		eva = try_parse_jj_low0_1(type)
	elif type == 'jj_low2':
		eva = try_parse_jj_low2_1(type)
	elif type == 'low1':
		eva = try_parse_low1_1(type)
	elif type == 'low0':
		eva = try_parse_low0_1(type)
	elif type == 'low2':
		eva = try_parse_low2_1(type)
	#elif type == 'fenqi3_3':
	#	eva = try_parse_fenqi3_3(type)
	elif type == 'fenqi2':
		eva = try_parse_fenqi2_1(type)
	elif type == 'fenqi3':
		eva = try_parse_fenqi3_1(type)
	elif type == 'fenqi4':
		eva = try_parse_fenqi4_1(type)
	elif type == 'break5':
		eva = try_parse_break5_1(type)
	elif type == 'break10':
		eva = try_parse_break10_1(type)
	elif type == 'breakup1':
		eva = try_parse_breakup_1(type)
	elif type in [ 'upbound20','bound20' ]:
		eva = try_parse_upbound20_1(type)
	elif type in [ 'upbound30','bound30' ]:
		eva = try_parse_upbound30_1(type)
	elif type in [ 'upbound40','bound40' ]:
		eva = try_parse_upbound40_1(type)
	elif type in [ 'upbound60','bound60' ]:
		eva = try_parse_upbound60_1(type)
	elif type in [ 'upbound70','bound70' ]:
		eva = try_parse_upbound70_1(type)
	elif type in [ 'oph','oph1' ]:
		eva = try_parse_oph_1(type)
	elif type in [ 'th2','tph2','top_height2' ]:
		eva = try_parse_top_height_2(type)
	elif type in [ 'top_height','top_height1','th1','tph1' ]:
		eva = try_parse_top_height_1(type)
	elif type in [ 'top_risk','top_risk1' ]:
		eva = try_parse_top_risk_1(type)
	elif type in [ 'chaoyq','chaoyq1','chaoyuqi1','cyq1' ]:
		eva = try_parse_chaoyq_1(type)
	elif type in [ 'chaoyq2','chaoyuqi2','cyq2' ]:
		eva = try_parse_chaoyq_2(type)
	elif type in [ 'chaoyq3','chaoyuqi3' ]:
		eva = try_parse_chaoyq_3(type)
	elif type in [ 'top','top1' ]:
		eva = try_parse_top_1(type)
	elif name == 'newp1':
		eva = try_parse_newp1_1(type)
	elif name == 'newp2':
		eva = try_parse_newp2_1(type)
	elif name == 'newp3':
		eva = try_parse_newp3_1(type)
	elif name == 'newp4':
		eva = try_parse_newp4_1(type)
	elif name in [ 'blpull','belowpull','below_pull' ]:
		eva = try_parse_below_pull_1(type)
	elif name in [ 'ampull','amtpull','amount_pull' ] or name.startswith('ampull'):
		eva = try_parse_amount_pull_1(type)
	elif name in [ 'outvpull','ovpull','ov_pull' ]:
		eva = try_parse_ov_pull_1(type)
	elif name in [ 'ovwenhe2','ov_wenhe2' ]:
		eva = try_parse_ov_wenhe_2(type)
	elif name in [ 'ovwenhe','ov_wenhe' ]:
		eva = try_parse_ov_wenhe_1(type)
	elif name in [ 'ovhot','ov_hot' ]:
		eva = try_parse_ov_hot_1(type)
	elif name in [ 'aov','auto_ov','autoov' ]:
		eva = try_parse_auto_ov_1(type)
	elif name in [ 'auto_pull','autopull','apull' ]:
		eva = try_parse_auto_pull_1(type)
	elif name in [ 'xt_dibu','xtdibu' ]:
		eva = try_parse_xt_dibu_1(type)
	elif type == 'trd2_1':
		eva = try_parse_trd2_1(type)
	elif type.startswith('Co_1') or type == 'Co':
                eva = try_parse_co_1(type)
	elif type == 'upma1':
		eva = try_parse_upma_1(type)
	elif type == 'upma2':
		eva = try_parse_upma_2(type)
	elif type.startswith('stage1'):
                eva = try_parse_stage1_eva(type)
	elif type.startswith('stage2'):
		eva = try_parse_stage2_eva(type)
	elif type == 'good5':
		eva = try_parse_good5_1(type)
	elif type == 'good4_2':
		eva = try_parse_good4_2(type)
	elif type == 'good4':
		eva = try_parse_good4_1(type)
	elif type == 'good3':
		eva = try_parse_good3_1(type)
	elif type == 'good2_0':
		eva = try_parse_good2_0(type)
	elif type == 'good2_2':
		eva = try_parse_good2_2(type)
	elif type == 'good2' or type == 'good2_1':
		eva = try_parse_good2_1(type)
	elif type == 'good1':
		eva = try_parse_good1_1(type)
	elif type == 'good':
		eva = try_parse_good_1(type)
	elif type.startswith('shake2'):
		eva = try_parse_shake2_1(type)
	elif type.startswith('shake3'):
		eva = try_parse_shake3_1(type)	
	elif type.startswith('shake4'):
		eva = try_parse_shake4_1(type)
	elif type.startswith('shake5'):
		eva = try_parse_shake5_1(type)
	elif type.startswith('shake6'):
		eva = try_parse_shake6_1(type)
	elif type.startswith('shake7'):
		eva = try_parse_shake7_1(type)
	#elif type in [ 'shake10','shake10_1' ]:
	#	eva = try_parse_shake10_1(type) 
	#elif type in [ 'shake20','shake20_1' ]:
	#	eva = try_parse_shake20_1_eva(type)
	#elif type.startswith( 'shake20_2' ):
	#	eva = try_parse_shake20_2_eva(type)
	#elif type.startswith( 'shake20_3' ):
	#	eva = try_parse_shake20_3_eva(type)
	elif type in [ 'newhigh10','newhigh10_1' ]:
		eva = try_parse_newhigh10_1(type)
	elif type == 'newhigh10_2':
		eva = try_parse_newhigh10_2(type)
	elif type == 'newhigh10_3':
		eva = try_parse_newhigh10_3(type)
	elif type == 'newlow5':
		eva = try_parse_newlow5_1(type)
	elif type == 'newlow6':
		eva = try_parse_newlow6_1(type)
	elif type == 'newlow7':
		eva = try_parse_newlow7_1(type)
	elif type == 'newlow8':
		eva = try_parse_newlow8_1(type)
	elif type == 'newlow10':
		eva = try_parse_newlow10_1(type)
	elif type == 'high02':
		eva = try_parse_high02_eva(type)
	elif type == 'high03':
		eva = try_parse_high03_eva(type)
	elif type == 'high05':
		eva = try_parse_high05_eva(type)
	elif type == 'high79':
		eva = try_parse_high79_eva(type)
	elif type.startswith('high7') or type == 'high7_1':
		eva = try_parse_high7_eva(type)
	elif type.startswith('high9') or type == 'high9_1':
		eva = try_parse_high9_eva(type)
	elif type == 'high57':
		eva = try_parse_high57_eva(type)
	elif type == 'high5_2':
		eva = try_parse_high5_2(type)
	elif name in  [ 'high5_1','high5' ]:
#type.startswith('high5') or type in [ 'high5_1','high5' ]:
		eva = try_parse_high5_eva(type)
	elif type == 'high45':
		eva = try_parse_high45_eva(type)
	elif type == 'high48':
		eva = try_parse_high48_eva(type)
	elif type.startswith('high4') or type == 'high4_1':
		eva = try_parse_high4_eva(type)
	elif type == 'high35':	
		eva = try_parse_high35_eva(type)
	elif type == 'high36':
		eva = try_parse_high36_eva(type)
	elif type.startswith('high3') or type == 'high3_1':
		eva = try_parse_high3_eva(type)
	elif type.startswith('high25') or type == 'high25_1':
		eva = try_parse_high25_eva(type)
	elif type == 'high23':
		eva = try_parse_high23_eva(type)
	elif type == 'high24':
		eva = try_parse_high24_eva(type)
	elif type == 'high2':
		eva = try_parse_high2_eva(type)
	elif type == 'high14':
		eva = try_parse_high14_eva(type)
	elif type in [ 'analyze','analyse','analyze1','analyse1' ]:
		eva = try_parse_analyze_1(type) 
	elif type == 'co01':
		eva = try_parse_co01(type)
	elif type == 'co02':
		eva = try_parse_co02(type)
	elif type == 'co03':
		eva = try_parse_co03(type)
	elif type == 'co13':
		eva = try_parse_co13(type)
	elif type == 'co2':
		eva = try_parse_co2(type)
	elif type == 'co24':
		eva = try_parse_co24(type)
	elif type == 'co25':
		eva = try_parse_co25(type)
	elif type == 'co3':
		eva = try_parse_co3(type)
	elif type == 'co4':
		eva = try_parse_co4(type)
	elif type == 'btw07':
		eva = try_parse_btw07(type)
	elif type == 'btw05':
		eva = try_parse_btw05(type)
	elif type == 'btw04':
		eva = try_parse_btw04(type)
	elif type == 'btw03':
		eva = try_parse_btw03(type)
	elif type == 'btw02':
		eva = try_parse_btw02(type)
	elif type == 'btw01':
		eva = try_parse_btw01(type)
	elif type == 'btw09':
		eva = try_parse_btw09(type)
	elif type == 'btw13':
		eva = try_parse_btw13(type)
	elif type == 'btw14':
                eva = try_parse_btw14(type)
	elif type == 'btw15':
		eva = try_parse_btw15(type)
	elif type == 'btw17':
		eva = try_parse_btw17(type)
	elif type == 'btw19':
		eva = try_parse_btw19(type)
	elif type == 'btw24':
		eva = try_parse_btw24(type)
	elif type == 'btw25':
		eva = try_parse_btw25(type)
	elif type == 'btw26':
		eva = try_parse_btw26(type)
	elif type == 'btw27':
		eva = try_parse_btw27(type)
	elif type == 'btw29':
		eva = try_parse_btw29(type)
	elif type == 'btw35':
		eva = try_parse_btw35(type)
	elif type == 'btw36':
		eva = try_parse_btw36(type)
	elif type == 'btw37':
		eva = try_parse_btw37(type)
	elif type == 'btw48':
		eva = try_parse_btw48(type)
	elif type == 'rup1':
		eva = try_parse_rup1(type)
	elif type == 'rup2':
		eva = try_parse_rup2(type)
	elif type == 'rup3':
		eva = try_parse_rup3(type)
	elif type == 'rup4':
		eva = try_parse_rup4(type)
	elif type == 'rup5':
		eva = try_parse_rup5(type)
	elif type == 'rup6':
		eva = try_parse_rup6(type)
	elif type == 'rup7':
		eva = try_parse_rup7(type)
	elif type == 'opp1':
		eva = try_parse_opp1(type)
	elif type == 'opp2':
		eva = try_parse_opp2(type)
	elif type == 'opp3':
		eva = try_parse_opp3(type)
	elif type == 'opp4':
                eva = try_parse_opp4(type)
	elif type == 'opp5':
		eva = try_parse_opp5(type)
	elif type == 'opp7':
		eva = try_parse_opp7(type)
	elif type == 'ban24':
		eva = try_parse_ban24(type)
	elif type in [ 'ban00','ban0','0ban' ]:
		eva = try_parse_ban0(type)
	elif type == 'ban30':
		eva = try_parse_ban30(type)
	elif type == 'ban50':
		eva = try_parse_ban50(type)
	elif type == 'ban12':
		eva = try_parse_ban12(type)
	elif type == 'ban13':
		eva = try_parse_ban13(type)
	elif type == 'ban11' or type == 'ban1' or type == '1ban':
		eva = try_parse_ban11(type)
	elif type == 'ban32':
                eva = try_parse_ban32(type)
	elif type == 'ban34':
                eva = try_parse_ban34(type)
	elif type == 'ban35':
                eva = try_parse_ban35(type)
	elif type == 'up0':
                eva = try_parse_up0(type)
	elif type == 'up1':
		eva = try_parse_up1(type)
	elif type == 'up10':
		eva = try_parse_up10(type)
	elif type == 'upm1':
		eva = try_parse_upm1(type)
        elif type == 'up2':
                eva = try_parse_up2(type)
	elif type == 'up2_2':
		eva = try_parse_up2_2(type)
        elif type == 'up3':
                eva = try_parse_up3(type)
	elif type == 'up4':
		eva = try_parse_up4(type)
        elif type == 'up5':
                eva = try_parse_up5(type)	
	elif type == 'up7':
		eva = try_parse_up7(type)
	elif type == 'up8':
                eva = try_parse_up8(type)
	elif type == 'up8':
                eva = try_parse_up9(type)
	elif type == 'risk2':
		eva = try_parse_risk2(type)
	elif type == 'risk3':
		eva = try_parse_risk3(type)
	elif type == 'risk4':
		eva = try_parse_risk4(type)
	elif type == 'risk5':
		eva = try_parse_risk5(type)
	elif type == 'risk7':
		eva = try_parse_risk7(type)
	elif type == 'cl2':
		eva = try_parse_cl2(type)
	elif type == 'cl3':
		eva = try_parse_cl3(type)
	elif type == 'cl4':
		eva = try_parse_cl4(type)
	elif type == 'cl5':
		eva = try_parse_cl5(type)
	elif type == 'cl7':
		eva = try_parse_cl7(type)
	elif type == 'amount3':
		eva = try_parse_amount3(type)
	elif type == 'amount5':
		eva = try_parse_amount5(type)
	elif type == 'amount10':
		eva = try_parse_amount10(type)
	elif type == 'tamount10':
		eva = try_parse_top_amount10(type)
	elif type == 'tamount20':
		eva = try_parse_top_amount20(type)
	elif type == 'tamount30':
		eva = try_parse_top_amount30(type)	
	elif type == 'tamount40':
		eva = try_parse_top_amount40(type)
	elif type == 'tamount50':
		eva = try_parse_top_amount50(type)
	elif type == 'tamount80':
		eva = try_parse_top_amount80(type)
	elif type == 'tamount100':
		eva = try_parse_top_amount100(type)
	elif type in [ '2day_good1','2days_good1' ]:
		eva = try_parse_2day_good1(type)
	elif type in [ 'amount_and_good','amount_and_good_1','aag' ]:
		eva = try_parse_amount_and_good_1(type)
	elif type in [ 'amount_and_bad','amount_and_bad_1','aab' ]:
		eva = try_parse_amount_and_bad_1(type)
	elif type in [ 'tover_and_good','tag' ]:
		eva = try_parse_tover_and_good_1(type)
	elif type in [ 'tover_and_bad','tab' ]:
		eva = try_parse_tover_and_bad_1(type)
	if not eva:
		return None

	if at_timestr:
		eva.set_at_timestr(at_timestr)  

	if limit > 0:
		eva.set_limit(limit)
	if day_len > 0:
		eva.set_day_len(day_len)
	return eva

# example: pull2,pull3,pull4,pull5
def try_parse_pulls(type):
	name = type.split(':')[0]

	eva = None
	if name == 'pull0':
		from eva.alias.pulls_1 import Pull0_1Eva
		eva = Pull0_1Eva()
	elif name == 'pull1':
		from eva.alias.pulls_1 import Pull1_1Eva
		eva = Pull1_1Eva()
	elif name == 'pull2':
		from eva.alias.pulls_1 import Pull2_1Eva
		eva = Pull2_1Eva()
	elif name == 'pull3':
		from eva.alias.pulls_1 import Pull3_1Eva
		eva = Pull3_1Eva()
	elif name == 'pull4':
		from eva.alias.pulls_1 import Pull4_1Eva
		eva = Pull4_1Eva()
	elif name == 'pull5':
		from eva.alias.pulls_1 import Pull5_1Eva
		eva = Pull5_1Eva()
	elif name == 'pull7':
		from eva.alias.pulls_1 import Pull7_1Eva
		eva = Pull7_1Eva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'len':
			eva.set_len(int(k[1]))
		elif k[0] == 't2':
			eva.set_t2(k[1])
		elif k[0] == 'mode':
			eva.set_mode(k[1])
	return eva

# example: xt_dibu
def try_parse_xt_dibu_1(type):
	from eva.alias.xt_dibus_1 import XtDibu_1Eva
	return XtDibu_1Eva()

# example: amount3
def try_parse_amount3(type):
	from eva.alias.amounts_1 import Amount3_1Eva
	return Amount3_1Eva()

# example: amount5
def try_parse_amount5(type):
	from eva.alias.amounts_1 import Amount5_1Eva
	return Amount5_1Eva()

# example: amount10
def try_parse_amount10(type):
	from eva.alias.amounts_1 import Amount10_1Eva
	return Amount10_1Eva()

# example: tamount10
def try_parse_top_amount10(type):
	from eva.alias.top_amounts_1 import TopAmount10_1Eva
	return TopAmount10_1Eva()

# example: tamount20
def try_parse_top_amount20(type):
	from eva.alias.top_amounts_1 import TopAmount20_1Eva
	return TopAmount20_1Eva()

# example: tamount30
def try_parse_top_amount30(type):
	from eva.alias.top_amounts_1 import TopAmount30_1Eva
	return TopAmount30_1Eva()

# example: tamount40
def try_parse_top_amount40(type):
	from eva.alias.top_amounts_1 import TopAmount40_1Eva
	return TopAmount40_1Eva()

# example: tamount50
def try_parse_top_amount50(type):
	from eva.alias.top_amounts_1 import TopAmount50_1Eva
	return TopAmount50_1Eva()

# example: tamount80
def try_parse_top_amount80(type):
	from eva.alias.top_amounts_1 import TopAmount80_1Eva
	return TopAmount80_1Eva()

# example: tamount100
def try_parse_top_amount100(type):
	from eva.alias.top_amounts_1 import TopAmount100_1Eva
	return TopAmount100_1Eva()

# example: good5
def try_parse_good5_1(type):
	from eva.alias.goods_1 import Good5_1Eva
	return Good5_1Eva()

# example: good4_2
def try_parse_good4_2(type):
	from eva.alias.goods_1 import Good4_2Eva
	return Good4_2Eva()

# example: good4
def try_parse_good4_1(type):
	from eva.alias.goods_1 import Good4_1Eva
	return Good4_1Eva()

# example: good3
def try_parse_good3_1(type):
	from eva.alias.goods_1 import Good3_1Eva
	return Good3_1Eva()

# example: good2_0
def try_parse_good2_0(type):
	from eva.alias.goods_1 import Good2_0Eva
	return Good2_0Eva()

# example: good2_2
def try_parse_good2_2(type):
	from eva.alias.goods_1 import Good2_2Eva
	return Good2_2Eva()

# example: good2
def try_parse_good2_1(type):
	from eva.alias.goods_1 import Good2_1Eva
	return Good2_1Eva()

# example: good1
def try_parse_good1_1(type):
	from eva.alias.goods_1 import Good1_1Eva
	return Good1_1Eva()

# example: good
def try_parse_good_1(type):
	from eva.alias.goods_1 import GoodEva
	return GoodEva()

# example: shake2
def try_parse_shake2_1(type):
	from eva.alias.shakes_1 import Shake2_1Eva
	return Shake2_1Eva()

# example: shake3
def try_parse_shake3_1(type):
	from eva.alias.shakes_1 import Shake3_1Eva
	return Shake3_1Eva()

# example: shake4
def try_parse_shake4_1(type):
	from eva.alias.shakes_1 import Shake4_1Eva
	return Shake4_1Eva()

# example: shake5
def try_parse_shake5_1(type):
	from eva.alias.shakes_1 import Shake5_1Eva
	return Shake5_1Eva()

# example: shake6
def try_parse_shake6_1(type):
	from eva.alias.shakes_1 import Shake6_1Eva
	return Shake6_1Eva()

# example: shake7
def try_parse_shake7_1(type):
	from eva.alias.shakes_1 import Shake7_1Eva
	return Shake7_1Eva()

# example: shake10
def try_parse_shake10_1(type):
	from eva.alias.shakes_1 import Shake10_1Eva
	return Shake10_1Eva()

# example: shake20
def try_parse_shake20_1_eva(type):
	from eva.alias.shakes_1 import Shake20_1Eva
	return Shake20_1Eva()

# example: shake20_2
def try_parse_shake20_2_eva(type):
	from eva.alias.shakes_2 import Shake20_2Eva
	return Shake20_2Eva()

# example: shake20_3
def try_parse_shake20_3_eva(type):
	from eva.alias.shakes_3 import Shake20_3Eva
	return Shake20_3Eva()

# example: tover_and_good_1
def try_parse_tover_and_good_1(type):
	from eva.alias.tover_and_good_1 import ToverAndGood_1Eva
	return ToverAndGood_1Eva()

# example: tover_and_bad_1
def try_parse_tover_and_bad_1(type):
	from eva.alias.tover_and_bad_1 import ToverAndBad_1Eva
	return ToverAndBad_1Eva()

# example: amount_and_good
def try_parse_amount_and_good_1(type):
	from eva.alias.amount_and_good_1 import AmountAndGood_1Eva
	return AmountAndGood_1Eva()

# example: amount_and_bad
def try_parse_amount_and_bad_1(type):
	from eva.alias.amount_and_bad_1 import AmountAndBad_1Eva
	return AmountAndBad_1Eva()

# example: 2day_good1
def try_parse_2day_good1(type):
	from eva.alias.two_day_good_1 import TwoDayGood_1Eva
	return TwoDayGood_1Eva()

# example: newp1:mode=
def try_parse_newp1_1(type):
	from eva.alias.newps_1 import Newp1_1Eva
	eva = Newp1_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	eva.set_mode(mode)

	t2 = get_param_from(type.split(':'),'t2')
	eva.set_t2(t2)

	return eva

# example: newp2:mode=
def try_parse_newp2_1(type):
	from eva.alias.newps_1 import Newp2_1Eva
	eva = Newp2_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	eva.set_mode(mode)

	t2 = get_param_from(type.split(':'),'t2')
	eva.set_t2(t2)

	return eva

# example: newp3:mode=
def try_parse_newp3_1(type):
	from eva.alias.newps_1 import Newp3_1Eva
	eva = Newp3_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	eva.set_mode(mode)

	t2 = get_param_from(type.split(':'),'t2')
	eva.set_t2(t2)

	return eva

# example: newp4:mode=
def try_parse_newp4_1(type):
	from eva.alias.newps_1 import Newp4_1Eva
	eva = Newp4_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	eva.set_mode(mode)

	t2 = get_param_from(type.split(':'),'t2')
	eva.set_t2(t2)

	return eva

# example: apull:mode=:min_pchg=
def try_parse_auto_pull_1(type):
	from eva.alias.pulls_1 import AutoPull_1Eva
	eva = AutoPull_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	if mode:
		eva.set_mode(mode)

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] == 'min_pchg':
			eva.set_min_pchg(float(k[1]))

	return eva

# example: blpull
def try_parse_below_pull_1(type):
	from eva.alias.below_pulls_1 import BelowPulls_1Eva
	eva = BelowPulls_1Eva()
	return eva

# example: ampull:mode=:t2=:min_pull=
def try_parse_amount_pull_1(type):
	from eva.alias.amt_pulls_1 import AmtPulls_1Eva
	eva = AmtPulls_1Eva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min_pull','min' ]:
			eva.set_min_pull(float(k[1]))
		elif k[0] in [ 'min_amt','min_rate','min_amount' ]:
			eva.set_min_amt(float(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 't2':
			eva.set_t2(k[1])
		else:
			print u'eva.parser.builder.wrap_alias_builder.try_parse_amount_pull_1,解析设置字符串:%s 失败'%(p)

	name = params[0]
	idx = name.index('pull')
	#print name,len(name),idx,idx+len('pull')
	if len(name) > idx+len('pull'):
		min_pull = float(name[idx+len('pull'):])
		eva.set_min_pull(min_pull)
	
	return eva

# example: aov
def try_parse_auto_ov_1(type):
	from eva.alias.auto_ovs_1 import AutoOv_1Eva
	eva = AutoOv_1Eva()
	return eva

# example: ovhot:min_amt=
def try_parse_ov_hot_1(type):
	from eva.alias.ov_hots_1 import OvHot_1Eva
	eva = OvHot_1Eva()
	return eva

# example: ovwenhe:min_amt=
def try_parse_ov_wenhe_1(type):
	from eva.alias.ov_wenhes_1 import OvWenhe_1Eva
	eva = OvWenhe_1Eva()
	return eva

# example: ovwenhe2:min_amt
def try_parse_ov_wenhe_2(type):
	from eva.alias.ov_wenhes_1 import OvWenhe2_1Eva
	eva = OvWenhe2_1Eva()
	return eva

# example: ovpull:mode=:t2=:min_pull=
def try_parse_ov_pull_1(type):
	from eva.alias.ov_pulls_1 import OvPulls_1Eva
	eva = OvPulls_1Eva()

	params = type.split(':')
	for p in params[1:]:
		k = p.split('=')
		if k[0] in [ 'min_pchg','min_pull','min' ]:
			eva.set_min_pull(float(k[1]))
		elif k[0] in [ 'min_ov','min_amt','min_rate','min_amount' ]:
			eva.set_min_amt(float(k[1]))
		elif k[0] == 'mode':
			eva.set_mode(k[1])
		elif k[0] == 't2':
			eva.set_t2(k[1])
		else:
			print u'eva.parser.builder.wrap_alias_builder.try_parse_amount_pull_1,解析设置字符串:%s 失败'%(p)
	return eva

# example: nh2_1
def try_parse_nh2_1(type):
	from eva.alias.nh2_1 import Nh2_1Eva
	return Nh2_1Eva()

# example: oph_1
def try_parse_oph_1(type):
	from eva.alias.oph_1 import Oph_1Eva
	return Oph_1Eva()

# example: top_height2
def try_parse_top_height_2(type):
	from eva.alias.top_height_2 import TopHeight_2Eva
	return TopHeight_2Eva()

# example: top_height1
def try_parse_top_height_1(type):
	from eva.alias.top_height_1 import TopHeight_1Eva
	return TopHeight_1Eva()

# example: top_risk1
def try_parse_top_risk_1(type):
	from eva.alias.top_risk_1 import TopRisk_1Eva
	return TopRisk_1Eva()

# example: chaoyq1
def try_parse_chaoyq_1(type):
	from eva.alias.chaoyq_1 import Chaoyuqi_1Eva
	return Chaoyuqi_1Eva()

# example: chaoyq2
def try_parse_chaoyq_2(type):
	from eva.alias.chaoyq_2 import Chaoyuqi_2Eva
	return Chaoyuqi_2Eva()

# example: chaoyq3
def try_parse_chaoyq_3(type):
	from eva.alias.chaoyq_3 import Chaoyuqi_3Eva
	return Chaoyuqi_3Eva()

# example: top:limit=
def try_parse_top_1(type):
	from eva.alias.top_eva import Top_1Eva
	return Top_1Eva()

# example: trd2_1
def try_parse_trd2_1(type):
	from eva.alias.trd2_1 import Trd2_1Eva
	return Trd2_1Eva()

# example: maodian
def try_parse_maodian_1(type):
	from eva.alias.maodian_1 import Maodian_1Eva
	return Maodian_1Eva()

# example: nhigh
def try_parse_nhigh_1(type):
	from eva.alias.nhigh_eva import NHigh_1Eva
	return NHigh_1Eva()

# example: fanbao
def try_parse_fanbao_1(type):
	from eva.alias.fanbaos_1 import FanbaoEva
	return FanbaoEva()

# example: low0
def try_parse_low0_1(type):
	from eva.alias.lows_1 import Low0_1Eva
	return Low0_1Eva()

# example: low1
def try_parse_low1_1(type):
	from eva.alias.lows_1 import Low1_1Eva
	return Low1_1Eva()

# example: low2
def try_parse_low2_1(type):
	from eva.alias.lows_1 import Low2_1Eva
	return Low2_1Eva()

# example: jj_low0
def try_parse_jj_low0_1(type):
	from eva.alias.jj_lows_1 import JJLow0_1Eva
	return JJLow0_1Eva()

# example: jj_low2
def try_parse_jj_low2_1(type):
	from eva.alias.jj_lows_1 import JJLow2_1Eva
	return JJLow2_1Eva()

# example: jj_rzq1
def try_parse_jj_rzq1_1(type):
	from eva.alias.jj_rzqs_1 import JJRzq1_1Eva
	eva = JJRzq1_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	if mode:
		eva.set_mode(mode)
	return eva

# example: jj_rzq3
def try_parse_jj_rzq3_1(type):
	from eva.alias.jj_rzqs_1 import JJRzq3_1Eva
	eva = JJRzq3_1Eva()

	from util.param_util import get_param_from
	mode = get_param_from(type.split(':'),'mode')
	if mode:
		eva.set_mode(mode)
	return eva

# example: jj_high2
def try_parse_jj_high2_1(type):
	from eva.alias.jj_highs_1 import JJHigh2_1Eva
	return JJHigh2_1Eva()

# example: jj_high3
def try_parse_jj_high3_1(type):
	from eva.alias.jj_highs_1 import JJHigh3_1Eva
	return JJHigh3_1Eva()

# example: jj_high5
def try_parse_jj_high5_1(type):
	from eva.alias.jj_highs_1 import JJHigh5_1Eva
	return JJHigh5_1Eva()

# example: jj_high7
def try_parse_jj_high7_1(type):
	from eva.alias.jj_highs_1 import JJHigh7_1Eva
	return JJHigh7_1Eva()

# example: jj_high10
def try_parse_jj_high10_1(type):
	from eva.alias.jj_highs_1 import JJHigh10_1Eva
	return JJHigh10_1Eva()

# example: jj_high15
def try_parse_jj_high15_1(type):
	from eva.alias.jj_highs_1 import JJHigh15_1Eva
	return JJHigh15_1Eva()

# example: break5
def try_parse_break5_1(type):
	from eva.alias.breaks_1 import Break5_1Eva
	return Break5_1Eva()

# example: break10
def try_parse_break10_1(type):
	from eva.alias.breaks_1 import Break10_1Eva
	return Break10_1Eva()

# example: breakup1
def try_parse_breakup_1(type):
	from eva.alias.breakup_1 import Breakup_1Eva
	return Breakup_1Eva()

# example: upbound20
def try_parse_upbound20_1(type):
	from eva.alias.upbounds_1 import Upbound20_1Eva
	return Upbound20_1Eva()

# example: upbound30
def try_parse_upbound30_1(type):
	from eva.alias.upbounds_1 import Upbound30_1Eva
	return Upbound30_1Eva()

# example: upbound40
def try_parse_upbound40_1(type):
	from eva.alias.upbounds_1 import Upbound40_1Eva
	return Upbound40_1Eva()

# example: upbound60
def try_parse_upbound60_1(type):
	from eva.alias.upbounds_1 import Upbound60_1Eva
	return Upbound60_1Eva()

# example: upbound70
def try_parse_upbound70_1(type):
	from eva.alias.upbounds_1 import Upbound70_1Eva
	return Upbound70_1Eva()

# example: fenqi2
def try_parse_fenqi2_1(type):
	from eva.alias.fenqis_1 import Fenqi2_1Eva
	return Fenqi2_1Eva()

# example: fenqi3_3
def try_parse_fenqi3_3(type):
	from eva.alias.fenqis_1 import Fenqi3_3Eva
	return Fenqi3_3Eva()

# example: fenqi4
def try_parse_fenqi4_1(type):
	from eva.alias.fenqis_1 import Fenqi4_1Eva
	return Fenqi4_1Eva()

# example: Co
def try_parse_co_1(type):
        from eva.alias.co_1_eva import Co_1Eva
        return Co_1Eva()

# example: upma1
def try_parse_upma_1(type):
	from eva.alias.upma_1 import Upma_1Eva
	eva = Upma_1Eva()
	return eva

# example: upma2
def try_parse_upma_2(type):
	from eva.alias.upma_2 import Upma_2Eva
	eva = Upma_2Eva()
	return eva

# example: opp
def try_parse_opp_1(type):
        from eva.alias.opp_1 import Opp_1Eva
        return Opp_1Eva()

# example: stage1
def try_parse_stage1_eva(type):
        from eva.alias.stage_1_eva import Stage_1Eva
        eva = Stage_1Eva()
        return eva

# example: stage2
def try_parse_stage2_eva(type):
        from eva.alias.stage_2_eva import Stage_2Eva
        eva = Stage_2Eva()
        return eva

# example: high02
def try_parse_high02_eva(type):
	from eva.alias.highs_1 import High02_1Eva
	eva = High02_1Eva()
	return eva

# example: high03
def try_parse_high03_eva(type):
	from eva.alias.highs_1 import High03_1Eva
	eva = High03_1Eva()
	return eva

# example: high05
def try_parse_high05_eva(type):
	from eva.alias.highs_1 import High05_1Eva
	eva = High05_1Eva()
	return eva

# example: high9
def try_parse_high9_eva(type):
	from eva.alias.highs_1 import High9_1Eva
	eva = High9_1Eva()
	return eva

# example: high79
def try_parse_high79_eva(type):
        from eva.alias.highs_1 import High79_1Eva
        eva = High79_1Eva()
        return eva

# example: high7
def try_parse_high7_eva(type):
        from eva.alias.highs_1 import High7_1Eva
        eva = High7_1Eva()
        return eva

# example: high5_2
def try_parse_high5_2(type):
        from eva.alias.highs_1 import High5_2Eva
        eva = High5_2Eva()
        return eva

# example: high57
def try_parse_high57_eva(type):
        from eva.alias.highs_1 import High57_1Eva
        eva = High57_1Eva()
        return eva

# example: high5
def try_parse_high5_eva(type):
	from eva.alias.highs_1 import High5_1Eva
	eva = High5_1Eva()
	return eva

# example: high4
def try_parse_high4_eva(type):
	from eva.alias.highs_1 import High4_1Eva
	eva = High4_1Eva()
	return eva

# example: high45
def try_parse_high45_eva(type):
	from eva.alias.highs_1 import High45_1Eva
	eva = High45_1Eva()
	return eva

# example: high48
def try_parse_high48_eva(type):
	from eva.alias.highs_1 import High48_1Eva
	eva = High48_1Eva()
	return eva

# example: high2
def try_parse_high2_eva(type):
        from eva.alias.highs_1 import High2_1Eva
        eva = High2_1Eva()
        return eva

# example: high35
def try_parse_high35_eva(type):
	from eva.alias.highs_1 import High35_1Eva
	eva = High35_1Eva()
	return eva

# example: high36
def try_parse_high36_eva(type):
	from eva.alias.highs_1 import High36_1Eva
	eva = High36_1Eva()
	return eva

# example: high3
def try_parse_high3_eva(type):
	from eva.alias.highs_1 import High3_1Eva
	eva = High3_1Eva()
	return eva

# example: high14
def try_parse_high14_eva(type):
	from eva.alias.highs_1 import High14_1Eva
	eva = High14_1Eva()
	return eva

# example: high23
def try_parse_high23_eva(type):
	from eva.alias.highs_1 import High23_1Eva
	eva = High23_1Eva()
	return eva

# example: high24
def try_parse_high24_eva(type):
	from eva.alias.highs_1 import High24_1Eva
	eva = High24_1Eva()
	return eva

# example: high25
def try_parse_high25_eva(type):
	from eva.alias.highs_1 import High25_1Eva
	eva = High25_1Eva()
	return eva

# example: analyze1
def try_parse_analyze_1(type):
	from eva.alias.analyze_1 import Analyze_1Eva
	eva = Analyze_1Eva()
	return eva

# example: co01
def try_parse_co01(type):
	from eva.alias.cos_1 import Co01Eva
	eva = Co01Eva()
	return eva

# example: co02
def try_parse_co02(type):
	from eva.alias.cos_1 import Co02Eva
	eva = Co02Eva()
	return eva

# example: co03
def try_parse_co03(type):
	from eva.alias.cos_1 import Co03Eva
	eva = Co03Eva()
	return eva

# example: co13
def try_parse_co13(type):
	from eva.alias.cos_1 import Co13Eva
	eva = Co13Eva()
	return eva

# example: co2
def try_parse_co2(type):
	from eva.alias.cos_1 import Co2Eva
	eva = Co2Eva()
	return eva

# example: co24
def try_parse_co24(type):
	from eva.alias.cos_1 import Co24Eva
	eva = Co24Eva()
	return eva

# example: co25
def try_parse_co25(type):
	from eva.alias.cos_1 import Co25Eva
	eva = Co25Eva()
	return eva

# example: co3
def try_parse_co3(type):
	from eva.alias.cos_1 import Co3Eva
	eva = Co3Eva()
	return eva

# example: co4
def try_parse_co4(type):
	from eva.alias.cos_1 import Co4Eva
	eva = Co4Eva()
	return eva

# example: btw01
def try_parse_btw01(type):
	from eva.alias.btws_1 import Btw01Eva
	eva = Btw01Eva()
	return eva

# example: btw02
def try_parse_btw02(type):
	from eva.alias.btws_1 import Btw02Eva
	eva = Btw02Eva()
	return eva

# example: btw04
def try_parse_btw04(type):
	from eva.alias.btws_1 import Btw04Eva
	eva = Btw04Eva()
	return eva

# example: btw07
def try_parse_btw07(type):
	from eva.alias.btws_1 import Btw07Eva
	eva = Btw07Eva()
	return eva

# example: btw09
def try_parse_btw09(type):
	from eva.alias.btws_1 import Btw09Eva
	eva = Btw09Eva()
	return eva

# example: btw05
def try_parse_btw05(type):
	from eva.alias.btws_1 import Btw05Eva
	eva = Btw05Eva()
	return eva

# example: btw03
def try_parse_btw03(type):
	from eva.alias.btws_1 import Btw03Eva
	eva = Btw03Eva()
	return eva

# example: btw13
def try_parse_btw13(type):
	from eva.alias.btws_1 import Btw13Eva
	eva = Btw13Eva()
	return eva

# example: btw14
def try_parse_btw14(type):
	from eva.alias.btws_1 import Btw14Eva
	eva = Btw14Eva()
	return eva

# example: btw15
def try_parse_btw15(type):
	from eva.alias.btws_1 import Btw15Eva
	eva = Btw15Eva()
	return eva

# example: btw17
def try_parse_btw17(type):
	from eva.alias.btws_1 import Btw17Eva
	eva = Btw17Eva()
	return eva

# example: btw19
def try_parse_btw19(type):
	from eva.alias.btws_1 import Btw19Eva
	eva = Btw19Eva()
	return eva

# example: btw24
def try_parse_btw24(type):
	from eva.alias.btws_1 import Btw24Eva
	eva = Btw24Eva()
	return eva

# example: btw25
def try_parse_btw25(type):
	from eva.alias.btws_1 import Btw25Eva
	eva = Btw25Eva()
	return eva

# example: btw26
def try_parse_btw26(type):
	from eva.alias.btws_1 import Btw26Eva
	eva = Btw26Eva()
	return eva

# example: btw27
def try_parse_btw27(type):
	from eva.alias.btws_1 import Btw27Eva
	eva = Btw27Eva()
	return eva

# example: btw29
def try_parse_btw29(type):
	from eva.alias.btws_1 import Btw29Eva
	eva = Btw29Eva()
	return eva

# example: btw35
def try_parse_btw35(type):
	from eva.alias.btws_1 import Btw35Eva
	eva = Btw35Eva()
	return eva

# example: btw36
def try_parse_btw36(type):
	from eva.alias.btws_1 import Btw36Eva
	eva = Btw36Eva()
	return eva

# example: btw37
def try_parse_btw37(type):
	from eva.alias.btws_1 import Btw37Eva
	eva = Btw37Eva()
	return eva

# example: btw48
def try_parse_btw48(type):
	from eva.alias.btws_1 import Btw48Eva
	eva = Btw48Eva()
	return eva

# example: rup1
def try_parse_rup1(type):
	from eva.alias.rups_1 import Rup1_1Eva
	eva = Rup1_1Eva()
	return eva

# example: rup2
def try_parse_rup2(type):
	from eva.alias.rups_1 import Rup2_1Eva
	eva = Rup2_1Eva()
	return eva

# example: rup3
def try_parse_rup3(type):
	from eva.alias.rups_1 import Rup3_1Eva
	eva = Rup3_1Eva()
	return eva

# example: rup4
def try_parse_rup4(type):
	from eva.alias.rups_1 import Rup4_1Eva
	eva = Rup4_1Eva()
	return eva

# example: rup5
def try_parse_rup5(type):
	from eva.alias.rups_1 import Rup5_1Eva
	eva = Rup5_1Eva()
	return eva

# example: rup6
def try_parse_rup6(type):
	from eva.alias.rups_1 import Rup6_1Eva
	eva = Rup6_1Eva()
	return eva

# example: rup7
def try_parse_rup7(type):
	from eva.alias.rups_1 import Rup7_1Eva
	eva = Rup7_1Eva()
	return eva

# example: opp1
def try_parse_opp1(type):
	from eva.alias.opps_1 import Opp1_1Eva
	eva = Opp1_1Eva()
	return eva

# example: opp2
def try_parse_opp2(type):
	from eva.alias.opps_1 import Opp2_1Eva
	eva = Opp2_1Eva()
	return eva

# example: opp3
def try_parse_opp3(type):
	from eva.alias.opps_1 import Opp3_1Eva
	eva = Opp3_1Eva()
	return eva

# example: opp4
def try_parse_opp4(type):
	from eva.alias.opps_1 import Opp4_1Eva
	eva = Opp4_1Eva()
	return eva

# example: opp5
def try_parse_opp5(type):
	from eva.alias.opps_1 import Opp5_1Eva
	eva = Opp5_1Eva()
	return eva

# example: opp7
def try_parse_opp7(type):
	from eva.alias.opps_1 import Opp7_1Eva
	eva = Opp7_1Eva()
	return eva

# example: ban0
def try_parse_ban0(type):
	from eva.alias.bans_1 import Ban0Eva
	eva = Ban0Eva()
	return eva

# example: ban30
def try_parse_ban30(type):
	from eva.alias.bans_1 import Ban30Eva
	eva = Ban30Eva()
	return eva

# example: ban50
def try_parse_ban50(type):
	from eva.alias.bans_1 import Ban50Eva
	eva = Ban50Eva()
	return eva

# example: ban13
def try_parse_ban13(type):
	from eva.alias.bans_1 import Ban13Eva
	eva = Ban13Eva()
	return eva

# example: ban12
def try_parse_ban12(type):
	from eva.alias.bans_1 import Ban12Eva
	eva = Ban12Eva()
	return eva

# example: ban11
def try_parse_ban11(type):
	from eva.alias.bans_1 import Ban11Eva
	eva = Ban11Eva()
	return eva

# example: ban24
def try_parse_ban24(type):
	from eva.alias.bans_1 import Ban24Eva
	eva = Ban24Eva()
	return eva

# example: ban32
def try_parse_ban32(type):
	from eva.alias.bans_1 import Ban32Eva
	eva = Ban32Eva()
	return eva

# example: ban34
def try_parse_ban34(type):
	from eva.alias.bans_1 import Ban34Eva
	eva = Ban34Eva()
	return eva

# example: ban35
def try_parse_ban35(type):
	from eva.alias.bans_1 import Ban35Eva
	eva = Ban35Eva()
	return eva

# example: newlow5
def try_parse_newlow5_1(type):
	from eva.alias.newlows_1 import Newlow5_1Eva
	eva = Newlow5_1Eva()
	return eva

# example: newlow6
def try_parse_newlow6_1(type):
	from eva.alias.newlows_1 import Newlow6_1Eva
	eva = Newlow6_1Eva()
	return eva

# example: newlow7
def try_parse_newlow7_1(type):
	from eva.alias.newlows_1 import Newlow7_1Eva
	eva = Newlow7_1Eva()
	return eva

# example: newlow8
def try_parse_newlow8_1(type):
	from eva.alias.newlows_1 import Newlow8_1Eva
	eva = Newlow8_1Eva()
	return eva

# example: newlow10
def try_parse_newlow10_1(type):
	from eva.alias.newlows_1 import Newlow10_1Eva
	eva = Newlow10_1Eva()
	return eva

# example: newhigh5
def try_parse_newhigh5_1(type):
	from eva.alias.newhighs_1 import Newhigh5_1Eva
	eva = Newhigh5_1Eva()
	return eva

# example: newhigh6
def try_parse_newhigh6_1(type):
	from eva.alias.newhighs_1 import Newhigh6_1Eva
	eva = Newhigh6_1Eva()
	return eva

# example: newhigh7
def try_parse_newhigh7_1(type):
	from eva.alias.newhighs_1 import Newhigh7_1Eva
	eva = Newhigh7_1Eva()
	return eva

# example: newhigh8
def try_parse_newhigh8_1(type):
	from eva.alias.newhighs_1 import Newhigh8_1Eva
	eva = Newhigh8_1Eva()
	return eva

# example: newhigh10
def try_parse_newhigh10_1(type):
	from eva.alias.newhighs_1 import Newhigh10_1Eva
	eva = Newhigh10_1Eva()
	return eva

# example: newhigh10_2
def try_parse_newhigh10_2(type):
	from eva.alias.newhighs_2 import Newhigh10_2Eva
	eva = Newhigh10_2Eva()
	return eva

# example: newhigh10_3
def try_parse_newhigh10_3(type):
	from eva.alias.newhighs_3 import Newhigh10_3Eva
	eva = Newhigh10_3Eva()
	return eva

# example: up0
def try_parse_up0(type):
	from eva.alias.ups_1 import Up0Eva
	eva = Up0Eva()
	return eva

# example: up1
def try_parse_up1(type):
        from eva.alias.ups_1 import Up1Eva
        eva = Up1Eva()
        return eva

# example: up10
def try_parse_up10(type):
        from eva.alias.ups_1 import Up10Eva
        eva = Up10Eva()
        return eva

# example: upm1
def try_parse_upm1(type):
        from eva.alias.ups_1 import UpM1Eva
        eva = UpM1Eva()
        return eva

# example: up2
def try_parse_up2(type):
	from eva.alias.ups_1 import Up2Eva
	eva = Up2Eva()
	return eva

# example: up2_2
def try_parse_up2_2(type):
	from eva.alias.ups_1 import Up2_2Eva
	eva = Up2_2Eva()
	return eva

# example: up3
def try_parse_up3(type):
        from eva.alias.ups_1 import Up3Eva
        eva = Up3Eva()
        return eva

# example: up4
def try_parse_up4(type):
        from eva.alias.ups_1 import Up4Eva
        eva = Up4Eva()
        return eva

# example: up5
def try_parse_up5(type):
	from eva.alias.ups_1 import Up5Eva
	eva = Up5Eva()
	return eva

# example: up7
def try_parse_up7(type):
	from eva.alias.ups_1 import Up7Eva
	eva = Up7Eva()
	return eva

# example: up8
def try_parse_up8(type):
	from eva.alias.ups_1 import Up8Eva
	eva = Up8Eva()
	return eva

# example: up9
def try_parse_up9(type):
	from eva.alias.ups_1 import Up9Eva
	eva = Up9Eva()
	return eva

# example: risk2
def try_parse_risk2(type):
        from eva.alias.risks_1 import Risk2_1Eva
        eva = Risk2_1Eva()
        return eva

# example: risk3
def try_parse_risk3(type):
        from eva.alias.risks_1 import Risk3_1Eva
        eva = Risk3_1Eva()
        return eva

# example: risk4
def try_parse_risk4(type):
        from eva.alias.risks_1 import Risk4_1Eva
        eva = Risk4_1Eva()
        return eva

# example: risk5
def try_parse_risk5(type):
        from eva.alias.risks_1 import Risk5_1Eva
        eva = Risk5_1Eva()
        return eva

# example: risk7
def try_parse_risk7(type):
        from eva.alias.risks_1 import Risk7_1Eva
        eva = Risk7_1Eva()
        return eva

# example: cl2
def try_parse_cl2(type):
        from eva.alias.cls_1 import Cl2_1Eva
        eva = Cl2_1Eva()
        return eva

# example: cl3
def try_parse_cl3(type):
        from eva.alias.cls_1 import Cl3_1Eva
        eva = Cl3_1Eva()
        return eva

# example: cl4
def try_parse_cl4(type):
        from eva.alias.cls_1 import Cl4_1Eva
        eva = Cl4_1Eva()
        return eva

# example: cl5
def try_parse_cl5(type):
        from eva.alias.cls_1 import Cl5_1Eva
        eva = Cl5_1Eva()
        return eva

# example: cl7
def try_parse_cl7(type):
        from eva.alias.cls_1 import Cl7_1Eva
        eva = Cl7_1Eva()
        return eva

if __name__ == "__main__":
	pass
