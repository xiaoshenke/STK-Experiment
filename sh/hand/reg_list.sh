#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/observe/tracing//register_cli.py last
python engine/observe/tracing//register_cli.py last

echo ""
echo ""
echo ""
echo "仅显示hand相关注册信息(仅代表历史 不代表进程依旧存在)"
echo "如果某个注册格式形如 file:abc.hand 那么打开日志的方式: sh/hand/tail_log.sh abc"
python engine/observe/tracing//register_cli.py last|grep hand

