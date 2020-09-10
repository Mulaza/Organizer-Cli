# TODO: write all of the things you move into a file
# TODO: Don't move self
import shutil
import os

# Paths -----
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


# ----------------------------------------------------------------------------

def clean():
    # The string that gets logged onto the file
    logText = ""

    files = os.listdir()
    for i in range(2):

        for extension in textFiles:
            if files[i].endswith(extension) == True:
                text = "{} was moved to Texts\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Texts")
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
                text = "{} was moved to Images\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Images")
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
                text = "{} was moved to Audio\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Audio")
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
                text = "{} was moved to Videos\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Videos")
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
                text = "{} was moved to Vectors\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Vectors")
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
                text = "{} was moved to Gifs\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Gifs")
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
                text = "{} was moved to Photoshop\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Photoshop")
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
                text = "{} was moved to Word\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Word")
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
                text = "{} was moved to Powerpoints\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Powerpoints")
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
                text = "{} was moved to Excels\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Excels")
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

        # --------------------------

        for extension in publisherFiles:
            if files[i].endswith(extension) == True:
                text = "{} was moved to Publisher\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Publisher")
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
                text = "{} was moved to Access\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Access")
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
                text = "{} was moved to Executables\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Executables")
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
                text = "{} was moved to PDFs\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to PDFs")
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
                text = "{} was moved to Fonts\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Fonts")
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
                text = "{} was moved to XHTMLs\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to XHTMLs")
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
                text = "{} was moved to HTML\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to HTML")
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
                text = "{} was moved to CSS\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to CSS")
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
                text = "{} was moved to Javascript\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Javascript")
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
                text = "{} was moved to Java\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Java")
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
                text = "{} was moved to PHP\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to PHP")
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
                text = "{} was moved to C\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to C")
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
                text = "{} was moved to C++\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to C++")
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
                text = "{} was moved to Swift\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Swift")
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
                text = "{} was moved to Visual Basic\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to Visual Basic")
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
                text = "{} was moved to APKs\n".format(files[i])
                logText = logText + text
                print(files[i], "was moved to APKs")
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

    return logText


def main():
    # Each returns the text of appended results of files moved
    sweep1 = clean()
    sweep2 = clean()
    gg = sweep1 + sweep2

    # Make the logged file
    os.chdir(organizedPath)
    with open('Moved Files Log.txt', 'w') as fileObject:
        fileObject.write(gg)


if __name__ == '__main__':
    main()
