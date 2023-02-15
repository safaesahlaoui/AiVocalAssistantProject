import pyttsx3 as pts
import  speech_recognition as sp
from selenium_web import infow
from Yt_auto import music
from News import *
engine = pts.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices =engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speack(text):
    engine.say(text)
    engine.runAndWait()
speack("hello there. my name is nova. and i am your voice assistant")

r = sp.Recognizer()
with sp.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening ...')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if 'what' and 'about' and 'you' in text:
    speack('I am having a good day sir')
speack('what can i do for you??')

# automation
with sp.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listening ...')
    audio = r.listen(source)
    text2= r.recognize_google(audio)
if 'information' in text2:
    speack('you need information related to witch  topic')
    with sp.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listening ...')
        audio = r.listen(source)
        info= r.recognize_google(audio)
        speack('searching {} in wikipedia'.format(info))

    assist=infow()
    assist.get_info(info)

elif 'play' and 'video' in text2:
    speack('you want to play wich video??')
    with sp.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listening...')
        audio = r.listen(source)
        vid=r.recognize_google(audio)
        print('Playing {} on youtube'.format(vid))
        assist=music()
        assist.playMusic(vid)

elif 'News' in text2 :
    speack('Sure , Now I will read news for you')
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speack(arr[i])

