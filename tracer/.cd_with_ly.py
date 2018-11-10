#!/usr/bin/python
# coding=utf-8

import pandas
from log import logger
from tracer.tracer2 import Tracer
from cons import CSV_PATH
from pandas import DataFrame,Series
from util.df_util import read_csv,to_csv,ser_to_df,copy_ser

DEBUG_OPEN = True

# stage状态 1:超跌中 2:超跌结束,但是在一段时间内没有反弹,认为结束了所有状态 3:超跌+反弹确认 4:超跌+反弹后立即结束 5:超跌+反弹确认后持续反弹 6:超跌+反弹正常结束流程
class CD_With_LY(Tracer):
    FILE = 'cd_with_ly.csv'
    def __init__(self):
	Tracer.__init__(self)
        self.file = "%stracer/%s"%(CSV_PATH,CD_With_LY.FILE)
        self.init_tracer()

    def set_file(self,file):
	self.file = file
        self.init_tracer()

    def init_tracer(self):
	import os
        if os.path.exists(self.file):
                return
        data = {}
        names = self.get_column_names()
        for name in names:
                data[name] = []
        df = DataFrame(data)
        df = df[names]
        return to_csv(df,self.file)

    def get_column_names(self):
	return ['code','cd_start','cd_end','ly_start','ly_end','stage','created','date','status']

    def get_db(self):
	return read_csv(self.file)

    def save_db(self,df):
	if not df.empty:
                df = df.sort_values(['date','code','cd_start'],ascending=[False,True,False])
        return to_csv(df,self.file)

    def trace_code_from_day(self,code,day,end=None,save_db=True,on_pp=True):
	from util.time_util import today
        from pandas import DataFrame,Series
        end = end if end else str(today())

	from strategy.cd.with_ly import WithLianyang

	wb = WithLianyang()
        wb.set_codes([code])
        wb.set_start_end(day,end)
        wb.set_on_pp(on_pp)
        ret = wb.apply_history()

	if ret.empty:
                return ret
	items = CD_With_LY_Item.from_stra_items(ret,end)
        sers = []
        for item in items:
                sers.append(item.to_ser())
        ret = DataFrame(sers)
        ret['created'] = str(today())
        ret['date'] = end
        ret['status'] = 1
        ret = ret[self.get_column_names()]

        if save_db and not ret.empty:
                df = self.get_db()
                ret = filter_stra_items(ret,df)
                df = pandas.concat([ret,df],axis=0)
                self.save_db(df)
        return ret

    def update_code_to_day(self,code,day,save_db=True,on_pp=True):
	df = self.get_db()
        df = df[df['code']==code]
        df = df.sort_values('cd_start',ascending=False)
        ser = df.ix[df.index.tolist()[0]]
        if ser['date'] >= day:
                logger.debug("update_code_to_day,code:%s day:%s but seems exist in db,so ignore",code,day)
                return DataFrame()

        stage = ser['stage']
        cd_start = ser['cd_start']

        update = self.trace_code_from_day(code,cd_start,day,save_db=False,on_pp=on_pp)
        if update.empty:
                return update
        if save_db:
                df = pandas.concat([update,df],axis=0)
                self.save_db(df)
        return update

    def is_code_alive(self,code,day,db=DataFrame()):
	df = self.get_db() if db.empty else db
        if df.empty:
                return False

        df = df[df['code']==code]
        if df.empty:
                return False
        df = df.sort_values('cd_start',ascending=False)
        ser = df.ix[df.index.tolist()[0]]
        stage = ser['stage']
        if stage == 2 or stage == 4 or stage == 6:
                return False
        return True

def filter_stra_dfs(df,hist_df):
	if df.empty:
                return df

        df = df.groupby(df['code']).apply(filter_stra_items,hist_df=hist_df)
        df.index = df.index.get_level_values(0)
        df = df.reset_index(drop=True)
        return df

def filter_stra_items(df,hist_df):
	if hist_df.empty or df.empty:
                return df
        code = df['code'].tolist()[0]
        tmp = hist_df
        tmp = tmp[tmp['code']==code]
        if tmp.empty:
                return df

        starts = tmp['cd_start'].tolist()
        tmp = df['cd_start'].tolist()
        filters = []
        for day in tmp:
                if day not in starts:
                        filters.append(day)

        if len(filters) == 0:
                return DataFrame()

        df = df.set_index('cd_start',drop=True)
        df = df.reindex(filters)
        df = df.reset_index(drop=False)
        return df

class CD_With_LY_Item:
    def __init__(self):
        self.code = "";self.cd_start = "";self.cd_end = "";
        self.ly_start = "";self.ly_end  = "";self.stage = -1

    def to_ser(self):
        ser = {'code':self.code,'cd_start':self.cd_start,'cd_end':self.cd_end,'ly_start':self.ly_start,'ly_end':self.ly_end,'stage':self.stage}
        return Series(ser)

    def to_df(self):
        ser = self.to_ser()
        return ser_to_df(ser)

    @staticmethod
    def from_db_item(ser):
        code,cd_start,cd_end,cd_stage,ly_start,ly_end,stage = (ser['code'],ser['cd_start'],ser['cd_end'],ser['stage'],ser['ly_start'],ser['ly_end'],ser['stage'])
        item = CD_With_Brk_Item()
        item.code = code; item.cd_start = cd_start; item.cd_end = cd_end
        item.ly_start = ly_start; item.ly_end = ly_end; item.stage = stage
        return item

    @staticmethod
    def from_stra_item(ser,cur_day):
        if ser.empty:
                return None
        code,cd_start,cd_end,cd_stage,ly_start,ly_end,fd_ly = (ser['code'],ser['cd_start'],ser['cd_end'],ser['stage'],ser['ly_start'],ser['ly_end'],ser['fd_ly'])
        stage = 1
	if cd_stage == 1 or cd_stage == 5:
		stage = 1

	else:
		if fd_ly == 0:
			from util.stk_merge import _len_of
			if _len_of(cd_end,cur_day) > 2+3:
				stage = 2
		else: 
			from core.ly.stk_lianyang import LianYang
			ly = LianYang(code,ly_start,ly_end)
			from core.ly.lianyang_stage import LYStage
			ly_stage = LYStage(ly,cur_day)
			ly_stage = ly_stage.get_current_stage()
			if ly_stage == 1:
				stage = 3
			elif ly_stage == 2:
				stage = 4
			elif ly_stage == 3:
				stage = 5
			else:
				stage = 6

        item = CD_With_LY_Item()
        item.code = code; item.cd_start = cd_start; item.cd_end = cd_end
        item.ly_start = ly_start; item.ly_end = ly_end; item.stage = stage
        return item

    @staticmethod
    def from_stra_items(df,cur_day):
        if df.empty:
                return []
        ret = []
        for idx in df.index.tolist():
                item = CD_With_LY_Item.from_stra_item(df.ix[idx],cur_day)
                ret.append(item)
        return ret

def update_codes_tracers(codes,end,file="",on_pp=False,create_if=False,save_db=True):
	if len(codes) == 0:
                logger.debug("update_codes_tracers but codes is empty,so return!")
                return

        cwly = CD_With_LY()
        if file:
                cwly.set_file(file)
        db = cwly.get_db()
        updates = []
        creates = []
        for code in codes:
                if cwly.is_code_alive(code,end,db):
                        updates.append(code)
                else:
                        creates.append(code)

        logger.debug("update_codes_tracers,we get updates:\n%s\nand creates:\n%s",updates,creates)

        from util.merge_on_df import merge_on_df
        update = merge_on_df(DataFrame({'code':updates}),on_pp,[],[cwly,end])(_update_codes_tracers)()
        if save_db:
                hist = cwly.get_db()
                df = filter_stra_dfs(df,hist)
                if not df.empty:
                        hist = pandas.concat([hist,update],axis=0)
                        cwly.save_db(hist)

        if create_if:
                from util.trade_day_util import get_trade_day_before
                create_init_codes_tracers(codes,get_trade_day_before(end,30),end,file,on_pp,save_db=save_db)
        return

def _update_codes_tracers(ser,cwly,end):
	return cwly.update_code_to_day(ser['code'],end,save_db=False,on_pp=False)

def create_init_codes_tracers(codes,start,end,file="",on_pp=False,save_db=True):
	if len(codes) == 0:
                raise Exception("create_init_codes_tracers,codes is empty!")

        cwly = CD_With_LY()
        if file:
                cwly.set_file(file)
        from util.merge_on_df import merge_on_df
        df = merge_on_df(DataFrame({'code':codes}),on_pp,[],[cwly,start,end])(_init_codes_tracers)()

        if save_db:
                hist = cwly.get_db()
                filter_df = filter_stra_dfs(df,hist)

		if DEBUG_OPEN:
			logger.debug("create_init_codes_tracers,after filter,df:\n%s",filter_df)
                if not filter_df.empty:
                        hist = pandas.concat([hist,filter_df],axis=0)
                        cwly.save_db(hist)
        return df

def _init_codes_tracers(ser,cwly,start,end):
        return cwly.trace_code_from_day(ser['code'],start,end,on_pp=False,save_db=False)

def demo():
	code = '600448'
        return create_init_codes_tracers([code],'2018-06-01','2018-10-19',file='cwly_tmp.csv',on_pp=False,save_db=True)

if __name__ == "__main__":
	print demo()

