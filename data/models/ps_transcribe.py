'''

Load pocketsphinx language model for use with Nala.

'''

from os import environ, path
import sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

# Get all the directories right

def transcribe(HOSTDIR, SAMPLE):
    
    # fix host directory if it doesn't contain a '/'
    
    if HOSTDIR[-1] != '/':
        HOSTDIR = HOSTDIR+'/'
    SAMPLEDIR = HOSTDIR+SAMPLE
    MODELDIR = HOSTDIR+"data/models"
    DATADIR = HOSTDIR+"data/wakewords"

    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', MODELDIR+'/en-us')
    config.set_string('-lm', MODELDIR+'/TAR7051/7051.lm')
    config.set_string('-dict', MODELDIR+'/TAR7051/7051.dic')
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(SAMPLEDIR, 'rb')
    while True:
      buf = stream.read(1024)
      if buf:
        decoder.process_raw(buf, False, False)
      else:
        break
    decoder.end_utt()

    print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
    output=[seg.word for seg in decoder.seg()]
    output.remove('<s>')
    output.remove('</s>')

    transcript = ''
    for i in range(len(output)):
        if i == 0:
            transcript=transcript+output[i]
        else:
            transcript=transcript+' '+output[i]

    transcript=transcript.lower()
    print('transcript: '+transcript)

    return transcript
  
# now pass transcript into speech recognition services. 
