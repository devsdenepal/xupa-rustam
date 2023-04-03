import threading
import requests
import argparse
parser = argparse.ArgumentParser(description='Proxy Filter for active proxy list.')
parser.add_argument('--path', type=str, help='Path for text file of proxy list to be checked.')
args = parser.parse_args()
path = args.path
# Define the function that will be executed by each thread
def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Active proxy: {proxy}")
    except:
        pass

# Read the list of proxy servers from a text file
with open(path, 'r') as file:
    proxies = [line.strip() for line in file]

# Create and start a thread for each proxy server
threads = []
for proxy in proxies:
    thread = threading.Thread(target=check_proxy, args=(proxy,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
