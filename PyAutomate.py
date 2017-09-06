# An automation script while I make my morning coffee
# By Christos Zonios https://czonios.github.io

import webbrowser
import os
import subprocess
import time
import sys

urls = {'http://habitica.com/#/tasks', 'http://myfitnesspal.com', 'https://feedly.com/i/category/Programming'}

# get default web browser
webbrowser.get()

# iterate through urls array and open each in a new tab
for url in urls:
    webbrowser.open_new_tab(url)
    # sleep to not overwhelm browser
    time.sleep(0.33)     

path_to_vlc = '/usr/bin/vlc'
path_to_playlist = '/home/christos/morninglist.m3u'
thunderbird = '/usr/bin/thunderbird'


# start playing music
pid = os.fork()
if pid==0:
    subprocess.call([path_to_vlc, path_to_playlist])
    sys.exit(0)

# open email client
else:
    pid = os.fork() 
    if pid==0:
        subprocess.call(thunderbird)
        sys.exit(0)


sys.exit(0)
