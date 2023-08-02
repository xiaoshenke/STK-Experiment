#!/bin/bash
# usage sh/clear_pools.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo 用于清空配置文件中的所有pool

echo python realtime/properties_cli.py clear_pools
python realtime/properties_cli.py clear_pools

