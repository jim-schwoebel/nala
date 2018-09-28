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
##                            MEDITATION.PY                                 ##
##############################################################################

Meditation is known to help alleviate stress. In this action, we guide the 
user through a 60 second meditation to breathe deeply in and out.
'''

##############################################################################
##                            IMPORT STATEMENTS                             ##
##############################################################################

import time, pygame, datetime, webbrowser, ftplib, getpass, os, importlib
import random, platform, json, sys
import pyttsx3 as pyttsx 

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def playbackaudio(question,filename):
#takes in a question and a filename to open and plays back the audio file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    print(question)
    return "playback completed"

def get_date():
    return str(datetime.datetime.now())

def speaktext(hostdir, text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

##############################################################################
##                            MAIN SCRIPT.                                  ##
##############################################################################
hostdir=sys.argv[1]

speaktext(hostdir, 'Now I will let James guide you through a meditation.')
playbackaudio("Starting meditation", "startmeditation.mp3")

time.sleep(5)

for i in range(6):
    playbackaudio("Breathe in, deeply", "breathein.mp3")
    time.sleep(5)
    playbackaudio("Breathe out, deeply", "breatheout.mp3")
    time.sleep(5)

# update database 
os.chdir(hostdir)
database=json.load(open('registration.json'))
name=database['name']
speaktext(hostdir, 'Hope you feel better now, %s. I am here for you if you need anything else.'%(name.split()[0]))
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'meditation.py',
    'date': get_date(),
    'meta': ['60 seconds'],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

