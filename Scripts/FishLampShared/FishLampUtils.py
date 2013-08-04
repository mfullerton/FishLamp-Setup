#!/usr/bin/python


import sys
import os
import subprocess
import glob
import fnmatch
import json
import shutil
import shutil, errno

# this doesn't work
gVerbose = False

def verbose(str):
    if gVerbose == True:
        print str

def enableVerbose():
    gVerbose = True;
    print "--Verbose"

def printError(str):
    print "##! " + str;

def assertPathExists(path):
    if os.path.exists(path):
        verbose("Found path:" + path)
        return path;
    else:
        printError("Path not found: " + path);
        sys.exit(1);

def assertNotNone(item, msg):
    if item is None:
        printError("unexpected None value: " + msg);
        sys.exit(1);
    return item;

def deleteDirectory(path) :
    path = path.strip();
    FishLamp.assertNotNone(path, "path is empty");
    
    if len(path) > 1 and os.path.exists(path):
        shutil.rmtree(path)

def copyFileOrDirectory(src, dest) :
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def readFileIntoString(path):
    assertPathExists(path);
    with open (path, "r") as myfile:
        data=myfile.read().replace('\n', '')
    return data;

def workingDirectory():
    return os.getcwd();

def setWorkingDirectory(dir):
    prev = os.getcwd();
    os.chdir(dir);
    return prev;

def runInDirectory(dir, func):
    prev = setWorkingDirectory(dir);
    func(args);
    setWorkingDirectory(prev);

def findFiles(directory, pattern):
    directory = directory.strip();

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename);
                yield filename;