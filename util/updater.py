#!/usr/bin/python
# coding=utf-8
import pandas
import os
from pandas import DataFrame,Series
from log import logger

DEBUG_OPEN = True

# 被updater注解的函数返回一个无效index的DataFrame 
def updater(file_name,keys=[],dtype={'code':object},encoding='utf-8',sort_key=None,ascending=False):
	def _updater(func):
		def _real(*args,**kwargs):
			ret = func(*args,**kwargs)

			if not file_name or len(file_name) == 0:
				if DEBUG_OPEN:
					logger.warn("filename empty,ignore")
				return ret

			elif not keys or len(keys) >= 3:
				if DEBUG_OPEN:
					logger.debug("keys is none,or length of keys is not supported!")
				return ret
						
			elif not _check_df_type_and_value(ret):
				return ret

			final_df = ret
			backup_df = DataFrame()
			do_write = True

			if os.path.exists(file_name):					
				try:
					origin_df = pandas.read_csv(file_name,date_parser=pandas.to_datetime,encoding=encoding,dtype=dtype)
					backup_df = origin_df

					# 校验一下从文件读取的origin_df和ret的columns是否相同,不相同则不进行存储
					do_write,ret = _check_df_names_same_2(origin_df,ret)
					if do_write:
						if len(keys) == 0:
							do_write,final_df = _deal_key_len_0(keys,origin_df,ret)
						elif len(keys) == 1:
							do_write,final_df = _deal_key_len_1(keys,origin_df,ret)					
						elif len(keys) == 2:
							do_write,final_df = _deal_key_len_2(keys,origin_df,ret)
					else:
						if DEBUG_OPEN:
							logger.debug("columns not all fit,simply ignore")
				except Exception,e:
					# 出现异常 不写文件
					do_write = False
					logger.warn("updater decorator exception:%s"%e)
			
			if do_write:
				try:
					if sort_key != None:
						final_df = final_df.sort_values(sort_key, ascending=ascending)
					final_df.to_csv(file_name,index=False,date_format="%Y-%m-%d",encoding=encoding)
					logger.info("@updater,file:%s updated!"%file_name)
				except Exception,e:
					logger.warn("updater decorator,exception:%s"%e)
					if not backup_df.empty:
						backup_df.to_csv(file_name,index=False,date_format="%Y-%m-%d",encoding=encoding)
			return ret
		return _real
	return _updater


def is_series_type(o):
	return type(o) == type(Series())

def is_df_type(o):
	return type(o) == type(DataFrame())

# df.ix[idx] 这个值可能是一个series也可能是一个dataframe,本函数统一返回一个dataframe
def get_df_by_idx(df,idx,key1):
	tmp = None
	if is_series_type(df.ix[idx]):
		tmp = DataFrame([df.ix[idx]])
		tmp.index.name = key1
		tmp = tmp.reset_index(drop=False)
	else:
		tmp = df.ix[idx].reset_index(drop=False)
	return tmp

def _check_df_type_and_value(ret):
	if not is_df_type(ret):
		if DEBUG_OPEN:
			logger.debug("func annotated with @updater return not dataframe type,ignore ")
		return False

	elif ret.empty:
		if DEBUG_OPEN:
			logger.warn("@updater.func return empty,ignore")
		return False
	return True

# return (bool,df)
def _check_df_names_same_2(origin_df,df):
	names = df.columns.values
	for name in names:
		if name not in origin_df.columns.values:
			return False,df
	return True,df


# 这里额外做了是否对df进行reset_index的兜底工作
# return (bool,df)
def _check_df_names_same(origin_df,df):
	names1 = df.columns.values
	same = True
	for n in names1:
		if n not in df.columns.values:
			same = False
			break
	if same:
		return True,df

	same = True
	df2 = df.reset_index(drop=False)
	for n in names1:
		if n not in df2.columns.values:
			same = False
			break
	return same,df2

# return (bool,final_df)
def _deal_key_len_0(keys,origin_df,df):
	if DEBUG_OPEN:
		logger.debug("updater._deal_key_len_0")
	return True,pandas.concat([origin_df,df],axis=0)

# return (bool,final_df)
def _deal_key_len_1(keys,origin_df,df):
	if DEBUG_OPEN:
		logger.debug("updater._deal_key_len_1,origin_df size:%s df size:%s",origin_df.index.size,df.index.size)

	# 在一个键的情况下,只要这个键的值不在原来列表,即认为应该插入
	key = keys[0]
	# 在df列表而不在origin_df列表
	cb_list = []
	origin_key_list = origin_df[key].tolist()
	cmp_keys = [ str(k) for k in origin_key_list ]

	if DEBUG_OPEN:
		logger.debug("df:%s",df[:3])

	for idx in df.index.tolist():
		# FIXME: 使用str遇到unicode是不安全的,但现在应该只会在'code'和'date'字段	
		if str(df.ix[idx][key]) not in cmp_keys:
			cb_list.append(idx)
	cb_df = df.ix[cb_list]
	if DEBUG_OPEN:
		if cb_df.empty:
			logger.debug("cb_df is empty,so nothing will updated!")
		else:
			logger.debug("concat df size:%s",cb_df.index.size)
	return not cb_df.empty, pandas.concat([origin_df,cb_df],axis=0)

# return (bool,final_df)
def _deal_key_len_2(keys,origin_df,df):
	if DEBUG_OPEN:
		logger.debug("updater._deal_key_len_2")

	filter_df = DataFrame()
	(key1,key2) = (keys[0],keys[1])
	# sed_index便于遍历
	reidx_origin_df = origin_df.set_index(key1,drop=True)
	reidx_df = df.set_index(key1,drop=True)

	# 由于dataframe的index相同的时候,会对同一个key多次调用,这里使用already_cal_list过滤掉
	already_cal_list = []
	for idx in reidx_df.index.tolist():
		if idx not in already_cal_list:
			already_cal_list.append(idx)
		else:
			continue
		
		# idx不在history df时直接进行append
		if idx not in reidx_origin_df.index.tolist():
			tmp = get_df_by_idx(reidx_df,idx,key1)
			filter_df = pandas.concat([filter_df,tmp],axis=0)
			continue
		
		#开始合并,需要考虑history对应的key和ret对应的key存在多值的情况
		# 先处理history是多值的情况
		if is_series_type(reidx_origin_df.ix[idx][key2]):
			if is_series_type(reidx_df.ix[idx][key2]):
				# history和return同时是多值的情况
				tmp = get_df_by_idx(reidx_df,idx,key1) 
				cb_list = []
										
				for iidx in tmp.index:
					if tmp.ix[iidx][key2] not in reidx_origin_df.ix[idx][key2].values:
						cb_list.append(iidx)
				tmp = tmp.ix[cb_list]
				filter_df = pandas.concat([filter_df,tmp],axis=0)
			else:
				# history是多个值,return是单个值
				if reidx_df.ix[idx][key2] not in reidx_origin_df.ix[idx][key2].values:
					tmp = get_df_by_idx(reidx_df,idx,key1) 
					filter_df = pandas.concat([filter_df,tmp],axis=0)
		else:
			# 处理history为单值的情况
			if is_series_type(reidx_df.ix[idx][key2]):
				tmp = get_df_by_idx(reidx_df,idx,key1)
				cb_list = []

				for iidx in tmp.index:
					if tmp.ix[iidx][key2] != reidx_origin_df.ix[idx][key2]:
						cb_list.append(iidx)
				tmp = tmp.ix[cb_list]
				filter_df = pandas.concat([filter_df,tmp],axis=0)	
			else:
				if reidx_df.ix[idx][key2] != reidx_origin_df.ix[idx][key2]:
					tmp = get_df_by_idx(reidx_df,idx,key1) 
					filter_df = pandas.concat([filter_df,tmp],axis=0)
	if DEBUG_OPEN:
		logger.debug("filter_df size:%s",filter_df.index.size)
	return (not filter_df.empty,pandas.concat([origin_df,filter_df],axis=0))

def demo():
	codes = ['000001','000002','000003','000004','000001','a']
	dates = ['2018-01-01','2018-01-02','2018-01-03','2018-01-04','2018-01-02','2018-01-01']
	close = [1.1,1.2,1.3,1.4,1.5,0.0]
	df = DataFrame({'code':codes,'date':dates,'close':close})
	df.code = df.code.astype(str)
	#df.to_csv('test_code.csv',date_format="%Y-%m-%d",index=False)
	
	@updater('test_code.csv',keys=['code','date'],dtype={'code':object})
	def update_func():
		codes = ['000005','000004','000001','000001']
		dates = ['2018-01-01','2018-01-04','2018-01-01','2018-01-03']
		close = [2.1,2.2,2.3,2.4]
		return DataFrame({'code':codes,'date':dates,'close':close})
	update_func()

if __name__ == "__main__":
	demo()
