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
