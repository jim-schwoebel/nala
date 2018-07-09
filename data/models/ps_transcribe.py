'''

Load pocketsphinx language model for use with Nala.

'''

from os import environ, path
import sys
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

# Get all the directories right

def transcribe(HOSTDIR, SAMPLEDIR):
  
    ##HOSTDIR = sys.argv[1]
    ##SAMPLEDIR = sys.argv[2]
    if HOSTDIR[-1] != '/':
        HOSTDIR = HOSTDIR+'/'
        
    MODELDIR = HOSTDIR+"data/models"
    DATADIR = HOSTDIR+"data/wakewords"

    # Create a decoder with certain model
    config = Decoder.default_config()
    config.set_string('-hmm', MODELDIR+'/en-us')
    config.set_string('-lm', MODELDIR+'/6008.lm')
    config.set_string('-dict', MODELDIR+'/6008.dic')
    decoder = Decoder(config)

    # Decode streaming data.
    decoder = Decoder(config)
    decoder.start_utt()
    stream = open(path.join(DATADIR, 'sample0_0.wav'), 'rb')
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
