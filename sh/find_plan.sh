#!/bin/bash
# usage sh/find_daily_report --day [day] a b c

day=`date +'%Y-%m-%d'`
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		break
		;;
	esac
	shift
done

greps=""
while [ -n "$1" ]
do 
	case "$1" in 
	*)
		if [ ${#greps} -eq 0 ]
		then
			greps=$1
		else
			greps="$greps,$1"
		fi
		;;
	esac
	shift
done


if [ ${#greps} -eq 0 ]
then
	echo find ../stk_daily/$day/plan/
	exit 0
fi

greps=(${greps//,/ })	
grep_cmd=''
for grep in ${greps[@]}
do
	if [ ${#grep_cmd} -eq 0 ]
	then
		grep_cmd="grep $grep"
	else
		grep_cmd="$grep_cmd|grep $grep"
	fi
	# not support more than 2 greps
	break
done

echo $grep_cmd
echo "find ../stk_daily/$day/plan/|$grep_cmd"

# fixme: not support more than 2 greps
# hard to fix...
find ../stk_daily/$day/plan/|$grep_cmd
