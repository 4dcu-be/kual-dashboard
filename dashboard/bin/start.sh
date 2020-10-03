#!/bin/sh

cd "/mnt/base-us/extensions/dashboard/"

# Make sure there is enough time to reconnect to the wifi
sleep 30

# Remove files
if [ -f ./svg/tmp.svg ]; then
    rm ./svg/tmp.svg
fi

if [ -f ./svg/tmp.png ]; then
    rm ./svg/tmp.png
fi

# Run script to download data and generate new SVG file
python3 ./bin/run.py

# Copy rsvg-convert to a share where it can be started
# The shared folder that can be accessed via USB is mounted with the noexec flag,
# copying file to /var/tmpt gets around this restriction.
if [ ! -f /var/tmp/rsvg-convert ]; then
    cp -rf ./external/* /var/tmp
fi

# Check if svg exists and if it does convert it to PNG and show on screen
if [ -e ./svg/tmp.svg ]; then
  export LD_LIBRARY_PATH=/var/tmp/rsvg-convert-lib:/usr/lib:/lib
  /var/tmp/rsvg-convert-lib/rsvg-convert --background-color=white -o ./svg/tmp.png ./svg/tmp.svg > /dev/null 2>&1
  fbink -c -g file=./svg/tmp.png,w=1072,halign=center,valign=center > /dev/null 2>&1
fi

# Make sure the screen is fully refreshed before going to sleep
sleep 5

echo "" > /sys/class/rtc/rtc1/wakealarm
# Following line contains sleep time in seconds
echo "+3600" > /sys/class/rtc/rtc1/wakealarm
# Following line will put device into deep sleep until the alarm above is triggered
echo mem > /sys/power/state

# Kill self and spawn a new instance
/bin/sh ./bin/start.sh && exit