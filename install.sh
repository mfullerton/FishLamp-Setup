#!/bin/bash

MY_PATH="`dirname \"$0\"`"              
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  

echo "$MY_PATH"

cd "$MY_PATH/Scripts"
bash "fishlamp-script-installer.sh" fishlamp-scripts .
