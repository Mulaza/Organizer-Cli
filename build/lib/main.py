# TODO: need to support microsof access files
# TODO: torresnt files
# TODO: some sort of case senisivity handeling for file extensions


import shutil
import os
import click
import colorama
from colorama import Fore, Back, Style

# Support for windows cmd
colorama.init()


# --------------------------------- Paths for each file type
organizedPath = os.path.join("Organized")
textPath = os.path.join("Organized", "Texts")
imagePath = os.path.join("Organized", "Images")
audioPath = os.path.join("Organized", "Audio")
videoPath = os.path.join("Organized", "Videos")
vectorPath = os.path.join("Organized", "Vectors")
gifpath = os.path.join("Organized", "Gifs")
photoshopPath = os.path.join("Organized", "Photoshop")
wordPath = os.path.join("Organized", "Word")
powerpointPath = os.path.join("Organized", "Powerpoints")
excelPath = os.path.join("Organized", "Excels")
publisherPath = os.path.join("Organized", "Publisher")
accessPath = os.path.join("Organized", "Access")
executablePath = os.path.join("Organized", "Executables")
pdfPath = os.path.join("Organized", "PDFs")
pythonPath = os.path.join("Organized", "Python")  # these arent included
fontPath = os.path.join("Organized", "Fonts")
xhtmlPath = os.path.join("Organized", "XHTMLs")
htmlPath = os.path.join("Organized", "HTMLs")
cssPath = os.path.join("Organized", "CSS")
javascriptPath = os.path.join("Organized", "Javascript")
javaPath = os.path.join("Organized", "Java")
phpPath = os.path.join("Organized", "PHP")
cPath = os.path.join("Organized", "C")
cplusplusPath = os.path.join("Organized", "C++")
swiftPath = os.path.join("Organized", "Swift")
visualbasicPath = os.path.join("Organized", "Visual Basic")
apkPath = os.path.join("Organized", "APKs")


# --------------------------------- An exception file, not to move (self)
exceptionFile = 'main.py'

# --------------------------------- Supported File extensions
textFiles = [".txt", ".rtf"]
imageFiles = [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]
audioFiles = [".wav", ".mp3", ".ogg", ".gsm", ".dct", ".flac", ".au", ".aiff", ".vox", "raw", ".wma", ".aac", ".atrac",
              ".ra", ".oma", ".omg", ".atp"]
videoFiles = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt",
              ".flv", ".swf", ".avchd", ".vob", ".rm", ".avi", ".3gp", ".3g2"]
vectorFiles = [".ai", ".svg"]
gifFiles = [".gif"]
photoshopFiles = [".psd"]
wordFiles = [".doc", ".docx"]
powerpointFiles = [".pptx", ".pptm", ".ppt", ".pps"]
excelFiles = [".xls", ".xlsx", ".xltx", ".xltm"]
publisherFiles = [".pub"]
accessFiles = []
executableFiles = [".exe", ".msi"]
pdfFiles = [".pdf"]
pythonFiles = [".py"]
fontFiles = [".fnt", ".fon", ".otf", ".ttf"]
xhtmlFiles = [".xhtml"]
htmlFiles = [".html"]
cssFiles = [".css"]
javascriptFiles = [".js"]
javaFiles = [".class"]
phpFiles = [".php"]
cFiles = [".c"]
cplusplusFiles = [".cpp"]
swiftFiles = [".swift"]
visualbasicFiles = [".vb"]
apkFiles = [".apk"]

# ---------------------------------


# --------------------------------- Holds all of the dictionary objects
masterList = []


# --------------------------------- Dictionaries of each file type, file path and text
textDict = {
    'move': False,
    'path': textPath,
    'extensions': textFiles,
    'text': Fore.LIGHTBLUE_EX + Fore.LIGHTBLUE_EX + "{} was moved to Texts\n" + Style.RESET_ALL + Style.RESET_ALL
}
masterList.append(textDict)

imageDict = {
    'move': False,
    'path': imagePath,
    'extensions': imageFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Images\n" + Style.RESET_ALL
}
masterList.append(imageDict)

audioDict = {
    'move': False,
    'path': audioPath,
    'extensions': audioFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Audio\n" + Style.RESET_ALL
}
masterList.append(audioDict)

videoDict = {
    'move': False,
    'path': videoPath,
    'extensions': videoFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Videos\n" + Style.RESET_ALL
}
masterList.append(videoDict)

vectorDict = {
    'move': False,
    'path': vectorPath,
    'extensions': vectorFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Vectors\n" + Style.RESET_ALL
}
masterList.append(vectorDict)

gifDict = {
    'move': False,
    'path': gifpath,
    'extensions': gifFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Gifs\n" + Style.RESET_ALL
}
masterList.append(gifDict)

photoshopDict = {
    'move': False,
    'path': photoshopPath,
    'extensions': photoshopFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Photoshop\n" + Style.RESET_ALL
}
masterList.append(photoshopDict)

wordDict = {
    'move': False,
    'path': wordPath,
    'extensions': wordFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Word\n" + Style.RESET_ALL
}
masterList.append(wordDict)

powerpointDict = {
    'move': False,
    'path': powerpointPath,
    'extensions': powerpointFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Powerpoints\n" + Style.RESET_ALL
}
masterList.append(powerpointDict)

excelDict = {
    'move': False,
    'path': excelPath,
    'extensions': excelFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Excels\n" + Style.RESET_ALL
}
masterList.append(excelDict)

publisherDict = {
    'move': False,
    'path': publisherPath,
    'extensions': publisherFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Publisher\n" + Style.RESET_ALL
}
masterList.append(publisherDict)

accessDict = {
    'move': False,
    'path': accessPath,
    'extensions': accessFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Access\n" + Style.RESET_ALL
}
masterList.append(accessDict)

executableDict = {
    'move': False,
    'path': executablePath,
    'extensions': executableFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Executables\n" + Style.RESET_ALL
}
masterList.append(executableDict)

pdfDict = {
    'move': False,
    'path': pdfPath,
    'extensions': pdfFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to PDFs\n" + Style.RESET_ALL
}
masterList.append(pdfDict)

pythonDict = {
    'move': False,
    'path': pythonPath,
    'extensions': pythonFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Python\n" + Style.RESET_ALL
}
masterList.append(pythonDict)

fontDict = {
    'move': False,
    'path': fontPath,
    'extensions': fontFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Fonts\n" + Style.RESET_ALL
}
masterList.append(fontDict)

xhtmlDict = {
    'move': False,
    'path': xhtmlPath,
    'extensions': xhtmlFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to XHTMLs\n" + Style.RESET_ALL
}
masterList.append(xhtmlDict)

htmlDict = {
    'move': False,
    'path': htmlPath,
    'extensions': htmlFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to HTML\n" + Style.RESET_ALL
}
masterList.append(htmlDict)

cssDict = {
    'move': False,
    'path': cssPath,
    'extensions': cssFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to CSS\n" + Style.RESET_ALL
}
masterList.append(cssDict)

javascriptDict = {
    'move': False,
    'path': javascriptPath,
    'extensions': javascriptFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Javascript\n" + Style.RESET_ALL
}
masterList.append(javascriptDict)

javaDict = {
    'move': False,
    'path': javaPath,
    'extensions': javaFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Java\n" + Style.RESET_ALL
}
masterList.append(javaDict)

phpDict = {
    'move': False,
    'path': phpPath,
    'extensions': phpFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to PHP\n" + Style.RESET_ALL
}
masterList.append(phpDict)

cDict = {
    'move': False,
    'path': cPath,
    'extensions': cFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to C\n" + Style.RESET_ALL
}
masterList.append(cDict)

cplusplusDict = {
    'move': False,
    'path': cplusplusPath,
    'extensions': cplusplusFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to C++\n" + Style.RESET_ALL
}
masterList.append(cplusplusDict)

swiftDict = {
    'move': False,
    'path': swiftPath,
    'extensions': swiftFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Swift\n" + Style.RESET_ALL
}
masterList.append(swiftDict)

visualbasicDict = {
    'move': False,
    'path': visualbasicPath,
    'extensions': visualbasicFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Visual Basic\n" + Style.RESET_ALL
}
masterList.append(visualbasicDict)

apkDict = {
    'move': False,
    'path': apkPath,
    'extensions': apkFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to APKs\n" + Style.RESET_ALL
}
masterList.append(apkDict)


def clean():

    # The log text of all files being moved
    logText = ""

    for i in range(2):

        directoryFiles = os.listdir()
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
                    if file.endswith(extension) == True:
                        text = item['text'].format(file)
                        click.echo(Fore.LIGHTBLACK_EX + text + Style.RESET_ALL)
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
                            click.echo(
                                Fore.LIGHTBLUE_EX + "{} file already exists".format(file) + Style.RESET_ALL)
                            click.echo(Fore.LIGHTBLUE_EX +
                                       file + Style.RESET_ALL)
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
# @click.option('--image', default="", help='Moves all image files')
# @click.option('--audio', default="", help='Moves all audio files')
# @click.option('--video', default="", help='Moves all video files')
# @click.option('--vector', default="", help='Moves all vector files')
# @click.option('--gif', default="", help='Moves all gif files')
# @click.option('--photoshop', default="", help='Moves all photoshop files')
# @click.option('--office', default="", help='Moves all office files')
# @click.option('--pdf', default="", help='Moves all pdf files')
# @click.option('--font', default="", help='Moves all font files')
# @click.option('--code', default="", help='Moves all code files')
# @click.option('--safe', default="", help='Moves all user friendly files')
# @click.option('--all', default="", help='Moves all supported files')
@click.argument('filetype', default="safe", type=str)
def main(filetype):

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

    # Make the logged file
    os.chdir(organizedPath)
    with open('Moved-Files-Log.txt', 'w') as fileObject:
        fileObject.write(sweep_text1)

    # remember to reset everything to false when done, or will it automatically
    for i in masterList:
        i['move'] = False


@click.command()
@click.argument('filetype', default="all")
def main2(filetype):
    click.echo('OK organizing {} '.format(filetype))


if __name__ == '__main__':
    main()
