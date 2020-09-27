#!/bin/sh

cd "$(dirname "$0")"

/usr/sbin/ -c
/usr/sbin/ 15  4 'Starting 4DCu.be Dashboard'


while true
do
    sleep 5
    # Refresh Dashboard
    python3 /mnt/base-us/extensions/dashboard/bin/run.py
    sleep 5

    echo "" > /sys/class/rtc/rtc1/wakealarm
    # Following line contains sleep time in seconds
    echo "+3600" > /sys/class/rtc/rtc1/wakealarm
    # Following line will put device into deep sleep until the alarm above is triggered
    echo mem > /sys/power/state
done