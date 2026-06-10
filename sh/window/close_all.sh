#!/bin/bash

do_log=0
force=0

if [ $# -eq 1 ]
then
	force=$1
fi

sh/close_codes.sh
sh/close_txt.sh --force $force
#sh/close_sublime.sh 

if [ $do_log -eq 0 ]
then
	exit 2
fi

cmd="sh/close_all.sh"
sh/log/log_to_operate.sh "$cmd" "CLOSE_ALL"
