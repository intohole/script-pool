#!/bin/sh



get_file_line()
{
	_sum=$(wc -l $1 | tail -n 1 | awk '{print $1}')
	return $_sum
}


