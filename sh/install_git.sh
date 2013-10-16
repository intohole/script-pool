#!/bin/sh



code_path="/home/xxxx/code/"
excute_path="/home/xxxx/usr/"
project_name="circus"
git_path="git@IP:xxxx/circus.git"
sh_path=$(pwd)
project_path=$code_path$project_name

if [ ! -d $project_path ];then
	cd $code_path
	git clone $git_path
	cd $project_path
else
	cd $project_path
	git pull origin master
fi
mvn clean
mvn package
if [ $? -ne 0 ]; then
	echo "工程编译错误"
	exit 
fi
if [ -d $project_path"/target" ]; then
	cd $project_path"/target"
	if [ ! -d $excute_path$project_name ]; then
		mkdir $excute_path$project_name	
	fi
	cp -r lib/ *.jar $excute_path$project_name
fi

if [ -d $sh_path"/bin"]; then
	cp $sh_path"/bin" $excute_path$project_name
fi










