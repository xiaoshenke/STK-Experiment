#!/bin/bash
# only work in mac os

#osascript -e 'quit app "TextEdit"'

function kill_pids {
        PIDS=(`echo "$@"`)
        if [ -z "$PIDS" ]; then
                echo -e "process not running,ignore.\n"
                return 0
        fi

        for PID in ${PIDS[@]} ; do
                echo try to kill $PID
                kill $PID > /dev/null 2>&1
        done
}

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

pan_id=$(python realtime/properties_cli.py read_pan_id)

echo python realtime/properties_cli.py read_pan_id的返回结果: $pan_id

PIDS=`ps aux|grep TextEdit|grep -v grep|awk '{print $2}'`

if [ $pan_id -gt 0 ]
then
	PIDS=`ps aux|grep TextEdit|grep -v grep|awk '{print $2}'|grep -v $pan_id`
fi

echo 找到的所有text进程id ${PIDS[@]}
kill_pids ${PIDS[@]}
