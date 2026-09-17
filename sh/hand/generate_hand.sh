#!/bin/bash

# Usage: sh/hand/generate_hand.sh type [to-name] [--day]   -> 语义:根据样本字符串生成文件 默认生成的名字和样本名字相同
# 定位: 用于根据@observe/hand/template下的模板文件生成hand文件

# copy from @sh/buyer/template/generate_buyer.sh

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
	echo Usage: sh/hand/generate_hand.sh type [to-name] [--day]
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
			type=$1
			to_name=$1
		elif [ $now -eq 1 ]
		then
			to_name=$1
		elif [ $now -eq 2 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cur_dir=/Users/wuxian/Desktop/STK-Experiment

to_file="/Users/wuxian/Desktop/stk_daily/$day/juben/$to_name.hand.properties"
file1="$cur_dir/engine/observe/hand/template/$type.hand.properties"

# 检验file1是否已经存在 且force标志位 != 1
if [ -f "$to_file" ] && [ $force -ne 1 ]
then
	echo 想要生成的hand文件已经存在,无须操作: $to_file
	exit 2
fi

if [ ! -f "$file1" ]
then
	echo 模板剧本文件: $file1 不存在,是否输入错误?
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo "复制文件 cp $file1 $to_file"
cp $file1 $to_file

# 注意 下面的代码不容易理解 可以参考@https://chat.deepseek.com/a/chat/s/9c8f2246-9f35-4c17-9b64-28fddf06900e
# 在插入之前 先特殊处理一下from-file
from_file="$file1"
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
\\
" $to_file

# 插入字符串结束 

echo ""
echo "最终生成的文件内容如下:"
cat $to_file

echo ""
echo 手工打开文件:  open $to_file

echo 可以继续启动对应的监听器: sh/hand/start_file_listener.sh $to_name

# 落日志
#cmd="sh/hand/generate_hand.sh $type $to_name"
#sh/log/log_to_operate.sh "$cmd" "GENERATE_HAND"

open $to_file
