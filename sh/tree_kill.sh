#!/bin/sh

if [ $# -ne 1 ]
then
    echo -e "\033[;36mUsage:\033[0m" "\033[;32mkillall\033[0m" "\033[;33mPID\033[0m"
    exit
else
    root=$1
fi

function treekill()
{
    local father=$1

    # children
    childs=(`ps -ef | awk -v father=$father 'BEGIN{ ORS=" "; } $3==father{ print $2; }'`)
    if [ ${#childs[@]} -ne 0 ]
    then
        for child in ${childs[*]}
        do
            treekill $child
        done
    fi
    # father 
    echo -e "\033[;32mkill\033[0m" "\033[;36mpid\033[0m" "\033[;33m$father\033[0m"
    kill -9 $father
}

treekill $root