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
##                            ESPN.PY                                       ##
##############################################################################
Get sports games.

ESPN website.
'''
import datetime, os, requests, webbrowser, sys, json
from bs4 import BeautifulSoup
import pyttsx3 as pyttsx
# get user location

def speaktext(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

url='http://www.espn.com/'

# sport_type=['nba', 'wnba', 'nfl','mlb','nhl','mls','ncaaf']
sport_type=sys.argv[2].lower()
if sport_type not in ['nba', 'wnba', 'nfl','mlb','nhl','mls','ncaaf']:
    sport_type = 'nba'

now=str(datetime.datetime.now())[0:10]
date='/schedule/_/date/%s'%(now)

url=url+sport_type+date

page=requests.get(url)
soup=BeautifulSoup(page.content, 'lxml')

#get table elements 
y=soup.find_all('tr')
dates=soup.find_all(class_='table-caption')

datecount=0
datelist=list()
descriptions=list()

for i in range(len(y)):
    try:
        if y[i].get_text().lower() == 'no games scheduled':
            date=dates[datecount].get_text()
            description='no games scheduled'
            descriptions.append(description)
            datelist.append(date)
            datecount=datecount+1 
        elif y[i].find_all(class_='matchup')[0].get_text().lower()=='matchup':
            date=dates[datecount].get_text()
            description=y[i+2].get_text()
            description_2=y[i+1].get_text()
            i2=description_2.find('tickets')
            description_2=description_2[0:i2].replace(',','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
            description=description+' '+description_2
            descriptions.append(description.replace('matchuptime\xa0(ET)nat tvaway tvhome tv ','').replace('matchuptime\xa0(ET)nat tvticketslocation ',''))
            datelist.append(date)
            datecount=datecount+1
        else:
            pass 
    except:
        pass 

print(descriptions)
print(datelist)

tonight=descriptions[0]
if tonight.lower()=='no games scheduled':
    speaktext('no games scheduled tonight')
else:
    speaktext('tonight %s is on ESPN'%(tonight))
        
# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'espn.py',
    'date': get_date(),
    'meta': [datelist, descriptions],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()
