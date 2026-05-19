#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
pool=#
template='buyer'
now=0
time_str=#
mode='now'
operate='flush'

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/run_qp_template.sh xls [template] [operate ] 
	exit 2
fi

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
	-operate | --operate)
		shift
		operate=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			pool=$1
		elif [ $now -eq 1 ]
		then
			template=$1
		elif [ $now -eq 2 ]
		then
			operate=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

# 旧版API
#echo python realtime/observe/juben.py run_qp_template $pool $template  --day $day --mode $mode --time_str $time_str
#python realtime/observe/juben.py run_qp_template $pool $template  --day $day --mode $mode --time_str $time_str

# 新版API
echo python engine/observe/buyer/runner/template_cli.py run_qp_template $pool $template  --day $day --mode $mode --time_str $time_str --operate $operate 
python engine/observe/buyer/runner/template_cli.py run_qp_template $pool $template  --day $day --mode $mode --time_str $time_str --operate $operate 
