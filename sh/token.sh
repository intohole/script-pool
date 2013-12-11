#!/bin/sh


_choice=0
log_path="/home/lixuze/tokenlogmota.dat"
reload()
{
    scp mota@mota4:/home/mota/usr/motor-server/logs/tokenlog.dat $log_path
}

catlog()
{
   cat $log_path
}

rmlog()
{
   rm $log_path
}


catiplimit()
{
    cat $log_path  | grep "因为ip限制"
}


catwork()
{
   cat $log_path | grep "更新失败 # 50 #"
}

catworksum()
{
    sum=$(cat $logpath | grep "更新失败 # 50 #" | wc -l)
    print $sum
    echo $((sum * 50))
}

catallwork()
{
  cat $log_path | grep "更新失败 #"
}

catclientrun()
{
  echo "输入iｐ地址"
  read ip
  cat $log_path | grep "192.168.70."$ip
}

catdata()
{
    cat $log_path | grep "数据库中读取"
}

catlogwithdate()
{
    read td
    cat $log_path | grep $td
}


print()
{
echo "rd reload"
echo "rm rmlog"
echo "ip catiplimit"
echo "cw catallwork"
echo "cf catfinishwork"
echo "cc catclientrun"
echo "cl catlog"
echo "cd catdata"
echo "cs catworksum"
echo "q exit"
}
Control()
{
  while :
  do
  print
  read choice
  print $choice
  case $choice in
  "rd" )
    reload
    ;;
  "rm" )
    rmlog
    ;;
  "ip" )
   catiplimit
   ;;
  "cf")
    catwork
    ;;
  "cc")
    catclientrun
    ;;
  "cl")
    catlog
    ;;
  "cd")
    catdata
    ;;
  "cs")
    catworksum
    ;;
  "q")
    clear
    rmlog
    exit
    ;;  
    *)
    catallwork
    ;;
  esac
  echo "按任意键...."
  read wait
  clear
  done
}


rmlog
reload
Control
