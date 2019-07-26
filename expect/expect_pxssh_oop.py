
#!/usr/bin/python  
#coding=utf-8
from optparse import OptionParser   
from pexpect import pxssh  
  
def send_command(child,cmd):  
  
    child.sendline(cmd)  
    #匹配prompt(提示符)  
    child.prompt()  
    #将prompt前所有内容打印出  
    print child.before  
  
def connect(host,user,password):  
    try:  
        child = pxssh.pxssh()  
        #利用pxssh类的login()方法进行ssh登录  
        child.login(host,user,password)  
        return child  
    except:  
        print '[-] Error Connecting'  
        exit(0)
 
def main():
    parser = OptionParser("[*] Usage : ./pxSsh.py -H <target host> -u <username> -p <password>")
    parser.add_option('-H',dest='host',type='string',help='specify target host')  
    parser.add_option('-u',dest='username',type='string',help='target username')  
    parser.add_option('-p',dest='password',type='string',help='target password')  
    (options,args) = parser.parse_args()  
  
    if (options.host == None) | (options.username == None) | (options.password == None):  
        print parser.usage  
        exit(0)
 
    child=connect(options.host,options.username,options.password)
 
    while True: 
        #raw_input将所有输入作为字符串看待，不管用户输入什么类型的都会转变成字符串 
        command = raw_input('<SSH> ')  
        send_command(child,command)
 
if __name__ == '__main__':
    main()
