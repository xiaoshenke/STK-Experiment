#!/bin/bash
# crypt version of git status
# Usage: ./git_status.sh

# update 2026-05-25: 出现py-list文件过多导致的奇怪bug 因此这里加上grep -v scheduler 用于减少大量文件来规避这个bug
# 以后再出现这种sh/git-status.sh的bug 大部分时间都是这个原因引起的
py_list=`find *|grep .py|grep -v subs_candi.py|grep -v stocks|grep -v tuxing|grep -v scheduler|grep -v "/[.]"|grep -v pyc|grep -v __init__`

#echo $py_list
#[@]
#echo ${#py_list[*]}

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
		#echo 2
		#echo $crypted
		origin=$(python $CRYPT_ALL_FILE get_origin_name_from_list "${py_list[@]}" $crypted)
		#echo 3
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

