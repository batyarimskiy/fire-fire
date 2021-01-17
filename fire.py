import os, sys

from modules import logo
from termcolor import colored

def weber():
    os.system('cd scripts && cd weber && python3 weber.py')

def admFind():
    os.system('cd scripts && python3 admfind.py')

def Cloud():
    os.system('cd scripts && python3 cloud.py')

def nmap():
    os.system('clear')
    print(logo.logo)
    d = input('Введите домен сайта: ')
    os.system('nmap -T4 -sV '+str(d))

def hydra():
    os.system('clear')
    print(logo.logo)
    print('Брутфорс - это грубый метод атаки или же перебор паролей')
    brut = '''
(1) ftp
(2) ssh
    '''
    print(brut)
    sf = input('Выберите параметр: ')
    if sf == "1":
        ftp = ':21'
        ip = input('IP Сайта: '+str(ftp))
        print('Используются стандартные пароли\nИзмените файлы Log и Pass для установки собственных паролей')
        os.system('hydra -L /data/data/com.termux/files/home/fire-fire/modules/log.txt -P /data/data/com.termux/files/home/fire-fire/modules/pass.txt ftp://'+str(ip))
    if sf == "2":
        ssh = ":22"
        ips = input('IP Сайта: '+str(ssh))
        print('Используются стандартные пароли\nИзмените файлы Log и Pass для установки собственных паролей')
        os.system('hydra -L /data/data/com.termux/files/home/fire-fire/modules/log.txt -P /data/data/com.termux/files/home/fire-fire/modules/pass.txt ssh://'+str(ips))

def main():
    os.system('clear')
    print(logo.logo)
    print(logo.menu)
    num_menu = input("=========!> ")
    if num_menu == "":
        main()
    if num_menu == "1":
        weber()
    if num_menu == "2":
        nmap()
    if num_menu == "3":
        admFind()
    if num_menu == "4":
        hydra()
    if num_menu == "5":
        check()
    if num_menu == "6":
        Cloud()
    if num_menu == "8":
        os.system('clear')
        sys.exit()
main()
