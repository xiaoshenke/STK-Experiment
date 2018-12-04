#!/usr/bin/python
# coding=utf-8

# 几个约定:
# 1,通过cli update_today_strategy,init_strategy生成的策略的路径在data/strategy,直接以策略命名
# 2,同理对应的全数据也在data/strategy/hist路径,命名规范xxx(_abc).hist.csv
# 3,策略的单日生成文件(包括子策略)在strategy/xxx/daily,命名规范xxxx-xx-xx_abc.csv
# 4,单日的策略code tracer文件在data/strategy/trc_codes,命名规范xxx.codes(.yyy).csv

