#!/usr/bin/python


import sys
import os
import subprocess
import glob
import fnmatch
import json
import shutil
import shutil, errno

import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))

import FishLamp
import FishLampUtils
import FishLampGit

def pieceFileName():
    return "fishlamp-piece.json";

def allPieces():

    fishlamp = absolutePathToPiecesFolder();

    FishLampUtils.verbose("found " + fishlamp)

    pieces = [];
    for filename in FishLampUtils.findFiles(fishlamp, pieceFileName()):
        FishLampUtils.assertPathExists(filename);
        piece = Piece(filename);
        pieces.append(piece);

    return pieces;

def findPieceForName(name):
    for piece in allPieces():
        if piece.name() == name:
            return piece;

def defaultPieces() :
    return [ "fishlamp-templates" ];

def githubReference() :
    return "git@github.com:"

def submoduleURI(name):
    return  + name;

def addPiece(name):
    FishLampGit.addSubmodule(githubReference() + "fishlamp", name, folderName());

def folderName() :
    return "FishLamp-Pieces";

def createFishLampFolderIfNeeded() :
    if os.path.exists(folderName()) == False:
        os.makedirs(folderName())

#    hp = hiddenFileRelativePath();
#    if os.path.exists(hp) == False:
#        f = open(hp,'w');
#        f.write("# this invisible file is here for scripts to find\n");
#        f.write(path);

def initFolder() :
    if os.path.exists(folderName()) == False:
        os.makedirs(folderName())

def searchForFishLampFolder(dir) :
    oldDir = FishLampUtils.workingDirectory();

    if(oldDir == "/"):
        return None;

    result = None;

    if os.path.exists(folderName()):

        if dir:
            result = os.path.join(dir, folderName());
        else:
            result = folderName();

    else:
        FishLampUtils.setWorkingDirectory("..");

        if dir:
            result = searchForFishLampFolder(os.path.join("..", dir));
        else:
            result = searchForFishLampFolder("..");

    FishLampUtils.setWorkingDirectory(oldDir);

    return result;

def relativePathToPiecesFolder():
    fishlamp = searchForFishLampFolder(None);

    if fishlamp:
        FishLampUtils.assertPathExists(fishlamp);

    return fishlamp

def absolutePathToPiecesFolder():
    fishlamp = relativePathToPiecesFolder();
    if fishlamp:
        fishlamp = os.path.abspath(fishlamp);
        FishLampUtils.assertPathExists(fishlamp);

    return fishlamp;

class Piece:
    _piece = 0;

    _folder = ""

    def name(self):
        return self._piece['pieceName'];

    def description(self):
        return self._piece['shortDescription']

    def folderPath(self):
        return self._folder;

    def allPaths(self):
        paths = []
        for path in self._piece['importPaths'].split(','):
            paths.append(os.path.join(self.name(), path.strip()));
        return paths;

    def printSelf(self):
        print "Piece Name: " + self.name();
        print "Piece folder: " + self.folderPath();
        print "Description: " + self.description();
        print "Paths: "
        for path in self.allPaths():
            print "  " + path;


    def __init__(self, path):
        filepath = path.strip();
        jsonString = FishLampUtils.readFileIntoString(filepath);
        self._piece = json.loads(jsonString)
        self._folder = os.path.dirname(filepath)

    def subDirectoryPath(self, relativePathToPiecesFolder) :
        path = os.path.join(self.folderPath(), relativePathToPiecesFolder);
        return FishLampUtils.assertPathExists(path);