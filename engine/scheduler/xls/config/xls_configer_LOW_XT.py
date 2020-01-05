#!/usr/bin/python
# coding=utf-8

from engine.scheduler.xls.config.base_eva_configer import BaseEvaConfiger

# TODO:

class XlsConfiger_LOW_XT(BaseEvaConfiger):
    def __init__(self):
        BaseEvaConfiger.__init__(self)

    # core API:
    def get_xls_cal_list(self,cal_xls,type,time_str):
	return []

if __name__ == "__main__":
        pass

