#!/bin/bash
# extract stock message from tonghuanshun wencai xls

debug=0
file=''
while [ -n "$1" ]
do 
	case "$1" in 
	-debug | --debug)
		shift
		debug=$1
		;;
	*)
		#break
		file=$1
		;;
	esac
	shift
done

#if [ $# -ne 1 ]
if [ ${#file} -eq 0 ]
then
	echo Usage:./xls.sh your-stock-xls-file
	exit 2
fi

count=0
if [ $debug -eq 1 ]
then
	cat $file | gawk 'BEGIN{RS="abcdefghi";FS="centerTitle"} {print $NF}' | gawk 'BEGIN{RS="<tr>|</tr>";FS="<td>|</td>"} {print $0}'|while read line
do
	echo $line
	if [[ $line =~ "<td>" ]]
	then
		echo 有效
		echo $line|gawk 'BEGIN{RS="<tr>|</tr>";FS="<td>|</td>"} {print $2}'
		declare -i count=$count+1
	fi
	echo $count
done
fi

count=1
cat $file | gawk 'BEGIN{RS="abcdefghi";FS="centerTitle"} {print $NF}' | gawk 'BEGIN{RS="<tr>|</tr>";FS="<td>|</td>"} {print $2}'|while read line
do
	if [[ $line =~ "SZ" ]] || [[ $line =~ "SH" ]] || [[ $line =~ "BJ" ]]
	then
		#stk=${line// }
		line=`eval echo $line`
		echo ${line:0:6}
		declare -i count=$count+1
	fi
	#echo $count
done > tmp.txt

lines=`cat tmp.txt`
echo $lines

rm -f tmp.txt
