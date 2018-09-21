#!/bin/bash

# 襾A壾G份潚~D录°彍®幾S佐~M﻾L壾Z个录°彍®幾S潔¨空庠¼佈~F廾@
databases=(spms_service)

# 壾G份彖~G件襾A侾]嬾X潚~D潛®弾U
#basepath='/opt/backup/mysql/'

#if [ ! -d "$basepath" ]; then
#  mkdir -p "$basepath"
#fi

# 循潎¯databases录°纾D
#for db in ${databases[*]}
#  do
    # 壾G份录°彍®幾S潔~_彈~PSQL彖~G件
    # mysqldump -uspms -pspms --databases $db > $basepath$db-$(date +%Y%m%d).sql
      mysqldump --all-databases  > /opt/backup/mysql/spms_all_$(date +%Y%m%d).sql

    # 対F潔~_彈~P潚~DSQL彖~G件低~K缩
    #tar zPcf $basepath$db-$(date +%Y%m%d).sql.tar.gz $basepath$db-$(date +%Y%m%d_%H:%M).sql

    # 佈| 轙¤32天举K佉~M潚~D壾G份录°彍®
#    find $basepath -mtime +32 -name "*.sql" -exec rm -rf {} \;
#  done

  # 佈| 轙¤潔~_彈~P潚~DSQL彖~G件
  #rm -rf $basepath/*.sql

