#!/bin/bash

# Usage: sh/hand/template/generate_xls_hand.sh xls [type] [to-name] [--day]

# 定位: 用于根据@observe/hand/template下的模板文件生成hand文件
# 注意: 会做replace的操作

# copy from @sh/buyer/template/generate_xls_buyer.sh 

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)
now=0
xls=#
type='default'
to_name=#
force=0

# 标志位=1的话 会去刷新一下tracing observe
flush=0

if [ $# -lt 1 ]
then
	echo Usage: sh/hand/generate_xls_hand.sh xls [type] [to-name] [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-force | --force)
		shift
		force=$1
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

type=$(python engine/observe/hand/gene_cli.py may_change_xls_template_type $type)

cur_dir=/Users/wuxian/Desktop/STK-Experiment

to_file="/Users/wuxian/Desktop/stk_daily/$day/juben/$to_name.hand.properties"
file1="$cur_dir/engine/observe/hand/template/xx_$type.hand.properties"

#file2=$(python engine/caop/hands/template/file_cli.py try_find_template_file xx_$type --day $day)
#file3=$(python engine/observe/juben/template/file_cli.py try_find_template_file xx_$type --day $day)

find=""

# 检验file1是否已经存在
if [ -f "$to_file" ] || [ $force -eq 1 ]
then
	echo 想要生成的xls文件已经存在,但标志位force=1,因此会覆盖旧文件
elif [ -f "$to_file" ]
then
	echo 想要生成的xls文件已经存在,无须操作: $to_file
	exit 2
fi

# 如果observe/hand/template下存在对应的文件 那么赋值为find
if [ -f "$file1" ]
then
	find=$file1
#elif [[ $file2 != "0" ]]
#then
#	find=$file2
#elif [[ $file3 != "0" ]]
#then
#	find=$file3
#else
#	# 尝试file2 即caop/hands/template下的文件
#	# 调用一下python接口
#	# 如果寻找失败 file2='0'
#	file2=$(python engine/caop/hands/template/file_cli.py try_find_template_file xx_$type --day $day)
#	find=$file2
fi

if [ ${#find} -lt 2 ]
then
	#echo 不论是observe/hand/template下 还是caop/hands/template下 都找不到xx_$type 对应的模板文件,终止计算
	echo 找不到对应的模板文件 是否输入错误?
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

# 做一下校验replace kv逻辑
#check_replace=$(python engine/observe/juben/template/juben_cli.py check_xls_by_replace_kv $xls $find)

#if [[ $check_replace == "0" ]]
#then
#	echo python engine/observe/juben/template/juben_cli.py check_xls_by_replace_kv 返回0,说明输入的xls:$xls 和对应文件中的replace kv不匹配
#	exit 2
#fi

echo "复制文件 cp $find $to_file"
cp $find $to_file

echo "进行内容替换 sed -i 's/xx/$xls/g' $to_file"
sed -i "" "s/xx/$xls/g" $to_file

# 注意 下面的代码不容易理解 可以参考@https://chat.deepseek.com/a/chat/s/9c8f2246-9f35-4c17-9b64-28fddf06900e
# 在插入之前 先特殊处理一下from-file
from_file="$find"
if [[ "$from_file" == *"STK-Experiment"* ]]
then
	from_file="${from_file#*STK-Experiment/}"
fi

# 同样处理to_file
home="$HOME"
to_file2="${to_file/#$home/~}"

# 插入特定的字符串 使的我能清晰的知道这是一个手工文件 而不是模板
sed -i '' "5a\\
# 注意: 这是由模板生成的手工文件\\
# 模板: ${from_file}\\
# 存储: ${to_file2}\\
# xls: ${xls}\\
\\
" $to_file

# 插入字符串结束 

echo ""
echo "最终生成的文件内容如下:"
cat $to_file

echo ""
echo 手工打开文件:  open $to_file
echo ""


echo 可以继续启动对应的监听器: sh/hand/start_file_listener.sh $to_name

#cmd="sh/hand/generate_xls_hand.sh $xls $type --start_at $start_at --end_at $end_at"
#sh/log/log_to_operate.sh "$cmd" "GENE-XLS-BUYER"

# 最后 如果标志位=1,那么刷新一下tracing(因为efile文件修改了 自然应该进行一次新的刷新)
#if [ $flush -eq 1 ]
#then
#	echo 标志位flush=1,因此刷新一下tracing文件
#	sh/tracing/flush_one.sh efiles:$xls
#fi

