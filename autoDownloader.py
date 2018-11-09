"""
What is this script?
This script goes to your clipboard, saves the image from the URL, and names it according to the number of files in the current directory
(if you have 5 files in the current directory, the image will be saved as '6.jpg' or '6.png', depending on the original file extension.

Instructions:
1. Make sure you have python3 and pywin32 installed. (run 'pip install pywin32' if you do not)
2. Download the script and save it in the directory in which you want to save the image(s).
3. Copy the direct link of an image. Make sure the URL links directly to the image, and not an image viewer
('i.imgur.com/foobar.jpg' instead of 'imgur.com/gallery/foobar' for example)
4. Run the script (via commandline or windows explorer)
"""

import requests
import win32clipboard
import shutil
import os

#get url from clipboard
win32clipboard.OpenClipboard()
url = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

count = 0

#count number of files in current directory
for folderName, subfolders, filenames in os.walk('./'):
    for filename in filenames:
        count += 1

#download file and save as 1 more than count
response = requests.get(url)
if response.status_code == 200:
    with open('./' + str(count+1) + url[-4:], 'wb') as f:
        f.write(response.content)
