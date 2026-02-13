#!/bin/bash

export PYTHONUNBUFFERED=1
       
echo python engine/ecore/window/txt_cli.py start_open_txt_manager_engine_mode --open_txt_mgr.log
nohup python engine/ecore/window/txt_cli.py start_open_txt_manager_engine_mode >>open_txt_mgr.log 2>&1 &

