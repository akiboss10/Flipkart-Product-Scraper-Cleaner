import requests

proxies = {
    'http': 'http://10.10.1.10:3128'
}

r = requests.get('https://api.ipify.org?format=json', proxies=proxies)
print(r.json())  # Print the public IP address in JSON format