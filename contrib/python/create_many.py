#!/usr/bin/env python

# (c) 2015-2016 Kyle Harrigan (kwharrigan@gmail.com)

import subprocess
import time
import os
import glob

N_PROCS = 5
processes = []

filename = glob.glob('*.dmtcp')[0]
for i in range(0, N_PROCS):
    #proc = subprocess.Popen(['ENV_FILE="dmtcp_env%d" ./dmtcp_restart_script.sh -p 0' % i], shell=True)
    proc = subprocess.Popen(['DMTCP_ENV_FILE="dmtcp_env%d.txt" dmtcp_restart --new-coordinator %s' % (i, filename)], shell=True)
    processes.append(proc)

processes[0].wait()
