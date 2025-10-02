#!/bin/bash

# 当前对于文件的依赖过重了 因此新增本命令: 将文件进行保存 并且同时清空原文件
# 具体的执行过程:
# 1, 杀死原先的juben observe进程(因为这个进程会起juben listener)
# 2, save-to + clean
# 3, 启动juben observe

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#
force=0
now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-juben | --juben)
		shift
		juben=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/save_to.sh juben --day abc [--force xyz]
		exit 2
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			juben=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo ""
echo 执行剧本文件的save-to + clean操作...
echo "#### 先杀死当前系统中存在的juben observe进程"
echo sh/juben/kill_juben_observe.sh ...
sh/juben/kill_juben_observe.sh  

echo ""
echo "#### 再执行save to操作"
echo python engine/observe/juben/config_cli.py save_to --day $day $juben --force $force
python engine/observe/juben/config_cli.py save_to --day $day $juben --force $force

echo ""
echo "#### 再执行clean操作"
file=/Users/wuxian/Desktop/stk_daily/$day/template/default.juben.properties

echo "rm $file"
rm $file

sh/juben/open_config.sh --day $day

echo ""
echo "#### 最后,启动juben observe"
echo sh/juben/start_juben_observe.sh 
sh/juben/start_juben_observe.sh 

echo ""
echo 结束!
echo ""

