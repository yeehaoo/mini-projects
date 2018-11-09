import os
import shutil

pathToRename = './oswalktest/'
count = 1

for folderName, subfolders, filenames in os.walk(pathToRename):
    print('The current folder is ' + folderName)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        shutil.move('./oswalktest/' + filename, './oswalktest/' + str(count) + filename[-4:])
        count += 1
    print('Renaming complete, ' + str(count) + ' files renamed.')
