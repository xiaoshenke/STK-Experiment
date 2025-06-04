#!/bin/bash

echo ATTENTION: MANUAL-CMDS CLI

day=#
time_str=#
mode='now'

type=''
tag=#
codes=#
ignore_cache=1

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
	-tag | --tag)
		shift
		tag=$1
		;;
	
	-mode | --mode)
		shift
		mode=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			tag=$1
			codes=$1
		elif [ $now -eq 2 ]
		then
			tag=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

#is_code_types=$(python realtime/flush_cli.py is_code_types $type)
#is_eva=$(python realtime/flush_cli.py is_front_type $flush_type)

#elif [[ $is_code_types == "1" ]] && [[ $is_eva == "1" ]]
#then
#	echo 不支持code-types+eva类型 不过可以  sh/front_cli.sh $type $flush_type --mode $mode --day $day --time_str $time_str
#	exit 2

is_xls=$(python realtime/manual_cli.py is_xls $type)
echo is_xls:$is_xls

if [[ $type =~ "clear" ]]
then
	if [[ $type =~ "code_types" ]] || [[ $type =~ "codetypes" ]]
	then
		echo 当前指定了清除code-types,这个操作是比较严重的 因此只能通过调用原生命令实现:  python realtime/manual_cli.py clear $type --tag "$tag" --day $day 
		echo ""
		exit 2

	elif [[ $type =~ "codes" ]] || [[ $type =~ "code_type" ]] || [[ $type =~ "codetype" ]]
	then
		echo python realtime/manual_cli.py clear_code_type $codes --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
		python realtime/manual_cli.py clear_code_type $codes --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
		exit 2
	fi
	
	echo python realtime/manual_cli.py clear $type --tag $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py clear $type --tag $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type =~ "checkout" ]] 
then
	if [[ $type =~ "code_types" ]] || [[ $type =~ "codetypes" ]]
	then
		echo 'checkou-code-types'

	elif [[ $type =~ "codes" ]] || [[ $type =~ "code_type" ]] || [[ $type =~ "codetype" ]]
	then
		echo python realtime/manual_cli.py checkout_codes $codes --tag_str $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
		python realtime/manual_cli.py checkout_codes $codes --tag_str $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
		exit 2
	fi

	echo python realtime/manual_cli.py checkout $type --tag_str $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py checkout $type --tag_str $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type =~ "codes_version" ]] || [[ $type =~ "codesversion" ]]
then
	echo python realtime/manual_cli.py codes_version $codes --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py codes_version $codes --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type =~ "version" ]]
then
	echo python realtime/manual_cli.py version $type --tag $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py version $type --tag $tag --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "pool" ]]
then
	echo python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

# 添加maoding计算支持
elif [[ ${type:0:3} == "md:" ]] || [[ ${type:0:8} == "maoding:" ]]
then

	echo python realtime/caop/maoding.py get --xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/caop/maoding.py get --xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type =~ "buyer" ]]
then
	echo python realtime/manual_cli.py buyer --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
        python realtime/manual_cli.py buyer --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "youzi" ]] || [[ $type == "chaoduan" ]] 
then
	echo python realtime/manual_cli.py youzi --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
        python realtime/manual_cli.py youzi --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "codetypes" ]] || [[ $type == "code_types" ]] 
then
	echo python realtime/manual_cli.py code_types --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
        python realtime/manual_cli.py code_types --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "market" ]]
then
	echo python realtime/manual_cli.py market --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py market --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $is_xls == "1" ]]
then
	echo python realtime/manual_cli.py xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --do_log 1

else
	#echo 当前不支持类型$type
	echo python realtime/observe/pan.py do_manual $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/observe/pan.py do_manual $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
fi

