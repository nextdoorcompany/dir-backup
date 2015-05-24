#! python3
# dir-backup.py

import sys
import os
import datetime
import shutil
import argparse
import time

parser = argparse.ArgumentParser(description = 'backs up files from source into dated directory in target')
parser.add_argument('source', help = 'directory to copy')
parser.add_argument('destination', help = 'directory to put copy')
parser.add_argument('-m', '--move', help = 'delete source after copy', action = 'store_true')
parser.add_argument('-d', '--days', type = int, default = -1, help= 'days of backup to store')
args = parser.parse_args()

date_format = '%Y-%m-%d'
source = os.path.abspath(args.source)
destination = os.path.join(args.destination, datetime.date.today().strftime(date_format))

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

if args.days >= 0:
    current_time = time.localtime()
    for dir in os.listdir(args.destination):
        dir_date = time.strptime(dir, date_format)
        interval = current_time.tm_yday - dir_date.tm_yday
        if interval > args.days:
            shutil.rmtree(os.path.join(args.destination, dir))


