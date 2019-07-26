#!/bin/python
import pexpect
import sys
child = pexpect.spawn('ssh luck@192.168.80.12')
#child.logfile = sys.stdout
#fout = file('log.txt', 'w')
#child.logfile = fout
child.expect('password')
child.sendline('goodluck')
print("out:" + str(child.before, encoding= 'utf-8') + "\n---------------\n")
child.expect('luck')
child.sendline('ls')
print("out:"+str(child.before, encoding= 'utf-8') + "\n---------------\n")
child.expect('luck')
print("out:"+str(child.before, encoding= 'utf-8') + "\n---------------\n")
child.close()
print("good\n")


