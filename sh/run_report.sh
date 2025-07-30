#!/bin/bash

export PYTHONUNBUFFERED=1

day=`date +'%Y-%m-%d'`
if [ $# -ne 1 ]
then
	echo Usage:sh/run_prerun.sh day
else
	day=$1
fi

ap='localhost:STK-Experiment wuxian$ '

echo "

生成一下市场的一些数据

"

echo $ap python realtime/stage/cli.py get db32*CODES_BAN size --mode close
python realtime/stage/cli.py get db32*CODES_BAN size --mode close --silent 1 --day $day 

echo "
"

sleep 2

echo $ap python eva/cli.py do_eva db102 dstp --mode close
python eva/cli.py do_eva db102 dstp --mode close --open 0 --day $day  --silent 1

echo "
"

sleep 2

echo $ap python engine/stage/xls/exp_cli.py day_stages db102 eva_size:eva_type=risk:min=5*dban_size:min=2 --size 6
python engine/stage/xls/exp_cli.py day_stages db102 eva_size:eva_type=risk:min=5*dban_size:min=2 --size 6 --day $day 

echo "
"

sleep 2

echo $ap python engine/stage/xls/exp_cli.py day_stages db32 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6
python engine/stage/xls/exp_cli.py day_stages db32 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6 --day $day 

echo "
"

sleep 2

echo $ap python engine/stage/xls/exp_cli.py day_stages db31 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6
python engine/stage/xls/exp_cli.py day_stages db31 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6 --day $day 

echo "
"

sleep 2

echo $ap python engine/stage/xls/exp_cli.py day_stages db102s*dgx3_2 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6
python engine/stage/xls/exp_cli.py day_stages db102s*dgx3_2 bodong --names xls,score,score2,total,good,bad,upstp,crash,weak --size 6 --day $day 

echo "
"

sleep 2

echo $ap python realtime/stage/cli.py gets list:db43,db32,db31 uptrend2:mode=noon --mode close
python realtime/stage/cli.py gets list:db43,db32,db31 uptrend2:mode=noon --mode close --silent 1 --day $day 

echo "
"

sleep 2
echo $ap python engine/stage/market/exp_cli.py day_stages maichong.atzao --size 5 
python engine/stage/market/exp_cli.py day_stages maichong.atzao --size 5 --silent 1 --day $day 
echo "
"

sleep 2
echo $ap python engine/stage/market/exp_cli.py day_stages emotion 
python engine/stage/market/exp_cli.py day_stages emotion --silent 1 --day $day 

echo "
"

sleep 2

echo $ap python engine/stage/market/exp_cli.py day_stages emotion3
python engine/stage/market/exp_cli.py day_stages emotion3 --silent 1 --day $day 

echo "


生成结束
"
