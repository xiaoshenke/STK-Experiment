#!/usr/bin/python
# coding=utf-8

from cons import INN_RUNNING
from util.time_util import today

import logging, sys, os
#logging.basicConfig(stream=sys.stderr,level=logging.DEBUG,filemode='a')
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,filemode='a')
logger = logging.getLogger('stock')

logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.INFO)

f_logger = logging.getLogger('fstock')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler("%s%s.csv"%(INN_RUNNING,str(today())))
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

f_logger.addHandler(fh)

