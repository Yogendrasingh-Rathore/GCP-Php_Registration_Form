#!/bin/bash
cd
mkdir yuvikool
sudo apt update
sudo apt install -y apache2 apache2-utils
sudo systemctl start apache2
sudo systemctl enable apache2