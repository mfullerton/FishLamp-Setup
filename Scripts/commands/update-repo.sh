#!/bin/bash

function usage() {
    echo "same as fishlamp init".
}

if [ "$1" == "--help" ]; then
    usage
    exit 0;
fi

fishlamp init