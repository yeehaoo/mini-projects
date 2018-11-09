import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Rename files in selected directory')
parser.add_argument('-p', '--path', help = 'path of directory', required = True)
args = vars(parser.parse_args())

pathToRename = args['path']
if(pathToRename[-1] != '/'):
    pathToRename = pathToRename + '/'
    
count = 0

for folderName, subfolders, filenames in os.walk(pathToRename):
    print('The current folder is ' + folderName)
    for filename in filenames:
        count += 1
        newFileName = str(count) + filename[-4:]
        shutil.move(pathToRename + filename, pathToRename + newFileName)
        print(filename + ' renamed to ' + newFileName)
    print('Renaming complete, ' + str(count) + ' files renamed.')
