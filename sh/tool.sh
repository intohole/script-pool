#!/bin/sh



get_file_line()
{
	_sum=$(wc -l $1 | tail -n 1 | awk '{print $1}')
	return $_sum
}


rm_zero_line()
{
	for file in $( wc -l | awk '{(if($1==0))print$2}');do
		if [ -f $file ];then
			rm $file
		fi
}