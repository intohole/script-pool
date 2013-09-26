#!/bin/bash
#coder:intoblack


TRUE=1
FALSE=0
WRONG=-1

len()
{
	if [  $# -lt 1 ]; then
		return 0
	fi
	_len=$(expr length $1)
	return $_len
}


isEmpty()
{
	len $1
	_l=$?
	if [ $_l -eq 0 ]; then
		return $TRUE
	else
		return $FALSE
	fi
}


with()
{
	if [ $# -lt 2 ]; then
		return $FALSE
	fi
	_same=$(echo "$1" | grep "^$2" )
	if [ "$_same" = "" ]; then
		return $FALSE
	else
		return $TRUE
	fi
}


endwith()
{
	if [ $# -lt 2 ]; then
		return $FALSE
	fi
	_same=$(echo "$1" | grep "$2$" )
	if [ "$_same" = "" ]; then
		return $FALSE
	else
		return $TRUE
	fi
}


split()
{
	
}




endwith "233" "3" 
a=$?
echo $a



