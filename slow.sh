#!/bin/bash
pkg install python3
pkg install nmap
pkg install hydra
cd scripts
unzip weber.zip
cd ..
chmod +x fire
mv fire /data/data/com.termux/files/usr/bin
clear
echo 'Установка прошла успешно!'
rm slow.sh
