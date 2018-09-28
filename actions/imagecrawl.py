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
##                           IMAGECRAWL.PY                                  ##
##############################################################################

PDF2Image: https://github.com/Belval/pdf2image

Can scale with http://docs.python-guide.org/en/latest/scenarios/scrape/
'''

##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract, argparse, cv2, os, tempfile, json, time, pdfkit, sys, datetime
import pyttsx3 as pyttsx 
                
##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def speak_text(text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']
loopnum=database['loopnum']

os.chdir(hostdir+'/data/actions/')
link=sys.argv[2]

filename='imagecrawl_%s.pdf'%(str(loopnum))
pdfkit.from_url(link, filename)
pdf_path=os.getcwd()+'/'+filename
images=convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm')

text_list=''
# load the example image and convert it to grayscale
for i in range(len(images)):
        image = images[i]
        ## testing image.show()
        text = pytesseract.image_to_string(image)
        print(text)
        text_list=text_list+text

speak_text(text_list[250:500])

os.chdir(hostdir)
action={
    'action': 'imagecrawl.py',
    'date': get_date(),
    'meta': [filename,link,text_list],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

