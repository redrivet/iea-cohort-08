#!/bin/bash
#echo "Enter your filename"
#read filename
filename="$1"
#test -z $filename
if [ -z $filename ]; #test legnth of string is zero
#if [ $filename -eq 0 ];##
then
	echo "no input file"
else
    if [ -f "$filename" ]; 
    then
        echo ""; 
     else
	 echo "file is not found"    
 	 fi
fi		

