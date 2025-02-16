#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/observe/buyer/config_cli.py show_template
python engine/observe/buyer/config_cli.py show_template
