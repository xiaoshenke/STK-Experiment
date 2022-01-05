#!/bin/bash
# usage sh/tail_realtime.sh [-day aaaa-bb-cc] idx

echo now support 1:market 2:zhz500 3:longhu 4:high 5:pool 6:xls 7:codes

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

if [ $# -ne 1 ]
then
	echo usage sh/less_observe_node.sh [-day aaaa-bb-cc] idx
fi

idx=$1
name=""
if [[ $idx == "1" ]]
then
	name="market"
elif [[ $idx == "2" ]]
then
	name="zhz500"
elif [[ $idx == "2" ]]
then
        name="zhz500"
elif [[ $idx == "3" ]]
then
	name="longhu"
elif [[ $idx == "4" ]]
then
	name="high"
elif [[ $idx == "5" ]]
then
	name="pool"
elif [[ $idx == "6" ]]
then
	name="xls"
elif [[ $idx == "7" ]]
then
	name="codes"
else
	name="codes"
fi

touch ../stk_daily/$day/"$name"_observe.log
echo less ../stk_daily/$day/"$name"_observe.log
less ../stk_daily/$day/"$name"_observe.log

