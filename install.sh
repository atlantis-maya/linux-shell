#!/bin/bash
########
#habout if install soft query
#if not install soft
#will retunr false
#else return true
######
function installsoft()
{
      result=$[`rpm -q $1`]
      echo $result
}

installsoft $1


