#!/bin/bash
source env_set.cfg
echo "1 重复率:"
echo "2 重复率:1.0%"
echo "3 爬取的微博数目"
read choice
if [ $choice -eq 2 ];then
    reg="重复率: 100"
elif [ $choice -eq 3 ];then
    reg="爬取微薄数："
else
    reg="重复率:"
fi
count=0
for File in $logpath/*;do
    if [ $choice -ne 3 ];then
        ncount=$(cat $File | grep "$reg" | wc -l)
        count=$((count + ncount))
    else
       cat $File | grep "爬取微薄数:" | awk '{FS=":|,"} {if($5<0) $5=-$5} {if($7<0)$7=-$7} {total=$5-$7} {if(total>0) print total}'>tmp.tmp
       sum=0
       for l in $(cat tmp.tmp);do
           sum=$((sum + l))
       done 
       count=$((count+sum))
       rm tmp.tmp
    fi
   done
echo $count
