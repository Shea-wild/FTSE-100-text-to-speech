import urllib.request, json
from datetime import datetime
import time

from gtts import gTTS

import pyttsx3
engine = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')


url = "https://spreadsheets.google.com/feeds/list/0AhySzEddwIC1dEtpWF9hQUhCWURZNEViUmpUeVgwdGc/1/public/basic?alt=json"
with urllib.request.urlopen(url) as url:
      data = json.loads(url.read().decode())
      feed = data['feed']
      entry = feed['entry']

      i=100
      for i in range(0,10):
            I = i
            Value = entry[I]
            content= Value['content']
            Split = content['$t'].replace( ',', ',\n')
            final = ''
            final = final + Split
            print(Split,'\r')
      tts=gTTS(final)
      tts.save('ftse100.mp3')
'''engine.say(Split,'\r')
engine.say('')
engine.runAndWait()
'''

'''
18
19
29
33
com.apple.speech.synthesis.voice.paulina

41
com.apple.speech.synthesis.voice.Victoria

com.apple.speech.synthesis.voice.Victoria
'''
