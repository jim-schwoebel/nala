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
##                            PLAN_TRIP.PY                                  ##
##############################################################################

Get flights and AirBnBs for US city trips.

'''
##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

from bs4 import BeautifulSoup
import os, requests, json, webbrowser, sys, datetime

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def curloc():
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    return location

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

airports=json.load(open('airport_data.json'))
cities=list(airports)

origin=input('where are you traveling from? \n')
destination=input('where are you traveling to? \n')
origin_city=''
destination_city=''

for i in range(len(cities)):
    #get origin city / destination 
    
    if cities[i].lower().find(origin) >= 0:
        origin_city=cities[i]
        
    if cities[i].lower().find(destination) >= 0:
        destination_city=cities[i]

# get airport codes
origin_code=airports[origin_city]
destination_code=airports[destination_city]

leave_date=input('what date are you leaving? (e.g. 2018-06-05) \n')
return_date=input("what time are you returning? (e.g. 2018-06-07 \n")

url='https://www.kayak.com/flights/%s-%s/%s/%s?sort=bestflight_a'%(origin_code, destination_code, leave_date, return_date)
flighturl=url
# in this case opening up the webbrowser makes sense because the soup is not available
webbrowser.open(url)

# now open airbnb 
city=destination
url='https://www.airbnb.com/s/%s--United-States/homes?refinement_paths'%(city)
other='%5B%5D=%2Fhomes&allow_override%5B%5D=&'
other2='checkin=%s&checkout=%s&s_tag=GDvS2YuG'%(leave_date,return_date)
url=url+other+other2
airbnburl=url

webbrowser.open(url)

#page=requests.get(url)
#soup=BeautifulSoup(page.content,'lxml')

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'plan_trip.py',
    'date': get_date(),
    'meta': [flighturl, airbnburl],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

                  
