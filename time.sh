#!/bin/bash
Time=`date +%M`
i=`echo ${Time} | awk '{printf("%d\n",$1)}'`
while(($i<60))
do
   if (($i%5 != 0))
     then
     echo $i
     date "+%Y%m%d"
     ls /etc/nginx
     break
   fi
   i=`date "+%M"`
done
