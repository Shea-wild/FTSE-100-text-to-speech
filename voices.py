import pyttsx3
n=0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in 17:
      engine.setProperty('voice', voice.id)
      say = 'i am a robot' + str( n)
      engine.say(say)
      n=n+1
      print(n)
      print(voice)
print(voices)
engine.runAndWait()
