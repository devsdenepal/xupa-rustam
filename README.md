# XUPA RUSTAM
![screenshot](https://raw.githubusercontent.com/devsdenepal/xupa-rustam/main/screenshots/IMG-20230403-WA0022.jpg)
``` A PYTHON BASED BRUTE FORCE PROJECT AIMED TO BYPASS ADMIN LOGIN PANEL OF WEBSITES (Pentesting tool) ```
# Description
This Python based CLI tool is made to host Brute-Force attack using `requests` module, and for keeping anonymity of the attacker's IP address `Tor proxy` is being used. 
The brute force works upon user defined admin and password list which tries each password from the list to every admin from the list.
## Aims of this project
- [x] Brute-Force to website
- [x] Use User-defined Admin list
- [x] Use User-defined Password list
- [x] Print returned response from the URL
- [x] Send request with Tor Proxy
- [x] Available without proxy feature
- [x] Stability in request with proxy (depends upon user's speed)
## Requirements
- Pysocks
- Tor proxy available on port 9050
- A possible list of admin and one for password
## Installation
```$ git clone https://github.com/devsdenepal/xupa-rustam ```
## Usage:
 ```$ python3 main.py ```
* Enter the  target URl of the login page
* Enter the parameter names
* Enter the admin and password list path
* The attack will start
## Contribute
*If you have any idea or suggestions to improve the code or interface, you can simply create a PR to this repo.*
## Author / Developer
> Dev. Gautam Kumar
## Special Credits
> Cold Bones (Anil Shrestha)
