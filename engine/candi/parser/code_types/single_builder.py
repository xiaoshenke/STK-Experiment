#!/usr/bin/python
# coding=utf-8

from util.param_util import fix_time_str

def is_single_type(type):
	node = build_single_one(type)
	if node:
		return True
	return False

# 尝试一下export类型
# return bool,node
def try_builded_exported_node(type,debug=False):
	# 3步走
	# 1, 判断整个字符串是否符合
	# 2, XXX:aa*bb 这种头部格式
	# 3, aa*bb*XXX 这种尾部格式

	from engine.candi.node.code_types.export.codetypes_loader import is_valid_reported_type
	from engine.candi.node.code_types.wrap_exported_candi import WrapExportedCandi
	if is_valid_reported_type(type):
		return True,WrapExportedCandi(type)

	# XXX:
	first = '' if not ':' in type else type.split(':')[0]
	if is_valid_reported_type(first) and len(type) > len(first)+1:
		xls = type[len(first)+1:]

		return True,WrapExportedCandi(first).set_xls(xls)

	# aaa*bbb*XXX
	last = '' if not '*' in type else type.split('*')[-1]
	if is_valid_reported_type(last):
		geshi = '*%s'%(last)
		xls = find_xls_param_template(type,geshi)

		return True,WrapExportedCandi(last).set_xls(xls)

	return False,None

def build_single_one(type,debug=False):
	if debug:
		print 'code_types_builder.build_single_one,type: %s'%(type)
		print u'debug: %s'%(debug)

	b,node = try_builded_exported_node(type,debug)
	if b:
		return node
	
	name = type.split(':')[0]
	last = '' if not '*' in type else type.split('*')[-1]

	if type.startswith('observes'):
		return try_parse_observes(type)
	if type == 'rec_all' or type == 'recall':
		return try_parse_rec_all(type)

	last = type if not '*' in type else type.split('*')[-1]
	if last == 'rec' or last.startswith('rec:'):
		return try_parse_rec_by_xls(type)

	if type.startswith('manuals'):
		return try_parse_manuals(type)

	if type.startswith('rela:'):
		return try_parse_xls_relative(type)

	if type.startswith( 'branches' ) or type.startswith( 'branchs' ) or type.startswith( 'branched' ):
		return try_parse_branches(type)

	if type.startswith( 'buyers2' ):
		return try_parse_buyers2(type)
	elif type.startswith( 'buyer' ):
# or type.startswith( 'rela:' ):
		return try_parse_buyers(type)

	if type == 'tracings':
		return try_parse_tracings(type)

	if type.startswith( 'tmps' ):
		return try_parse_tmps(type)

	if type.startswith( 'pan_codes' ):
		return try_parse_pan_codes(type)

	if type in [ 'schedules','schedulers' ]:
		return try_parse_schedules(type)

	if type.startswith( 'dyna_maoding' ) or type.startswith( 'maodings' ):
		return try_parse_dyna_maodings(type)

	qpc_by_name = type.startswith('qpc:') or type.startswith('qpc_')
	if not qpc_by_name and type.startswith('qpc') and len(type) > len('qpc'):
		return try_parse_qpc_by_id(type)

	if qpc_by_name or type.startswith('qq:') or type.startswith('pp:'):
		return try_parse_qpc_by_name(type)

	last = type if not '*' in type else type.split('*')[-1]
	if last == 'youzi2':
		return try_parse_youzi2(type)
	if last == 'youzi' or name == 'youzi' or name.startswith( 'chaoduan' ):
		return try_parse_youzi(type)

	#if last == 'hexin':
	#	return try_parse_hexin(type)

	# spec name支持两种格式
	# 格式1: 以spec name开头
	name1 = name == 'specnames' or name.startswith( 'specname' ) or name.startswith( 'spec_n' )
	# 格式2: 以spec name结尾
	name2 = last == 'specnames' or last.startswith( 'specname' ) or last.startswith( 'spec_n' )
	if name1 or name2:
		return try_parse_specnames(type)

	last = type if not '*' in type else type.split('*')[-1]
	if last in [ 'random_xls','randomxls' ]:
		return try_parse_random_xls(type)

	if last.startswith('rand') or last.startswith('rank'):
		return try_parse_random(type)

	#if last == 'dapiao2':
	#	return try_parse_dapiao2(type)
	#if last in [ 'dapiao','jigou' ]:
	#	return try_parse_dapiao(type)

	if last in [ 'maichong' ]:
		return try_parse_maichong(type)
	elif last == 'maichong2':
		return try_parse_maichong2(type)

	if last in [ 'hq:zhendang','hq:zhendang1' ]:
		return try_parse_hq_zhendang1(type)

	if name == 'pan' or last == 'pan':
		return try_parse_pan(type)

	if name == 'zao' or last == 'zao':
		return try_parse_zao(type)

	last = last.split(':')[0]
	if type in [ 'all_ydys','yyys','yyds','ydys','allydys' ]:
		return try_parse_all_yudingyis(type)
	elif last == 'yudingyi' or last in [ 'ydy','yyy' ]:
		return try_parse_yudingyi(type)

	last = '' if not '*' in type else type.split('*')[-1]
	if last.startswith('pool:'):
		return try_parse_wrap_pool(type)

	# 将candi.node.subs包下的node转换成WrapSubsCandi
	support_subs = [ 'shizhi','name','amount','qushi','hexin','basic','base_shape','baseshape','dis','dapiao' ]

	last = '' if not '*' in type else type.split('*')[-1]
	if last.startswith('subs:') or last.startswith('subs_'):
		return try_parse_wrap_subs(type)

	elif last in support_subs:
		from helper import to_str
		types = type.split('*')
		xls = to_str(types[:-1],sep='*')

		from engine.candi.node.code_types.wrap_subs_candi import WrapSubsCandi
		candi = WrapSubsCandi()
		candi.set_type(last)
		candi.set_xls(xls)
		return candi

	return None

# example: manuals:rec=:asc
def try_parse_manuals(type):
	from engine.candi.node.code_types.manuals_candi import ManualsCandi
	candi = ManualsCandi()
	
	from util.param_util import get_param_from
	rec = get_param_from(type.split(':'),'rec','')
	if rec:
		candi.set_rec(rec)

	if 'asc' in type:
		asc = get_param_from(type.split(':'),'asc','')
		if asc in [ 'true','True','TRUE','1' ]:
			asc = True
		else:
			asc = False
		candi.set_asc(asc)
	return candi

# example: qpcXYZ
def try_parse_qpc_by_id(type):
	name = type.split(':')[0]

	id = int(type[len('qpc'):])
	
	from engine.candi.node.code_types.qpc_by_id_candi import QpcByIdCandi
	return QpcByIdCandi().set_id(id)

# example: qpc:XYZ
def try_parse_qpc_by_name(type):
	type = type.replace('qpc_','qpc:')

	idx = type.index(':')
	name = type[idx+1:]
	
	from engine.candi.node.code_types.qpc_by_name_candi import QpcByNameCandi
	return QpcByNameCandi().set_name(name)

# example: xxx*yy*hexin
def try_parse_hexin(type):
	from engine.candi.node.code_types.hexin_candi import HexinCandi
	candi = HexinCandi()

	geshi = '*hexin'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	return candi

# example: youzi:ABC
def try_parse_youzi(type):
	# 注意: 如果仅为'youzi',那么应该走@engine/candi//node/youzi_candi.py,因此这里返回空
	if type == 'youzi':
		return None

	from engine.candi.node.code_types.youzi_candi import YouziCandi
	candi = YouziCandi()

	geshi = '*youzi'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	
	return candi

# example: youzi2:ABC
def try_parse_youzi2(type):
	from engine.candi.node.code_types.youzi_candi import Youzi2Candi
	candi = Youzi2Candi()

	geshi = '*youzi2'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	
	return candi

# example: specname:ABC
def try_parse_specnames(type):
	from engine.candi.node.code_types.spec_names_candi import SpecNamesCandi
	candi = SpecNamesCandi()

	geshi = '*spec'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	return candi

# example: random:ABC
def try_parse_random(type):
	origin = type
	last = type if not '*' in type else type.split('*')[-1]
        
	name = last.split(':')[0]
	
	from engine.candi.node.code_types.random_candi import RandomCandi
	candi = RandomCandi()

	if len(last) > len(name)+1:
		type = last[len(name)+1:]
		candi.set_type(type)
	
	type = origin
	tmp = '*rank' if 'rank' in name else '*rand' 
	idx = type.rfind(tmp)
	if idx > 0:
		xls = type[:idx]
		candi.set_xls(xls)
	return candi

# example: aa*bb*random_xls
def try_parse_random_xls(type):
	last = type if not '*' in type else type.split('*')[-1]
        
	from engine.candi.node.code_types.random_xls_candi import RandomXlsCandi
	candi = RandomXlsCandi()

	tmp = '*random'
	idx = type.rfind(tmp)
	if idx > 0:
		xls = type[:idx]
		candi.set_xls(xls)
	return candi

# example: dapiao2
def try_parse_dapiao2(type):
	from engine.candi.node.code_types.dapiao_candi import Dapiao2Candi
	candi = Dapiao2Candi()

	geshi = '*dapiao'
	xls = find_xls_param_template(type,geshi)
	candi.set_xls(xls)
	
	return candi

# example: dapiao|jigou
def try_parse_dapiao(type):
	from engine.candi.node.code_types.dapiao_candi import DapiaoCandi
	candi = DapiaoCandi()

	geshi = '*dapiao' if 'dapiao' in type else '*jigou' 
	xls = find_xls_param_template(type,geshi)
	candi.set_xls(xls)
	
	return candi

# example: yyds
def try_parse_all_yudingyis(type):
	from engine.candi.node.code_types.all_ydys_candi import AllYudingyisCandi
        candi = AllYudingyisCandi()
	return candi

# example: ydy|yyy
def try_parse_yudingyi(type):
	from util.param_util import get_param_from,get_param_removed_type_by
	limit = int(get_param_from( type.split(':'),'limit',-1 ))
	type = get_param_removed_type_by( type,['limit'] )

	from engine.candi.node.code_types.yudingyi_candi import YudingyiCandi
        candi = YudingyiCandi()
	geshi = '*ydy'
	if 'yudingyi' in type:
		geshi = '*yudin'	
	elif 'yyy' in type:
		geshi = '*yyy'

	xls = find_xls_param_template(type,geshi)
	candi.set_xls(xls)
	if limit > 0:
		candi.set_limit(limit)

        return candi

# example: maichong
def try_parse_maichong(type):
	from engine.candi.node.code_types.maichong_candi import MaichongCandi
	candi = MaichongCandi()

	geshi = '*maic'
	xls = find_xls_param_template(type,geshi)
	candi.set_xls(xls)
	return candi

# example: maichong2
def try_parse_maichong2(type):

	from engine.candi.node.code_types.maichong_candi import Maichong2Candi
	candi = Maichong2Candi()

	geshi = '*maichong2'
	xls = find_xls_param_template(type,geshi)

	candi.set_xls(xls)
	return candi

# example: pool:ABC
def try_parse_wrap_pool(type):
	origin = type
	last = '' if not '*' in type else type.split('*')[-1]
        
	name = last.split(':')[0]
	
	from engine.candi.node.code_types.wrap_pool_candi import WrapPoolCandi
	candi = WrapPoolCandi()

	if len(last) > len(name)+1:
		type = last[len(name)+1:]
		candi.set_type(type)

	type = origin	
	tmp = '*pool'
	idx = type.rfind(tmp)
	if idx > 0:
		xls = type[:idx]
		candi.set_xls(xls)
	return candi

# example: subs:ABC
def try_parse_wrap_subs(type):
	origin = type
	last = type if not '*' in type else type.split('*')[-1]
        
	name = last.split(':')[0]
	
	from engine.candi.node.code_types.wrap_subs_candi import WrapSubsCandi
	candi = WrapSubsCandi()

	if len(last) > len(name)+1:
		type = last[len(name)+1:]
		candi.set_type(type)

	type = origin	
	tmp = '*subs'
	idx = type.rfind(tmp)
	if idx > 0:
		xls = type[:idx]
		candi.set_xls(xls)
	return candi

# example: hq:zhendang
def try_parse_hq_zhendang1(type):
	from engine.candi.node.code_types.hq.zhendang1_candi import Zhendang1Candi
	candi = Zhendang1Candi()

	geshi = '*hq:zhend'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	return candi

# example: pan:ABC
def try_parse_pan(type):
	from engine.candi.node.code_types.pan_candi import PanCandi
	candi = PanCandi()

	geshi = '*pan'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	return candi

# example: zao:ABC
def try_parse_zao(type):
	from engine.candi.node.code_types.zao_candi import ZaoCandi
	candi = ZaoCandi()

	geshi = '*zao'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	
	return candi

# example: rec:XXX or aa*rec
def try_parse_rec_by_xls(type):
	from engine.candi.node.code_types.rec_by_xls_candi import RecByXlsCandi
	candi = RecByXlsCandi()

	geshi = '*rec'
	xls = find_xls_param_template(type,geshi)
	if xls:
		candi.set_xls(xls)
	return candi

# example: rec_all
def try_parse_rec_all(type):
	from engine.candi.node.code_types.rec_all_candi import RecAllCandi
	candi = RecAllCandi()

	return candi

# example: observes
def try_parse_observes(type):
	from engine.candi.node.code_types.observes_candi import ObservesCandi
	candi = ObservesCandi()
	
	from util.param_util import get_param_from
	evaed = int(get_param_from(type.split(':'),'evaed',-1))

	return candi.set_evaed(evaed)

# example: branches
def try_parse_branches(type):
	from engine.candi.node.code_types.branches_candi import BranchesCandi
	candi = BranchesCandi()
	return candi

# example: schedules
def try_parse_schedules(type):
	from engine.candi.node.code_types.schedules_candi import SchedulesCandi
	candi = SchedulesCandi()
	return candi

# example: buyers2
def try_parse_buyers2(type):
	from engine.candi.node.code_types.buyers2_candi import Buyers2Candi
	candi = Buyers2Candi()
	return candi

# example: buyers|buyers:abc
def try_parse_buyers(type):
	from engine.candi.node.code_types.buyers_candi import BuyersCandi
	candi = BuyersCandi()

	name = type.split(':')[0]
	if len(type) > len(name)+1:
		xls = type[len(name)+1:]
		candi.set_xls(xls)
	return candi

# example: tracings
def try_parse_tracings(type):
	from engine.candi.node.code_types.tracings_candi import TracingsCandi
	candi = TracingsCandi()
	return candi

# example: tmps:ABC
def try_parse_tmps(type):
	from engine.candi.node.code_types.tmps_candi import TmpsCandi
	candi = TmpsCandi()

	name = type.split(':')[0]
	if len(type) > len(name)+1:
		xls = type[len(name)+1:]
		candi.set_xls(xls)
	return candi

# example: pan_codes:ABC
def try_parse_pan_codes(type):
	from engine.candi.node.code_types.pan_codes_candi import PanCodesCandi
	candi = PanCodesCandi()

	name = type.split(':')[0]
	if len(type) > len(name)+1:
		xls = type[len(name)+1:]
		candi.set_xls(xls)
	return candi

# example: dyna_maodings
def try_parse_dyna_maodings(type):
	from engine.candi.node.code_types.dyna_maodings_candi import DynaMaodingsCandi
	candi = DynaMaodingsCandi()
	return candi

# example: rela:ABC
def try_parse_xls_relative(type):
	from engine.candi.node.code_types.xls_relative_candi import XlsRelativeCandi
	candi = XlsRelativeCandi()

	if type.startswith('rela:') and len(type) > len('rela:'):
		xls = type[len('rela:'):]
		candi.set_xls(xls)

	return candi

# 封装了一般的寻找xls的逻辑
# 格式 *XYZ
def find_xls_param_template(type,geshi):
	#print u'code_types.single_builder.find_xls_param_template,type:%s geshi:%s'%(type,geshi)

	# 假设type的类型为 aa*bc*XYZ:xxxx, 此时认为aa*bc,xxxx是两类xls的指定方式,若两者同时被指定,返回xxxx

	# 1, 寻找xxxx
	last = type if not '*' in type else type.split('*')[-1]

	# update 2025-04-27: 注意这里的replace是为了做代码兼容
	name = last.replace('hq:','hq_').split(':')[0]

	if len(last) > len(name)+1:
		xls = type[len(name)+1:]
		return xls

	if not geshi or not geshi[0] == '*':
		return ''
	
	idx = type.rfind(geshi)
	if idx > 0:
		xls = type[:idx]
		return xls
	return ''


if __name__ == "__main__":
	pass
