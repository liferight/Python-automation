#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import paramiko
import os,sys,time

blip="192.168.0.174"
bluser="root"
blpasswd="123456"

hostname="192.168.0.156"
username="root"
password="123456"

port=22
passinfo='\'s password:'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient() #ssh登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shell() #创建会话 开启命令调用
channel.settimeout(20)  #会话命令执行超时时间秒

buff = ''
resp = ''
print username,hostname
channel.send('ssh '+username+'@'+hostname+'\n') #执行ssh登录
while not buff.endswith(passinfo): #ssh登录的提示信息判断，输出串尾有 退出while循环
	try:
		resp = channel.recv(9999)
	except Exception,e:
		print 'Error info:%s connection time.' % (str(e))
		channel.close()
		ssh.close()
		sys.exit()
	buff += resp
	if not buff.find('yes/no')==-1:
		channel.send('yes/n')
		buff=''

channel.send(password+'\n') #发送业务主机密码

buff=''
while not buff.endswith('# '):
	resp = channel.resv(9999)
	if not resp.find(passinfo)==-1: #输出串尾含有‘password’时说明输入密码不正确，重新输入
	
		print 'Error info: Authentication failed.'
		channel.close() #关闭连接对象后退出
		ssh.close()
		sys.exit()
	buff += resp
	
channel.send('ifconfig\n') #认证通过后发送ifconfig命令来查看结果
buff=''
try:
	while buff.find('# ')==-1:
		resp = channel.resv(9999)
		buff += resp
except Exception, e:
	print "error info:"+str(e)
	
print buff #打印输出
channel.close()
ssh.close()	
