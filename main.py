import requests
# Open the text file containing the list of proxies
# with open('elite.txt', 'r') as f:
#     proxy_list = f.readlines()

# Strip any newline characters from the end of each line
# proxy_list = [x.strip() for x in proxy_list]

# # Define a function to rotate the proxy list and return the next proxy


# def rotate_proxy():
#     # Get the first proxy in the list
#     proxy = proxy_list[0]

#     # Move the first proxy to the end of the list
#     proxy_list.append(proxy_list.pop(0))

#     # Return the proxy
#     return proxy


# URL to make the request to
a_url = 'https://jsonip.com/'

# Make the request using a rotating proxy
while True:
    # Get the next proxy from the list
    # proxy = rotate_proxy()

    # Set the proxy for the request
    proxies = {
        'http': '46.101.49.62:80',
        'https': '64.225.8.118:9990'
    }

    try:
        # Make the request using the proxy
        response = requests.get(a_url, proxies=proxies)

        # Print the response content
        print(response.content)

        # If the request was successful, break out of the loop
        break
    except:
        # If the request failed, continue to the next proxy
        continue
