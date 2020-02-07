import urllib.request, json
from datetime import datetime
import time
from gtts import gTTS

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')

url = "http://api.openrates.io/latest"

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 220)     # setting up new voice rate

replacements = {'GBP':'Great British Pound'} 
with urllib.request.urlopen(url) as url:
      data = json.loads(url.read().decode())
      R = data['rates']
      rates = str(R)
      Split = rates.replace( ',', ',\n')
      print(Split)
      '''tts=gTTS(Split)
      tts.save('rates.mp3')
'''
      dis = ''
      x = 0
      rates = rates.replace( "'",'' )
      
      rates = rates.replace(':','')
      while x != 30:
            x=x+1
            letter = rates[x]
            letter = letter.replace('.','point')
            if letter == '.':
                  letter = 'point'
            if letter == "'":
                  letter = ' '

            print(rates[x])
            engine.say(letter)
            engine.runAndWait()

            
      
