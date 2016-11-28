#!/usr/bin/env python
# coding:utf-8
#create zyn 2016
from fabric.api import run

def host_type():
	run('uname -s')