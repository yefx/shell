#!/bin/bash
i=`date "+%M"`
while(($i<60))
do
   if (($i%5 != 0))
     then
     echo $i
     break
   fi
   i=`date "+%M"`
done
