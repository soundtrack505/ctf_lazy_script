#!/bin/bash

sudo apt update && sudo apt  full-upgrade -y;
sudo mv php-reverse-shell.php /opt/;
wget 'https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb';
sudo dpkg -i rustscan_2.0.1_amd64.deb;
sudo rm rustscan_2.0.1_amd64.deb;
sudo apt install python3-pip -y && sudo pip3 install colorama pyfiglet pynput pyperclip git+https://github.com/calebstewart/pwncat.git;
sudo wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar;
sudo mv stegsolve.jar /opt/.stegsolve.jar;
sudo gem install zsteg;
sudo apt install gobuster ftp-upload nmap sshpass xclip metasploit-framework terminator smbclient hexedit steghide enum4linux vim binwalk hydra wpscan -y;
sudo mkdir /opt/wordlist;
sudo cp /usr/share/wordlist/dirbuster/directory-list-2.3-medium.txt /opt/wordlist/directory-list-2.3-medium.txt;
sudo apt autoremove -y;

echo '[+] Done!'
