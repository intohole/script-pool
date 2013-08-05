


path1=$1
path2=$2

for i in $( ls $path1);do
    cat $path1/$i >> $path2/$i
done