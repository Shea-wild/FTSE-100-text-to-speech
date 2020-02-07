import urllib.request, json
from datetime import datetime
import time
from gtts import gTTS



'''
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')
'''
url = "http://api.openrates.io/latest"

replacements = {'GBP':'Great British Pound'} 
with urllib.request.urlopen(url) as url:
      data = json.loads(url.read().decode())
      R = data['rates']
      print(R)
      rates = str(R)
 
      rates = rates.replace(replacements)
      print(rates)
      Split = rates.replace( ',', ',\n')
      print(Split)
      tts=gTTS(Split)
      tts.save('rates.mp3')
      
      '''engine.say(Split,'\r')
      engine.say('')
      engine.runAndWait()
      '''


