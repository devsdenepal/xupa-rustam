import requests
import urllib
proxies = {
"http" : "43.239.155.130:32650",
"https":"186.159.6.163:1994"
}
params ={
    'user_name':'gautam',
    'user_pass':'123456789'
}
a_url = 'https://jsonip.com/'
response = requests.get('https://',params=params,proxies=proxies,timeout=8)
print(response.content)
