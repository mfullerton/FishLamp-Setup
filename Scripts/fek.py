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

    def status(self, folders):
        count = 0;
        allClear = True;

        dirty = []

        for folder in folders:
            count += 1;
            os.chdir(folder)
            (out, error) = FishLampGit.executeSilent(self.scriptArguments());

            if out.find("nothing to commit") >= 0:
                d = 0;
            #    print "# " + folder + " clean"
            else:
                allClear = False;
                print "#### " + folder + " ####"
                print out;
                print "#### " + folder + " ####"
                dirty.append(folder)

        if allClear:
            print "# all clear (" + str(count) + " repos checked)"
        else:
            print "# dirty repos:"
            for f in dirty:
                print f;

    def run(self):

        folders = FishLampGit.findGitFolders();

        if self.hasParameter("status"):
            self.status(folders);
        else:
            for folder in folders:
                os.chdir(folder)

                print ""
                print "#### " + folder + " ####"
                FishLampGit.execute(self.scriptArguments());
                print "#### " + folder + " ####"

Script().run();
