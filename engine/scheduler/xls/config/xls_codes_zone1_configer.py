#!/usr/bin/python
# coding=utf-8
# 09:45:00前的配置器实现
# TUNING AND CONFIG, 本框架用于调优和配置的地方

from eva.clever_eva import clever_build_eva
from strategy.sc.clever_source import safe_get_codes
from engine.scheduler.xls.xls_cons import *
from engine.scheduler.xls.config.base_codes_configer import BaseCodesConfiger

class XlsCodesZone1Configer(BaseCodesConfiger):
    def __init__(self):
        BaseCodesConfiger.__init__(self)

    # core API:
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	sort = cal_xls.sort
	xls = cal_xls.xls
	type_map = {}
	if sort <= 1:
		# 全level数据	
		type = '%s*%s'%(xls,'CODES_XLS_LEVEL_ALL')
		alias = '%s*%s'%(xls,SHAPE_CODES_XLS_LEVEL_ALL)
		codes = safe_get_codes(type,day)
                if len(codes) > 0:
                        type_map[alias] = codes

		# 低位箱体数据
		codes = self.get_low_xt_codes_data(xls,day,time_str,enable_realtime_df)
                alias = '%s*%s'%(xls,SHAPE_LOW_XT)
                if len(codes) > 0:
                        type_map[alias] = codes		
	else:
		type,alias = '%s*%s'%(xls,'(CODES_XLS_LEVEL_3|CODES_XLS_LEVEL_2)'),'%s*%s'%(xls,SHAPE_CODES_XLS_LEVEL_23)
                codes = safe_get_codes(type,day)
                if len(codes) > 0:
                        type_map[alias] = codes
	return type_map

if __name__ == "__main__":
        pass
