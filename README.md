# Cobra

Cobra is a simple 2D C++ engine made by a 13 year old kid.

# How to Build it
## 1- Windows
First, make sure you have [Git](https://git-scm.com/downloads) installed!
Then in an empty directory, open the terminal and type this:
```
git clone https://github.com/ms2010gamer/Cobra
cd Cobra
```
Now, also make sure you have [Python 3](https://www.python.org/downloads/release/python-3109/) installed properly and type:
```
python cli.py gensln
```
After that command, you should see a .sln file, open that and make sure you have the **main.cpp** showing.
Now, run this:
```
python cli.py buildsln
```
If that runs without any errors, run the program in Visual Studio 2022!

## 2- Linux
First, we need to install the requirements, to do that:

**Debian based distro:**
```
sudo apt update
sudo apt install python3 make git
```
**Arch based distro:**
```
sudo pacman -Sy python3 make git
```
**Fedora based distro:**
```
sudo dnf search python3 make git
sudo dnf install python3 make git
```
