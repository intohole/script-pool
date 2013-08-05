#!/bin/bash
pid=$(ps -ef | awk '{print $2":"$8}'|grep $1 | awk -F ":" '{print $1}')
if [ $pid -gt 1 ]
then
kill $pid
else
echo "没有找到你输入的名称的进程"
fi
