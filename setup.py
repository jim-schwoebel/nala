'''
setup.py

For installing all dependencies for nala.
'''
import os

def pip_install(modules):
    for i in range(len(modules)):
        os.system('pip3 install %s'%(modules[i]))

def brew_install(modules):
    for i in range(len(modules)):
        os.system('brew install %s'%(modules[i]))

brew_modules=['portaudio',
              'shpotify']

pip_modules=['',
             '',
             '',
             '',
             '',
             '',
             '',
             '',
             '',
             '']

brew_install(brew_modules)
pip_install(pip_modules)

# need to fix pocketsphinx for custom language model 
# https://github.com/watsonbox/homebrew-cmu-sphinx
os.system('brew uninstall pocketsphinx')
os.system('brew tap watsonbox/cmu-sphinx')
os.system('brew install --HEAD watsonbox/cmu-sphinx/cmu-sphinxbase')
os.system('brew install --HEAD watsonbox/cmu-sphinx/cmu-pocketsphinx')

# test pocketsphinx with this command (can exit out of screen whenever).
os.system('pocketsphinx_continuous -inmic yes')

# done! now you're ready
