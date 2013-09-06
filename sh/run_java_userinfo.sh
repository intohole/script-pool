#!/bin/sh


javafilepath=$1
userfilepath=$2
cat_save_file_path=$3
for i in $(ls $userfilepath);do
	while [ "$(jps -l | grep sinauserinfo)" != "" ]; do
		clear
		echo $(date)"     sinauserinfo..... working 文件总数："$(ls $cat_save_file_path | wc -l)
		sleep 50
	done
	userlist=$userfilepath$i
	nohup java -jar $javafilepath  $userlist $cat_save_file_path >> log.dat &
	echo "$userfilepath$i....working"
done
