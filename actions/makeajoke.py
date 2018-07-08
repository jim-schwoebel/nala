'''
Makeajoke.py

Action to call Nala and make a joke.
'''
##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

import random, os, sys, json, datetime

##############################################################################
##                            HELPER FUNCTIONS                              ##
##############################################################################

def get_date():
    return str(datetime.datetime.now())

def speaktext(hostdir,text):
    # speak to user from a text sample (tts system)  
    curdir=os.getcwd()
    os.chdir(hostdir+'/actions') 
    os.system("python3 speak.py '%s'"%(str(text)))
    os.chdir(curdir)

##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################
    
hostdir=sys.argv[1]
os.chdir(hostdir)

jokes=['What do you call a speeding french motorist? A speeding Monseiur.',
       'What do chemists’ dogs do with their bones? They barium!',
       'What did the cat say when the mouse got away? You’ve got to be kitten me!',
       'What did the ocean\xa0say to the sailboat? Nothing, it just waved.',
       'What do you call a snowman in July? A puddle.',
       'What lies at the bottom of the ocean and twitches? A nervous wreck.',
       'What does a dolphin say when he’s confused? Can you please be more Pacific?',
       'What is a Queens favorite kind of precipitation? Reign!',
       'What is the Mexican weather report? Chili today and hot tamale.',
       'What did the evaporating raindrop say? I’m going to pieces.',
       'What did the hail storm say to the roof? Hang onto your shingles, this will be no ordinary sprinkles.',
       'What do you call a wet bear? A drizzly bear',
       'What do you call two straight days of rain in Seattle? A weekend.',
       'What goes up when the rain comes down? An Umbrella.',
       'What does it do before it rains candy? It sprinkles!',
       'What did one raindrop say to the other? Two’s company, three’s a cloud',
       'What’s the difference between a horse and the weather? One is reined up and the other rains down.',
       'What is a king’s favorite kind of precipitation? Hail!',
       'What kind of music are balloons afraid of? Pop Music',
       'What is the musical part of a snake? The scales.',
       'What did Beethoven say to Johann Sebastian when he was helping him parallel park? “Bach it up.”',
       'What’s an avocado’s favorite music? Guac ‘n’ roll.',
       'What do you get when you drop a piano down a mineshaft? A-flat minor.',
       'What do you call a cow that can play a musical instrument? A moo-sician.',
       'What do you call a musician with problems? A trebled man.',
       'What was Beethoven’s favorite fruit? BA-NA-NA-NAAAAAA.',
       'What did Jay-Z call his wife before they got married? Feyonce.',
       'What’s a golf clubs favorite type of music? Swing.']

# tell a random joke 
randomint=random.randint(0,len(jokes)-1)
joke = jokes[randomint]
speaktext(hostdir, joke)

# update database
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action':'makeajoke.py',
    'date': get_date(),
    'meta': [joke],
}

action_log.append(action)
jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()


