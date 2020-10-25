import os
import sys
import pathlib
import shutil
import time
from progress.bar import IncrementalBar

# Modules
from file_extensions import exceptionFile, masterList


# Displays the cleaning progress bar
def displayProgressbar(item_count):
    # Only show the bar if something was moved
    if (item_count > 0):
        # The progress bar
        bar = IncrementalBar('Organizing...', max=item_count)

        for i in range(item_count):
            # Increment the bar
            bar.next()
            time.sleep(0.01)

        bar.finish()


# The clean function that
def clean():

    # The log text of all files being moved
    logText = ""

    for i in range(3):

        directoryFiles = []

        # Only use the files not folders
        for item in os.listdir():
            if os.path.isfile(os.path.join(item)):
                directoryFiles.append(item)

        for file in directoryFiles:

            # Skip my own file, don't want to move myself
            if file == exceptionFile:
                continue

            for item in masterList:

                # Skip file types that shouldn't be moved
                if item['move'] == False:
                    continue

                for extension in item['extensions']:

                    # Check if the file extension is exists in that list
                    if pathlib.Path(file).suffix.lower() == extension.lower():
                        text = item['text'].format(file)
                        logText = logText + text

                        # Try to make the directory
                        try:
                            os.makedirs(item['path'])
                        except FileExistsError:
                            pass

                        # Try to move the file / rename file
                        try:
                            shutil.move(file, item['path'])
                        except shutil.Error:
                         #                           click.echo(Fore.LIGHTBLUE_EX + "{} file already exists".format(file) + Style.RESET_ALL)
                         #                           click.echo(Fore.LIGHTBLUE_EX +file + Style.RESET_ALL)
                            array = file.split('.')
                            name = array[0] + " - Copy"
                            array[0] = name
                            new = '.'.join(array)
                            os.rename(file, new)
                    else:
                        pass

    return logText


# MovableFilesCount, know how many files will be moved
def movableFilesCount():
    # Lists for holding files and movabele files
    directoryFiles2 = []
    movableFiles = []

    # Only use the files not folders
    for item in os.listdir():
        if os.path.isfile(os.path.join(item)):
            directoryFiles2.append(item)

    for file in directoryFiles2:
        # print(pathlib.Path(file).suffix.lower())

        # Skip my own file, don't want to move myself
        if file == exceptionFile:
            continue

        # For each item in that file extinsion in that items list of extensions
        for item in masterList:
            if item['move'] == True:
                if pathlib.Path(file).suffix.lower() in item['extensions']:
                    movableFiles.append(file)

    # Return the number of movable items
    return len(movableFiles)
