#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
#远程ssh执行命令exec_command
import paramiko

hostname='192.168.0.181'
username='root'
password='123456'
paramiko.util.log_to_file('syslogin.log') #发送paramiko日志到syslogin.log文件

ssh=paramiko.SSHClient() #创建一个ssh客户端client对象
ssh.load_system_host_keys() #获取客户端host_keys 

ssh.connect(hostname=hostname,username=username,password=password) #创建ssh链接
stdin,stdout,stderr=ssh.exec_command('free -m') #调用远程执行命令exec_command
print stdout.read() #打印执行结果
ssh.close() #关闭ssh
