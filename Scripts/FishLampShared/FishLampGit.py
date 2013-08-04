#!/usr/bin/python

import sys
import os
import subprocess
import glob

import sys
import os
scriptName = os.path.basename(sys.argv[0])
scriptPath = os.path.dirname(sys.argv[0])
sharedPath = os.path.join(scriptPath, "../FishLampShared/")
sys.path.append(os.path.abspath(sharedPath))

import FishLamp
import FishLampUtils
import re

def _print(str) :
    if str:
        str = str.strip();

        if len(str):
            print str;

def execute(args) :

    cmd = "/usr/bin/git";
    for arg in args:
        cmd += " ";
        if(arg.find(" ") > 0):
            cmd += ("\"" + arg + "\"");
        else:
            cmd += arg;

    pr = subprocess.Popen(cmd, cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    (out, error) = pr.communicate()

    _print(out);
    _print(error);

    return (out, error);

#    (out, error) =

#    print "Error : " + str(error) 
#    print "out : " + str(out)


#    gitArgs = ["git"];
#    for aArg in args:
#        gitArgs.append(aArg);
#
#    return subprocess.check_output(gitArgs).strip();

def init():
    return execute(["init"]);

def status():
    return execute(["status"])

def isGitRepo():
    return os.path.exists(".git");

def confirmGitRoot() :
    if isGitRepo() == False :
        FishLampUtils.printError("git not found - please run in root of your repository.");
        sys.exit(1)

def updateSubModules() :
    confirmGitRoot();
    return execute(["submodule", "update", "--init", "--recursive"]);

def hasSubmodule(name):
    file = gitmodulesFile();
    return file.find(name) >= 0;

def addSubmodule(modulePath, moduleName, inFolder):
    confirmGitRoot();

    if inFolder == None:
        inFolder = "";

    modulePath = os.path.join(modulePath, moduleName);

    if hasSubmodule(moduleName) == False:
        execute(["submodule", "add", modulePath, os.path.join(inFolder, moduleName)]);

def branch() :
    return execute(["rev-parse", "--abbreve-ref", "HEAD"]);

def gitmodulesFile() :
    confirmGitRoot();
    fileContents = FishLampUtils.readFileIntoString(".gitmodules");
    return fileContents;

def submodules() :
    confirmGitRoot();

    if os.path.exists(".gitmodules") == False:
        return [];

    repos = [];
    with open(".gitmodules") as f:
        for line in f:
            line = line.strip();
            if line.find("submodule") >= 0:
                match = re.search("\"(.+)\"",line);
                if(match):
                    repo = match.string[match.start() + 1 :match.end() - 1]
                    repos.append(repo);

    return repos;

def findGitFolders():
    folders = [];
    for root, dirs, files in os.walk(os.getcwd()):
        for basename in dirs:
            if basename == ".git":
                folders.append(os.path.dirname(os.path.join(root, basename)));

        for basename in files:
            if basename == ".git":
                folders.append(os.path.dirname(os.path.join(root, basename)));

    sort_key = lambda s: (-len(s), s)
    folders.sort(key=sort_key)

    return folders;

