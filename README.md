# HoldMyFile


### What is it?
HoldMyFile is a python program that can backup your file on the web with a single command. The same file can be restored back to its original path with just another command.



### Requirements
* Python
* Python modules: click

### Quickstart
Install from source
```shell
$ git clone https://github.com/JuanPotato/Legofy.git
$ cd HoldMyFile
$ python setup.py install
```
Make sure pip is installed before hand.

### Usage
```
Usage: holdmyfile [OPTIONS] MODE FILE_DETAILS

  This program is used to temporarily just backup your files on the
  web.  The absolute file address is also stored. So you can just
  restore the files backs with a single command. This program is
  specially useful when you are experimenting with changes to a
  file that may later turn out to be hazardous for your system.

  To back up a file: holdmyfile give /home/dave/file.txt File
  Backed up successfully. Id is qvje

  To restore it again: holdmyfile take qvje File Restored
  successfully. File address is /home/dave/file.txt

Options:
  --help  Show this message and exit.
```

### A real quick tutorial
Run the command to backup file
```shell
holdmyfile give /home/dave/file.txt
File Backed up successfully. Note down the id: ifgi
```
After some period of time when you want to restore the file back, run the following command
```shell
holdmyfile take ifgi
File Restored successfully. File address is /home/dave/file.txt
```
### Notes
- Has only been tested on linux so far. Not sure if it runs on Windows and Mac as well.
- Does not support non plain-text files. Will be adding support for binary files as well.
