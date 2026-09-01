#!/usr/bin/python
# coding=utf-8

# 判断是否是@strategy.no 包下的类,语义为: 具备编号的个股图形

from util.df_util import empty

def is_no_type(type,debug=False):
	tmp = type[:3]
	if tmp in [ 'no:','no-','no_' ]:
		return True

	# 如果是 no123456 那么也视作try_parse_wrap_no 
	import re
	pattern = r'^no\d{5,6}$'
	if re.match( pattern,type ):
		return True
	
	node = build_no_one(type)
	if node:
		return True
	return False

def build_no_one(type,debug=False):
	import re
	tmp = type[:3]
	if tmp in [ 'no:','no-','no_' ]:
		last = type[3:]

		pattern = r'^\d{5,6}$'
		if re.match( pattern,last ):
			return try_parse_wrap_no(last)

	# 如果是 no123456 那么也视作try_parse_wrap_no 
	pattern = r'^no\d{5,6}$'
	if re.match( pattern,type ):
		return try_parse_wrap_no(type[2:])

	stra = None

	if type == 'no114_sumbad_1':
		stra = try_parse_no114_sumbad_1(type)
	elif type == 'no38_suo4_1':
		stra = try_parse_no38_suo4_1(type)
	elif type == 'no38_suo4_2':
		stra = try_parse_no38_suo4_2(type)

	elif type == 'no701_dst_1':
		stra = try_parse_no701_dst_1(type)

	elif type == 'no702_liangyang_7':
		stra = try_parse_no702_liangyang_7(type)
	elif type == 'no704_baov_1':
		stra = try_parse_no704_baov_1(type)

	elif type == 'no707_yangs2_1':
		stra = try_parse_no707_yangs2_1(type)
	elif type == 'no707_yangs3_1':
		stra = try_parse_no707_yangs3_1(type)
	elif type == 'no707_yangs1_1':
                stra = try_parse_no707_yangs1_1(type)

	elif type == 'no300_basic_0':
		stra = try_parse_no300_basic_0(type)
	elif type == 'no300_basic_1':
		stra = try_parse_no300_basic_1(type)


	# xt+good-shape: 指图形有一点辨识度 不是路人图形
	elif type == 'no301_goodshape_0':
		stra = try_parse_no301_goodshape_0(type)
	elif type == 'no301_goodshape_1':
                stra = try_parse_no301_goodshape_1(type)
	elif type == 'no301_goodshape_2':
                stra = try_parse_no301_goodshape_2(type)
	# xt+suo-xt
	elif type == 'no303_suoxt_0':
		stra = try_parse_no303_suoxt_0(type)
	elif type == 'no303_suoxt_1':
                stra = try_parse_no303_suoxt_1(type)
	elif type == 'no303_suoxt_2':
                stra = try_parse_no303_suoxt_2(type)

	# xt+long
	elif type == 'no302_long_0':
		stra = try_parse_no302_long_0(type)
	elif type == 'no302_long_1':
                stra = try_parse_no302_long_1(type)

	# redu+mid
	elif type == 'no401_mid_0':
                stra = try_parse_no401_mid_0(type)
	elif type == 'no401_mid_1':
		stra = try_parse_no401_mid_1(type)
	elif type == 'no401_mid_2':
                stra = try_parse_no401_mid_2(type)
	elif type == 'no401_mid_3':
                stra = try_parse_no401_mid_3(type)
	elif type == 'no401_mid_21':
		stra = try_parse_no401_mid_21(type)

	# redu+hot
	elif type == 'no403_hot_0':
                stra = try_parse_no403_hot_0(type)
	elif type == 'no403_hot_1':
		stra = try_parse_no403_hot_1(type)
	elif type == 'no403_hot_2':
                stra = try_parse_no403_hot_2(type)
	elif type == 'no403_hot_3':
                stra = try_parse_no403_hot_3(type)
	
	# redu+pos-high
	elif type == 'no407_pos_1':
		stra = try_parse_no407_pos_1(type)

	return stra

# example: no407_pos_1
def try_parse_no407_pos_1(type):
	from strategy.no.redu.pos_high.pos_highs_1 import No407Pos_1Strategy
	return No407Pos_1Strategy()

# example: no401_mid_0
def try_parse_no401_mid_0(type):
	from strategy.no.redu.mid.mids_1 import No401Mid_0Strategy
	return No401Mid_0Strategy()

# example: no401_mid_1
def try_parse_no401_mid_1(type):
	from strategy.no.redu.mid.mids_1 import No401Mid_1Strategy
	return No401Mid_1Strategy()

# example: no401_mid_2
def try_parse_no401_mid_2(type):
	from strategy.no.redu.mid.mids_1 import No401Mid_2Strategy
	return No401Mid_2Strategy()

# example: no401_mid_3
def try_parse_no401_mid_3(type):
	from strategy.no.redu.mid.mids_1 import No401Mid_3Strategy
	return No401Mid_3Strategy()

# example: no401_mid_21
def try_parse_no401_mid_21(type):
	from strategy.no.redu.mid.mids_2 import No401Mid_21Strategy
	return No401Mid_21Strategy()

# example: no403_hot_0
def try_parse_no403_hot_0(type):
	from strategy.no.redu.hot.hots_1 import No403Hot_0Strategy
	return No403Hot_0Strategy()

# example: no403_hot_1
def try_parse_no403_hot_1(type):
	from strategy.no.redu.hot.hots_1 import No403Hot_1Strategy
	return No403Hot_1Strategy()

# example: no403_hot_2
def try_parse_no403_hot_2(type):
	from strategy.no.redu.hot.hots_1 import No403Hot_2Strategy
	return No403Hot_2Strategy()

# example: no403_hot_3
def try_parse_no403_hot_3(type):
	from strategy.no.redu.hot.hots_1 import No403Hot_3Strategy
	return No403Hot_3Strategy()

# example: no300_basic_0
def try_parse_no300_basic_0(type):
	from strategy.no.xt.basic.basics_1 import No300Basic_0Strategy
	return No300Basic_0Strategy()

# example: no300_basic_1
def try_parse_no300_basic_1(type):
	from strategy.no.xt.basic.basics_1 import No300Basic_1Strategy
	return No300Basic_1Strategy()


# example: no302_long_0
def try_parse_no302_long_0(type):
	from strategy.no.xt.long.longs_1 import No302Long_0Strategy
	return No302Long_0Strategy()

# example: no302_long_1
def try_parse_no302_long_1(type):
	from strategy.no.xt.long.longs_1 import No302Long_1Strategy
	return No302Long_1Strategy()

# example: no303_suoxt_0
def try_parse_no303_suoxt_0(type):
	from strategy.no.xt.suo.suo_xts_1 import No303Suo_0Strategy
	return No303Suo_0Strategy()

# example: no303_suoxt_1
def try_parse_no303_suoxt_1(type):
	from strategy.no.xt.suo.suo_xts_1 import No303Suo_1Strategy
	return No303Suo_1Strategy()

# example: no303_suoxt_2
def try_parse_no303_suoxt_2(type):
	from strategy.no.xt.suo.suo_xts_1 import No303Suo_2Strategy
	return No303Suo_2Strategy()


# example: no301_goodshape_0
def try_parse_no301_goodshape_0(type):
	from strategy.no.xt.basic.good_shapes_1 import No301GoodShapes_0Strategy
	return No301GoodShapes_0Strategy()

# example: no301_goodshape_1
def try_parse_no301_goodshape_1(type):
	from strategy.no.xt.basic.good_shapes_1 import No301GoodShapes_1Strategy
	return No301GoodShapes_1Strategy()

# example: no301_goodshape_2
def try_parse_no301_goodshape_2(type):
	from strategy.no.xt.basic.good_shapes_1 import No301GoodShapes_2Strategy
	return No301GoodShapes_2Strategy()


# example: no707_yangs1_1
def try_parse_no707_yangs1_1(type):
	from strategy.no.small.yangxians.yangxians_1 import No707Yangs1_1Strategy
	return No707Yangs1_1Strategy()

# example: no707_yangs2_1
def try_parse_no707_yangs2_1(type):
	from strategy.no.small.yangxians.yangxians_1 import No707Yangs2_1Strategy
	return No707Yangs2_1Strategy()

# example: no707_yangs3_1
def try_parse_no707_yangs3_1(type):
	from strategy.no.small.yangxians.yangxians_1 import No707Yangs3_1Strategy
	return No707Yangs3_1Strategy()

# example: no704_baov_1
def try_parse_no704_baov_1(type):
	from strategy.no.small.baov.baovs_1 import No704Baov_1Strategy
	return No704Baov_1Strategy()

# example: no702_liangyang_7
def try_parse_no702_liangyang_7(type):
	from strategy.no.small.lianyang.lianyangs_1 import No702Lianyang_1Strategy
	return No702Lianyang_1Strategy()

# example: no701_dst_1
def try_parse_no701_dst_1(type):
	from strategy.no.small.dst.dsts_1 import No701Dst_1Strategy
	return No701Dst_1Strategy()

# example: no38_suo4_1
def try_parse_no38_suo4_1(type):
	from strategy.no.duanxt.suo.suo_xts_1 import No38Suo_1Strategy
	return No38Suo_1Strategy()

# example: no38_suo4_2
def try_parse_no38_suo4_2(type):
	from strategy.no.duanxt.suo.suo_xts_1 import No38Suo_2Strategy
	return No38Suo_2Strategy()

# example: no114_sumbad_1
def try_parse_no114_sumbad_1(type):
	from strategy.no.sure.bad.lowers_1 import No114SumBad_1Strategy
	return No114SumBad_1Strategy()

# 从数据库中读取编号no的数据 找到具体的类型 然后再执行计算
def try_parse_wrap_no(type):
	from strategy.wrap.wrap_no_strategy import WrapNoStrategy
	return WrapNoStrategy(type)


if __name__ == "__main__":
	pass
