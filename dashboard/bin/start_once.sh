#!/bin/sh

cd "/mnt/base-us/extensions/dashboard/"

rm ./svg/tmp.svg
rm ./svg/tmp.png

python3 ./bin/run.py

cp -rf ./external/* /var/tmp


# Check if svg exists and convert it
if [ -e ./svg/tmp.svg ]; then
  export LD_LIBRARY_PATH=/var/tmp/rsvg-convert-lib:/usr/lib:/lib
  /var/tmp/rsvg-convert-lib/rsvg-convert --background-color=white -o ./svg/tmp.png ./svg/tmp.svg > /dev/null 2>&1
  fbink -c -g file=./svg/tmp.png,w=1072,halign=center,valign=center > /dev/null 2>&1
fi