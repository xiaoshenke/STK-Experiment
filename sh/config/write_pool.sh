#!/bin/bash

key=''
val=''
force=0

now=0
while [ -n "$1" ]
do 
        case "$1" in 
	-force | --force | --froce)
		shift
		force=$1
		;;	
        -help | --help)
		echo usage sh/config/write_pool.sh key val
                exit 1
                ;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			key=$1
		else
			val=$1
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

echo python realtime/properties_cli.py write_pool $key $val --force $force
python realtime/properties_cli.py write_pool $key $val --force $force

