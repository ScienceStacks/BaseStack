#!/bin/bash
# Installs Apache so that the server runs from
sudo apt-get install -y apache2

# Handle the case of running without vagrant
if ! [ -L /vagrant ]; then
  mkdir $HOME/apache_home
  mkdir $HOME/apache_home/html
  echo "Hello ubuntu World!" > $HOME/apache_home/html/index.html
  sudo ln -s $HOME/apache_home /vagrant
fi

# Set up the link for running  apache
if ! [ -L /var/www/html ]; then
  sudo rm -rf /var/www
  sudo ln -fs /vagrant /var/www
fi
