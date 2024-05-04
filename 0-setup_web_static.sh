#!/usr/bin/env bash
# A Bash script to set up web servers for the deployment of web_static.

# Update the server
sudo apt-get update

# Install nginx if it is not installed
sudo apt-get -y install nginx

# Use allow ufw for the firewall
sudo ufw allow 'Nginx HTTP'

# Run these command to set up server for deployment
# Create ----:

# data/ if it doesn’t already exist
sudo mkdir -p /data/

# /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static/

# /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/

# /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
# linked to the /data/web_static/releases/test/ folder
# If symbolic link exists, it should be deleted and recreated.
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
