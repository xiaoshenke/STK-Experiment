#!/bin/bash

# 列举当前的listener进程列表

echo "ps aux|grep python |grep listener_cli|grep -v grep"
ps aux|grep python |grep listener_cli|grep -v grep 

echo ""
ps aux|grep python |grep listener_cli|grep -v grep | awk '{print $14}'

