#!/bin/bash

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/add_pull_codes.sh code-type [--day ] [--reason ]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		desc=$1
		;;
	-group | --group)
		shift
		group=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then
			desc=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/codes/add_codes.sh $code_type pull --day $day --reason $desc
sh/codes/add_codes.sh $code_type pull --day $day --reason $desc

