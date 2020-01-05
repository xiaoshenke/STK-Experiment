#!/usr/bin/python
# coding=utf-8

# 实际是一个wrap类,实现会根据tag调用其他类实现

from engine.scheduler.xls.xls_cons import *
from engine.scheduler.xls.config.base_eva_configer import BaseEvaConfiger

# TODO:

class XlsCalEvaConfiger(BaseEvaConfiger):
    def __init__(self):
	BaseEvaConfiger.__init__(self)

    # core API: 根据type的tag给出对应的列表
    def get_xls_cal_list(self,cal_xls,type,time_str):
	xls = cal_xls.xls
	level = cal_xls.level
	tag = self.get_tag_from(type)

	if tag == SHAPE_CODES_XLS_LEVEL_ALL:
		pass
	elif tag == SHAPE_LOW_XT:
		from engine.scheduler.xls.config.xls_configer_LOW_XT import XlsConfiger_LOW_XT
		return XlsConfiger_LOW_XT().get_xls_cal_list(cal_xls,type,time_str)
	elif tag == SHAPE_CODES_XLS_LEVEL_23:
		pass
	elif tag == SHAPE_ZONE1_7:
		pass
	elif tag == SHAPE_CODES_BAN:
		pass
        return []

    def get_tag_from(self,type):
	if not type:
		return ''
	return type.split('*')[-1]


if __name__ == "__main__":
        pass
