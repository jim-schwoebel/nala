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
##                            YELP.PY                                       ##
##############################################################################

Find a local coffee shop based on your current location using Yelp.

'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import pyttsx3 as pyttsx
import requests, time, datetime, ftplib, platform, json, getpass, os, sys
from bs4 import BeautifulSoup
import random, webbrowser

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def speaktext(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

def curloc():
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    return location

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

keyword = sys.argv[2].lower()

if keyword not in ['coffee', 'restaurants', 'food', 'nightlife', 'ice cream', 'beer', 'beers']:
    keyword='Coffee+%26+Tea'
elif keyword in ['restaurants', 'food']:
    keyword = 'Restaurants'
elif keyword == 'coffee':
    keyword='Coffee+%26+Tea'
elif keyword == 'nightlife':
    keyword='Nightlife'
elif keyword == 'ice cream':
    keyword='Ice+Cream'
elif keyword in ['beer', 'beers']:
    keyword='Bars'

location=curloc()
city=location['city']
url='https://www.yelp.com/search?find_desc=%s&find_loc=%s&start=30'%(keyword,city.lower())

print('connecting to %s'%(url))

page=requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
linklist=soup.find_all('a')
# print(linklist)
linklist2=list()

for c in range(len(linklist)):
    try:
        tlink=linklist[c]['href']
        if tlink[0:4]=='/biz':
            # print(linklist[c]['href'])
            i1=linklist[c]['href'].find('?')
            tlink='https://www.yelp.com'+linklist[c]['href'][0:i1]
            if tlink not in linklist2 and tlink.find('popup')<0:
                linklist2.append(tlink)
    except:
        pass

print('found %s links'%(str(len(linklist2))))
entrylist=list()

rand=random.randint(0,len(linklist2)-1)
link=linklist2[rand]
yelplink=link
time.sleep(1)
print('pulling data from %s'%(link))
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')

#get link
try:
    g=soup.find_all('a')
    h=list()
    for q in range(len(g)):
        if str(g[q]).count('/biz_redir?url=http%3A%2F%2F')>0:
            h.append(g[q])
    #link
    weblink='http://www.'+str(h[0].get_text())
except:
    weblink='n/a'

#name and address
try:
    j=soup.find_all('div',class_='media-story')
    sample=str(j[0])
    i1=sample.find('<span>')
    sample=sample[i1+len('<span>'):]
    i2=sample.find('</span>')
    name=str(sample[0:i2])
    i3=sample.find('<address')
    sample=sample[i3+len('<address>'):]
    i4=sample.find('</address>')
    address=str(sample[0:i4]).replace('\n','').replace('  ','')
except:
    name='n/a'
    address='n/a'

#get reviews
try:
    k=soup.find_all('p')
    klist=list()
    for l in range(len(k)):
        kstring=str(k[l].get_text())
        if kstring.count('people voted for this review')>0:
            pass
        elif kstring.count('Was this review …?')>0:
            pass
        elif kstring.count('First, try refreshing the page and clicking Current Location again.')>0 or kstring.count("If you're still having trouble")>0:
            pass
        elif kstring.count('You can also search')>0 or kstring.count("Oops! We don't recognize the web browser you're currently using.")>0 or kstring.count('Ask the Yelp community!')>0:
            pass
        else:
            klist.append(str(k[l].get_text()))
    reviews=klist
except:
    reviews='n/a'

#ratingsinfo
try:
    m=soup.find_all('p',class_='rating-details-ratings-info')
    ratingsinfo=str(m[0].get_text())
except:
    ratingsinfo='n/a'

entry=[keyword,location,yelplink,weblink,name,address,reviews,ratingsinfo]

rand=random.randint(0,len(reviews)-1)
review=reviews[rand].replace('\n','').replace('}','').replace('{','')

if weblink=='n/a':
    webbrowser.open(yelplink)
else:
    webbrowser.open(weblink)
    
speak_text='You should check out %s at %s. %s'%(name, address, review)
speaktext(speak_text)

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'search.py',
    'date': get_date(),
    'meta': [keyword, linklist2, entry, speak_text],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()
