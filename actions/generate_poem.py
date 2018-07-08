'''
Generate a random poem and read it through TTS.

Trained on my own poems :) 
'''

##############################################################################
##                            IMPORT STATEMENTS                             ##
##############################################################################

import speech_recognition as sr
import nltk, os, re, random, datetime, sys, json
from nltk import FreqDist
from collections import Counter
import numpy as np 
from textblob import TextBlob
from nameparser.parser import HumanName
from nltk.corpus import genesis
import pyttsx3 as pyttsx 

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def randselect(stringlist):
    length=len(stringlist)-1
    randnum=random.randint(0,length)
    return stringlist[randnum]

def speaktext(hostdir, text):
    # speak to user from a text sample (tts system)
    engine = pyttsx.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.fiona')
    engine.say(text)
    engine.runAndWait()

def get_date():
    return str(datetime.datetime.now())

##############################################################################
##                            MAIN SCRIPT.                                  ##
##############################################################################

# get hostdir from argv passthrough variable
hostdir=sys.argv[1]

# load poems for training 
poetry=open('poetry.txt', encoding="utf8").read()

os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']
loopnum=database['loopnum']

# now go to actions data directory to store poem 
os.chdir(hostdir+'/data/actions/')
tokens=poetry.split()

# get text tags and tokens 
text=nltk.Text(tokens)
tags=nltk.pos_tag(text)

# initialize lists for loop 
verbs=list()
##['VB','VBD']
nouns=list()
##['NN','NNS']
adjectives=list()
##['JJ','JJS']
adverbs=list()
##['RB','RBS']
vbed=list()
ned=list()
eadj=list()
nounend=list()

# specity random poem field 
randompoem= 'y'

if randompoem in ['y','yes']:

    for i in range(len(tags)):
        if tags[i][1] in ['VB','VBD']:
            verbs.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                vbed.append(tags[i][0])
        elif tags[i][1] in ['NN','NNS']:
            nouns.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                ned.append(tags[i][0])   
        elif tags[i][1] in ['JJ','JJS']:
            adjectives.append(tags[i][0])
            if tags[i][0].endswith('e')==True:
                eadj.append(tags[i][0])
        elif tags[i][1] in ['RB','RBS']:
            adverbs.append(tags[i][0])
        else:
            pass
    poemname=randselect(nouns)
    #random selection of a noun
    description='I feel %s and %s and %s toward %s'%(randselect(adjectives),randselect(adjectives),randselect(adjectives),poemname)
    #I feel [adjective] and [adjective] and [adjective] towards [poemname].
    tokens2=description.split()
    text2=nltk.Text(tokens)
    tags2=nltk.pos_tag(text)
    name=poemname.title()

    for i in range(len(tags)):
        if tags[i][1] in ['NN','NNS']:
          if tags[i][0].endswith(name[len(name)-1])==True:
                nounend.append(tags[i][0])     

    #make a poem - funny 
    poem=open('poem_'+str(loopnum)+'_'+name+'.txt','w')
    poem.write(name)
    for i in range(5):
        poem.write('\n\n')
        #X5 stanzas
        poem.write("I seek a %s %s \n"%(randselect(adjectives),name))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("Why is it %s to %s? \n"%(randselect(adverbs),randselect(verbs)))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("The %s is a %s %s \n"%(randselect(nouns),randselect(adjectives),randselect(nounend)))

    poem.close()
               
elif randompoem in ['n','no']:
    poemname=input('what is the name of the poem? (noun)')
    description=input('what is the description?')
    tokens2=description.split()
    text2=nltk.Text(tokens)
    tags2=nltk.pos_tag(text)
    name=poemname.title()

    for i in range(len(tags)):
        if tags[i][1] in ['VB','VBD']:
            verbs.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                vbed.append(tags[i][0])
        elif tags[i][1] in ['NN','NNS']:
            nouns.append(tags[i][0])
            if tags[i][0].endswith('ed')==True:
                ned.append(tags[i][0])
            if tags[i][0].endswith(name[len(name)-1])==True:
                nounend.append(tags[i][0])        
        elif tags[i][1] in ['JJ','JJS']:
            adjectives.append(tags[i][0])
            if tags[i][0].endswith('e')==True:
                eadj.append(tags[i][0])
        elif tags[i][1] in ['RB','RBS']:
            adverbs.append(tags[i][0])
        else:
            pass

    #make a poem - funny 
    poem=open('poem_'+str(loopnum)+'_'+name+'.txt','w')
    poem.write(name)
    for i in range(5):
        poem.write('\n\n')
        #X5 stanzas
        poem.write("I seek a %s %s \n"%(randselect(adjectives),name))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("Why is it %s to %s? \n"%(randselect(adverbs),randselect(verbs)))
        poem.write("The %s is %s \n"%(randselect(nouns),randselect(eadj)))
        poem.write("The %s is a %s %s \n"%(randselect(nouns),randselect(adjectives),randselect(nounend)))

    poem.close()

poem_name='poem_'+str(loopnum)+'_'+name+'.txt'
poem_text=open(poem_name).read().replace(' \n',',')
speaktext(hostdir, 'I call this poem %s'%(name))
speaktext(hostdir,poem_text)
os.chdir(hostdir)

action={
    'action': 'generate_poem.py',
    'date': get_date(),
    'meta': [poem_text],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

