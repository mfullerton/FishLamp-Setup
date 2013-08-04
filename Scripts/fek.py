#!/usr/bin/python

# begin boilerplate
import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))
import FishLampGit
import FishLampScript

import subprocess


class Script(FishLampScript.Script):

    def helpString(self):
        return "finds all installed FishLamp pieces";

    def run(self):

#        if self.hasParameter("-r"):
#            args = self.scriptArguments();
#            args.remove("-r");

        print self.scriptArguments();
        print sys.argv;

        folders = FishLampGit.findGitFolders();
        for folder in folders:
            print "#### " + folder + " ####"
            os.chdir(folder)
            FishLampGit.execute(self.scriptArguments());
#        else:
#            FishLampGit.execute(self.scriptArguments());

            

Script().run();
