'''
Get flights.

'''
##############################################################################
##                           IMPORT STATEMENTS                              ##
##############################################################################

from bs4 import BeautifulSoup
import os, requests, json, webbrowser, sys, datetime, pygame, time, pyaudio
import wave, shutil
import speech_recognition as sr_audio

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

def playbackaudio(filename):
    # takes in a question and a filename to open and plays back the audio
    # file and prints on the screen the question for the user 
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    return "playback completed"

def speaktext(hostdir,text,playback):
    # speak to user from a text sample (tts system)  
    curdir=os.getcwd()
    os.chdir(hostdir+'/actions') 
    os.system("python3 speak.py '%s'"%(str(text)))
    if playback == True:
        playbackaudio(hostdir+'/data/tone.wav')
    os.chdir(curdir)

def transcribe_audio_google(filename):
    # transcribe the audio (note this is only done if a voice sample)
    r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        audio = r.record(source) 
    text=r.recognize_google_cloud(audio)

    return text  

def record_to_file(path,filename,recordtime):

    # record 3 second voice file 
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 1 
    RATE = 16000 #sample rate
    RECORD_SECONDS = recordtime
    WAVE_OUTPUT_FILENAME = filename

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def reformat_date(transcript):
    transcript=transcript.lower()

    # get back month by formal transcription 
    months=['january','february','march','april','may','june',
            'july','august','september','october','november','december']

    month = transcript.split()

    for i in range(len(month)):
        if month[i] in months:
            if month[i]=='january':
                out_month='01'
            elif month[i]=='february':
                out_month='02'
            elif month[i]=='march':
                out_month='03'
            elif month[i]=='april':
                out_month='04'
            elif month[i]=='may':
                out_month='05'
            elif month[i]=='june':
                out_month='06'
            elif month[i]=='july':
                out_month='07'
            elif month[i]=='august':
                out_month='08'
            elif month[i]=='september':
                out_month='09'
            elif month[i]=='october':
                out_month='10'
            elif month[i]=='november':
                out_month='11'
            elif month[i]=='december':
                out_month='12'

    out_year=str(datetime.datetime.now().year)

    # get back numbers by removing characters 
    chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z',' ','.',"'",'<','>','"',
            '[',']','-','=','+','(',')','*','&','^','%','$','#','@','!','~',
            '`']

    day=transcript

    for i in range(len(chars)):
        day=day.replace(chars[i],'')

    if day in ['1','2','3','4','5','6','7','8','9']:
        day = '0'+day

    out_day=day

    formatted_date=out_year+'-'+out_month+'-'+out_day
    
    return formatted_date 

def clean_city(city):
    if city == 'new york city':
        city = 'new york'
        
    return city 
##############################################################################
##                            MAIN SCRIPT                                   ##
##############################################################################

hostdir=sys.argv[1]
airports=json.load(open('airport_data.json'))
cities=list(airports)

os.chdir(hostdir+'/data/actions')

speaktext(hostdir, 'where are you traveling from?', True)
record_to_file(os.getcwd(),'from.wav', 3.0)
origin=clean_city(transcribe_audio_google('from.wav').lower()[0:-1])
print(origin)


speaktext(hostdir, 'where are you traveling to?', True)
record_to_file(os.getcwd(),'to.wav', 3.0)
destination=clean_city(transcribe_audio_google('to.wav').lower()[0:-1])
print(destination)

origin_city=''
destination_city=''

for i in range(len(cities)):
    #get origin city / destination 
    if cities[i].lower().find(origin) >= 0:
        origin_city=cities[i]
    if cities[i].lower().find(destination) >= 0:
        destination_city=cities[i]

speaktext(hostdir, 'what date are you leaving? (for example, April twenty fifth)', True)
record_to_file(os.getcwd(),'leave_date.wav', 3.0)
transcript=transcribe_audio_google('leave_date.wav')
leave_date=reformat_date(transcript)
print(leave_date)

speaktext(hostdir, 'what time are you returning? (for example, May first)', True)
record_to_file(os.getcwd(),'return_date.wav', 3.0)
transcript=transcribe_audio_google('return_date.wav')
return_date=reformat_date(transcript)
print(return_date)

# get airport codes
origin_code=airports[origin_city]
destination_code=airports[destination_city]

speaktext(hostdir, 'Great! Here are some flights and air bee and bees during those dates.', False)

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

# update database 
hostdir=sys.argv[1]
os.chdir(hostdir)
database=json.load(open('actions.json'))
action_log=database['action log']
loopnum=database['loopnum']

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

# rename the files now that you know the loopnumber 
os.chdir(hostdir+'/data/actions')
os.rename('leave_date.wav',str(loopnum)+'_'+'leave_date'+'_'+leave_date+'.wav')
os.rename('return_date.wav',str(loopnum)+'_'+'return_date'+'_'+return_date+'.wav')
os.rename('from.wav',str(loopnum)+'_'+'origin'+'_'+origin+'.wav')
os.rename('to.wav',str(loopnum)+'_'+'destination'+'_'+destination+'.wav')

# go back to host directory 
os.chdir(hostdir)
                  
