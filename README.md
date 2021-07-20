![banner](https://user-images.githubusercontent.com/60890281/101989091-f40c9580-3cd8-11eb-83d6-c6df0cb28cd5.png)


# Organizer CLI
A Python CLI tool that runs through a given directory and organizes all un-folder bound files into folders by file extension.
Supports 108 different file extensions over 27 file type categories.

## Dependencies
* [click](https://pypi.org/project/click8/)
* [colorama](https://pypi.org/project/colorama/) 
* [progress](https://pypi.org/project/progress/)


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


## Commands

* safe
* all
* image
* audio
* video
* office
* vector
* gif
* photoshop
* pdf
* font
* code
* safe
* all


## Usage 

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
