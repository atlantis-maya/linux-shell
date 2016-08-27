#!/bin/bash
#判断文件的编码
function ifutf8()
{
	$1
for shname in `find . -type f -name "*.sh"`
do 
    name=`echo "$shname" | awk -F/ '{print $2}'`
	echo $name
	encoding= file -i $name |awk -F ';' '{print $2}'
	echo $encoding
done
}
ifutf8 $1
