#!/usr/bin/python


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
import FishLampUtils

#end boilerplate

class Script(FishLampScript.Script):

    def helpString(self):
        return "finds all installed FishLamp pieces";

    def run(self):

        fishlamp = None;
        if self.hasParameterAtIndex(1) and self.parameterAtIndex(1, "expecting -r") == "-r":
            fishlamp = FishLampPiece.relativePathToPiecesFolder();
        else:
            fishlamp = FishLampPiece.absolutePathToPiecesFolder();

        if fishlamp:
            print fishlamp;
        else:
            FishLampUtils.printError(FishLampPiece.folderName() + " not found");

Script().run();






"""

#!/bin/sh

option="$1"

function usage() {
    echo "print path to fishlamp from current direction"
	echo "-r: relative path (default)"
	echo "-a: absolute path"
	echo "usage:"
	echo "  fishlamp-find <-r -a>";
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

if [ "$option" != "-r" -a "$option" != "-a" ]; then
    option="-r"
fi


function verbose() {
#	echo "$1"
	noop=""
}

verbose ""
verbose "Looking for FishLamp..."

cd "$DEST_FOLDER"
FISHLAMP_RELATIVE_PATH=""
LAST_DIR=""

while [[ "$LAST_DIR" != `pwd` ]]
do
	if [ -d "FishLamp" ]; then
		if [ -d "FishLamp/fishlamp-core" ]; then
			FISHLAMP_ROOT="`pwd`/FishLamp"
			FISHLAMP_RELATIVE_PATH="$FISHLAMP_RELATIVE_PATH"FishLamp
			
			if [ "$option" == "-r" ]; then
				echo "$FISHLAMP_RELATIVE_PATH";
			else 
				echo "$FISHLAMP_ROOT";
			fi
				
			exit 0;
		fi
	fi

	LAST_DIR=`pwd`
	cd ..
	FISHLAMP_RELATIVE_PATH="../$FISHLAMP_RELATIVE_PATH"
done

echo "FishLamp not found"
exit 1

"""