import requests

requests = requests.get("https://ident.me")
ip_publica = requests.text
print(ip_publica)