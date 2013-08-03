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


import shutil

import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

class Script(FishLamp.ScriptBase):

    def helpString(self):
        return "installs or updates Xcode configs for FishLamp";

    def destinationPath(self):
        destinationDir = self.workingDirectory();

        if self.hasParameterAtIndex(1) :
            destinationDir = self.parameterAtIndex(1);
            assertPathExists(destinationDir);

        return os.path.join(destinationDir, "FishLampXcodeConfigs");

    def removeDestinationPath(self, path):
        path = path.strip();
        FishLamp.assertNotNone(path, "path is empty");
        
        if len(path) > 1 and os.path.exists(path):
            shutil.rmtree(path)

    def arrayOfPaths(self) :
        paths = []
        for piece in self.allPieces():
            for aPath in piece.allPaths():
                paths.append(aPath);

        return paths;

    def generateFileWithPath(self, destFolder, path) :
        filePath = os.path.join(destFolder, "FISHLAMP_PIECES_PATHS.xcconfig");
        f = open(filePath,'w');
        f.write("# generated on " + "date" + "\n\n");
        f.write(path);

        FishLamp.assertPathExists(filePath);

    def run(self):

        destDir = self.destinationPath();
        self.removeDestinationPath(destDir);

        srcPath = self.templatePath("XcodeConfigs");

#        print srcPath
#        print destDir

        copyanything(srcPath, destDir)

        fl = self.fishLampRelativePath();

        configPath = "FISHLAMP_PIECES_PATHS = "
        for path in self.arrayOfPaths():
            relativePath = os.path.join(fl, path)
            print "# added path: \"" + relativePath + "\"";
            configPath += relativePath + "/** "

        self.generateFileWithPath(destDir, configPath);

        print "# updated folder: " + destDir;


script = Script();
script.run();




