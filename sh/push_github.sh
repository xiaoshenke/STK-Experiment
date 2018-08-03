#!/bin/bash

if [ $# -ne 1 ] 
then
	echo Usage:./push_github commit-message
	exit 2
fi

python crypt_all.py

message=$*

git add .
git commit -m "${message[*]}"
git push origin master

sh sh/uncrpyt.sh
