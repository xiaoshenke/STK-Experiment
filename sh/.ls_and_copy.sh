#!/bin/bash
# Usage ./ls_and_copy.sh your-code

is_week=0

while [ -n "$1" ]
do
        case "$1" in
        -w)
		is_week=1	
		;;
        *)
                break
                ;;
        esac
	shift
done

if [ $# -ne 1 ]
then
        echo Usage: ./ls_and_copy.sh your-code
        exit 2
fi

if [ $is_week -eq 0 ]
then
	ls |grep $1 |xargs sh sh/copy_to.sh
else
	ls |grep $1 |grep w_ |xargs sh sh/copy_to.sh
fi

