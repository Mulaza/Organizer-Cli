
import shutil
import pathlib
import os


# Paths -----
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
pythonPath = os.path.join("Organized", "Python")
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




# File format lists -----
files = ["res.pptx", "main.py", "test.png", "kk.mp3", "img.png", "src.exe", "meek.aac", "lif.py", "tek.pdf"]



textFiles = [".txt", ".rtf"]
imageFiles = [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]
audioFiles = [".wav", ".mp3", ".ogg", ".gsm", ".dct", ".flac", ".au", ".aiff", ".vox", "raw", ".wma", ".aac", ".atrac", ".ra", ".oma", ".omg", ".atp"]
videoFiles = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd", ".vob", ".rm", ".avi", ".3gp", ".3g2"]
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




#   ----------------------------------------------------------------------------




import sys
import time
import logging
import os
import string

#from extensions import *  # All of the file extensions -----



#dir = os.path.join("..", "renaming")
#os.chdir(dir)

for i in os.listdir():
    print(i)



def clean():
    files = os.listdir()
    for i in range(len(files)):


        for extension in textFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an text file")
                try:
                    os.makedirs(textPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], textPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in imageFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an image file")
                try:
                    os.makedirs(imagePath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], imagePath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in audioFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an audio file")
                try:
                    os.makedirs(audioPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], audioPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in videoFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an video file")
                try:
                    os.makedirs(videoPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], videoPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in vectorFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an vector file")
                try:
                    os.makedirs(vectorPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], vectorPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in gifFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a gif file")
                try:
                    os.makedirs(gifpath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], gifpath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in photoshopFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an Photoshop file")
                try:
                    os.makedirs(photoshopPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], photoshopPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in wordFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an word file")
                try:
                    os.makedirs(wordPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], wordPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in powerpointFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an powerpoint file")
                try:
                    os.makedirs(powerpointPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], powerpointPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in excelFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an excel file")
                try:
                    os.makedirs(excelPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], excelPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


#--------------------------

        for extension in publisherFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an publisher file")
                try:
                    os.makedirs(publisherPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], publisherPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in accessFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an access file")
                try:
                    os.makedirs(accessPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], accessPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in executableFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is an execuatble file")
                try:
                    os.makedirs(executablePath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], executablePath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in pdfFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a PDF file")
                try:
                    os.makedirs(pdfPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], pdfPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in fontFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a font file")
                try:
                    os.makedirs(fontPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], fontPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in xhtmlFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a XHtML file")
                try:
                    os.makedirs(xhtmlPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], xhtmlPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in htmlFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a HTML file")
                try:
                    os.makedirs(htmlPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], htmlPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in cssFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a CSS file")
                try:
                    os.makedirs(cssPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], cssPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in javascriptFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a javascript file")
                try:
                    os.makedirs(javascriptPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], javascriptPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass


        for extension in javaFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a java file")
                try:
                    os.makedirs(javaPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], javaPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in phpFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a PHP file")
                try:
                    os.makedirs(phpPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], phpPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in cFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a C file")
                try:
                    os.makedirs(cPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], cPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in cplusplusFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a C++ file")
                try:
                    os.makedirs(cplusplusPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], cplusplusPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in swiftFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a Swift file")
                try:
                    os.makedirs(swiftPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], swiftPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in visualbasicFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a Visual Basic file")
                try:
                    os.makedirs(visualbasicPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], visualbasicPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass



        for extension in apkFiles:
            if files[i].endswith(extension) == True:
                print(files[i], "is a APK file")
                try:
                    os.makedirs(apkPath)
                except FileExistsError:
                    pass

                try:
                    shutil.move(files[i], apkPath)
                except shutil.Error:
                    print("{} file already exists".format(files[i]))
                    print(files[i])
                    array = files[i].split(".")
                    name = array[0] + " - Copy"
                    array[0] = name
                    new = ".".join(array)
                    os.rename(files[i], new)
            else:
                pass





"""
"""

for i in range(2):
    clean()
    print("sweep {}".format(i))
    time.sleep(3)


