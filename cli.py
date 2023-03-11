# cli build
# cli run
# cli gen
# cli version
# cli gen build run

import sys, os
import subprocess

TOOLS_DIR = "tools"

def RunCommand(cmd):
    script = f"{os.curdir}/{TOOLS_DIR}/{cmd}.py"
    if os.path.exists(script):
        print("Excuting: ", cmd)
        subprocess.call(["python3", ])
    else:
        print("Invalid command: ", cmd)

for i in range(1, len(sys.argv)):
    cmd = sys.argv[1]

    print("\n----------------------------------")

    RunCommand(cmd)