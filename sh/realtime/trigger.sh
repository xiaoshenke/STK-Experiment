#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

comps=''

if [ $# -lt 1 ]
then
	echo Usage: sh/realtime/trigger.sh ABC
	exit 2
fi

comps=$1

function do_trigger {
	type=$1
	
	if [[ $type == 'code_types' ]] || [[ $type == 'codetypes' ]]
	then
		echo python realtime/observe/code_types.py trigger
		python realtime/observe/code_types.py trigger
	else
		echo python realtime/observe/$type.py trigger
		python realtime/observe/$type.py trigger
	fi

}

comps=(${comps//,/ })
for comp in ${comps[@]}
do
	do_trigger $comp
done


