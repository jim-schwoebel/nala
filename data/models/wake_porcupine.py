'''
wake_porcupine.py

simple wrapper to call the porcupine wake script
'''
import os

os.chdir('porcupine')
os.system('python3 wake_porcupine.py --keyword_file_paths hey_nala_mac.ppn') 
