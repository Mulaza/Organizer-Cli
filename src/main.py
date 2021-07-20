
import pathlib
import shutil
import time

# Modules
from file_extensions import *
from functions import *

# External dependencies
from progress.bar import IncrementalBar
from colorama import Fore, Back, Style
import colorama
import click


# Support for windows cmd
colorama.init()


# TODO: take the loop out of this & have it take in a single file item argument
# TODO: break into 2 parts find files and move files


# Click stuff
@click.command()
@click.argument('filetype', default="safe", type=str)
def main(filetype):

    sweep_text1 = ""

    if (filetype == "image"):

        imageDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == 'audio'):

        audioDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "video"):

        videoDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "vector"):

        vectorDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "gif"):

        gifDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "photoshop"):

        photoshopDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "office"):

        textDict['move'] = True
        wordDict['move'] = True
        powerpointDict['move'] = True
        excelDict['move'] = True
        publisherDict['move'] = True
        accessDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == 'pdf'):

        pdfDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "font"):

        fontDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

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

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "program"):

        executableDict['move'] = True
        apkDict['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

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

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    elif (filetype == "all"):

        for i in masterList:
            i['move'] = True

        # Find out the number if files that are able to be moved
        moveable_num_2 = movableFilesCount()

        # Only ask the user to move files if there are files of that type available
        askToMove(moveable_num_2, click)

    else:
        click.echo("Command '{}' is currently unsupported".format(filetype))

    # Only write to the file if something was moved
    if (sweep_text1.strip() == ""):
        # Do nothing if nothing was moved
        pass

    else:

        # Make the logged file
        os.chdir(organizedPath)
        with open('Moved-Files-Log.txt', 'w') as fileObject:
            fileObject.write(sweep_text1)

        # Remember to reset everything to false when done, or will it automatically
        for i in masterList:
            i['move'] = False


if __name__ == '__main__':
    main()
