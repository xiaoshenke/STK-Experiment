#!/usr/bin/python
# coding=utf-8
# 实际是一个wrap类,实现会根据time str调用其他类实现

from engine.scheduler.xls.config.base_codes_configer import BaseCodesConfiger

class XlsDerivedCodesConfiger(BaseCodesConfiger):
    def __init__(self,enable_realtime_df=True):
	BaseCodesConfiger.__init__(self,enable_realtime_df)

    # core API:
    # return {} key: alias val: [code]
    def get_xls_derived_codes_map(self,cal_xls,day,time_str,enable_realtime_df):
	if time_str <= '09:45:00':
		from engine.scheduler.xls.config.xls_codes_zone1_configer import XlsCodesZone1Configer
		return XlsCodesZone1Configer(self.enable_realtime_df).get_xls_derived_codes_map(cal_xls,day,time_str,enable_realtime_df)

	if time_str <= '10:10:00':
		from engine.scheduler.xls.config.xls_codes_zone2_configer import XlsCodesZone2Configer
		return XlsCodesZone2Configer(self.enable_realtime_df).get_xls_derived_codes_map(cal_xls,day,time_str,enable_realtime_df)

	if time_str >= '14:20:00':
		from engine.scheduler.xls.config.xls_codes_zone8_configer import XlsCodesZone8Configer
		return XlsCodesZone8Configer(self.enable_realtime_df).get_xls_derived_codes_map(cal_xls,day,time_str,enable_realtime_df)
	
	if time_str >= '13:00:00':
		from engine.scheduler.xls.config.xls_codes_zone5_configer import XlsCodesZone5Configer
		return XlsCodesZone5Configer(self.enable_realtime_df).get_xls_derived_codes_map(cal_xls,day,time_str,enable_realtime_df)

	from engine.scheduler.xls.config.xls_codes_rest_configer import XlsCodesRestConfiger
	return XlsCodesRestConfiger(self.enable_realtime_df).get_xls_derived_codes_map(cal_xls,day,time_str,enable_realtime_df)

if __name__ == "__main__":
        pass
