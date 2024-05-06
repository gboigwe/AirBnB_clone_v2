#!/usr/bin/python3
"""
A Fabric script to generates a .tgz archive
from the web_static contents folder of
AirBnB Clone repo, using do_pack function
"""


from time import strftime
from datetime import date
from fabric.api import local


def do_pack():
    """Function to generate the archive web_static contents folder"""

    file_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_name))
        return "versions/web_static_{}.tgz".format(file_name)
    except Exception as e:
        return None
