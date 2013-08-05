#!/bin/sh

if [ $# -lt 2];then
    exit
fi

if [ ! -f $1 ];then
    exit
fi

if [ ! -f $2 ];then
    exit
fi

for i in $(cat $1);do
    data=$(cat $2 | grep $i)
    if [ ! -z $data ];then
       echo  $i>> /home/lixuze/crontab/motor-client/logs/tmp2
    fi
done
