#!/usr/bin/python3
# do the deploy

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['34.74.140.171', '	3.95.67.118']


def do_deploy(archive_path):
    """Deploy"""
    if not path.exists(archive_path):
        return False
    if (path.exists(archive_path) and path.isdir(archive_path)):
        return False
    try:
        task_1 = put(archive_path, '/tmp/')
        _file = archive_path.replace(".tgz", "").replace("versions/", "")
        task_2 = run('mkdir -p /data/web_static/releases/' + _file + '/')
        task_3 = run('tar -xzf /tmp/' + _file + '.tgz' +
                    ' -C /data/web_static/releases/' + _file + '/')
        task_4 = run('rm /tmp/' + _file + '.tgz')
        task_5 = run('mv /data/web_static/releases/' + _file +
                    '/web_static/* /data/web_static/releases/' + _file + '/')
        task_6 = run('rm -rf /data/web_static/releases/' + _file + '/web_static')
        task_7 = run('rm -rf /data/web_static/current')
        task_8 = run('ln -sf /data/web_static/releases/' + _file +
                    '/' + ' /data/web_static/current')
        print("New version deployed!")
        return True
    except:
        return False
