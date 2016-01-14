# Copyright (C) 2015 Kyle Harrigan (kwharrigan@gmail.com)
# portions based off hookexample.py

import dmtcp
import os
from ctypes import *

# Note that we must use the libc version of getenv.  As it turns out,
# the python version makes the actual getenv call upon module import,
# and then caches the result for calls by os.environ, os.getenv, etc.
#
# This makes it tricky for modify-env to get restarted env vars into
# Python.  
#
# So, as undesirable as it may seem, the trick for now is to use CDLL
# and get it straight from the horse's mouth.

libc = CDLL('libc.so.6')
getenv = libc.getenv
getenv.restype = c_char_p # getenv returns a char*

def do_ckpt():
    '''
    Check point, and then indicate if we are in the initial checkpoint
    or in a restarted version
    '''
    print "About to checkpoint."
    dmtcp.checkpoint()
    print "Checkpoint done."
    if dmtcp.isResume():
        print "The process is resuming from a checkpoint."
    else:
        print "The process is restarting from a previous checkpoint."
    return

print "Calling do_ckpt()"
do_ckpt()
if dmtcp.isRestart():
    print 'Restarted...MYVAR should be set to value in dmtcp_env.txt'
else:
    print 'First time...MYVAR should be empty'
print 'MYVAR=[%s] (from libc.so getenv)' % getenv('MYVAR')
print 'MYVAR=[%s] (from os.getenv)' % os.getenv('MYVAR')
print 'DMTCP_ENV_FILE=[%s] (from libc.so getenv)' % getenv('DMTCP_ENV_FILE')

if dmtcp.isRestart():
    raw_input()
    
