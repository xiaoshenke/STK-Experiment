#!/bin/bash

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

	COUNT=0
	while [ $COUNT -lt 1 ]; do
    		echo -e ".\c"
    		sleep 1
    		COUNT=1
    		for PID in $PIDS ; do
        		PID_EXIST=`ps -f -p $PID |grep -v TIME`
        		if [ -n "$PID_EXIST" ]; then
				echo $PID still alive....
            			COUNT=0
            			break
        		fi
    		done
	done

	echo "OK!"
	echo PIDs: ${PIDS[@]}
	return 1
}

# step1: kill standby scheduler
echo trying to kill juben-observe
PIDS=`ps aux|grep python|grep juben|grep observe|grep start_engine_mode|grep -v grep|awk '{print $2}'`

size=($PIDS)
if [ ${#size[@]} -eq 0 ]
then
	echo 不存在juben observe进程,直接返回
	exit 2
fi

echo juben-observe pid:${PIDS[@]}
echo killing juben-observe at `date +'%Y-%m-%d %H:%M:%S'`...

kill_pids ${PIDS[@]}

#if [ $? -eq 0 ]
#then
#	echo killing standby scheduler fail.
#fi


