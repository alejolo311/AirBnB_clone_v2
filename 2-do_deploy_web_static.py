#!/usr/bin/python3
# Creates and distributes an archive to web servers

from fabric.api import *
from os import path

env.hosts = ['34.74.140.171', '	3.95.67.118']


def do_deploy(archive_path):
    """Deploy"""
    if not path.exists(archive_path):
        return False
    ret = True
    task_1 = put(archive_path, '/tmp/')
    if task_1.failed:
        ret = False
    _file = archive_path.replace(".tgz", "").replace("versions/", "")
    task_2 = run('mkdir -p /data/web_static/releases/' + _file + '/')
    if task_2.failed:
        ret = False
    task_3 = run('tar -xzf /tmp/' + _file + '.tgz' +
                 ' -C /data/web_static/releases/' + _file + '/')
    if task_3.failed:
        ret = False
    task_4 = run('rm /tmp/' + _file + '.tgz')
    if task_4.failed:
        ret = False
    task_5 = run('mv /data/web_static/releases/' + _file +
                 '/web_static/* /data/web_static/releases/' + _file + '/')
    if task_5.failed:
        ret = False
    task_6 = run('rm -rf /data/web_static/releases/' + _file + '/web_static')
    if task_6.failed:
        ret = False
    task_7 = run('rm -rf /data/web_static/current')
    if task_7.failed:
        ret = False
    task_8 = run('ln -sf /data/web_static/releases/' + _file +
                 '/' + ' /data/web_static/current')
    if task_8.failed:
        ret = False
    if ret:
        print("All tasks succeeded!")
    return ret
