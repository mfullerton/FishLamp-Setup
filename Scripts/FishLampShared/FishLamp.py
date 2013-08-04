#!/usr/bin/python


import sys
import os
import subprocess
import glob
import fnmatch
import json
import shutil
import shutil, errno
import datetime
import time


scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))
import FishLampUtils
import FishLampGit

def scriptsPath() :
    path = subprocess.check_output(["fishlamp", "scripts-path"]).strip();
    FishLampUtils.assertPathExists(path);
    return path;

def templatePath(self, subDir) :
    return FishLampUtils.assertPathExists(os.path.join(os.path.join(self.scriptsPath(), "templates"), subDir));










