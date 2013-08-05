#!/bin/bash

clear

i=1
while (($1<100))
    do
        if (( $i%3 -eq 0 ))
        then
            echo "$i"
        fi
        i=$(($i+1))
    done
           
