import subprocess
import globals

if globals.isWindows():
    subprocess.call(["cmd.exe", "/c", "premake\\premake5", "vs2022"])

if globals.isLinux():
    subprocess.call(["premake/premake5", "gmake2"])

if globals.isMac():
    subprocess.call(["premake/premake5", "gmake2"])
    subprocess.call(["premake/premake5.mac", "xcode4"])