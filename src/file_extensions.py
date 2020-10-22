import os
from colorama import Fore, Back, Style

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
              ".ra", ".oma", ".omg", ".atp", ".waptt", ".i3pack", ".3ga", ".opus", ".cda", ".wpl", ".rec", ".vdjsample",
              ".mus", ".aax", ".amr", ".ds2", ".sng", ".dss", ".nvf", ".midi", ".m4a", ".pcm", ".mscz", ".ses", ".dvf",
              ".gp5", ".gp4", ".bnk", ".aup", ".acd", ".sf2", ".thd", ".sty", ".mxl", ".band", ".cdfs", ".ram", ".aa",
              ".eac3", ".mogg", ".au", ".seq", ".uax", ".mid", ".kar", ".dlp", ".vce", ".spx", ".m4r", ".wax"]

videoFiles = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt",
              ".flv", ".swf", ".avchd", ".vob", ".rm", ".avi", ".3gp", ".3g2"]
vectorFiles = [".ai", ".svg"]
gifFiles = [".gif"]
photoshopFiles = [".psd"]
wordFiles = [".doc", ".docx", ".asd", ".dotx",
             ".svd", ".dot", ".wbk", ".docm", ".dotm", ".wll"]
powerpointFiles = [".pptx", ".pptm", ".ppt", ".pps", ".ppsx", ".ppsm",
                   ".pptm", ".sldx", ".pot", ".potx", ".ppam", ".ppa", ".sldm", ".pa", ".potm"]
excelFiles = [".xls", ".xlsx", ".xltx", ".xltm", ".xlsb", ".xlsm", ".xlam",
              ".xlb", ".xla", ".xlt", ".xar", ".xlm", ".xl", ".xlw", ".xltx", ".xll", ".xlc"]
publisherFiles = [".pub"]
accessFiles = [".accdb"]
executableFiles = [".exe", ".msi"]
pdfFiles = [".pdf"]
pythonFiles = [".py"]
fontFiles = [".fnt", ".fon", ".otf", ".ttf", ".woff",
             ".woff2", ".ofm", ".bmap", ".frf", ".afs"]
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


# --------------------------------- Holds all of the dictionary objects
masterList = []


# --------------------------------- Dictionaries of each file type, file path and text
textDict = {
    'move': False,
    'path': textPath,
    'extensions': textFiles,
    'text': Fore.LIGHTBLUE_EX + "{} was moved to Texts\n" + Style.RESET_ALL + Style.RESET_ALL
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
