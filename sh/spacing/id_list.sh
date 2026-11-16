#!/bin/bash
# usage sh/ls_fenshi.sh [day]

# 列出当前的所有id列表

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
        day=$1
fi

echo python engine/spacing/schedule_cli.py list_all_id --day $day
python engine/spacing/schedule_cli.py list_all_id --day $day

echo ""

