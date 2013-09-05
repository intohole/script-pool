#!/usr/bin/sh




split_num()
{
	_index=0
	num=$1
	echo $num
	while [ $num -gt 0 ]; do
		_n=$((num % 10))
		array[$_index]=$_n
		_index=$((_index + 1))
		num=$((num / 10))
	done
	echo $array
	return $array
}

while true; do
	echo $(split_num 301)
	sleep 10
done