#!/bin/sh

cd "$(dirname "$0")"

/usr/sbin/ -c
/usr/sbin/ 15  4 'Starting 4DCu.be Dashboard (Once)'
sleep 1

python3 /mnt/base-us/extensions/dashboard/bin/run.py
