#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/pan_config_cli.py open_config
python realtime/pan_config_cli.py open_config
