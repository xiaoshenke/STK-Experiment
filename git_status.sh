#!/bin/bash
# crypt version of git status
# Usage: ./git_status.sh

py_list=`ls *.py`

python crypt_all.py

git status |while read word;do
if [[ $word =~ "deleted" ]] || [[ $word =~ "modified" ]] 
then
	crypted=${word##* }
	# ugly way...
	origin=$(python crypt_all.py get_origin_name_from_list "${py_list[@]}" $crypted)
	if [ ${#origin[@]} -gt 0 ] && [[ ! $word =~ ".py" ]]
	then
		echo ${word%% *} $origin
	else
		echo $word
	fi
else
	echo $word	
fi
done

sh uncrpyt.sh

