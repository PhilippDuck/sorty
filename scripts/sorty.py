#!/usr/bin/python3

import os
import shutil
import datetime
import time
import locale

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core import config as HachoirConfig
HachoirConfig.quiet = True

#Location with uploads
searchPath = "/mymedia/Smartphone"
#location with new datastructure und names
workingPath = "/mymedia"
#used datatypes
dataTypes = [".jpg", ".JPG", ".mp4", ".MP4", ".mov", ".MOV"]
#language used for new filenames
locale.setlocale(locale.LC_ALL, "de_DE")


def scan(path):
    counter = 0
    counterEdited = 0

    for entry in os.scandir(path):
        for dataType in dataTypes:
            if entry.is_file and entry.name.endswith(dataType):
                counter += 1
                try:
                    dateTime = creation_date(entry.path)
                except:
                    print("{:20} {} no metadata found. skiped".format(nowStr, entry.name))
                    break
                locale.setlocale(locale.LC_ALL, "de_DE")
                targetDir = workingPath + "/" + dateTime.strftime("%Y/%Y_%m %B/")
                newName = dateTime.strftime("%Y-%m-%d_%H%M%S")
                moveFileToDir(entry, entry.path, newName, dataType, targetDir)
                counterEdited += 1
    print("{} files found. {} files processed".format(str(counter), str(counterEdited)))


def moveFileToDir(entry, filePath, newName, dataType, targetDir):
    #print(targetDir) 
    #Create directorys if not excists
    now = datetime.datetime.now()
    nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        os.makedirs(targetDir, mode=0o777)
        #print(f"{nowStr:20} Created dir {targetDir}")
        print("{:20} Created dir {}".format(nowStr, targetDir))
    except:
        pass
    #Move to directory
    counter = 0
    name = newName + dataType
    while os.path.exists(targetDir + name):
        print("{:20} File {} already exists".format(nowStr, name))
        counter += 1
        name = newName + "_" + str(counter) + dataType
    print("{:20} File {} renamed to {}".format(nowStr, entry.name, name))
    os.rename(entry.path, searchPath + "/" + name)
    try:
        shutil.move(searchPath + "/" + name, targetDir)
        #print(f"{nowStr:20} Moved {entry.name} to {targetDir}")
        print("{:20} Moved {} to {}".format(nowStr, name, targetDir))
    except shutil.Error as error:
        print(error)


def creation_date(filename):
    parser = createParser(filename)
    metadata = extractMetadata(parser)
    return metadata.get("creation_date")


now = datetime.datetime.now()
nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
print("{:20} Starting Programm".format(nowStr))
scan(searchPath)
now = datetime.datetime.now()
nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
print("{:20} Programm finished".format(nowStr))
