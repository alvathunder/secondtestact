#!/usr/bin/sudo bash

apt update
apt upgrade
apt install apache2 -y
systemctl enable --now apache2.service -y
systemctl status apache2


#curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
#unzip awscliv2.zip
#./install --update
#aws --version
