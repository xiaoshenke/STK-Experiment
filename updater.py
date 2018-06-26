#!/usr/bin/python
# coding=utf-8
import pandas
import os
from pandas import DataFrame,Series
from log import logger

def is_series_type(o):
	return type(o) == type(Series())

# df.ix[idx] 这个值可能是一个series也可能是一个dataframe,本函数统一返回一个dataframe
def get_df_by_idx(df,idx,key1):
	df_tmp = None
	if is_series_type(df.ix[idx]):
		df_tmp = DataFrame([df.ix[idx]])
		df_tmp.index.name = key1
		df_tmp = df_tmp.reset_index(drop=False)
	else:
		df_tmp = df.ix[idx].reset_index(drop=False)
	return df_tmp

# 被updater注解的函数返回一个无效index的DataFrame 
def updater(file_name,keys=[],dtype=None,encoding='utf-8',sort_key=None,ascending=False):
	def _updater(func):
		def _real(*args,**kwargs):
			ret = func(*args,**kwargs)
			final_write = ret
			do_write = False
			df_backup = DataFrame()
			while True:
				try:
					# DataFrame为空 直接跳过
					if ret.empty:
						logger.warn("@updater.func return empty")
						break
					if not file_name or len(file_name) == 0:
						do_write = False
						break
					# 文件不存在时,直接写结果 -> 说明是第一次写
					if not os.path.exists(file_name):
						do_write = True
						break
	
					do_write = True
					df = pandas.read_csv(file_name,date_parser=pandas.to_datetime,encoding=encoding)
					df_backup = df
					# 1 校验一下columns和indexs,这里假设从file中读取的index是无用的,因为在存入file的时候已经处理过了,但是ret不一定
					df_names = df.columns.values
					for n in df_names:
						if n not in ret.columns.values:
							do_write = False
							break
					if not do_write:
						do_write = True
						ret2 = ret.reset_index(drop=False)
						for n  in df_names:
							if n not in ret2.columns.values:
								do_write = False
								break
						if do_write:
						 	ret = ret2

					# column不是完全匹配,那么不进行写文件,或者keys长度超过3了,那么认为这个keys是不合理的,进行忽略,跳出循环
					if not do_write:
						logger.debug("columns not all fit,simply ignore")
						break

					# column能够对上,进行过滤 校验keys数组长度,目前只支持0,1,2
					if not keys or len(keys) >= 3:
						logger.debug("keys is none,or length of keys is not supported!")
						do_write = False
						break

					# keys为[]时,直接concat			
					if len(keys) == 0:
						final_write = pandas.concat([df,ret],axis=0)
						break

					if len(keys) == 1:
						# 在一个键的情况下,只要这个键的值不在history列表,即认为应该插入
						key = keys[0]
						cb_list = []
						for idx in ret.index.tolist():
							if ret.ix[idx][key] not in df[key].tolist():
								cb_list.append(idx)
						if len(cb_list) == 0:
							do_write = False
							break
						cb_df = ret.ix[cb_list]
						final_write = pandas.concat([df,cb_df],axis=0)	
						break

					# 处理复杂的两个键的情况
					# combine_dataframe:这个dataframe是已经reindex过的,不用调用set_index
					filter_df = DataFrame()

					(key1,key2) = (keys[0],keys[1])
					# 重置一下index 便于计算
					reindex_df = df.set_index(key1,drop=True)
					reindex_ret = ret.set_index(key1,drop=True)
					caled_list = []
					
					# 由于dataframe的index相同的时候,会对同一个key多次调用,这里使用caled_list过滤掉
					for idx in reindex_ret.index.tolist():
						if idx not in caled_list:
							caled_list.append(idx)
						else:
							continue
						# 处理idx不在history中的情况,这种情况可以直接append
						if idx not in reindex_df.index.tolist():
							df_tmp = get_df_by_idx(reindex_ret,idx,key1)
							filter_df = pandas.concat([filter_df,df_tmp],axis=0)
							continue

						#开始合并,需要考虑history对应的key和ret对应的key存在多值的情况
						# 先处理history是多值的情况
						if is_series_type(reindex_df.ix[idx][key2]):
							if is_series_type(reindex_ret.ix[idx][key2]):
								# history和return同时是多值的情况
								df_tmp = get_df_by_idx(reindex_ret,idx,key1) 
								cb_list = []
										
								for iidx in df_tmp.index:
									if df_tmp.ix[iidx][key2] not in reindex_df.ix[idx][key2].values:
										cb_list.append(iidx)
								df_tmp = df_tmp.ix[cb_list]
								filter_df = pandas.concat([filter_df,df_tmp],axis=0)
							else:
								# history是多个值,return是单个值
								if reindex_ret.ix[idx][key2] not in reindex_df.ix[idx][key2].values:
									df_tmp = get_df_by_idx(reindex_ret,idx,key1) 
									filter_df = pandas.concat([filter_df,df_tmp],axis=0)
						else:
							# history为单个值
							if is_series_type(reindex_ret.ix[idx][key2]):
								df_tmp = get_df_by_idx(reindex_ret,idx,key1)
								cb_list = []

								for iidx in df_tmp.index:
									if df_tmp.ix[iidx][key2] != reindex_df.ix[idx][key2]:
										cb_list.append(iidx)
								df_tmp = df_tmp.ix[cb_list]
								filter_df = pandas.concat([filter_df,df_tmp],axis=0)	
							else:
								if reindex_ret.ix[idx][key2] != reindex_df.ix[idx][key2]:
									df_tmp = get_df_by_idx(reindex_ret,idx,key1) 
									filter_df = pandas.concat([filter_df,df_tmp],axis=0)
					if filter_df.index.size == 0:
						do_write = False
						break
					final_write = pandas.concat([df,filter_df],axis=0)
					break
				except Exception,e:
					# 出现异常 不写文件
					do_write = False
					logger.warn("updater decorator exception:%s"%e)
					break
				finally:
					if do_write:
						try:
							if sort_key != None:
								final_write = final_write.sort_values(sort_key, ascending=ascending)
							final_write.to_csv(file_name,index=False,date_format="%Y-%m-%d",encoding=encoding)
							logger.info("@updater,file:%s updated!"%file_name)
						except Exception,e:
							logger.warn("updater decorator,exception:%s"%e)
							if not df_backup.empty:
								df_backup.to_csv(file_name,index=False,date_format="%Y-%m-%d",encoding=encoding)
			return ret
		return _real
	return _updater

@updater('updater.csv')
def test_column_not_fit():
	from pandas import DataFrame
	return DataFrame({'column1':['m'],'column3':[1]}) 

@updater('updater.csv',keys=[])
def test_no_keys():
	from pandas import DataFrame
	return DataFrame({'column1':['m'],'column2':[11]})

@updater('updater.csv',keys=['column1'])
def test_1_right_key():
	from pandas import DataFrame
	return DataFrame({'column1':['n'],'column2':[11]})

@updater('updater.csv',keys=['column1'])
def test_1_wrong_key():
	from pandas import DataFrame
	return DataFrame({'column1':['a'],'column2':[11]})

@updater('updater.csv',keys=['column1','column2'])
def test_2_right_key_1():
	from pandas import DataFrame
	return DataFrame({'column1':['a'],'column2':[11]})

@updater('updater.csv',keys=['column1','column2'])
def test_2_right_key_2():
	from pandas import DataFrame
	return DataFrame({'column1':['a','a'],'column2':[11,1]})

def test1():
	from pandas import DataFrame,Series
	codes = ['000001','000002','000003','000004','000001','a']
	dates = ['2018-01-01','2018-01-02','2018-01-03','2018-01-04','2018-01-02','2018-01-01']
	close = [1.1,1.2,1.3,1.4,1.5,0.0]
	df = DataFrame({'code':codes,'date':dates,'close':close})
	df.code = df.code.astype(str)
	df.to_csv('test_code.csv',date_format="%Y-%m-%d",index=False)
	
	@updater('test_code.csv',keys=['code','date'],dtype={'code':object})
	def update_func():
		codes = ['000005','000004','000001','000001']
		dates = ['2018-01-01','2018-01-04','2018-01-01','2018-01-03']
		close = [2.1,2.2,2.3,2.4]
		return DataFrame({'code':codes,'date':dates,'close':close})
	update_func()

def test_empty_file():
	@updater('test_code2.csv',keys=['code','date'],dtype={'code':object})
	def update_func():
		codes = ['000005','000004','000001','000001']
		dates = ['2018-01-01','2018-01-04','2018-01-01','2018-01-03']
		close = [2.1,2.2,2.3,2.4]
		return DataFrame({'code':codes,'date':dates,'close':close})
	update_func()

if __name__ == "__main__":
	pass
