#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi
cd IceBreaker
sudo python3 telegram_bot.py
cd /