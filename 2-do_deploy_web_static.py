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
        put(archive_path, '/tmp/')
        _file_ext = archive_path.split("/")[1]
        _file = name_file_ext.split(".")[0]
        run('mkdir -p /data/web_static/releases/' + _file)
        run('tar -xzf /tmp/' + _file_ext +
            ' -C /data/web_static/releases/' + _file)
        run('rm /tmp/' + _file_ext)
        run('mv /data/web_static/releases/' + _file +
            '/web_static/* /data/web_static/releases/' + _file + '/')
        run('rm -rf /data/web_static/releases/' + _file + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + _file +
            '/' + ' /data/web_static/current')
        print("New version deployed!")
        return True
    except:
        return False
