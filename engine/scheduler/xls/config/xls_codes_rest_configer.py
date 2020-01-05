#!/usr/bin/python
# coding=utf-8
# 默认时间段的配置实现

from eva.clever_eva import clever_build_eva
from strategy.sc.clever_source import safe_get_codes
from engine.scheduler.xls.xls_cons import *
from engine.scheduler.xls.config.base_codes_configer import BaseCodesConfiger

# TODO: 添加更多数据

class XlsCodesRestConfiger(BaseCodesConfiger):
    def __init__(self):
        BaseCodesConfiger.__init__(self)

    # core API:
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	xls = cal_xls.xls

	type_map = {}
	# 进板数据
	type = '%s*CODES_BAN'%xls
	alias = '%s*%s'%(xls,SHAPE_CODES_BAN)
	codes = safe_get_codes(type,day)
	if len(codes) > 0:
		type_map[alias] = codes	
	return type_map

if __name__ == "__main__":
        pass
