#!/bin/bash
cp /data/redis/src/dump.rdb /opt/backup/redis/product-dump-$(date +%Y%m%d_%H:%M).rdp
cp /data/redis/src/appendonly.aof /opt/backup/redis/product-appendonly-$(date +%Y%m%d_%H:%M).aof
scp /opt/backup/redis/* root@192.168.0.1:/opt/data-backup/product-redis/
