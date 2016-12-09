#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import time
import traceback

def doRsync():
    cmd = "rsync -azPq --delete /opt/test/rsync root@192.168.0.179:/opt/test/rsync"
    #print cmd
    try:
        ssh = pexpect.spawn(cmd)
     #   print cmd
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)
        if i == 0 :
            ssh.sendline('123456')
        elif i == 1:
            ssh.sendline('yes')
            ssh.expect('password: ')
            ssh.sendline('123456')
        ssh.read()
        ssh.close()
    except :
        #print traceback.format_exc()
        pass

if __name__ == '__main__':
    doRsync()
