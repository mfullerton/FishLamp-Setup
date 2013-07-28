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
fishlamp init