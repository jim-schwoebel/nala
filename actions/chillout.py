'''
############################################################################
##                         NALA REPOSITORY                                ##
############################################################################

repository name: nala 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/nala 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: Nala is an open source voice assistant. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (nala) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

##############################################################################
##                            LICENSE TERMS                                 ##
##############################################################################

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

##############################################################################
##                            SERVICE STATEMENT                             ##
##############################################################################

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

##############################################################################
##                            CHILLOUT.PY                                   ##
##############################################################################
Setup chill music.

Note that before you run this script you should purchase all the songs 
in the playlist so you don't run into issues with copyright infringement.
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
        
