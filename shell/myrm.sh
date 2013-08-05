#/bin/sh

if [ $# -lt 1 ];then 
    exit
fi
fix_name=$(date '+%Y%m%d%H%M%S') 
trash_forlder="/home/lixuze/.mytrash"
if [ ! -d "$trash_forlder" ];then
    mkdir $trash_forlder
fi

for r_file in $@;do
   if [ -f $r_file ];then
       mv $r_file $trash_forlder"/"$r_file"_"$fix_name
   elif [ -d $r_file ];then
       mv -r $r_file $trash_forlder"/"$r_file"_"$fix_name
   fi
done

