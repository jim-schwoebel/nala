'''
Shutdown.py

Simple program to shutdown computer using environment vars and terminal.
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
    'action': 'shutdown.py',
    'date': get_date(),
    'meta': [],
}

action_log.append(action)
database['action log']=action_log

jsonfile=open('actions.json','w')
json.dump(database,jsonfile)
jsonfile.close()

# now do the command
command = 'shutdown -h now'
os.system('echo %s|sudo -S %s'%(os.environ['SUDO_PASSWORD'], command))
