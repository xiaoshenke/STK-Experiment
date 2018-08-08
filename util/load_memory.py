#!/usr/bin/python
# coding=utf-8
# 从内存加载结果装饰器

from log import logger

DEBUG_OPEN = False

STOCK = 1;INDEX = 2;PLATE = 3;AREA  = 4;TOVER = 5

stk_map = {};index_map = {};plate_map = {};area_map = {};tover_map = {}

def load_memory(code,type=STOCK):
	def _load_memory(func):
		def _real(*args,**kwargs):
			r_map = None
			if type == STOCK:
				r_map = stk_map
			elif type == INDEX:
				r_map = index_map
			elif type == PLATE:
				r_map = plate_map
			elif type == AREA:
				r_map = area_map
			elif type == TOVER:
				r_map = tover_map			
			else:
				if DEBUG_OPEN:
					logger.debug("@load_memory,type:%s not supported,ignore decrator"%type)
				return func(*args,**kwargs)

			if code in r_map:
				if DEBUG_OPEN:
					logger.debug("@load_memory hit memory")
				return r_map[code]
			if DEBUG_OPEN:
				logger.debug("@load_memory hit memory fail")

			ret = func(*args,**kwargs)
			r_map[code] = ret
			return ret
		return _real
	return _load_memory

def test_load():
	def hi():
		return "hello"
	load_memory("1")(hi)()
	load_memory("1")(hi)()

if __name__ == "__main__":
	test_load()

