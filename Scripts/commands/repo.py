#!/usr/bin/python

# begin boilerplate
import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))
import FishLamp
import FishLampPiece
import FishLampGit
import FishLampScript
import FishLampUtils

#end boilerplat

class Script(FishLampScript.Script):

    def helpString(self):
        return "fishlamp repo <init or update> <repo name if init>\nIf current repo is not a FishLamp repo, this inits the current repo to be a FishLamp project. Otherwise it just updates the submodules\nAlso and adds fishlamp-core submodule if it's not added"

    def update(self) :
        FishLampGit.confirmGitRoot();
        FishLampPiece.createFishLampFolderIfNeeded();
#        FishLampGit.addSubmodules(FishLampPiece.defaultPieces(), FishLampPiece.folderName());

    def init(self) :
        parm = self.parameterAtIndex(2, "Expecting name of path as first argument");

        if os.path.exits(parm):
            FishLampUtils.printError(parm + " already exists");
            sys.exit(1);

        os.makedirs(directory)
        os.chdir(directory)

        if FishLampGit.isGitRepo() :
            FishLampUtils.printError("git repo already exists");
            sys.exit(1);

        FishLampGit.init();
        self.update();

    def run(self):

        mode = self.parameterAtIndex(1, "Expecting either update or init as first parameter");

        if mode == "update":
            self.update();
        elif mode == "init":
            self.init();
        else:
            FishLampUtils.printError("expecting mode or update");

Script().run();



"""

init repo

#!/bin/bash

function usage() {
    echo "if current repo is not a FishLamp repo, this inits the current repo to be a FishLamp project. Otherwise it just updates the submodules".
    echo "Also and adds fishlamp-core submodule if it's not added"
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

set -e

MY_PATH="`dirname \"$0\"`"              
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  

fishlamp="FishLamp"
fishlamp_dir="`pwd`/$fishlamp"

if [ ! -d ".git" -a ! -f ".git" ]; then
    echo "# git folder not found - please run in root of your repository."
    exit 1
fi

if [ ! -d "$fishlamp_dir" ]; then
    mkdir "$fishlamp_dir"
fi

declare -a repo_list=( "fishlamp-core" )

git submodule update --init --recursive

for submodule in "${repo_list[@]}"; do
    fishlamp update-submodule "$submodule"
done


"""


"""
#!/bin/sh

#  fishlamp-new-repo.sh
#  fishlamp-install
#
#  Created by Mike Fullerton on 7/27/13.
#

function usage() {
    echo "creates a new folder for the repo and then inits the new repo to be a FishLamp project."
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi


set -e

new_repo="$1"

if [ -d "$new_repo" ]; then
    echo "$new_repo already exists"
    exit 1;
fi

mkdir -p "$new_repo"
cd "$new_repo"

if [ -d ".git" -o -f ".git" ]; then
    echo "# git repo already created"
    exit 1
fi

git init
fishlamp init-repo
"""