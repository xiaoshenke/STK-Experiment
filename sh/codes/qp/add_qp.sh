#!/bin/bash

# 向@engine/recorder/ztt/qp_recorder.py 注册一条切片数据

# @engine/recorder/ztt/regist/qp_req_cli.py

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
rank=-1
sure=-1
risk=-1
itrend=-1
trends=-1
desc=#
name=#
mode='now'
time_str='0'
sort=-1
start=#
end=#
flush=0
max_times=-1
force=0
with_logic=-1

now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
        -sort | --sort)
		shift
		sort=$1
		;;
	-with_logic | --with_logic | -logic| --logic)
		shift
		with_logic=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-rank | --rank)
		shift
		rank=$1
		;;
	-sure | --sure)
		shift
		sure=$1
		;;
	-risk | --risk)
		shift
		risk=$1
		;;
	-itrend | --itrend | -itrned | --itrned | -trend | --trend)
		shift
		itrend=$1
		;;
	-trends | --trends)
		shift
		trends=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		desc="$1"
		;;
	-name | --name)
		shift
		name=$1
		;;
	*)
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then 
			desc="$1"
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/recorder/ztt/regist/qp_req_cli.py add $code_type --rank $rank --sure $sure --risk $risk --itrend $itrend --trends $trends --day $day --time_str $time_str --desc "$desc"

python engine/recorder/ztt/regist/qp_req_cli.py add $code_type --rank $rank --sure $sure --risk $risk --itrend $itrend --trends $trends --day $day --time_str $time_str --desc "$desc"

