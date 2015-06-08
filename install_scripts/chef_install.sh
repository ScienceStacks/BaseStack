#!/bin/bash
cd $HOME
sudo curl -L https://www.opscode.com/chef/install.sh | bash
wget http://github.com/opscode/chef-repo/tarball/master
tar -zxf master
mv chef-chef-repo* chef-repo
rm master
cp -r BaseStack/cookbooks/* chef-repo/cookbooks
