#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
#调用local()方法执行本地命令，调用run()方法执行远程命令
from fabric.api import *

env.user='root'
env.host=['192.168.0.181']
env.password='123456'

@runs_once  #查看本地系统信息，当有多台主机时只运行一次
def local_task():  #本地任务函数
	local("uname -a")

def remote_task():
	with cd("/opt/test"):#with的作用是让后面的表达式的语句继承当前状态
	run("ls -l")
#def remote_task():
#	with cd("/opt/test"):
#       run("ls -l")
