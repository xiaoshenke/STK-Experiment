#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/config/write_manual.sh abc
	exit 2
fi

sh/config/write_pool.sh --force 1 manual $1
