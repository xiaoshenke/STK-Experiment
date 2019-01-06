#!/usr/bin/python
# coding=utf-8

import os
from pandas import DataFrame
from util.df_util import read_csv,to_csv

def updater(file_name,keys=[],key='',dtype={'code':object},encoding='utf-8',sort_key=None,ascending=False):
	def _updater(func):
                def _real(*args,**kwargs):
			if len(keys) >= 1:
				key = keys[0]

			# 计算结果
			ret = func(*args,**kwargs)
			hist = read_csv(file_name) if os.path.exists(file_name) else DataFrame()

			# 使用hist文件来过滤ret
			if not ret.empty and not hist.empty and key:
				filters = hist[key].tolist()
				ret = ret[ret[key].apply(lambda x: x not in filters )]

			# 若ret不为空,那么进行写文件
			if not ret.empty:
				import pandas
				hist = pandas.concat([hist,ret],axis=0) if not hist.empty else ret
				if sort_key:
					hist = hist.sort_values(sort_key,ascending=ascending)
					hist = hist.reset_index(drop=True)
				to_csv(hist,file_name)
			return ret
		return _real
        return _updater

def demo():
	from pandas import DataFrame
        codes = ['000001','000002','000003','000004','000001']
        dates = ['2018-01-01','2018-01-02','2018-01-03','2018-01-04','2018-01-02']
        close = [1.1,1.2,1.3,1.4,1.5]
        df = DataFrame({'code':codes,'date':dates,'close':close})
        df.code = df.code.astype(str)
	to_csv(df,'test_code.csv')

        @updater('test_code.csv',keys=['code'],dtype={'code':object})
        def update_func():
                codes = ['000005','000004','000001','000001']
                dates = ['2018-01-01','2018-01-04','2018-01-01','2018-01-03']
                close = [2.1,2.2,2.3,2.4]
                return DataFrame({'code':codes,'date':dates,'close':close})
        update_func()

if __name__ == "__main__":
        demo()
