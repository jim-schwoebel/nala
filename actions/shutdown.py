'''
Shutdown.py

Simple program to shutdown computer using environment vars and terminal.
'''
import os

command = 'shutdown -h now'
os.system('echo %s|sudo -S %s'%(os.environ['SUDO_PASSWORD'], command))
