#!/usr/bin/python
# coding=utf-8
from cons import INN_RUNNING
from util.time_util import today

import logging, sys, os
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,filemode='a')
logger = logging.getLogger('stock')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger.setLevel(logging.DEBUG)

f_logger = logging.getLogger('fstock')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
# 配置文件路径
fh = logging.FileHandler("%s%s.log"%(INN_RUNNING,str(today())))
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
f_logger.addHandler(fh)
fh = logging.StreamHandler(sys.stdout)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
f_logger.setLevel(logging.DEBUG)

INN_EVA_LOG_NAME="inn_eva"
