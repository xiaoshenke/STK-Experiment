#!/bin/bash

export PYTHONUNBUFFERED=1
       
echo python engine/observe/buyer/server/cli.py start_engine_mode --buyer_server.log  
nohup python engine/observe/buyer/server/cli.py start_engine_mode  >>buyer_server.log 2>&1 &

