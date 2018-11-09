import os
import shutil
import argparse

#add argument to allow user to input directory path at command line
parser = argparse.ArgumentParser(description='Rename files in selected directory')
parser.add_argument('-p', '--path', help = 'path of directory', required = True)
args = vars(parser.parse_args())

#if user did not end directory path with '/', concatenate a '/'
pathToRename = args['path']
if(pathToRename[-1] != '/'):
    pathToRename = pathToRename + '/'
    
count = 0

for folderName, subfolders, filenames in os.walk(pathToRename):
    print('The current folder is ' + folderName)
    for filename in filenames:
        count += 1 #increment count
        newFileName = str(count) + filename[-4:] #set new file name to count + original extension
        shutil.move(pathToRename + filename, pathToRename + newFileName) #rename file to newFileName
        print(filename + ' renamed to ' + newFileName)
    print('Renaming complete, ' + str(count) + ' files renamed.')
