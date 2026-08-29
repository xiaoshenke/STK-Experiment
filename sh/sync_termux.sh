#!/bin/bash
# usage sh/sync_termux.sh [day] [dry_run]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)
dry_run=0

now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-dry_run | --dry_run | -dry-run | --dry-run)
		shift
		dry_run=$1
		;;
        *)
		# set value to type|front by now-flag
		if [ $now -eq 0 ]
		then
			day=$1
		else
			dry_run=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

echo python tool/sync_by_copyparty.py sync --day $day --dry_run $dry_run
python tool/sync_by_copyparty.py sync --day $day --dry_run $dry_run

