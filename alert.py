# -*- coding: utf8 -*-
import time
import os
import sys
from subprocess import call
# When get up ?
h = 8
m = 45

loop = True
while(loop):
    # now
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    # get up ?
    if h == hour and m == minute:
        return_code = call("/Applications/iTunes.app/Contents/MacOS/iTunes 十年.mp3", shell=True)
        loop = False

    # display current time
    timestr = "%04d-%02d-%02d %02d:%02d:%02d\r" \
            % (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5])
    sys.stdout.write(timestr)
    sys.stdout.flush()
    time.sleep(1)
    # end
