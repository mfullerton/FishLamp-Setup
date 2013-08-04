#!/usr/bin/python

#  pieces.py
#  fishlamp-install
#
#  Created by Mike Fullerton on 8/3/13.
#

import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))

import FishLamp
import FishLampUtils
import FishLampPiece;
import FishLampScript

import datetime
import time

class Script(FishLampScript.Script):

    def helpString(self):
        return "installs or updates Xcode configs for FishLamp";

    def destinationPath(self):
        destinationDir = FishLamp.workingDirectory();

        if self.hasParameterAtIndex(1) :
            destinationDir = self.parameterAtIndex(1);
            assertPathExists(destinationDir);

        return os.path.join(destinationDir, "FishLampXcodeConfigs");

    def arrayOfPaths(self) :
        paths = []
        for piece in FishLampPiece.allPieces():
            for aPath in piece.allPaths():
                paths.append(aPath);

        return paths;

    def generateFileWithPath(self, destFolder, path) :
        filePath = os.path.join(destFolder, "FISHLAMP_PIECES_PATHS.xcconfig");
        f = open(filePath,'w');
        f.write("# generated on " + datetime.datetime.now() + "\n\n");
        f.write(path);

        FishLamp.assertPathExists(filePath);

    def run(self):

        destDir = self.destinationPath();

        FishLamp.deleteDirectory(destDir);

        srcPath = self.templatePath("XcodeConfigs");
        FishLamp.copyFileOrDirectory(srcPath, destDir)

        fl = FishLampPieces.relativePathToPiecesFolder();

        configPath = "FISHLAMP_PIECES_PATHS = "
        for path in self.arrayOfPaths():
            relativePathToPiecesFolder = os.path.join(fl, path)
            print "# added path: \"" + relativePathToPiecesFolder + "\"";
            configPath += relativePathToPiecesFolder + "/** "

        self.generateFileWithPath(destDir, configPath);

        print "# updated folder: " + destDir;


Script().run();




