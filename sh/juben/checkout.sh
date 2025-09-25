#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-juben | --juben)
		shift
		juben=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/checkout.sh juben --day abc
		exit 2
		;;
	*)
		juben=$1
		;;
	esac
	shift
done

echo python engine/observe/juben/config_cli.py checkout --day $day $juben
python engine/observe/juben/config_cli.py checkout --day $day $juben

echo 
echo 考虑把所有的buyer配置也进行checkout?     
echo sh/manual/buyer_cli.sh checkout $juben --day $day

