import urllib.request, json
from datetime import datetime
import time

url = "http://api.openrates.io/latest"

replacements = {'GBP':'Great British Pound'} 

with urllib.request.urlopen(url) as url:
      
      data = json.loads(url.read().decode())
      
      R = data['rates']

      print(R)

      rates = str(R)
                  
      print(rates)

      Split = rates.replace( ',', ',\n')

      print(Split)
