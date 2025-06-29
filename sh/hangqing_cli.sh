#!/bin/bash

echo ATTENTION: HANGQING-CMDS CLI

day=#
time_str=#
mode=#

# 默认行情类型为zhendang
hq_type='zhendang'
type=''
ignore_cache=0
debug=0
now=0
while [ -n "$1" ]
do 
        case "$1" in 
        -day | --day)
                shift
                day=$1
                ;;
        -time_str | --time_str)
                shift
                time_str=$1
                ;;
        -mode | --mode)
                shift
                mode=$1
                ;;
	-debug | --debug)
		shift
		debug=$1
		;;
	-ignore_cache | --ignore_cache)
                shift
                ignore_cache=$1
                ;;
        -help | --help)
		echo usage sh/hangqing_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] zhendang|zhuxian|trends|itrend|youzi
                exit 1
                ;;
        *)
		# set value to type|hq_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		else
			hq_type=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

if [ $# -eq 2 ]
then
	type=$1
	hq_type=$2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_lei_cross=$(python realtime/hangqing_cli.py is_lei_cross_stage $hq_type)
can_be_stage=$(python realtime/hangqing_cli.py can_be_stage_type $hq_type)

echo is_lei_cross:$is_lei_cross,can_be_stage:$can_be_stage

if [[ $hq_type =~ ".hist" ]] || [[ $hq_type =~ ".times" ]] || [[ $hq_type =~ ".cross" ]] || [[ $is_lei_cross == "1" ]]
then
	echo python realtime/stage/cli.py get $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --do_log 1
	python realtime/stage/cli.py get $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --do_log 1

elif [[ $can_be_stage == "1" ]]
then
	echo python realtime/hangqing_cli.py do_stage $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py do_stage $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "zhendang" ]] || [[ $hq_type == "zd" ]]
then
	echo python realtime/hangqing_cli.py zhendang $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py zhendang $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "buyer_plan" ]] || [[ $hq_type == "bp" ]] 
then
	echo python realtime/hangqing_cli.py buyer_plan $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py buyer_plan $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "itrend" ]] || [[ $hq_type =~ "trend2" ]]
then
	echo python realtime/flush_cli.py flush_itrend $type --itrend_str $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush_itrend $type --itrend_str $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "change" ]]
then
	echo python realtime/hangqing_cli.py change $type --change_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py change $type --change_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "pulls" ]]
then
	echo python realtime/hangqing_cli.py pulls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py pulls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "pull" ]]
then
	echo python realtime/hangqing_cli.py pull $type --pull_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py pull $type --pull_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "maoding" ]]
then
	echo python realtime/hangqing_cli.py maoding $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/hangqing_cli.py maoding $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

#elif [[ $hq_type == "youzi" ]] || [[ $hq_type == "yz" ]]
#then
#	echo python realtime/hangqing_cli.py maoding $type maoding:yz --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
#	python realtime/hangqing_cli.py maoding $type maoding:yz --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "zhuxian" ]] || [[ $hq_type =~ "zhuxians" ]]
then
	echo python realtime/hangqing_cli.py zhuxian $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py zhuxian $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "tidui" ]] || [[ $hq_type =~ "tiduis" ]]
then
	echo python realtime/hangqing_cli.py tidui $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py tidui $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "realtime" ]] || [[ $hq_type =~ "realtimes" ]]
then
	echo python realtime/hangqing_cli.py realtime $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py realtime $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "chaoduan" ]] || [[ $hq_type == "cd" ]] || [[ $hq_type == "youzi" ]] || [[ $hq_type == "yz" ]] 
then
	echo python realtime/hangqing_cli.py chaoduan $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py chaoduan $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "zhudong" ]]
then
	echo python realtime/hangqing_cli.py zhudong $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/hangqing_cli.py zhudong $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "bodong" ]]
then
	echo python realtime/hangqing_cli.py bodong $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/hangqing_cli.py bodong $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "jinji" ]]
then
	echo python realtime/hangqing_cli.py jinji $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/hangqing_cli.py jinji $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "zhushen" ]]
then
	echo python realtime/hangqing_cli.py zhusheng $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	python realtime/hangqing_cli.py zhusheng $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "qieh" ]] || [[ $hq_type =~ "qh" ]]
then
	echo python realtime/hangqing_cli.py qiehuan $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --debug $debug
	python realtime/hangqing_cli.py qiehuan $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --debug $debug

elif [[ $hq_type =~ "trend" ]]
then
	echo python realtime/hangqing_cli.py days_trend $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py days_trend $type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "maichong" ]]
then
	echo python realtime/hangqing_cli.py maichong $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py maichong $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "maodingb" ]] || [[ $hq_type == "md" ]] || [[ $hq_type == "mdb" ]]
then
	echo python realtime/hangqing_cli.py maodingb $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py maodingb $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "zhudao" ]]
then
	echo python realtime/hangqing_cli.py zhudao $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py zhudao $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type == "lianghua" ]] || [[ $hq_type == "lh" ]]
then
	echo python realtime/hangqing_cli.py lianghua $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py lianghua $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $hq_type =~ "fenbu" ]]
then
	echo python realtime/hangqing_cli.py fenbu $type --fenbu_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py fenbu $type --fenbu_type $hq_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo 输入的行情类型$hq_type 不正确
fi
