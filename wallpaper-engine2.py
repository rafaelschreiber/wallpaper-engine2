#!/usr/bin/env python3
import sys
import os
import time
from random import *

try:
    interval = int(sys.argv[1])
    if interval <= 0:
        print("Please type in a number greater than 0")    
        raise ValueError

except:
    print("Type in an update interval (in sec)")
    while True:
        try:
            interval = int(input(">>> "))
            if interval <= 0:
                print("Please type in a number greate than 0\n")
                continue
            else:
                break
        except ValueError:
            print("Please type in a number\n")
    


while True:
    while True:
        randomnumber = randint(1, 99999)
        link = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-" + str(randomnumber) +".jpg"
        if os.system("wget -O /tmp/" + str(randomnumber) + ".jpg " + link) == 0:
            break
        else:
            continue
    pathtofile = "/tmp/" + str(randomnumber) + ".jpg"
    cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + pathtofile + "\"'"
    os.system(cmd)
    time.sleep(interval)
