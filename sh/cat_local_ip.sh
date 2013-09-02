#!/bin/sh
#function look local ip
#idea get info from 
#split ip
echo $( curl http://homer.meso.com/remoteip.php |  grep meta | awk -F '//' '{print $3}' | awk -F '\"' '{print $1}')