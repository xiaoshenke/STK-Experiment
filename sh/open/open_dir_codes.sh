#!/bin/bash
# Usage: sh/open_dir_codes.sh dir [code1,code2,...]

if [ $# -eq 0 ]
then
	echo Usage: sh/open_dir_codes.sh dir [code1,code2,...]
	exit 2
fi

dir=$1
has_codes=0
codes=''
if [ $# -eq 2 ]
then
	has_codes=1
	codes=$2
fi

# if no codes,just open dir/*.jpg
if [ $has_codes -eq 0 ]
then
	#echo open $dir/*.jpg
	open $dir/*.jpg
	exit 0
fi

codes=(${codes//,/ })
# gather all open command string
cmd=''
for code in ${codes[@]}
do
	if [ -f "$dir/$code.d.jpg" ]
	then
		cmd="$cmd $dir/$code.d.jpg $dir/$code.f.jpg"
	fi
done

open $cmd
