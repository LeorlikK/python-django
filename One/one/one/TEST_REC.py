import requests
import datetime
import time


url = 'http://127.0.0.1:8000/news/get'
rec = requests.get(url).text
print(rec)