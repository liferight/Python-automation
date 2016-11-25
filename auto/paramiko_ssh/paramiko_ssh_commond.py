#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import paramiko

hostname='192.168.0.181'
username='root'
password='123456'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.load_system_host_keys()

ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print stdout.read()
ssh.close()
