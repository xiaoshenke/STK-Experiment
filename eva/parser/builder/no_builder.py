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

	eva = None

	if type == 'no301_newhigh_0':
		eva = try_parse_no301_newhigh_0(type)
	elif type == 'no301_newhigh_1':
                eva = try_parse_no301_newhigh_1(type)

	elif type == 'no304_reach_btw_0':
		eva  = try_parse_no304_reach_btw_0(type)
	elif type == 'no304_reach_btw_1':
                eva  = try_parse_no304_reach_btw_1(type)

	return eva

# example: no301_newhigh_0
def try_parse_no301_newhigh_0(type):
	from eva.no.len3.newhigh.newhighs_1 import No301Newhigh_0Eva
	return No301Newhigh_0Eva()

# example: no301_newhigh_1
def try_parse_no301_newhigh_1(type):
	from eva.no.len3.newhigh.newhighs_1 import No301Newhigh_1Eva
	return No301Newhigh_1Eva()

# example: no304_reach_btw_0
def try_parse_no304_reach_btw_0(type):
	from eva.no.len3.reach_btw.reach_btws_1 import No304ReachBtw_0Eva
	return No304ReachBtw_0Eva()

# example: no304_reach_btw_1
def try_parse_no304_reach_btw_1(type):
	from eva.no.len3.reach_btw.reach_btws_1 import No304ReachBtw_1Eva
	return No304ReachBtw_1Eva()


# 从数据库中读取编号no的数据 找到具体的类型 然后再执行计算
def try_parse_wrap_no(type):
	from eva.wrap.wrap_no_eva import WrapNoEva
	return WrapNoEva(type)

if __name__ == "__main__":
	pass
