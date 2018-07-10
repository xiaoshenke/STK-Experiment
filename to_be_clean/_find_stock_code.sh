#!/bin/bash 

# Usage: ./find_stock_code.sh your-code-name

if [ $# -ne 1 ]
then
	echo Usage:./find_stock_code.sh your-code-name
	exit2
fi

code=$(python cli.py get_code_by_name_exact $1)


if [ ${#code} -eq 0 ]
then
	echo fail to find code of name:$1
	exit 2
fi

echo $code


