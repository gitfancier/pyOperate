#!/bin/python
import pexpect
child = pexpect.spawn('ftp 192.168.80.12')
child.expect('Name')
child.sendline('luck')
print("1:"+str(child.before))
child.expect('Password')
child.sendline("goodluc")
print("2:"+str(child.before))
child.expect('ftp> ')
child.sendline('pwd')
print("3:"+str(child.before))
child.expect('ftp> ')
print("good\n")


