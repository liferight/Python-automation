#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import paramiko
import os

hostname='192.168.0.181'
username='root'
paramiko.util.log_to_file(syslogin.log)

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()

privatakey = os.path.expanduser('/home/key/id_rsa') #定义私钥存放目录
key = paramiko.RASKey.form_private_key_file(privatakey)#创建私钥对象key

ssh.connect(hostname=hostname,username=username,pkey=key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()