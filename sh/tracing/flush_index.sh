#!/bin/bash
# usage sh/tracing/flush_index.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

type=$( sh/tracing/tracing_list.sh --silent 1|grep index )

if [ ${#type} -eq 0 ]
then
	echo 当前不存在index类型的tracing node 
	exit 2
fi

echo python realtime/observe/tracing.py trigger  $type
python realtime/observe/tracing.py trigger $type
