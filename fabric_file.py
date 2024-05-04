#!/usr/bin/python3
from fabric import Connection

# servers = ['52.3.240.1', '100.24.237.31']
# for server in servers:
with Connection(host='52.3.240.1',
                user='ubuntu',
                connect_kwargs={
                    'key_filename':'/home/age/.ssh/id_rsa.pub',
                },
                ) as c:
                    print(c.run('hostname'))
