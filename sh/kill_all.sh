#!/bin/sh
#循环所有列表中 查看qq进程 不包含有 grep使用的进程 进程号在第二列 awk 执行  
if [ $# -lt 1 ];then
	echo "sh kill_all [thread name]"
fi

for i in $(ps aux | grep $1 | grep -v "grep" | grep -v $0 | awk {'print $2'});do echo "kill"$i ;kill -9 $i; echo "kill"$i" state"$?; done
