#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/stage/cli.py gets bkzj.top:no_index=1:limit=10 eva_size:eva_type=ggzj
python realtime/stage/cli.py gets bkzj.top:no_index=1:limit=10 eva_size:eva_type=ggzj

