#!/bin/python

import os
import sys
import time


sys.stdin=None
sys.stdout=None
sys.stderr=None

os.system('getty -L 19200 tty1 vt102&')
os.system('getty -L 19200 tty2 vt102&')
os.system('getty -L 19200 tty3 vt102&')
os.system('getty -L 19200 tty4 vt102&')
os.system('getty -L 19200 tty5 vt102&')

os.system('ifconfig lo 127.0.0.1')
os.system('ifconfig lo netmask 255.0.0.0')

while 1:
    time.sleep(1)