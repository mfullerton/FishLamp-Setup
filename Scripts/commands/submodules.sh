#!/bin/sh

#  fishlamp-submodules.sh
#  fishlamp-install
#
#  Created by Mike Fullerton on 7/27/13.
#

function usage() {
    echo "lists the current FishLamp submodules in use by the repo"
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

if [ ! -d ".git" -a ! -f ".git" ]; then
    echo "# git folder not found - please run in root of your repository."
    exit 1
fi

if [ -f ".gitmodules" ]; then

    while IFS= read -r line; do
        if [[ "$line" == *submodule* ]]; then
            if [[ "$line" == *FishLamp\/fishlamp-* ]]; then
                newline="${line#[submodule \"}"
                newline="${newline%\"]}"
                echo "$newline"
            fi
       fi
    done < ".gitmodules"

fi



