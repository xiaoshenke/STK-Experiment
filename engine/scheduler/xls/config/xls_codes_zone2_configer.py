#!/usr/bin/python
# coding=utf-8
# 10:10:00前的配置器实现
# TUNING AND CONFIG, 本框架用于调优和配置的地方

from eva.clever_eva import clever_build_eva
from strategy.sc.clever_source import safe_get_codes
from engine.scheduler.xls.xls_cons import *
from engine.scheduler.xls.config.base_codes_configer import BaseCodesConfiger
from util.df_util import empty

class XlsCodesZone2Configer(BaseCodesConfiger):
    def __init__(self):
        BaseCodesConfiger.__init__(self)

    # core API:
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	xls = cal_xls.xls
	type_map = {}

	# 全level数据 + 7分位数据下跌
        type,alias = '%s*%s'%(xls,'CODES_XLS_LEVEL_ALL'),''
        alias = '%s*%s'%(xls,SHAPE_CODES_XLS_LEVEL_ALL)
        codes = safe_get_codes(type,day)
        if len(codes) > 0:
                type_map[alias] = codes 

	# 前15min到过7个点的数据
        codes = safe_get_codes(xls,day)
        codes = self.drop_from_7pchg_zone1(codes,xls,day,time_str,enable_realtime_df)
        alias = '%s*%s'%(xls,SHAPE_ZONE1_7)
        if len(codes) > 0:
                type_map[alias] = codes

        # 更多zone相关形态?     -> TODO:

        # 低位箱体数据
        codes = self.get_low_xt_codes_data(xls,day,time_str,enable_realtime_df)
        alias = '%s*%s'%(xls,SHAPE_LOW_XT)
        if len(codes) > 0:
                type_map[alias] = codes
        return type_map

    def drop_from_7pchg_zone1(self,codes,type,day,time_str,enable_realtime_df):
	from engine.ecore.realtime_df_manager import g_realtime_df_mgr
	from engine.ecore.df_merger_util import get_fenshi_path_from,parse_dir_and_startswith_from
        if len(codes) == 0:
                return []

	df = empty()
        merged_file = get_fenshi_path_from(day)
	if enable_realtime_df:
		df = g_realtime_df_mgr.get_realtime_df(type,time_str,timeout=20,codes=codes)
	else:
		# 默认使用fenshi数据
		from util.df_util import get_codes_filtered_df
		from eva.eva_util import get_end_nearest_df
		from inn_strategy.icore.inn_util import full_df_to_bounch
		dir,startswith = parse_dir_and_startswith_from(merged_file)
		# 注意:这个数据的时效性当前未校验 	-> FIXME:
		df,_,_ = get_end_nearest_df(dir,startswith,'',time_str)
		if df.empty:
			return []
		df = get_codes_filtered_df(df,codes)
		df = full_df_to_bounch(df,day,[],-1)

	from eva.eva_context2 import EvaContext
        eva_type = 'STG_15_Z1_HPCHG_1'
	context = EvaContext().set_day(day).set_eva_type(eva_type).set_merge_file(merged_file).set_is_fenshi_data(True) 
        eva = clever_build_eva(eva_type).set_day(day).set_df(df)
	eva.set_context(context)
        ret = eva.evaluate()
        codes = [] if ret.empty else ret['code'].tolist()
        return codes

if __name__ == "__main__":
        pass
