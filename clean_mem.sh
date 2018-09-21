#!/bin/bash

used=`free -m | awk 'NR==2' | awk '{print $3}'`
free=`free -m | awk 'NR==2' | awk '{print $4}'`

if [ $free -le 51534 ] ; then
       echo -e "\n`date`:">>/opt/backup/Mem.log
       echo -e "________________________________">>/opt/backup/Mem.log
       echo -e "Before Cleanup:">>/opt/backup/Mem.log
       echo "Warn: Memory usage | [Use﻾Z${used}MB][Free﻾Z${free}MB]" >> /opt/backup/Mem.log
       free -b >> /opt/backup/Mem.log
       free -g >> /opt/backup/Mem.log
       echo -e "_______">>/opt/backup/Mem.log

       sync;sync;echo 3 > /proc/sys/vm/drop_caches

       echo -e "After Cleanup:">>/opt/backup/Mem.log
       free -b >> /opt/backup/Mem.log
       free -g >> /opt/backup/Mem.log
       echo -e "MemCleaned" >>/opt/backup/Mem.log
else
       echo -e "\n`date`:">>/opt/backup/Mem.log
       echo -e "_____OK_______">>/opt/backup/Mem.log
       free -b >> /opt/backup/Mem.log
       free -m >> /opt/backup/Mem.log

#       echo "Normal: | [Use﻾Z${used}MB][Free﻾Z${free}MB]" >> /opt/backup/Mem.log
fi

