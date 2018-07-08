'''
Setup chill music 
'''
from pytube import Playlist
import pyttsx3 as pyttsx 
import random, webbrowser, librosa, os, time, pygame, datetime, json

def speaktext(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def playaudio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def get_date():
    return str(datetime.datetime.now())

start=get_date()
curdir=os.getcwd()
listdir=os.listdir()

if 'data' not in listdir:
    os.mkdir(curdir+'/data')
    os.chdir(curdir+'/data')
    speaktext('downloading playlist...')
    pl=Playlist("https://www.youtube.com/watch?v=Uf8AP2Yhr9k&list=PL11Wnnyw47LpkF3McMjHwG0HZ23CcfYUX")
    pl.download_all()
    for i in range(len(listdir)):
        if listdir[i][-4:]=='.mp4':
            print(listdir[i])
            os.rename(listdir[i],str(i)+'.mp4')
            os.system('ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s'%(str(i)+'.mp4',str(i)+'.wav'))

else:
    os.chdir(os.getcwd()+'/data')

listdir=os.listdir()
random.shuffle(listdir)
t=1

for i in range(len(listdir)):
    try:
        print('playing '+listdir[i])
        playaudio(listdir[i])
        y,sr=librosa.load(listdir[i])
        duration=librosa.core.get_duration(y=y,sr=sr)
        time.sleep(duration)
    except:
        pass 

speaktext('playlist is done!')

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']
end=get_date()

action={
    'action': 'chillout.py',
    'date': get_date(),
    'meta': [start, end],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()
        
