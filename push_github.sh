#!/bin/bash

if [ $# -ne 1 ] 
then
	echo Usage:./push_github commit-message
	exit 2
fi

python crypt_all.py

git add .
git commit -m $*
git push origin master


