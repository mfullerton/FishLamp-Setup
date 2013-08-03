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

class PiecesScript(FishLamp.Script):

    def helpString(self):
        return "finds all installed FishLamp pieces";

    def run(self):
        pieces = self.findPieces()
        for piece in pieces:
            piece.printSelf();



script = PiecesScript();
script.run();




