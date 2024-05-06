#!/usr/bin/python3
"""
A Fabric script that distributes an archive
to my web servers, with the do_deploy function:
executing: fabric file:
fab -f 3-deploy_web_static.py
deploy to ubuntu user on server
"""

from os.path import exists, isdir
from fabric.api import env, local, put, run
from datetime import datetime
env.hosts = ['52.3.240.1', '100.24.237.31']


def do_pack():
    """Using tgz to archive web_static files"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None

def do_deploy(archive_path):
    """Creating and deploying the archived file"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """Created an archive file for the web_static deploment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
