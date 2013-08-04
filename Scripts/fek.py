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

    def status(self, folders, quick):
        dirty = [];
        clean = [];

        for folder in folders:

            dir = os.getcwd();
            os.chdir(folder);
            (out, error) = FishLampGit.executeSilent(["status"]);
            os.chdir(dir);

            if out.find("nothing to commit") >= 0:
                clean.append(folder);
            else:
                dirty.append(folder);

                if quick == False:
                    print "#### " + folder + " ####";
                    print out;
                    print "#### " + folder + " ####";


#        os.chdir("..");
        print "# " + str(len(clean)) + " clean repos:"
        for f in clean:
            print "  " + os.path.relpath(f);

        if len(dirty) == 0:
            print "# all clear!"
        else:
            print "# " + str(len(dirty)) + " dirty repos:"
            for f in dirty:
                print "  " + os.path.relpath(f);

    def run(self):

        folders = FishLampGit.findGitFolders();

        if self.hasParameter("status"):
            self.status(folders, False);
        elif self.hasParameter("check"):
            self.status(folders, True)
        else:
            for folder in folders:
                os.chdir(folder)

                print ""
                print "#### " + folder + " ####"
                FishLampGit.execute(self.scriptArguments());
                print "#### " + folder + " ####"

Script().run();
