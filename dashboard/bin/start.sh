#!/bin/sh

cd "$(dirname "$0")"

#sleep 1
#
#/usr/sbin/eips -c
#/usr/sbin/eips -c
#/usr/sbin/eips 15  4 'Starting Script'
#
#sleep 1

python3 /mnt/base-us/extensions/dashboard/bin/run.py
