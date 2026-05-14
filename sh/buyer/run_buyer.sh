#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#
now=0
add=0
mode='now'
operate='flush'
time_str='0'

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/run_buyer.sh id [--day ] 
      	exit 2
fi

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
	-operate | --operate)
		shift
		operate=$1
		;;
	-add | --add_codes | --add)
		shift
		add=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type="$1"
		elif [ $now -eq 1 ]
		then
			operate=$1
		elif [ $now -eq 2 ]
		then
			day=$day
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

do_register=$(python engine/observe/buyer/runner/cli.py may_register_first $type)
if [[ $do_register == "1" ]]
then
	echo "检测到必须先注册到buyer recorder中 即: sh/buyer/add_buyer.sh \"$type\" --day $day --print_run_msg 1"
	exit 2

	#id=$(python engine/observe/buyer/runner/cli.py register_type_and_return $type --day $day)
	#type=$id
fi

#is_single_id=$(python engine/observe/buyer/runner/cli.py is_single_id $type)
#if [[ $is_single_id == "1" ]]

is_valid_buyer_id=$(python engine/observe/buyer/runner/cli.py is_valid_buyer_id $type $day)
echo is_valid_buyer_id:$is_valid_buyer_id
# 取最后一个字符
is_valid_buyer_id="${is_valid_buyer_id:${#is_valid_buyer_id}-1}"

if [[ $is_valid_buyer_id == "1" ]]
then
	#echo python engine/observe/buyer/server/flush_one.py flush $type $day $time_str --mode $mode
	#python engine/observe/buyer/server/flush_one.py flush $type $day $time_str --mode $mode

	echo python engine/observe/buyer/server/flush_buyer_id.py flush $type $day $time_str --mode $mode
	python engine/observe/buyer/server/flush_buyer_id.py flush $type $day $time_str --mode $mode

else
	echo ""
	echo ""
	echo python engine/observe/buyer/runner/cli.py run $type --day $day --time_str $time_str --mode $mode 
	python engine/observe/buyer/runner/cli.py run $type --day $day --time_str $time_str --mode $mode 
fi
