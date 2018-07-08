'''
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

