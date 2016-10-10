#!/bin/bash
date
if who|grep "^$1"
then
write $1<<!
!
echo "hello!"
fi

