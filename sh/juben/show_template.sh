#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/observe/juben/config_cli.py show_template
python engine/observe/juben/config_cli.py show_template
