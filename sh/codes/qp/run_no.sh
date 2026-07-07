#!/bin/bash

# 尝试读取@engine/codes/recorder/qp_operate_recorder.py 是否有过数据 如果有 那么成功读取到对应的properties no,然后再从@engine/recorder/properties_recorder.py 中读取实际的properties 然后进行调度运行
# 如果没有 那么打开默认的overall tips文件

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
now=0
add=0
mode='now'
operate='flush'
time_str='0'
no='0'

if [ $# -lt 2 ]
then
	echo Usage: sh/codes/qp/analyze.sh code_type no [--day ] 
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
			code_type="$1"
		elif [ $now -eq 1 ]
		then
			no=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/codes/runner/cli.py run $code_type $no --day $day --time_str $time_str --mode $mode
python engine/codes/runner/cli.py run $code_type $no --day $day --time_str $time_str --mode $mode 
