'''
A simple script that copies the info.log and contents of the stats folder to my Google Drive every minute.

Mischa van den Burg
www.mischavandenburg.com

'''

from pathlib import Path, PurePath
import time, shutil


# log_location = Path(Path.home() / 'bot' / '15feb' / 'botty' / 'info.log')
log_location = '/Users/mischa/bot/info.log'

# log_destination = Path(/Users/mischa/Google Drive/My Drive/2 - Diablo 2/Stats)

#log_destination = PurePath('Users' / 'mischa' / 'Google Drive' / 'My Drive' / '2 - Diablo 2' / 'Stats')

log_destination = '/Users/mischa/Google Drive/My Drive/2 - Diablo 2/Stats'

print('Starting copying. Press Ctrl + C to abort.')

while True:
    shutil.copy(log_location, log_destination)
    print('Copied.')
    time.sleep(60)