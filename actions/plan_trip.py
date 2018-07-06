'''
Get flights.

'''
from bs4 import BeautifulSoup
import os, requests, json, webbrowser 

def curloc():
    # get current location, limit 1000 requests/day
    r=requests.get('http://ipinfo.io')
    location=r.json()
    return location

airports=json.load(open('airport_data.json'))
cities=list(airports)

origin=input('where are you traveling from?')
destination=input('where are you traveling to?')
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

leave_date=input('what date are you leaving? (e.g. 2018-06-05)')
return_date=input("what time are you returning? (e.g. 2018-06-07")

url='https://www.kayak.com/flights/%s-%s/%s/%s?sort=bestflight_a'%(origin_code, destination_code, leave_date, return_date)

# in this case opening up the webbrowser makes sense because the soup is not available
webbrowser.open(url)

# now open airbnb 
city=destination
url='https://www.airbnb.com/s/%s--United-States/homes?refinement_paths'%(city)
other='%5B%5D=%2Fhomes&allow_override%5B%5D=&'
other2='checkin=%s&checkout=%s&s_tag=GDvS2YuG'%(leave_date,return_date)
url=url+other+other2

webbrowser.open(url)

#page=requests.get(url)
#soup=BeautifulSoup(page.content,'lxml')

                  
