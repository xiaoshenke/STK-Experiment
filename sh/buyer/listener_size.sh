#!/bin/bash

# 获取listener的进程数量

listens=$(ps aux|grep python |grep listener_cli|grep -v grep | awk '{print $14}')
listens=($listens)

echo ${#listens[@]}

