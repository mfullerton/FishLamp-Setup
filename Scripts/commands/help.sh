#!/bin/sh

#  fishlamp-help.sh
#  FishLampScripts
#
#  Created by Mike Fullerton on 6/22/13.
#

function usage() {
    echo "prints help for fishlamp commands"
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

PARM="$1"

INSTALL_PATH="$HOME/Library/Developer/fishlamp-scripts"

cd "$INSTALL_PATH/commands"

FILES=`ls`
for file in $FILES; do
    extension=${file##*.}

    if [[ "$extension" == "sh" ]] || [[ "$extension" == "py" ]]; then
        filename_no_extension=`basename "$file" .$extension`

        if [[ "$PARM" != "-s" ]]; then
            echo "fishlamp $filename_no_extension:"
            bash "$file" --help | awk '{print "    "$0}'
            echo ""
        else
            echo "fishlamp $filename_no_extension"
        fi
    fi
done

