
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
##                            EVENTS.PY .                                   ##
##############################################################################

Get events around you using Meetup.com (specific to categories).

Defaults to tech but can be any one of these categories on meetup.com:

Outdoors adventure, tech, parents family, health and wellness, sports
and fitness, education, photography, food, writing, language, music,
movements, lgbtq, film, games/scifi, beliefs, arts/culture, book-clubs,
dancing, pets, hobbies/crafts, fashion/beauty, social, career-business.

'''


##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

from bs4 import BeautifulSoup
import random, os, requests, time, getpass, webbrowser, datetime, sys
import ftplib, platform, json 
import pyttsx3 as pyttsx

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def speaktext(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def curloc():
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    return location

def cleanlist(listname,cleanstart,cleanend,stopwords):
    h=list()
    if stopwords==[]:
        for i in range(len(listname)):
            element=str(listname[i]).replace(cleanstart,'').replace(cleanend,'')
            h.append(element)
    else:
         for i in range(len(listname)):
            element=str(listname[i]).replace(cleanstart,'').replace(cleanend,'')
            for j in range(len(stopwords)):
                element=element.replace(stopwords[j],'')
                
            h.append(element)
            
    return h 
    
def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

# get events around you in your city
location=curloc()
city=location['city']

# links

urls=['https://www.meetup.com/find/outdoors-adventure/',
      'https://www.meetup.com/find/tech/',
      'https://www.meetup.com/find/parents-family/',
      'https://www.meetup.com/find/health-wellness/',
      'https://www.meetup.com/find/sports-fitness/',
      'https://www.meetup.com/find/education/',
      'https://www.meetup.com/find/photography/',
      'https://www.meetup.com/find/food/',
      'https://www.meetup.com/find/writing/',
      'https://www.meetup.com/find/language/',
      'https://www.meetup.com/find/music/',
      'https://www.meetup.com/find/movements/',
      'https://www.meetup.com/find/lgbtq/',
      'https://www.meetup.com/find/film/',
      'https://www.meetup.com/find/games-sci-fi/',
      'https://www.meetup.com/find/beliefs/',
      'https://www.meetup.com/find/arts-culture/',
      'https://www.meetup.com/find/book-clubs/',
      'https://www.meetup.com/find/dancing/',
      'https://www.meetup.com/find/pets/',
      'https://www.meetup.com/find/hobbies-crafts/',
      'https://www.meetup.com/find/fashion-beauty/',
      'https://www.meetup.com/find/social/',
      'https://www.meetup.com/find/career-business/']

rand=random.randint(0,len(urls)-1)

# create a list of URLs to scrape
link=urls[rand]
category=link[len('https://www.meetup.com/find/')-1:-1]
topic=link[0:27].replace('/','').replace('-',' ')

# now get urls 
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')

orgname=cleanlist(soup.find_all('h3',class_='padding-none inline-block loading'),'<h3 class="padding-none inline-block loading" itemprop="name">','</h3>',['\n', '  ','\t'])
sizeorg=cleanlist(soup.find_all('p',class_='small ellipsize'),'<p class="small ellipsize">','</p>',['  ','\t','\n'])
links=soup.find_all('a',class_='display-none')

links2=list()
for i in range(len(links)):
    ind=str(links[i]).find('">')
    links2.append(str(links[i])[0:ind])

links2=cleanlist(links2,'<a class="display-none" href="','>',[])
rand=random.randint(0,len(links2)-1)
link=links2[rand]
orgname=link[22:].replace('-',' ').replace('/','')

#default description of the group
time.sleep(0.5)
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')

#date
date_sample=cleanlist(soup.find_all('span',class_='eventTimeDisplay-startDate'),'','',[])
date2_sample2=list()
time2_sample2=list()
for j in range(0,len(date_sample),2):
    date2_sample=date_sample[j]
    date2_sample2.append(date2_sample)
for j in range(1,len(date_sample),2):
    time2_sample=date_sample[j]
    time2_sample2.append(time2_sample)
date2=date2_sample2
time2=time2_sample2

nextevent=BeautifulSoup(date2[0]).get_text()

# description 
time.sleep(0.5)
page=requests.get(link+'?scroll=true')
soup=BeautifulSoup(page.content,'html.parser')

try:
    descriptions=cleanlist(soup.find_all('div',class_='group-description runningText'),'<div class="group-description runningText" style="height:175px"><div><div class="chunk"><p>','</p></div></div></div>',[])
    descriptions=BeautifulSoup(descriptions[0]).get_text()
    descriptions=descriptions.split('.')
    # make descriptions first 2 sentences 
    description=descriptions[0]+' ' + descriptions[1]
except:
    description='none'

webbrowser.open(link)

if description != 'none':
    speak_text='Check out %s. %s. The next event scheduled is %s'%(orgname, description, nextevent)
    speaktext(speak_text)

else:
    speak_text='Check out %s. The next event scheduled is %s'%(orgname, nextevent)
    speaktext(speak_text)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'events.py',
    'date': get_date(),
    'meta': [link, links2, speak_text],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()
