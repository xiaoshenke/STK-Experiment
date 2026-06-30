#!/bin/bash

path=`pwd`

if [ $# -lt 1 ]
then
	echo Usage: sh/tips/trend/qp_trend.sh codes
	exit 2
fi

codes=$1

echo sh/tips/run_xls_template.sh $codes qp_trend_overall
sh/tips/run_xls_template.sh $codes qp_trend_overall


