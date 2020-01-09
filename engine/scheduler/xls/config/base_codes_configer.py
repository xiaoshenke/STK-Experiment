#!/usr/bin/python
# coding=utf-8
# code config基类

from eva.clever_eva import clever_build_eva
from strategy.sc.clever_source import safe_get_codes
from engine.ecore.realtime_df_manager import g_realtime_df_mgr

class BaseCodesConfiger:
    def __init__(self,enable_realtime_df=True):
	self.enable_realtime_df = enable_realtime_df

    # core API:
    # return {} key: alias val: [code]
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	return {}

    # return [code]
    # 1,先通过realtime df manager对type,day股票池拿到df, 2,执行eva type计算 3,返回结果
    def get_evaed_codes_data(self,type,day,time_str,eva_type,extra_type=''):
	if not self.enable_realtime_df:
		return []
	codes = safe_get_codes(type,day)
	if len(codes) == 0:
		return []
	df = g_realtime_df_mgr.get_realtime_df(type,time_str,timeout=20)
	eva = clever_build_eva(eva_type).set_day(day).set_df(df)

	# 设置try files类型的context
	# TODO: 设置merge file为xls scheduler对应的merged file
	from eva.eva_context2 import EvaContext
	context = EvaContext().set_day(day).set_eva_type(eva_type).set_end_at(time_str).set_try_files(True)
	eva.set_context(context)

	ret = eva.evaluate()
	codes = [] if ret.empty else ret['code'].tolist()
	if len(codes) > 0 and extra_type:
		codes = safe_get_codes(extra_type,day,codes=codes)
	return codes

    # 低位箱体数据
    def get_low_xt_codes_data(self,xls,day,time_str,enable_realtime_df):
	from eva.clever_eva import clever_build_eva
	from strategy.sc.clever_source import safe_get_codes
	from engine.ecore.realtime_df_manager import g_realtime_df_mgr
        if not enable_realtime_df:
                return []

        df = g_realtime_df_mgr.get_realtime_df(xls,time_str,timeout=20)
        eva_type = 'rup:min_pchg=1.8*upbound:rate=0.5*btw:max_pchg=5.2'
        eva = clever_build_eva(eva_type).set_day(day).set_df(df)
        ret = eva.evaluate()
        codes = [] if ret.empty else ret['code'].tolist()
        if len(codes) > 0:
                codes = safe_get_codes('CODES_LOW_XT',day,codes=codes)
        return codes

    def set_enable_realtime_df(self,enable):
	self.enable_realtime_df = enable
	return self

if __name__ == "__main__":
	pass
