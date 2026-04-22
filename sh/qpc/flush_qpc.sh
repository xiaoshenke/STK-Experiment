#!/bin/bash

key=''
val=''
force=0
reason=#
flush=0
mode='now'
day=`date +'%Y-%m-%d'`

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
	-force | --force | --froce)
		shift
		force=$1
		;;	
	-flush | --flush)
		shift
		flush=$1
		;;	
	-reason | --reason | -desc | --desc)
		shift
		reason=$1
		;;
        -help | --help)
		echo usage sh/qpc/flush_qpc.sh val
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			val=$1
		elif [ $now -eq 1 ]
		then
			reason=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ ${#val} -eq 0 ]
then
	echo val empty.
	echo usage sh/qpc/add_qpc.sh val
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/qpc_cli.py fast_flush --day $day $val --force $force --reason $reason --flush $flush --mode $mode
python realtime/qpc_cli.py fast_flush --day $day $val --force $force --reason $reason --flush $flush --mode $mode

