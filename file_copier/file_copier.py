'''
A simple script that copies the info.log to my Google Drive every minute.

Mischa van den Burg
www.mischavandenburg.com
test
'''

from pathlib import Path 
import time, shutil

log_location = Path('C:/Users/Mischa/bot/15feb/botty/info.log')
log_destination = Path('C:/Users/Mischa/Mijn Drive/2 - Diablo 2/Stats')

print('Starting copying. Press Ctrl + C to abort.')

while True:
    shutil.copy(log_location, log_destination)
    print('Copied.')
    time.sleep(60)

