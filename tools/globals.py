ENGINE_NAME = "cobra"
PROJECT_NAME = "cobraeditor"

VERSION_MAJOR = 1
VERSION_MINOR = 0

import sys, platform

PLATFORM = sys.platform
for x in platform.uname():
    if "microsoft" in x.lower():
        PLATFORM = "windows"
        break

def isWindows():    return PLATFORM == "windows"
def isLinux():      return PLATFORM == "linux"
def isMac():        return PLATFORM == "darwin"