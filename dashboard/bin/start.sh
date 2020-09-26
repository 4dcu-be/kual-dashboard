#!/bin/sh

cd "$(dirname "$0")"

/usr/sbin/ -c
/usr/sbin/ 15  4 'Starting 4DCu.be Dashboard'
sleep 5


while true
do
    # Refresh Dashboard
    python3 /mnt/base-us/extensions/dashboard/bin/run.py

    sleep 3600
done