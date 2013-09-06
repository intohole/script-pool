#!/bin/bash



echo "count down!"

num_0=(0 1 0 0 1 0 0 1 0 0 1 0 0 1 0)

split_num()
{
	ret_num=""
	if [ $# -ge 1 ]; then
		_num=$1
		while [ $_num -ne 0 ]; do
			_mod=$(( _num % 10 ))
			_num=$(( _num / 10 ))
			ret_num=$_mod" "$ret_num
		done
	fi
	echo $ret_num
	return $ret_num
}

draw_num()
{
	
	for i in ${num_0[@]};do
		echo $i
	done
}


while true
do
	# num=$(split_num 102)
	# num_len=$(( (${#num} +1) / 2)) # 1 0 2 = (n - 1) * backspace + n *  char 
	# for i in $num;do
	# 	echo $i
	# 
	draw_num
	sleep 10
done
