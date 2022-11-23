#!/bin/bash

apt update
apt upgrade
apt install awscli --upgrade
aws --version


#curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
#unzip awscliv2.zip
#./install --update
#aws --version
