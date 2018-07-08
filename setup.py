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

# done! now you're ready
