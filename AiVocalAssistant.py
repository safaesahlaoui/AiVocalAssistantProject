import pyttsx3 as pts
import  speech_recognition as sp
from selenium_web import infow
from Yt_auto import music
from News import *
from getJokes import  *
from weather import  *
import datetime
import  randfacts
engine = pts.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',175)
voices =engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speack(text):
    engine.say(text)
    engine.runAndWait()
def sayHi():
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour <12:
        return 'morning'
    if hour>=12 and hour<16:
        return 'afternoon'
    else:
        return 'evening'

today=datetime.datetime.now()

r = sp.Recognizer()
speack("Hello Sir , Good "+sayHi()+", my name is nova , And I am your voice assistant")
speack("Today is ,"+today.strftime("%d")+  " ,of "+today.strftime('%B') +", and its currently "+today.strftime("%I") +today.strftime("%M") + today.strftime("%p") )
# %d = day of month 1-->31 ---------- %B = Month name with full version December %b -->small version
speack("Temperature in your city is , " +str(temp())+", degree with "+str(des()))

speack("What can I do for you?")
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

elif 'fact' or 'facts' in text2 :
    speack('Sure ,give me one second ')
    fact= randfacts.getFact()
    print(fact)
    print(fact)
    speack('Did you know that ,'+fact)

elif 'joke' or 'jokes' in text2:
    speack('Sure ,get ready for some chukles ')
    arr=joke()
    print(arr[0])
    print(arr[0])
    speack(arr[1])
    speack(arr[1])
    speack('So funny heeh')