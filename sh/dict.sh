#!/bash/sh


usage="请输入一个查询单词"

if [ $# -lt 1 ]; then
	echo $usage 
	exit
fi

dict_html=$(curl  http://dict.cn/$1 | grep 基本)
