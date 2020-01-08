#!/usr/bin/python
# coding=utf-8
# code config基类

class BaseCodesConfiger:
    def __init__(self):
	self.enable_realtime_df = True

    # core API:
    # return {} key: alias val: [code]
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	return {}

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
