#!/bin/bash

# 列举当前的tracing进程列表

echo "ps aux|grep python |grep entity_cli|grep -v grep"
ps aux|grep python |grep entity_cli|grep -v grep 

echo ""
ps aux|grep python |grep entity_cli|grep start_engine_mode|grep -v grep | awk '{print $14}'

