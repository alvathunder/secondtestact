#!/bin/sh

apk update
apk upgrade 
apk add --no-cache aws-cli
aws --version

