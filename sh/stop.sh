#!/bin/bash

function kill_pids {
	PIDS=(`echo "$@"`)
	if [ -z "$PIDS" ]; then
        	echo "server does not started!"
		return 0
	fi

	for PID in $PIDS ; do
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
            			COUNT=0
            			break
        		fi
    		done
	done

	echo "OK!"
	echo "PID: $PIDS"
	return 1
}

# example:
#pids=("86")
#kill_pids ${pids[@]}

# step1: kill standby scheduler

PIDS=`ps -aux|grep python|grep schedule|grep -v grep|awk '{print $2}'`
echo standby scheduler pid:${PIDS[@]}
echo killing standby scheduler...

kill_pids ${PIDS[@]}
if [ $? -eq 0 ]
then
	echo killing standby scheduler fail,please manual checkout!!
	exit 1
fi

# step2: kill main engine
PIDS=`ps -aux|grep python|grep engine|grep -v grep|awk '{print $2}'`
echo main engine pid:${PIDS[@]}
echo killing main engine...

kill_pids ${PIDS[@]}


