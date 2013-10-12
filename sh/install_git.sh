#!/bin/sh



base_path="/home/xxxx/code/"
dest_path="/home/xxxx/usr/"
project_name="circus"
git_path="git@IP:xxxx/circus.git"
project_path=$base_path$project_name

if [ ! -d $project_path ];then
	cd $base_path
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
	if [ ! -d $dest_path$project_name ]; then
		mkdir $dest_path$project_name	
	fi
	cp -r lib/ *.jar $dest_path$project_name
fi







