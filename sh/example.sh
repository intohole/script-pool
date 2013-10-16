




read_file_by_line()
{
	if [ $# -lt 1 ]; then
		return
	fi
	if [  -f $1 ]; then
		while read line; do
			echo $line
		done < $1
	fi
}




read_file_by_line "run_java_userinfo.sh"
