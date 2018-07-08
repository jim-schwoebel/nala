'''
Turnoff.py

Simple script to turn off all python scripts using sys.exit()
'''
import os, sys, datetime, json

def get_date():
    return str(datetime.datetime.now())

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']

action={
    'action': 'turnoff.py',
    'date': get_date(),
    'meta': [],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

# turn off python script 
sys.exit()
