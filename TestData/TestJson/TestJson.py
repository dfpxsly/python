from urllib.request import urlopen as op
import json

json_url = 'D:\\Code\\python\\TestData\\TestJson\\btc_close_2017.json'
response = op(json_url)

req = response.read()