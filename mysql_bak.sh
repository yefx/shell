#!/bin/bash

databases=(dev test prep)

basepath='/opt/backup/mysql/'

if [ ! -d "$basepath" ]; then
  mkdir -p "$basepath"
fi

for db in ${databases[*]}
  do
     mysqldump -uuser -ppasswd --databases $db > $basepath$db-$(date +%Y%m%d).sql

    #tar zPcf $basepath$db-$(date +%Y%m%d).sql.tar.gz $basepath$db-$(date +%Y%m%d_%H:%M).sql

    find $basepath -mtime +32 -name "*.sql" -exec rm -rf {} \;
  done

  #rm -rf $basepath/*.sql

