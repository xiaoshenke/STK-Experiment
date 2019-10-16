#!/usr/bin/python
# coding=utf-8

# 根据版块的stage过滤个股

# 注意:stage在一天的过程中可能是会变化的,因此不同的time str需要进行重新计算

# 注意,以day+timestr作为key进行cache

import time
from util.df_util import empty,read_csv
from engine.hit.base_hit import BaseHit
from functools import partial

# TODO:测试

class HitXlsStage(BaseHit):
    def __init__(self,engine):
        BaseHit.__init__(self,engine)
	self.cur_xls_list = []
	self.stage_type = ''
	self.singleton = True

	# 由于一天的不同时候,版块所处的stage很可能不同,因此需要以time str为key
	# key: day+time_str+xls val:xls_stage
	self.cached_xls_stage = {}

    def on_before_hit_processer(self):
	pass

    def deal_chained_hit(self,time_str,input_df,idx,hits,emotion=None,cal_hit=None):
	return BaseHit.deal_chained_hit(self,time_str,input_df,idx,hits,emotion,cal_hit)

    def deal_hit(self,time_str,from_str,df,emotion,cal_hit=None):
	if df.empty and not self.react_to_fenshi():
		return empty()

	if not self.stage_type:
		return empty()

	xls_list = self.cur_xls_list	
	print 'xls_list:%s'%xls_list
	df = self.get_with_xls_df(df,xls_list)
	if df.empty:
		return df

	# 简单处理掉unkown类型
	df = df[(df['xls_str']!='unknown')&(df['xls_str']!='unkown')]
	
	# hit没有指定xls list参数,直接的场景一般都会指定
	if len(xls_list) == 0:
		for xls_str in df['xls_str'].tolist():
			xlss = xls_str.split(',')
			for xls in xlss:
				if xls in xls_list:
					continue
				xls_list.append(xls)
	valid_xls_list = []
	for xls in xls_list:
		key = self.get_key(self.day,time_str,xls)
		if key in self.cached_xls_stage:
			stage = self.cached_xls_stage[key]
			if stage != self.stage_type:
				continue
			valid_xls_list.append(xls)
			continue
		stage = self.cal_xls_stage(xls,self.day,time_str)
		self.cached_xls_stage[key] = stage
		if stage != self.stage_type:
			continue
		valid_xls_list.append(xls)
	
	df = df[df.apply(partial(self.filter_by_xls_list,xls_list=valid_xls_list),axis=1)]
	if df.empty:
		return df
	return df

    def filter_by_xls_list(self,ser,xls_list):
        xls = ser['xls_str']
        if not xls:
                return False
        xlss = xls.split(',')
        for xls in xlss:
                if xls in xls_list:
                        return True
        return False

    # return df,data_map
    def get_with_xls_df(self,df,xls_list):
	from engine.codes_builder import g_codes_builder
	from util.xls_util import get_code_xls_str
	# 有一种很常见的场景就是以传入的参数df作为数据源进行rank,此时xls_list为['df'],这时候就直接将xls str设为df即可
	# 当xls_list为df的时候,
	if len(xls_list) == 1 and xls_list[0] in ['df','DF','Df']:
		df['xls_str'] = 'df'
		return df

	xls_map = {}
	for xls in xls_list:
		codes = g_codes_builder.safe_get_codes(xls,self.day)
		if len(codes) == 0:
			continue
		xls_map[xls] = codes

	df['xls_str'] = df['code'].map(lambda x: get_code_xls_str(x,xls_map=xls_map))
	df = df[(df['xls_str']!='unkown')&(df['xls_str']!='unknown')]
	df = df.reset_index(drop=True)
	if df.empty:
		return empty()
	return df

    def cal_xls_stage(self,xls,day,time_str):
	from engine.hit.xls_stage.xls_stage import get_stage_from_df
	df = self.get_cached_wfenshi_df(day,time_str)	
	return get_stage_from_df(df,day,xls)

    def get_key(self,day,time_str,xls):
	return "%s,%s,%s"%(day,time_str,xls)

    def set_xls_list(self,xls_list):
	self.cur_xls_list = xls_list
	return self

    def set_stage_type(self,type):
	self.stage_type = type
	return self

    def react_to_fenshi(self):
	return False

    def get_name(self):
	return "HITxls_stage"

g_xls_stage = HitXlsStage(None)

if __name__ == "__main__":
	pass
