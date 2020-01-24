import urllib.request, json
from datetime import datetime
import time

url = "https://spreadsheets.google.com/feeds/list/0AhySzEddwIC1dEtpWF9hQUhCWURZNEViUmpUeVgwdGc/1/public/basic?alt=json"
with urllib.request.urlopen(url) as url:
      data = json.loads(url.read().decode())
      feed = data['feed']
      entry = feed['entry']
      i=100
      for i in range(0,2):
            I = i
            Value = entry[I]
            content= Value['content']
            '''name = content['name']
            price = content['price']
            change =content['change']'''
            Split = content['$t'].split('\r')
            print(Split)
            print(i)
