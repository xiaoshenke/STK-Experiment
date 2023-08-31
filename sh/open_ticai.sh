#!/bin/bash
# Usage: ./open_ticai.sh code

if [ $# -ne 1 ]
then
	echo Usage:./open_ticai.sh code
	exit 2
fi

code=$1
if [[ ${code:0:2} == "60" ]] || [[ ${code:0:2} == "68" ]]
then
	code=SH$code
else
	code=SZ$code
fi

url="https://emweb.securities.eastmoney.com/pc_hsf10/pages/index.html?type=web&code=$code&color=b#/hxtc"
echo $url
echo going to open url:$url ...
open $url

