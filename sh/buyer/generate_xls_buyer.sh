#!/bin/bash

# Usage: sh/buyer/generate_xls_buyer.sh xls [type] [to-name] [--day]
# 定位: 用于根据@observe/buyer/template下的模板文件生成buyer文件
# 注意: 会做replace的操作

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
xls=#
type='default'
to_name=#
force=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/generate_xls_buyer.sh xls [type] [to-name] [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
			to_name=$1
		elif [ $now -eq 1 ]
		then
			type=$1
		elif [ $now -eq 2 ]
		then
			to_name=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment

to_file="/Users/wuxian/Desktop/stk_daily/$day/buyer/$to_name.properties"
file1="$cur_dir/engine/observe/buyer/template/xx_$type.buyer.properties"
file2=$(python engine/caop/buyers/template/file_cli.py try_find_template_file xx_$type --day $day)
file3=$(python engine/observe/juben/template/file_cli.py try_find_template_file xx_$type --day $day)

find=""

# 检验file1是否已经存在
if [ -f "$to_file" ]
then
	echo 想要生成的xls文件已经存在,无须操作: $to_file
	exit 2
fi

# 如果observe/buyer/template下存在对应的文件 那么赋值为find
if [ -f "$file1" ]
then
	find=$file1
elif [[ $file2 != "0" ]]
then
	find=$file2
elif [[ $file3 != "0" ]]
then
	find=$file3
else
	# 尝试file2 即caop/buyers/template下的文件
	# 调用一下python接口
	# 如果寻找失败 file2='0'
	file2=$(python engine/caop/buyers/template/file_cli.py try_find_template_file xx_$type --day $day)
	find=$file2
fi

if [ ${#find} -lt 2 ]
then
	echo 不论是observe/buyer/template下 还是caop/buyers/template下 都找不到xx_$type 对应的模板文件,终止计算
	exit 2
fi

#if [ ! -f "$file1" ]
#then
#	echo 模板剧本文件: $file1 不存在,是否输入错误?
#	exit 2
#fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

# 做一下校验replace kv逻辑
check_replace=$(python engine/observe/juben/template/juben_cli.py check_xls_by_replace_kv $xls $find)

if [[ $check_replace == "0" ]]
then
	echo python engine/observe/juben/template/juben_cli.py check_xls_by_replace_kv 返回0,说明输入的xls:$xls 和对应文件中的replace kv不匹配
	exit 2
fi

echo "复制文件 cp $find $to_file"
cp $find $to_file

echo "进行内容替换 sed -i 's/xx/$xls/g' $to_file"
sed -i "" "s/xx/$xls/g" $to_file

echo ""
echo "最终生成的文件内容如下:"
cat $to_file

echo ""
echo 手工打开文件:  open $to_file
echo ""

