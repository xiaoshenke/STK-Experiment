#!/usr/bin/python
# coding=utf-8

# 13:00:00-14:20:00时区配置器

from eva.clever_eva import clever_build_eva
from strategy.sc.clever_source import safe_get_codes
from engine.scheduler.xls.xls_cons import *
from engine.scheduler.xls.config.base_codes_configer import BaseCodesConfiger

class XlsCodesZone5Configer(BaseCodesConfiger):
    def __init__(self,enable_realtime_df=True):
	BaseCodesConfiger.__init__(self,enable_realtime_df)

    # core API:
    # return {} key: alias val: [code]
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	xls = cal_xls.xls
	type_map = {}

	eva_type = 'XLS_UD_DBOUND_1'
	alias = '%s*%s'%(xls,SHAPE_UD_DBOUND_1)
	type = '%s*%s'%(xls,'(CODES_XLS_LEVEL_3|CODES_XLS_LEVEL_2)')
	codes = self.get_evaed_codes_data(type,day,time_str,eva_type)
	if len(codes) > 0:
		type_map[alias] = codes

	type = '%s*CODES_BAN'%xls
        alias = '%s*%s'%(xls,SHAPE_CODES_BAN)
        codes = safe_get_codes(type,day)
        if len(codes) > 0:
                type_map[alias] = codes
	return type_map

if __name__ == "__main__":
        pass
