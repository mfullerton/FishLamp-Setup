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
#end boilerplat

class Script(FishLamp.ScriptBase):

    def helpString(self):
        return "finds all installed FishLamp pieces";

    def run(self):
        print ""
        for piece in self.allPieces():
            piece.printSelf();
            print ""

Script().run();





