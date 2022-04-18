#!/bin/bash
# crypt version of git status
# Usage: ./git_status.sh

py_list=`find *|grep .py|grep -v "/[.]"|grep -v pyc`

#echo $py_list[@]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

CRYPT_ALL_FILE="util/crypt/crypt_all.py"

python $CRYPT_ALL_FILE

before_track=1
function deal_word {
	word=$@
	if [[ $word =~ "Untracked" ]]
	then
		before_track=0
	fi
	if [ $before_track -eq 1 ]
	then
		deal_before_track ${word[*]}
	else
		deal_after_track ${word[*]}
	fi
}

function deal_before_track {
	word=$@
	if [[ $word =~ "deleted" ]] || [[ $word =~ "modified" ]]
	then
		crypted=${word##* }
		origin=$(python $CRYPT_ALL_FILE get_origin_name_from_list "${py_list[@]}" $crypted)
		if [ ${#origin} -gt 1 ] && [[ ! $word =~ ".py" ]]
		then
			echo ${word%% *} $origin
		else
			echo ${word[*]}
		fi
	else
		echo $word
	fi
}

function deal_after_track {
	word=$@
	crypted=$word
	origin=$(python $CRYPT_ALL_FILE get_origin_name_from_list "${py_list[@]}" "$crypted")
	if [ ${#origin} -gt 1 ] && [[ ! $word =~ ".py" ]]
	then
		echo $origin
	else
		echo ${word[*]}
	fi
}

git status |while read word;do
deal_word ${word[*]}
done

sh sh/uncrpyt.sh

