

import pathlib
import shutil
import time
import os
import sys

# Modules
from file_extensions import *

# External dependencies
import click
import colorama
from colorama import Fore, Back, Style
from progress.bar import IncrementalBar


# Support for windows cmd
colorama.init()


# TODO: take the loop out of this & have it take in a single file item argument

# --------------------------------- The clean function that
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
 #                       click.echo(Fore.LIGHTBLACK_EX + text + Style.RESET_ALL)
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


# --------------------------------- The main executable file

# Click stuff
@click.command()
@click.argument('filetype', default="safe", type=str)
def main(filetype):

    attention_text = Fore.YELLOW + "ATTENTION " + Style.RESET_ALL + \
        "This action will be moving files would you like to continue (y/n)"

    decide = click.prompt(attention_text,  type=str)

    if (decide == "y"):

        if (filetype == "image"):

            imageDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == 'audio'):

            audioDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "video"):

            videoDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "vector"):

            vectorDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "gif"):

            gifDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "photoshop"):

            photoshopDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "office"):

            textDict['move'] = True
            wordDict['move'] = True
            powerpointDict['move'] = True
            excelDict['move'] = True
            publisherDict['move'] = True
            accessDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == 'pdf'):

            pdfDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "font"):

            fontDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "code"):

            xhtmlDict['move'] = True
            htmlDict['move'] = True
            cssDict['move'] = True
            javascriptDict['move'] = True
            javaDict['move'] = True
            phpDict['move'] = True
            cDict['move'] = True
            cplusplusDict['move'] = True
            swiftDict['move'] = True
            visualbasicDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "program"):

            executableDict['move'] = True
            apkDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "safe"):

            imageDict['move'] = True
            audioDict['move'] = True
            videoDict['move'] = True
            vectorDict['move'] = True
            gifDict['move'] = True
            photoshopDict['move'] = True
            textDict['move'] = True
            wordDict['move'] = True
            powerpointDict['move'] = True
            excelDict['move'] = True
            publisherDict['move'] = True
            accessDict['move'] = True
            pdfDict['move'] = True
            fontDict['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

        elif (filetype == "all"):

            for i in masterList:
                i['move'] = True

            # Each returns the text of appended results of files moved
            sweep_text1 = clean()

    else:
        sys.exit()

    bar = IncrementalBar('Organizing...', max=100)

    for i in range(100):
        # Increment the bar
        bar.next()
        time.sleep(0.01)

    bar.finish()

    # If nothing was moved, no ned to write a file
    if (sweep_text1.strip() == ""):
        # Do nothing if nothing was moved
        pass

    else:

        # --------------------------------- Make the logged file
        os.chdir(organizedPath)
        with open('Moved-Files-Log.txt', 'w') as fileObject:
            fileObject.write(sweep_text1)

        # --------------------------------- remember to reset everything to false when done, or will it automatically
        for i in masterList:
            i['move'] = False


if __name__ == '__main__':
    main()
