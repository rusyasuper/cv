from Arina.html import *
import requests
res = requests.get(url = Arina.html)
data = res.json()
print(data)