![g1445](https://user-images.githubusercontent.com/60890281/126904401-d7e48d16-0d3f-4f7e-9111-04f37251435a.png)


# Organizer CLI
![](https://img.shields.io/pypi/v/organizer-cli?color=blue&style=flat-square) ![](https://img.shields.io/github/license/Mulaza/Organizer-Cli?color=green&style=flat-square)

Organizer CLI is a python command line tool that goes through a given directory and organizes all un-folder bound files into folders by file extension.
Organize CLI Supports 108 different file extensions over 27 file type categories and the list is ever growing.

## Installation
### Pip Install
```text
pip install organizer-cli
```
### Local Install
```text
cd Organizer-Cli
pip install -e .
```


## Whats New
### Features
* Pre-action prompt to the number of files that will be moved.
* Prompts the user if no files extensions are supported in the directory.
### Extensions
* Added extensions include [.webp, .vce, .spx, .m4r, .wax, .xlsb, .xlsm, .xlam,
  .xlb, .xla, .xlt, .xar, .xlm, .xl, .xlw, .xltx, .xll, .xlc, .ppsx, .ppsm,
  .pptm, .sldx, .pot, .potx, .ppam, .ppa, .sldm, .pa, .potm]



## How To Use

After installing the CLI tool you will be able to use the `Organize` command in any directory, followed by a tag specifying the type of file you want organized.  
```text
Organize [command]        
```

Simply running the `Organize` command will organize all the current directory.
```text
Organize               
```

Running the `Organize` command with the `safe` tag will organize all  media files in the current directory.
```text
Organize safe         
```

Running the `Organize` command with the `all` tag will organize all supported file formats in the current directory.
```text
Organize all     
```
## Commands

### Safe
The `safe` command moves the most common types of media file, this includes images, audio, video etc. this command avoids filetypes that might be dependent on other programs running, like `.cpp` or  `.exe` files. This is also the default command if no command is specified after the initial `Organize` call is made.
### All
The `all` command moves all supported file formats.  
### Image
The `image` command moves all supported image formats like .PNG, .JPG, .JPEG etc.

### Audio
The `audio` command moves all supported audio formats like .MP3, .WAV, .OOG etc.

### Video
The `video` command moves all supported video formats like .MP$, .MOV, .WMV etc.

### Office
The `office` command moves all supported Microsoft Office files including .DOCX, .PPT, .XLS etc.

### Vector
The `vector` command moves  all supported vector files like .SVG and .AI.

### Gif
The `gif` command moves .GIF files exclusively.

### Photoshop
The `photoshop` command moves .PSD files exclusively.

### Pdf
The `pdf` command moves .PDF files exclusively.

### Font
The `font` command moves all supported font files, like .OTF, .TTF, .WOFF etc.

### Code
The `code` command moves all supported file formats of different programming languages like .PY, .CPP, .JS etc.
