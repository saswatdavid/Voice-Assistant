#Current Speaking Rate
print(engine.getProperty('rate'))
#Current Volume
print(engine.getProperty('volume'))
#Choose Voice
i = 0
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say(str(i)+'I am a dinosaur')
   i = i+1
engine.runAndWait()
engine.setProperty('voice', voices[0].id) #Male 1
engine.setProperty('voice', voices[7].id) #Male 2
engine.setProperty('voice', voices[17].id) #Female 1
engine.setProperty('voice', voices[33].id) #Female 2
engine.setProperty('voice', voices[41].id) #Female 3