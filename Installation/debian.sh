#!/bin/sh

# Django run on python3.4+
apt install -y python3.7

# Python package manager
apt install -y python3-pip

# Install Django
apt install
pip3 install Django==2.1.1

# Install virtualenv to use django commands
pip3 install virtualenv