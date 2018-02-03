#!/bin/bash
/usr/sbin/nginx
uwsgi --ini /scripts/potato-uwsgi.ini &
sleep 10000d
exec $@

