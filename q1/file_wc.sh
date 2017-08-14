#!/bin/sh 
 # Shell script to find out all the files under a subdirectory and its subdirectories. 
 # This also takes into consideration those files 
 # or directories which have spaces or newlines in their names 

DIR="."

function list_files()
{
 if !(test -d "$1") 
 then echo "Not a directory"; return;
fi

cd "$1"
 for i in *
 do
 if test -d "$i" #if directory
 then 
 list_files "$i" #recursively list files
cd ..
 else
     wc -w $PWD/"$i"   #Counts the words in each file
fi

 done
}

for i in $*
do
 DIR=$1 
 list_files $DIR
 shift 1 #To read next directory/file name
done
