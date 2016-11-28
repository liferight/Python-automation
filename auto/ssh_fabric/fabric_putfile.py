#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
#fabric的env对象定义网关模式，即堡垒机，再结合任务函数实现主机文件上传与执行操作
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user='root'
env.gateway='192.168.0.181'
env.hosts='192.168.0.174'
env.passwords = {
	'root@192.168.0.174': '123456',
	'root@192.168.0.181': '123456'}

lpackpath="/opt/test/123.txt"
rpackpath="/tmp/test"

@task
def put_task():
	run("mkdir -p /tmp/test")
	with settings(warn_only=True):
		result = put(lpackpath, rpackpath)
	if result.failed and not confirm("put file failed,continue[Y/N]?"):
		abort("Aborting file put task!")

@task
def run_task():
	with cd("/tmp/test"):
		run("cat 123.txt")

@task
def go():
	put_task()
	run_task()

