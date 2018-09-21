#!/bin/bash

databases=(spms_service)

basepath='/opt/backup/mysql/'

if [ ! -d "$basepath" ]; then
  mkdir -p "$basepath"
fi

for db in ${databases[*]}
  do
    # mysqldump -uspms -pspms --databases $db > $basepath$db-$(date +%Y%m%d).sql
      mysqldump -uspms -pspms --databases $db > $basepath$db-$(date +%Y%m%d).sql

    #tar zPcf $basepath$db-$(date +%Y%m%d).sql.tar.gz $basepath$db-$(date +%Y%m%d_%H:%M).sql

    find $basepath -mtime +32 -name "*.sql" -exec rm -rf {} \;
  done

  #rm -rf $basepath/*.sql

