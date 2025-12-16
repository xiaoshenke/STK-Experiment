#!/bin/bash
# Usage: sh/realtime/set_running_mode.sh [mode]

mode='default'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo python realtime/properties_cli.py write_running_mode $mode
python realtime/properties_cli.py write_running_mode $mode

