#!/bin/bash
sudo curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
export PATH="~/.pyenv/bin:$PATH"
echo 'export PATH="~/.pyenv/bin:$PATH"'>>$HOME/.bashrc
eval "$(pyenv init -)"
echo 'eval "$(pyenv init -)"'>>$HOME/.bashrc
eval "$(pyenv virtualenv-init -)"
echo 'eval "$(pyenv virtualenv-init -)"'>>$HOME/.bashrc
pyenv update
sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-developenssl-devel xz xz-devel apt­get install curl git­core gcc make zlib1g­dev libbz2­dev libreadline­dev libsqlite3­dev libssl­dev
pyenv install 2.7.14
pyenv install 3.5.4
sudo pip install virtualenv
sudo easy_install virtualenv
sudo yum -y install python-virtualenv
mkdir -p 2_7_14  3_4_5
pyenv global 2.7.14
cd 2_7_14/
pyenv virtualenv for_2_7
virtualenv for_2_7
cd ../3_4_5/
pyenv global 3.5.4
pyenv virtualenv for_3_5_4
virtualenv for_3_5_4




