#!/usr/bin/python
# coding=utf-8

# -- LOGGIING规范 --
# 1, 触发函数(如handle_wfenshi_modified),以[Trigger]:标记
# 2, 调度逻辑,以[Schedule]:标记
# 3, 配置逻辑,以[Config]:标记
# 4, 通知函数,以[Notify]:标记
# 5, 动作逻辑,以对应的动作做标记,比如[Submit]:,[Remove]:
