# LIBRARIES
import speech_recognition as sr     # Speech Recognition
import pyttsx3                      # Test to Speech
import pywhatkit                    
import datetime                     # Date & Time
import wikipedia                    # Wikipedia
import pyjokes                      # Python Jokes
import sys

assistant_name = 'Rito'

listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.8)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)

def say_and_print(output):
    print(output)
    engine.say(output)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            print('\nHello Master. I am ' + str(assistant_name) + '. Say Something!')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # command = command.lower()
            if assistant_name in command:
                command = command.replace(str(assistant_name) + ' ', '')
    except:
        print("Error!")
        pass
    return command

def run_assistant():
    command = user_commands()
    print('\nINPUT COMMAND: '+ str(command))
    print('\nOUTPUT COMMAND: ')
    if 'stop' in command:
        sys.exit()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say_and_print('The current time is ' + time)
    elif 'name' in command:
        say_and_print('My name is ' + str(assistant_name))
    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        say_and_print(info)
    elif 'play' in command:
        song = command.replace('play', '')
        say_and_print('Playing' +song)
        pywhatkit.playonyt(song)
    elif 'what is' in command:
        item = command.replace('what is' , '')
        info =  wikipedia.summary(item, 1)
        say_and_print(info)
    elif 'joke' in command:
        say_and_print(pyjokes.get_joke())
    elif 'are you' in command:
        reply = command.replace('are you ', '')
        say_and_print('Yes, I am ' + reply)
    else:
        say_and_print('Not sure about that.')
        engine.runAndWait()

while True:
    run_assistant()

run_assistant()