#! python3
# dir-backup.py

import sys
import os
import datetime
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', help = 'directory to copy')
parser.add_argument('destination', help = 'directory to put copy')
parser.add_argument('-m', '--move', help = 'delete source after copy', action = 'store_true')
args = parser.parse_args()

source = os.path.abspath(args.source)
destination = os.path.join(args.destination, datetime.date.today().strftime('%Y-%m-%d'))

command_text = 'source: %s\ndestination: %s' % (source, destination)
if args.move:
    command_text = 'move ->\n' + command_text
else:
    command_text = 'copy ->\n' + command_text

print(command_text)

if not os.path.exists(source) or not os.path.isdir(source):
    print('source invalid')
    sys.exit()

if os.path.exists(destination):
    print('directory exists')
    sys.exit()

shutil.copytree(source, destination)
if args.move:
    shutil.rmtree(source)
    os.mkdir(source)