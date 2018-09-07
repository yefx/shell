#!/bin/bash

Date=`date '+%c'`

nginx_status(){ 
######check nginx && php-fpm runing status######
if ! ps aux | grep -w nginx | grep -v grep > /dev/null 2>&1  
	then
		if ! ps aux | grep -w php-fpm | grep -v grep > /dev/null 2>&1  
			then
				cd /usr/local/php/sbin && ./php-fpm
				echo "$Date reboot php-fpm" >> /tmp/reboot_php-fpm.log
		fi
		/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
		echo "$Date reboot nginx" >> /tmp/reboot_nginx.log
fi
}

$1