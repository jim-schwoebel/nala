'''
Reboot.py

Simple command to reboot the computer from the terminal.
'''
import os

command = 'reboot'
os.system('echo %s|sudo -S %s'%(os.environ['SUDO_PASSWORD'], command))
