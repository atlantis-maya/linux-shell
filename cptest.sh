#!/bin/bash
#########
# copy file
#
#######
echo $@
for dir in $@ ;do
if [ "$dir"x == "$1"x ] ;then
  continue
else
cp  -RP $dir $1
fi
done
