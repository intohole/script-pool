#/bin/sh
if [ $# -ne 0 ];then
    cm="mota@mota$1:/home/mota/TokenUpdateSQL/logs/tokenlog.dat ./tmp.tmp"
    scp $cm
    cat ./tmp.tmp
    rm ./tmp.tmp 
fi
