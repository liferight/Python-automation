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

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shell()
channel.settimeout(20)

buff = ''
resp = ''
print username,hostname
channel.send('ssh '+username+'@'+hostname+'\n')
while not buff.endswith(passinfo):
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

channel.send(password+'\n')

buff=''
while not buff.endswith('# '):
	resp = channel.resv(9999)
	if not resp.find(passinfo)==-1:
	
		print 'Error info: Authentication failed.'
		channel.close()
		ssh.close()
		sys.exit()
	buff += resp
	
channel.send('ifconfig\n')
buff=''
try:
	while buff.find('# ')==-1:
		resp = channel.resv(9999)
		buff += resp
except Exception, e:
	print "error info:"+str(e)
	
print buff
channel.close()
ssh.close()	
