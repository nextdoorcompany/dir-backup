#! python3
# dir-backup.py

import sys
import os
import datetime
import shutil

if len(sys.argv) < 3:
    print('Usage: python dir-backup.py [source] [destination]')
    sys.exit()

source = os.path.abspath(sys.argv[1])
destination = os.path.join(sys.argv[2], datetime.date.today().strftime('%Y-%m-%d'))

print('source: %s\ndestination: %s' % (source, destination))

if not os.path.exists(source) or not os.path.isdir(source):
    print('source invalid')
    sys.exit()

if os.path.exists(destination):
    print('directory exists')
    sys.exit()

shutil.copytree(source, destination)