'''
setup.py

For installing all dependencies for nala.
'''
import os

# need to fix pocketsphinx for custom language model 
# https://github.com/watsonbox/homebrew-cmu-sphinx
os.system('brew uninstall pocketsphinx')
os.system('brew tap watsonbox/cmu-sphinx')
os.system('brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase')
os.system('brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx')

# prompt user if they want to integrate with google? / open up docs to setup env vars 
# set up env var for host password 

def pip_install(modules):
    for i in range(len(modules)):
        os.system('pip3 install %s'%(modules[i]))

def brew_install(modules):
    for i in range(len(modules)):
        os.system('brew install %s'%(modules[i]))

brew_modules=['portaudio', 'ffmpeg', 'sox', 'shpotify']

# ADD ACTIONS MODULES 
pip_modules=['ftplib', 'smtplib', 'getpass', 'pyaudio','pygame'
             'wave','shutil','importlib','geocoder','librosa',
             'urrllib','random','webbrowser','pyperclip','pydub',
             'array','struct','soundfile','pandas','numpy',
             'bs4','cryptography','pyscreenshot','pyautogui',
             'cv2','readchar','psutil','SpeechRecognition',
             'pyttsx3','soundfile','skvideo','moviepy','PIL']

brew_install(brew_modules)
pip_install(pip_modules)

# done! now you're ready
