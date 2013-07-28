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


