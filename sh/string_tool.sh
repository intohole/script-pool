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


startwith()
{
	len $2
	len $1
	_l=$?
	if [ $_l -eq; then
		#statements
	fi

}





isempty 
a=$?
echo $a


