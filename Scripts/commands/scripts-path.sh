#!/bin/sh

#  scripts-path.sh
#  fishlamp-install
#
#  Created by Mike Fullerton on 8/3/13.
#

MY_PATH="`dirname \"$0\"`"
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"

function usage() {
    echo "prints path to installed scripts"
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

"$MY_PATH/../fishlamp-scripts-dir"