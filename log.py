#!/usr/bin/python
# coding=utf-8

import logging, sys, os
logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)
logger = logging.getLogger('stock')

#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
