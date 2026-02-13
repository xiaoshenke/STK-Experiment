#!/bin/bash

sh/close_codes.sh
sh/close_txt.sh
#sh/close_sublime.sh 

cmd="sh/close_all.sh"
sh/log/log_to_operate.sh "$cmd" "CLOSE_ALL"
