# cli build
# cli run
# cli gen
# cli version
# cli gen build run

import sys, os
import subprocess

TOOLS_DIR = "tools"

def RunCommand(cmd):
    subprocess.call(["python3", f"{os.curdir}/{TOOLS_DIR}/{cmd}.py"])

for i in range(1, len(sys.argv)):
    cmd = sys.argv[1]

    print("\n----------------------------------")
    print("Excuting: ", cmd)

    RunCommand(cmd)