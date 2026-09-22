#!/bin/bash

# Usage: sh/hand/settings/not_open.sh xx [0|1]

if [ $# -lt 1 ]
then
	echo "Usage: sh/hand/settings/not_open.sh xx [0|1]"
	exit 2
fi

key=''
val=''
day=#
force=0
desc=#
mode=#
now=0
val="1"

while [ -n "$1" ]
do 
        case "$1" in 
	-force | --force | --froce)
		shift
		force=$1
		;;	
	-day | --day)
		shift
		day=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-reason | --reason | -desc | --desc | -detail | --detail)
		shift
		desc=$1
		;;
        -help | --help)
		echo usage sh/config/write_pool.sh key val [--day] [--force] [--reason|desc]
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			key=$1
		elif [ $now -eq 1 ]
		then
			val=$1
		elif [ $now -eq 2 ]
		then
			day=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [ ${#key} -eq 0 ]
then
	echo key empty.
	echo usage sh/config/write_pool.sh key val
	exit 1
fi

if [ ${#val} -eq 0 ]
then
	echo val empty.
	echo usage sh/config/write_pool.sh key val
	exit 1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

key="hand.not_open-$key"
# 注意替换一下=
key="${key//alias=/alias.}"

echo python realtime/properties_cli.py write_key_val $key $val 
python realtime/properties_cli.py write_key_val $key $val 

