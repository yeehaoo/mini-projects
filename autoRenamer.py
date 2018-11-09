import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Rename files in selected directory')
parser.add_argument('-p', '--path', help = 'path of directory', required = True)
args = vars(parser.parse_args())

pathToRename = args['path']
count = 0

for folderName, subfolders, filenames in os.walk(pathToRename):
    print('The current folder is ' + folderName)
    for filename in filenames:
        count += 1
        print('FILE INSIDE ' + folderName + ': '+ filename)
        shutil.move(pathToRename + filename, pathToRename + str(count) + filename[-4:])
        
    print('Renaming complete, ' + str(count) + ' files renamed.')
