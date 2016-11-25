#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
import paramiko

hostname='192.168.0.181'
username='root'
password='123456'
port = 22

try:
	t = paramiko.Transport((hostname,port))
	t.connect(username=username, password=password)
	sftp = paramiko.SFTPClient.from_transport(t)
	
	sftp.put("/opt/test/1.txt","/root/1.txt") #上传文件
	sftp.get("/root/2.txt", "/opt/test/2.txt") #下载文件
	sftp.mkdir("/opt/test/userdir",0755) #创建目录
	sftp.rmdir("/opt/test/userdir1") #删除目录
	sftp.rename("/opt/test/3.txt","/opt/test/4.txt") #重命名文件
	print sftp.stat("/opt/test/4.txt") #打印文件信息
	print sftp.listdir("/opt/test") #打印目录列表
	t.close();
except Exception, e:
	print str(e)
