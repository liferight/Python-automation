#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
from fabric.api import *

env.user='root'
env.host=['192.168.0.181']
env.password='s6vd154d4DFukFAR'

@runs_once
def local_task():
	local("uname -a")

def remote_task():
	with cd("/opt/test"):
	run("ls -l")
#def remote_task():
#	with cd("/opt/test"):
#       run("ls -l")
