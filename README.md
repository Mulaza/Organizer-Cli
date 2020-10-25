![banner3](https://user-images.githubusercontent.com/60890281/96828268-ede10200-1469-11eb-832d-f2808434797c.png)


# Organizer cli
A Python CLI tool that runs throught a given directory and organizes all un-folder bound files into folders by file extension.
Supports 108 different file extensions over 27 file type categories.

## Dependencies
* [click](https://pypi.org/project/click8/)
* [colorama](https://pypi.org/project/colorama/)
* [progress](https://pypi.org/project/progress/)

## Whats New
### Features
* Pre-action prompt to the number of files that will be moved.
* Prompts the user if no files extensions are supported in the directory.
* Moving 'code' files is now optional with the `code` command.
### Extensions
* Added extensions include [.vce, .spx, .m4r, .wax, .xlsb, .xlsm, .xlam,
  .xlb, .xla, .xlt, .xar, .xlm, .xl, .xlw, .xltx, .xll, .xlc, .ppsx, .ppsm,
  .pptm, .sldx, .pot, .potx, .ppam, .ppa, .sldm, .pa, .potm]


## Installation
```python
pip install organizer-cli
```

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
```text
>> Organize               # Organizes all user friendly files
```
```text
>> Organize image         # Organizes all image files
```
```text
>> Organize video         # Organizes all video files
```
```text
>> Organize audio         # Organizes all audio files
```
```text
>> Organize office        # Organizes all office files
```
```text
>> Organize vector        # Organizes all vector files
```
```text
>> Organize gif           # Organizes all gif files
```
```text
>> Organize photoshop     # Organizes all photoshop files
```
```text
>> Organize pdf           # Organizes all pdf files
```
```text
>> Organize font          # Organizes all font files
```
```text
>> Organize code          # Organizes all programming files
```
```text
>> Organize safe          # Organizes all user friendly files
```
```text
>> Organize all           # Organizes all supported files
```
