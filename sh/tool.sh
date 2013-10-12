#!/bin/sh


#得到文件行数
get_file_line()
{
	_sum=$(wc -l $1 | tail -n 1 | awk '{print $1}')
	return $_sum
}

#删除没有行数的空文件
rm_zero_line()
{
	for file in $( wc -l * | awk '{if($1==0) print $2}');do
		if [ -f $file ];then
			rm $file
		fi
	done
}


read_file_line()
{
      if [ ! -f $1 ] ; then
      	
          return 
      fi
      while read -r line;do  $line ; done < $1
}



read_file_line /home/lixuze/Script/sh/cat_newestfile.sh
echo $?




