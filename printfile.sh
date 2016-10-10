#!/bin/bash
for dirname in $@ ;do
if [ "$dirname"x == "$1"x ] ; then
    continue
else
path=$1
file=$dirname
pathfile=${path}"/"${file}
cat $pathfile
fi
done
