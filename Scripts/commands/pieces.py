#!/usr/bin/python

#  pieces.py
#  fishlamp-install
#
#  Created by Mike Fullerton on 8/3/13.
#

# begin boilerplate
import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))
import FishLamp
import FishLampScript
import FishLampPiece
import FishLampGit

#end boilerplate

class Script(FishLampScript.Script):

    def helpString(self):
        return "finds all installed FishLamp pieces";

    def addPiece(self, name):
        FishLampPiece.addPiece(name);

    def listAll(self):
        all = FishLampPiece.allPieces();

        if all and len(all):
            print ""
            for piece in all:
                piece.printSelf();
                print ""

        else:
            print "# No pieces installed";

    def run(self):

        if self.hasParameter("add"):
            self.addPiece(self.parameterAtIndex(2, "expected piece name"));
        elif self.hasParameter("init"):
            FishLampPiece.createFishLampFolderIfNeeded();
        else:
            self.listAll();

Script().run();





