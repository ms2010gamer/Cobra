import globals
import subprocess, os

CONFIG = "debug"

if globals.isWindows():
    VS_BUILD_PATH = os.environ["VS_BUILD_PATH"][8:-1]
    VS_BUILD_PATH = "C:\\\\" + VS_BUILD_PATH

    subprocess.call(["cmd.exe", "/c", VS_BUILD_PATH, f"{globals.ENGINE_NAME}.sln", f"/property:Configuration={CONFIG}"])

if globals.isLinux():
    subprocess.call(["make"])