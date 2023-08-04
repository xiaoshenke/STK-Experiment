#!/bin/bash
# usage sh/current_keys.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo 用于显示当前所有的key

echo python realtime/properties_cli.py current_keys
python realtime/properties_cli.py current_keys

