#!/bin/bash

function usage() {
    echo "prints help for fishlamp scripts"
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

MY_PATH="`dirname \"$0\"`"
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"

SUB_PATH="$MY_PATH/commands"

if [ "$1" == "" ]; then
    "$SUB_PATH/help.sh" -s | awk '{print "    "$0}'
    echo ""
    echo "#! try 'fishlamp help' for more info"
    echo ""

    exit 1
fi

DEBUG=0

function dout() {
    if [ $DEBUG == 1 ]; then
        echo "$1"
    fi
}

MY_COMMAND="$1"
dout "Command is: $MY_COMMAND"

dout "find \"$SUB_PATH\" -name \"$MY_COMMAND*\""

MY_SCRIPT=`find "$SUB_PATH" -name "$MY_COMMAND*"`

dout "Script: $MY_SCRIPT"

MY_PARMS=${*:2}
dout "Parms: $MY_PARMS"

# echo "command = $MY_COMMAND $PARMS"

if [ -f "$MY_SCRIPT" ]; then
    dout "$MY_SCRIPT\" $MY_PARMS"
    "$MY_SCRIPT" $MY_PARMS
else
    echo "unknown command \"$MY_COMMAND\""
    exit 1
fi

exit 0

    echo "commands:"

    FILES=`find "$MY_PATH" -type f -depth 1`
    for file in $FILES; do

        filename=$(basename "$file")

        echo "$filename" | awk '{print "    "$0}'
    done

    echo ""
