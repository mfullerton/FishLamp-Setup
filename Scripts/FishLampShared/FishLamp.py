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

def assertPathExists(path):
    if os.path.exists(path):
        verbose("Found path:" + path)
        return path;
    else:
        print "Path not found: " + path;
        sys.exit(1);

def assertNotNone(item, msg):
    if item is None:
        print "unexpected None value: " + msg
        sys.exit(1);
    return item;

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

    def readFileIntoString(self, path):
        assertPathExists(path);
        with open (path, "r") as myfile:
            data=myfile.read().replace('\n', '')
        return data;

    def __init__(self, path):
        filepath = path.strip();
        jsonString = self.readFileIntoString(filepath);
        self._piece = json.loads(jsonString)
        self._folder = os.path.dirname(filepath)

    def subDirectoryPath(self, relativePath) :
        path = os.path.join(self.folderPath(), relativePath);
        return assertPathExists(path);


class ScriptBase :
    _pieces = []

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
        assertPathExists(fishlamp);
        return fishlamp;

    def fishLampRelativePath(self):
        fishlamp = subprocess.check_output(["fishlamp", "find", "-r"]).strip();
        assertPathExists(fishlamp);
        return fishlamp;

    def findFiles(self, directory, pattern):
        directory = directory.strip();

        for root, dirs, files in os.walk(directory):
            for basename in files:
                if fnmatch.fnmatch(basename, pattern):
                    filename = os.path.join(root, basename);
                    yield filename;

    def allPieces(self):

        if len(self._pieces) > 0:
            return self._pieces;

        fishlamp = self.findFishLamp();
        verbose("found " + fishlamp)

        self._pieces = [];
        for filename in self.findFiles(fishlamp, "fishlamp-piece.json"):
#            print filename;
            assertPathExists(filename);
            piece = Piece(filename);
            self._pieces.append(piece);

        return self._pieces;

    def findPieceForName(self, name):

        for piece in self.allPieces():
            if piece.name() == name:
                return piece;

    def corePiece(self):
        return assertNotNone(self.findPieceForName("fishlamp-core"), "unabled to find fishlamp-core piece");

    def hasParameterAtIndex(self, index):
        if len(sys.argv) > index:
            return True;
        return False;

    def parameterAtIndex(self, index):
        parm = sys.argv[index];
        assertNotNone(parm, "parameter at Index: " + index);
        return parm;

    def workingDirectory(self):
        return os.getcwd();
