


if [ $# -lt 3 ]; then
	exit
fi


for file in $(ls $1);do
firstfilerow=$(wc -l $1$file | awk '{print $1}') 
secoundfilerow=$(wc -l $2$file | awk '{print $1}')
echo $firstfilerow
echo $secoundfilerow
diffrow=$((firstfilerow - secoundfilerow))
if [ $diffrow -ge 0 ]; then
	filename="$3$file.diff"
	echo $diffrow
	tail -n $diffrow $1$file> $filename
else
	filename="$3$file.diff"
	tail -n diffrow $2$file> $filename
fi

done