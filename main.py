import shutil
import os


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
executableFiles = [".exe"]
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
    'path': textPath,
    'extensions': textFiles,
    'text': "{} was moved to Texts\n"
}
masterList.append(textDict)

imageDict = {
    'path': imagePath ,
    'extensions': imageFiles,
    'text': "{} was moved to Images\n"
}
masterList.append(imageDict)

audioDict = {
    'path': audioPath,
    'extensions': audioFiles,
    'text': "{} was moved to Audio\n"
}
masterList.append(audioDict)

videoDict ={
    'path': videoPath,
    'extensions': videoFiles,
    'text': "{} was moved to Videos\n"
}
masterList.append(videoDict)

vectorDict = {
    'path': vectorPath,
    'extensions': vectorFiles,
    'text': "{} was moved to Vectors\n"
}
masterList.append(vectorDict)

gifDict = {
    'path': gifpath,
    'extensions': gifFiles,
    'text': "{} was moved to Gifs\n"
}
masterList.append(gifDict)

photoshopDict = {
    'path': photoshopPath,
    'extensions': photoshopFiles,
    'text': "{} was moved to Photoshop\n"
}
masterList.append(photoshopDict)

wordDict = {
    'path': wordPath,
    'extensions': wordFiles,
    'text': "{} was moved to Word\n"
}
masterList.append(wordDict)

powerpointDict = {
    'path': powerpointPath,
    'extensions': powerpointFiles,
    'text': "{} was moved to Powerpoints\n"
}
masterList.append(powerpointDict)

excelDict = {
    'path': excelPath,
    'extensions': excelFiles,
    'text': "{} was moved to Excels\n"
}
masterList.append(excelDict)

publisherDict = {
    'path': publisherPath,
    'extensions': publisherFiles,
    'text': "{} was moved to Publisher\n"
}
masterList.append(publisherDict)

accessDict = {
    'path': accessPath,
    'extensions': accessFiles,
    'text': "{} was moved to Access\n"
}
masterList.append(accessDict)

executableDict = {
    'path': executablePath,
    'extensions': executableFiles,
    'text': "{} was moved to Executables\n"
}
masterList.append(executableDict)

pdfDict = {
    'path': pdfPath,
    'extensions': pdfFiles,
    'text': "{} was moved to PDFs\n"
}
masterList.append(pdfDict)

pythonDict = {
    'path': pythonPath,
    'extensions': pythonFiles,
    'text': "{} was moved to Python\n"
}
masterList.append(pythonDict)

fontDict = {
    'path': fontPath,
    'extensions': fontFiles,
    'text': "{} was moved to Fonts\n"
}
masterList.append(fontDict)

xhtmlDict = {
    'path': xhtmlPath,
    'extensions': xhtmlFiles,
    'text': "{} was moved to XHTMLs\n"
}
masterList.append(xhtmlDict)

htmlDict = {
    'path': htmlPath,
    'extensions': htmlFiles,
    'text': "{} was moved to HTML\n"
}
masterList.append(htmlDict)

cssDict = {
    'path': cssPath,
    'extensions': cssFiles,
    'text': "{} was moved to CSS\n"
}
masterList.append(cssDict)

javascriptDict = {
    'path': javascriptPath,
    'extensions': javascriptFiles,
    'text': "{} was moved to Javascript\n"
}
masterList.append(javascriptDict)

javaDict ={
    'path': javaPath,
    'extensions': javaFiles,
    'text': "{} was moved to Java\n"
}
masterList.append(javaDict)

phpDict = {
    'path': phpPath,
    'extensions': phpFiles,
    'text': "{} was moved to PHP\n"
}
masterList.append(phpDict)

cDict = {
    'path': cPath,
    'extensions': cFiles,
    'text': "{} was moved to C\n"
}
masterList.append(cDict)

cplusplusDict = {
    'path': cplusplusPath,
    'extensions': cplusplusFiles,
    'text': "{} was moved to C++\n"
}
masterList.append(cplusplusDict)

swiftDict = {
    'path': swiftPath,
    'extensions': swiftFiles,
    'text': "{} was moved to Swift\n"
}
masterList.append(swiftDict)

visualbasicDict ={
    'path': visualbasicPath,
    'extensions': visualbasicFiles,
    'text': "{} was moved to Visual Basic\n"
}
masterList.append(visualbasicDict)

apkDict = {
    'path': apkPath,
    'extensions': apkFiles,
    'text': "{} was moved to APKs\n"
}
masterList.append(apkDict)





def clean():

    # The log text of all files being moved
    logText = ""


    directoryFiles = os.listdir()
    for file in directoryFiles:

        # Skip my own file, don't want to move myself
        if file == exceptionFile:
            continue

        for item in masterList:

            for extension in item['extensions']:

                # Check if the file extension is exists in that list
                if file.endswith(extension) == True:
                    print("supported file")
                    text = item['text'].format(file)
                    print(text)
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
                        print("{} file already exists".format(file))
                        print(file)
                        array = file.split('.')
                        name = array[0] + " - Copy"
                        array[0] = name
                        new = '.'.join(array)
                        os.rename(file, new)
                else:
                    pass

    return logText


# --------------------------------- The main executable file
def main():

    """
    Only need two sweeps, the first moves or renames files, the second ones moves the previously
    renamed files
    """
    # Each returns the text of appended results of files moved
    sweep_text1 = clean()
    sweep_text2 = clean()
    print('------------ sweep completed ---')

    sweep_text_final = sweep_text1 + sweep_text2

    # Make the logged file
    os.chdir(organizedPath)
    with open('Moved-Files-Log.txt', 'w') as fileObject:
        fileObject.write(sweep_text_final)





if __name__ == '__main__':
    main()


