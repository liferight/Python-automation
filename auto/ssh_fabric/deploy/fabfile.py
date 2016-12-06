#!/usr/bin/env python
# coding:utf-8

from fabric.api import run, env, task, settings, parallel, runs_once, local, execute, roles
from fabric.contrib.project import rsync_project
import os
import sys
import ConfigParser

conf_path = '/opt/ops/deploy/deploy.conf'

conf = ConfigParser.ConfigParser()
conf.read(conf_path)

env.disable_known_hosts = True

env.user = 'root'

env.roledefs = {
    'prod': conf.options("prod"),
    'test': conf.options("test")
}


@task
def set_env(e):
    env.hosts = conf.options(e)

@task
def hostname_status():
    run('hostname')
