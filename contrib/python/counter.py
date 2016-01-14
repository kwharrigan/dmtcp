#!/usr/bin/python

import time
import sys
from ctypes import CDLL, c_char_p
import dmtcp

libc = CDLL('libc.so.6')
getenv = libc.getenv
getenv.restype = c_char_p

n = 0
increment = 1
while True:
    n += increment
    if n == 5:
        dmtcp.checkpoint()
    if dmtcp.isRestart():
        increment = int(getenv('INCREMENT'))
    print "\t"*increment + "%d " % (n)
    sys.stdout.flush()
    time.sleep(1)
