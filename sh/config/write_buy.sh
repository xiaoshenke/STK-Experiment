#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/config/write_buy.sh abc
	exit 2
fi

sh/config/write_pool.sh --force 1 buy $1
