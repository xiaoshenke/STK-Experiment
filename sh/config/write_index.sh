#!/bin/bash

if [ $# -lt 1 ]
then
	echo 当前未输入有效的index列表 读取一下当前的配置 
	sh/config/read_index.sh

	echo Usage: sh/config/write_index.sh abc
	exit 2
fi

sh/config/write_pool.sh --force 1 index $1
