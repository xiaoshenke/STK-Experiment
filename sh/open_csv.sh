#!/bin/bash
# Usage: sh/open_csv.sh [file]

file='tmp.csv'
if [ $# -eq 1 ]
then
	file=$1
fi

echo python inn_strategy/ana_cli.py open_csv $file
python inn_strategy/ana_cli.py open_csv $file
