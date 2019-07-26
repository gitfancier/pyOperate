#!/bin/python
from pexpect import  pxssh
import sys

s = pxssh.pxssh()
#s.logfile = sys.stdout
hostname = '192.168.80.12'
username = 'luck'
password = 'goodluck'
s.login(hostname, username, password)
s.sendline('ls')
s.prompt()
s.sendline('whoami')
s.prompt()
s.logout()