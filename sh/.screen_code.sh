#!/bin/bash
# Usage: ./screen_code.sh your-code [your-day]
# ATTENTION! browser should be in width-full mode

SAVE_PATH='/Users/wuxian/Desktop/'

if [ $# -lt 1 ]
then
        echo Usage: ./screen_code.sh your-code [your-day] 
        exit 2
fi

code=$1
day=""
if [ $# -eq 2 ]
then
	day=$2
fi

sh/open_stock.sh $code

sleep 7
# gain focus to browser
cliclick c:500,500

sleep 0.5
# scroll down screen a little bit..
for i in `seq 1 10`
do
	cliclick kp:arrow-down
done

sleep 0.2
# switch to day k-line
cliclick c:570,280

sleep 2
times=`python helper.py cal_day_mouse_move_intervals $day`
echo we will scroll $times

if [ $times -gt 0 ]
then
	for i in `seq 1 $times`
	do
		cliclick -e 100 dd:600,400 du:650,400
		sleep 0.1
	done
	sleep 0.1
	cliclick c:700,200
	sleep 0.3
fi

screencapture -R 350,265,590,370 $SAVE_PATH/$code.png
