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

class Script :
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
                FishLampUtils.enableVerbose();

    def printUsage(self):
        print self.usageString();

    def usageString(self):
        return "usage TBD";

    def helpString(self):
        return "help TBD";

    def checkParams(self):
        self.checkForHelp();

    def run(self):
        FishLampUtils.printError("override this");

    def hasParameterAtIndex(self, index):
        if len(sys.argv) > index:
            return True;
        return False;

    def parameterAtIndex(self, index, errorString):

        parm = None;
        if len(sys.argv) > index:
            parm = sys.argv[index];
            FishLampUtils.assertNotNone(parm, "parameter at Index: " );
#            + index
        else:
            FishLampUtils.printError(errorString);
            sys.exit(1)

        return parm;

    def scriptArguments(self) :
        args = [];
        i = 0;
        for arg in sys.argv:
            if i > 0:
                args.append(arg);
            i += 1;
        return args;

    def hasParameter(self, p) :
        for arg in sys.argv:
            if p == arg:
                return True;
        return False;
