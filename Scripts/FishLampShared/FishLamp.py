#!/usr/bin/python


import sys
import os
import subprocess
import glob
import fnmatch
import json

gVerbose = False

def verbose(str):
    if gVerbose == True:
        print str

def enableVerbose():
    gVerbose = True;
    print "--Verbose"

def assertPath(path):
    if os.path.exists(path):
        verbose("Found path:" + path)
    else:
        print "Path not found: " + path;
        sys.exit(1);

class Piece:
    _piece = 0;

    def name(self):
        return self._piece['pieceName'];

    def description(self):
        return self._piece['shortDescription']

    def printSelf(self):
        print "Piece Name: " + self.name();
        print "Description: " + self.description();

    def readFileIntoString(self, path):
        assertPath(path);
        with open (path, "r") as myfile:
            data=myfile.read().replace('\n', '')
        return data;

    def __init__(self, path):
        path = path.strip();
        jsonString = self.readFileIntoString(path);
        self._piece = json.loads(jsonString)

class Script :

    def __init__(self):
        self.checkParams();

    def scriptName(self):
        return os.path.basename(sys.argv[0]);

    def scriptPath(self):
        return os.path.dirname(sys.argv[0]);

    def checkForHelp(self):
        for str in sys.argv:
            if str == "--help":
                print self.helpString()
                sys.exit(0);
            elif (str == "--usage" or str == "-u"):
                self.printUsage()
                sys.exit(0);
            elif (str == "-v" or str == "--verbose"):
                enableVerbose();

    def printUsage(self):
        print self.usageString();

    def usageString(self):
        return "usage TBD";

    def helpString(self):
        return "help TBD";

    def checkParams(self):
        self.checkForHelp();

    def run(self):
        print "override this";

    def findFishLamp(self):
        fishlamp = subprocess.check_output(["fishlamp", "find", "-a"]).strip();
        assertPath(fishlamp);
        return fishlamp;

    def findFiles(self, directory, pattern):
        directory = directory.strip();

        for root, dirs, files in os.walk(directory):
            for basename in files:
                if fnmatch.fnmatch(basename, pattern):
                    filename = os.path.join(root, basename);
                    yield filename;

    def findPieces(self):
        fishlamp = self.findFishLamp();
        verbose("found " + fishlamp)

        pieces = [];
        for filename in self.findFiles(fishlamp, "fishlamp-piece.json"):
            print filename;

            assertPath(filename);
            piece = Piece(filename);
            pieces.append(piece);

        return pieces;


    
