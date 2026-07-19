#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
xls=#
template=#
now=0
time_str=#
mode='now'
operate='flush'
with_logic=-1
ignore_cache=0

if [ $# -lt 2 ]
then
	echo Usage: sh/juben/run_xls_template.sh xls template [--day ] 
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
	-ignore_cache | --ignore_cache | -ignore | --ignore)
		shift
		ignore_cache=$1
		;;
	-operate| --operate)
		shift
		operate=$1
		;;
        -with_logic | --with_logic | -logic| --logic)
		shift
		with_logic=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			template=$1
		elif [ $now -eq 2 ]
		then
			#operate=$1
			day=$1
		elif [ $now -eq 3 ]
		then
			mode=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

valid_logic=$(python realtime/observe/juben.py is_a_valid_with_logic $with_logic)
# 取最后一个字符
valid_logic="${valid_logic:${#valid_logic}-1}"

if [[ $valid_logic == "1" ]]
then
	# 仅在指定with logic的时候 会走到这个分支
	echo 当前手工指定了with_logic:$with_logic 因此走buyer下的实现
	echo python engine/observe/buyer/runner/template_cli.py run_xls_template $xls $template  --day $day --mode $mode --time_str $time_str --operate $operate --with_logic $with_logic 
	python engine/observe/buyer/runner/template_cli.py run_xls_template $xls $template  --day $day --mode $mode --time_str $time_str --operate $operate --with_logic $with_logic 

else

	echo python realtime/observe/juben.py run_xls_template $xls $template --day $day --mode $mode --time_str $time_str --operate $operate --ignore_cache $ignore_cache
	python realtime/observe/juben.py run_xls_template $xls $template --day $day --mode $mode --time_str $time_str --operate $operate --ignore_cache $ignore_cache

fi
