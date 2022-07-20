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

# example:
#pids=("86")
#kill_pids ${pids[@]}

# step1: kill standby scheduler
echo trying to kill inn-standy..
PIDS=`ps aux|grep python|grep schedule|grep -v grep|awk '{print $2}'`
echo standby scheduler pid:${PIDS[@]}
echo killing standby scheduler at `date +'%Y-%m-%d %H:%M:%S'`...

# not killing standby
kill_pids ${PIDS[@]}
if [ $? -eq 0 ]
then
	echo killing standby scheduler fail.
fi

# step2: kill main engine
echo trying to kill python-process-with-engine-str..
PIDS=`ps aux|grep python|grep engine|grep -v grep|awk '{print $2}'`
echo main engine pid:${PIDS[@]}
echo killing main engine at `date +'%Y-%m-%d %H:%M:%S'`...

kill_pids ${PIDS[@]}

# step3: kill advisors
echo trying to kill python-process-with-engine-mode..
PIDS=`ps aux|grep python|grep start_node_engine_mode|grep -v grep|awk '{print $2}'`
echo advisors pid:${PIDS[@]}
echo killing engine-mode-python-process at `date +'%Y-%m-%d %H:%M:%S'`...
kill_pids ${PIDS[@]}


