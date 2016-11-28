#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
#动态获取远程目录列表，调用worktask()任务函数实现远程命令执行
from fabric.api import *

env.user='root'
env.hosts=['192.168.0.181']
env.password='123456'

@runs_once
def input_raw():
	return prompt("please input directory name:",default="/opt")

def  worktask(dirname):
	run("ls -l" +dirname)

@task #限定只有go函数对fab命令可见
def go():
	getdirname = input_raw()
	worktask(getdirname)
