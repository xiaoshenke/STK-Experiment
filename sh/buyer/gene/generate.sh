#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/gene/generate.sh xx [action]
	exit 2
fi

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
name=#
now=0
mode='now'
action='print'
print_run_msg=0
flush=0
force=0
hq='0'
risk=-1
type='0'
rank=-1

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
	-flush | --flush)
		shift
		flush=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-print_run_msg | --print_run_msg)
		shift
		print_run_msg=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		desc=$1
		;;
	-name | --name)
		shift
		name=$1
		;;
	-type | --type)
		shift
		type=$1
		;;
	-risk | --risk)
		shift
		risk=$1
		;;
	-rank | --rank)
		shift
		rank=$1
		;;
	-hq | --hq)
		shift
		hq=$1
		;;
	*)
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then 
			action=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/observe/buyer/gene_cli.py generate "$code_type" --action $action --day $day --mode $mode --risk $risk --hq $hq --type $type --rank $rank

python engine/observe/buyer/gene_cli.py generate "$code_type" --action $action --day $day --mode $mode --risk $risk --hq $hq --type $type --rank $rank
