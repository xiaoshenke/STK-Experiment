#!/bin/bash
# extract stock message from tonghuanshun wencai xls

if [ $# -ne 1 ]
then
	echo Usage:./xls.sh your-stock-xls-file
	exit 2
fi

cat $1 | gawk 'BEGIN{RS="abcdefghi";FS="centerTitle"} {print $NF}' | gawk 'BEGIN{RS="<tr>|</tr>";FS="<td>|</td>"} {print $2}'|while read line
do
	if [[ $line =~ "SZ" ]] || [[ $line =~ "SH" ]]
	then
		stk=${line// }
		echo ${line:0:6}
	fi
done > tmp.txt

lines=`cat tmp.txt`
echo $lines

rm -f tmp.txt
